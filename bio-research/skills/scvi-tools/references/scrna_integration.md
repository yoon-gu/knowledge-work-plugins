# scVI와 scANVI를 사용한 scRNA-seq 통합

이 참조 문서는 scVI(비지도 학습)와 scANVI(세포 유형 라벨을 사용한 반지도 학습)를 사용한 배치 보정 및 데이터셋 통합을 다룹니다.

## 개요

단일 세포 데이터셋은 종종 다음과 같은 요인으로 인한 배치 효과를 가집니다:
- 서로 다른 기증자/환자
- 서로 다른 실험 배치
- 서로 다른 기술 (10x v2 vs v3)
- 서로 다른 연구

scVI와 scANVI는 배치 효과가 제거되면서 생물학적 변이가 보존되는 공유 잠재 공간을 학습합니다.

## 어떤 모델을 사용할지

| 모델 | 사용 시기 | 라벨 필요 여부 |
|-------|----------|---------------|
| **scVI** | 라벨이 없는 경우, 탐색적 분석 | 아니오 |
| **scANVI** | 부분/전체 라벨이 있는 경우, 더 나은 보존을 원할 때 | 예 (부분적 OK) |

## scVI 통합 워크플로우

### 1단계: 데이터 준비

```python
import scvi
import scanpy as sc

# 데이터셋 로드
adata1 = sc.read_h5ad("dataset1.h5ad")
adata2 = sc.read_h5ad("dataset2.h5ad")

# 배치 주석 추가
adata1.obs["batch"] = "batch1"
adata2.obs["batch"] = "batch2"

# 결합
adata = sc.concat([adata1, adata2], label="batch")

# 원시 카운트인지 확인
# 정규화된 데이터라면 .raw에서 복구
if hasattr(adata, 'raw') and adata.raw is not None:
    adata = adata.raw.to_adata()

# 카운트 저장
adata.layers["counts"] = adata.X.copy()
```

### 2단계: 배치 간 HVG 선택

```python
# 배치를 고려한 HVG 선택
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2000,
    flavor="seurat_v3",
    batch_key="batch",
    layer="counts"
)

# HVG로 서브셋
adata = adata[:, adata.var["highly_variable"]].copy()
```

### 3단계: scVI 설정 및 훈련

```python
# scVI에 데이터 등록
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch"
)

# 모델 생성
model = scvi.model.SCVI(
    adata,
    n_latent=30,          # 잠재 차원
    n_layers=2,           # 인코더/디코더 깊이
    gene_likelihood="nb"  # 음이항 분포 (또는 "zinb")
)

# 훈련
model.train(
    max_epochs=200,
    early_stopping=True,
    early_stopping_patience=10,
    batch_size=128
)

# 훈련 이력 플롯
model.history["elbo_train"].plot()
```

### 4단계: 통합된 표현 획득

```python
# 잠재 표현 획득
adata.obsm["X_scVI"] = model.get_latent_representation()

# 클러스터링 및 시각화에 사용
sc.pp.neighbors(adata, use_rep="X_scVI", n_neighbors=15)
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=1.0)

# 통합 시각화
sc.pl.umap(adata, color=["batch", "leiden"], ncols=2)
```

### 5단계: 모델 저장

```python
# 나중에 사용하기 위해 모델 저장
model.save("scvi_model/")

# 모델 로드
model = scvi.model.SCVI.load("scvi_model/", adata=adata)
```

## scANVI 통합 워크플로우

scANVI는 더 나은 생물학적 보존을 위해 세포 유형 라벨로 scVI를 확장합니다.

### 1단계: 라벨이 포함된 데이터 준비

```python
# 라벨은 adata.obs에 있어야 합니다
# 라벨이 없는 세포에는 "Unknown" 사용
print(adata.obs["cell_type"].value_counts())

# 부분적으로 라벨된 데이터의 경우
# 라벨이 없는 세포 표시
adata.obs["cell_type_scanvi"] = adata.obs["cell_type"].copy()
# adata.obs.loc[unlabeled_mask, "cell_type_scanvi"] = "Unknown"
```

### 2단계: 옵션 A - scANVI를 처음부터 훈련

```python
# scANVI 설정
scvi.model.SCANVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    labels_key="cell_type"
)

# 모델 생성
scanvi_model = scvi.model.SCANVI(
    adata,
    n_latent=30,
    n_layers=2
)

# 훈련
scanvi_model.train(max_epochs=200)
```

### 2단계: 옵션 B - scVI에서 scANVI 초기화 (권장)

```python
# 먼저 scVI 훈련
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
scvi_model = scvi.model.SCVI(adata, n_latent=30)
scvi_model.train(max_epochs=200)

# scVI에서 scANVI 초기화
scanvi_model = scvi.model.SCANVI.from_scvi_model(
    scvi_model,
    labels_key="cell_type",
    unlabeled_category="Unknown"  # 부분적으로 라벨된 데이터용
)

# scANVI 미세 조정 (더 적은 에포크 필요)
scanvi_model.train(max_epochs=50)
```

### 3단계: 결과 획득

```python
# 잠재 표현
adata.obsm["X_scANVI"] = scanvi_model.get_latent_representation()

# 라벨이 없는 세포에 대한 예측 라벨
predictions = scanvi_model.predict()
adata.obs["predicted_cell_type"] = predictions

# 예측 확률
soft_predictions = scanvi_model.predict(soft=True)

# 시각화
sc.pp.neighbors(adata, use_rep="X_scANVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color=["batch", "cell_type", "predicted_cell_type"])
```

## 통합 품질 비교

### 시각적 평가

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 통합 전 (PCA 기반)
sc.pp.pca(adata)
sc.pl.pca(adata, color="batch", ax=axes[0], title="Before (PCA)", show=False)

# scVI 후
sc.pp.neighbors(adata, use_rep="X_scVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color="batch", ax=axes[1], title="After scVI", show=False)

# scANVI 후
sc.pp.neighbors(adata, use_rep="X_scANVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color="batch", ax=axes[2], title="After scANVI", show=False)

plt.tight_layout()
```

### 정량적 지표 (scib)

```python
# pip install scib-metrics

from scib_metrics.benchmark import Benchmarker

bm = Benchmarker(
    adata,
    batch_key="batch",
    label_key="cell_type",
    embedding_obsm_keys=["X_pca", "X_scVI", "X_scANVI"]
)

bm.benchmark()
bm.plot_results_table()
```

## 차등 발현 분석

scVI는 배치 효과를 고려한 차등 발현 분석을 제공합니다:

```python
# 그룹 간 DE
de_results = model.differential_expression(
    groupby="cell_type",
    group1="T cells",
    group2="B cells"
)

# 유의미한 결과 필터링
de_sig = de_results[
    (de_results["is_de_fdr_0.05"] == True) &
    (abs(de_results["lfc_mean"]) > 1)
]

print(de_sig.head(20))
```

## 고급: 다중 범주형 공변량

```python
# 배치 외에 추가 공변량 포함
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    categorical_covariate_keys=["donor", "technology"]
)

model = scvi.model.SCVI(adata, n_latent=30)
model.train()
```

## 훈련 팁

### 대규모 데이터셋의 경우 (>100k 세포)

```python
model.train(
    max_epochs=100,      # 더 적은 에포크 필요
    batch_size=256,      # 더 큰 배치
    train_size=0.9,      # 더 적은 검증
    early_stopping=True
)
```

### 소규모 데이터셋의 경우 (<10k 세포)

```python
model = scvi.model.SCVI(
    adata,
    n_latent=10,         # 더 작은 잠재 공간
    n_layers=1,          # 더 간단한 모델
    dropout_rate=0.2     # 더 많은 정규화
)

model.train(
    max_epochs=400,
    batch_size=64
)
```

### 훈련 모니터링

```python
# 훈련 곡선 확인
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(model.history["elbo_train"], label="Train")
ax.plot(model.history["elbo_validation"], label="Validation")
ax.set_xlabel("Epoch")
ax.set_ylabel("ELBO")
ax.legend()

# 과적합 없이 수렴이 보여야 합니다
```

## 전체 파이프라인

```python
def integrate_datasets(
    adatas,
    batch_key="batch",
    labels_key=None,
    n_top_genes=2000,
    n_latent=30
):
    """
    여러 scRNA-seq 데이터셋을 통합합니다.

    Parameters
    ----------
    adatas : dict
        {batch_name: AnnData} 딕셔너리
    batch_key : str
        배치 주석 키
    labels_key : str, optional
        세포 유형 라벨 키 (제공 시 scANVI 사용)
    n_top_genes : int
        HVG 수
    n_latent : int
        잠재 차원

    Returns
    -------
    통합된 표현이 포함된 AnnData
    """
    import scvi
    import scanpy as sc

    # 배치 라벨 추가 및 결합
    for batch_name, adata in adatas.items():
        adata.obs[batch_key] = batch_name

    adata = sc.concat(list(adatas.values()), label=batch_key)

    # 카운트 저장
    adata.layers["counts"] = adata.X.copy()

    # HVG 선택
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=n_top_genes,
        flavor="seurat_v3",
        batch_key=batch_key,
        layer="counts"
    )
    adata = adata[:, adata.var["highly_variable"]].copy()

    # 모델 훈련
    if labels_key and labels_key in adata.obs.columns:
        # scANVI 사용
        scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key=batch_key)
        scvi_model = scvi.model.SCVI(adata, n_latent=n_latent)
        scvi_model.train(max_epochs=200)

        model = scvi.model.SCANVI.from_scvi_model(
            scvi_model,
            labels_key=labels_key,
            unlabeled_category="Unknown"
        )
        model.train(max_epochs=50)
        rep_key = "X_scANVI"
    else:
        # scVI 사용
        scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key=batch_key)
        model = scvi.model.SCVI(adata, n_latent=n_latent)
        model.train(max_epochs=200)
        rep_key = "X_scVI"

    # 표현 추가
    adata.obsm[rep_key] = model.get_latent_representation()

    # 이웃 및 UMAP 계산
    sc.pp.neighbors(adata, use_rep=rep_key)
    sc.tl.umap(adata)
    sc.tl.leiden(adata)

    return adata, model

# 사용법
adatas = {
    "study1": sc.read_h5ad("study1.h5ad"),
    "study2": sc.read_h5ad("study2.h5ad"),
    "study3": sc.read_h5ad("study3.h5ad")
}

adata_integrated, model = integrate_datasets(
    adatas,
    labels_key="cell_type"
)

sc.pl.umap(adata_integrated, color=["batch", "leiden", "cell_type"])
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|-------|-------|----------|
| 배치가 혼합되지 않음 | 공유 유전자가 너무 적음 | HVG 증가, 유전자 겹침 확인 |
| 과보정 | 생물학적 변이 제거됨 | 라벨과 함께 scANVI 사용 |
| 훈련이 발산함 | 학습률이 너무 높음 | lr 감소, batch_size 증가 |
| NaN 손실 | 불량 데이터 | 카운트가 0인 세포/유전자 확인 |
| 메모리 오류 | 세포가 너무 많음 | batch_size 감소, GPU 사용 |
