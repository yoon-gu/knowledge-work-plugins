# scArches를 사용한 참조 매핑

이 참조 문서는 처음부터 재훈련하지 않고 사전 훈련된 참조 모델에 쿼리 데이터를 매핑하기 위한 scArches 사용 방법을 다룹니다.

## 개요

scArches(single-cell architecture surgery)는 다음을 가능하게 합니다:
- 기존 참조 아틀라스에 새 데이터 매핑
- 새로운 배치/연구로 모델 확장
- 전체 재훈련 없이 전이 학습
- 쿼리를 통합하면서 참조 구조 보존

## scArches 사용 시기

| 시나리오 | 접근 방식 |
|----------|----------|
| 기존 아틀라스에 쿼리 매핑 | scArches 쿼리 매핑 |
| 새 데이터로 아틀라스 확장 | scArches 모델 수술 |
| 사전 훈련된 모델이 없는 경우 | scANVI를 처음부터 훈련 |
| 쿼리가 참조와 매우 다른 경우 | 재훈련 고려 |

## 사전 요구 사항

```python
import scvi
import scanpy as sc
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

## 워크플로우 1: 사전 훈련된 참조에 쿼리 매핑

### 1단계: 사전 훈련된 참조 모델 로드

```python
# 저장된 참조 모델 로드
# 모델은 scvi-tools로 훈련되어 있어야 합니다
reference_model = scvi.model.SCVI.load("reference_model/")

# 또는 라벨 전이를 위한 scANVI 로드
reference_model = scvi.model.SCANVI.load("reference_scanvi_model/")

# 모델 정보 확인
print(f"Model type: {type(reference_model)}")
print(f"Training data shape: {reference_model.adata.shape}")
```

### 2단계: 쿼리 데이터 준비

```python
# 쿼리 데이터 로드
adata_query = sc.read_h5ad("query_data.h5ad")

# 중요: 유전자를 참조와 일치시키기
reference_genes = reference_model.adata.var_names
query_genes = adata_query.var_names

# 겹침 확인
common_genes = reference_genes.intersection(query_genes)
print(f"Reference genes: {len(reference_genes)}")
print(f"Query genes: {len(query_genes)}")
print(f"Overlap: {len(common_genes)}")

# 참조 유전자로 쿼리 서브셋
adata_query = adata_query[:, reference_genes].copy()

# 누락된 유전자 처리 (prepare_query_anndata에 의해 자동으로 0으로 채워짐)
```

### 3단계: 쿼리 AnnData 준비

```python
# 원시 카운트 저장
adata_query.layers["counts"] = adata_query.X.copy()

# 매핑을 위한 쿼리 준비
# 이것은 참조와 일치하도록 쿼리 데이터 구조를 정렬합니다
scvi.model.SCVI.prepare_query_anndata(adata_query, reference_model)
```

### 4단계: 쿼리 모델 생성

```python
# 참조로부터 쿼리 모델 생성
# 참조 가중치로 초기화됩니다
query_model = scvi.model.SCVI.load_query_data(
    adata_query,
    reference_model
)

# 쿼리 모델은 다음을 상속합니다:
# - 참조 아키텍처
# - 참조 인코더 가중치 (기본적으로 고정)
# - 디코더는 쿼리에 맞게 미세 조정
```

### 5단계: 쿼리에 대한 미세 조정

```python
# 쿼리 모델 미세 조정
# 쿼리 특이적 효과에 대해 디코더 가중치를 조정합니다
query_model.train(
    max_epochs=200,
    plan_kwargs={
        "weight_decay": 0.0  # 미세 조정을 위한 적은 정규화
    }
)

# 훈련 확인
query_model.history['elbo_train'].plot()
```

### 6단계: 쿼리 표현 획득

```python
# 잠재 표현 획득
# 쿼리 세포는 참조와 동일한 공간에 임베딩됩니다
adata_query.obsm["X_scVI"] = query_model.get_latent_representation()

# 시각화
sc.pp.neighbors(adata_query, use_rep="X_scVI")
sc.tl.umap(adata_query)
sc.pl.umap(adata_query, color=['cell_type', 'batch'])
```

## 워크플로우 2: 라벨 전이를 사용한 scANVI 쿼리 매핑

참조에서 쿼리로 세포 유형 라벨을 전이하는 경우:

### 1단계: scANVI 참조 로드

```python
# 참조는 scANVI 모델이어야 합니다 (라벨로 훈련됨)
reference_scanvi = scvi.model.SCANVI.load("scanvi_reference/")

# 사용 가능한 라벨 확인
print("Reference cell types:")
print(reference_scanvi.adata.obs['cell_type'].value_counts())
```

### 2단계: 쿼리 준비 및 매핑

```python
# 쿼리 준비
adata_query.layers["counts"] = adata_query.X.copy()
adata_query = adata_query[:, reference_scanvi.adata.var_names].copy()

scvi.model.SCANVI.prepare_query_anndata(adata_query, reference_scanvi)

# 쿼리 모델 생성
query_scanvi = scvi.model.SCANVI.load_query_data(
    adata_query,
    reference_scanvi
)

# 미세 조정
query_scanvi.train(
    max_epochs=100,
    plan_kwargs={"weight_decay": 0.0}
)
```

### 3단계: 예측 결과 획득

```python
# 세포 유형 예측
predictions = query_scanvi.predict()
adata_query.obs["predicted_cell_type"] = predictions

# 예측 확률 획득
soft_predictions = query_scanvi.predict(soft=True)
adata_query.obs["prediction_confidence"] = soft_predictions.max(axis=1)

# 잠재 표현
adata_query.obsm["X_scANVI"] = query_scanvi.get_latent_representation()

# 예측 시각화
sc.pp.neighbors(adata_query, use_rep="X_scANVI")
sc.tl.umap(adata_query)
sc.pl.umap(adata_query, color=['predicted_cell_type', 'prediction_confidence'])
```

### 4단계: 예측 평가

```python
# 예측 분포
print(adata_query.obs['predicted_cell_type'].value_counts())

# 신뢰도 통계
print(f"Mean confidence: {adata_query.obs['prediction_confidence'].mean():.3f}")
print(f"Low confidence (<0.5): {(adata_query.obs['prediction_confidence'] < 0.5).sum()}")

# 낮은 신뢰도 예측 필터링
high_conf = adata_query[adata_query.obs['prediction_confidence'] >= 0.7].copy()
print(f"High confidence cells: {len(high_conf)} ({len(high_conf)/len(adata_query)*100:.1f}%)")
```

## 워크플로우 3: 모델 수술 (참조 확장)

기존 참조 모델을 새 데이터로 확장:

### 1단계: 참조 레이어 고정

```python
# 참조 모델 로드
reference_model = scvi.model.SCVI.load("reference_model/")

# 참조 표현 획득 (수술 전)
adata_ref = reference_model.adata
adata_ref.obsm["X_scVI_before"] = reference_model.get_latent_representation()
```

### 2단계: 결합 데이터 준비

```python
# 배치 정보 추가
adata_ref.obs["dataset"] = "reference"
adata_query.obs["dataset"] = "query"

# 결합
adata_combined = sc.concat([adata_ref, adata_query])
adata_combined.layers["counts"] = adata_combined.X.copy()
```

### 3단계: 수술 접근 방식

```python
# 옵션 A: load_query_data 사용 (권장)
scvi.model.SCVI.prepare_query_anndata(adata_query, reference_model)
extended_model = scvi.model.SCVI.load_query_data(adata_query, reference_model)
extended_model.train(max_epochs=200)

# 옵션 B: 결합 데이터로 재훈련 (쿼리가 큰 경우)
# 참조를 정확히 보존하지는 않지만 더 나은 결과를 줄 수 있습니다
scvi.model.SCVI.setup_anndata(
    adata_combined,
    layer="counts",
    batch_key="dataset"
)
new_model = scvi.model.SCVI(adata_combined, n_latent=30)
new_model.train(max_epochs=200)
```

## 공동 시각화

참조와 쿼리를 함께 시각화:

```python
# 잠재 표현 획득
adata_ref.obsm["X_scVI"] = reference_model.get_latent_representation()
adata_query.obsm["X_scVI"] = query_model.get_latent_representation()

# 시각화를 위해 결합
adata_ref.obs["source"] = "reference"
adata_query.obs["source"] = "query"
adata_combined = sc.concat([adata_ref, adata_query])

# 공동 UMAP 계산
sc.pp.neighbors(adata_combined, use_rep="X_scVI")
sc.tl.umap(adata_combined)

# 시각화
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sc.pl.umap(adata_combined, color="source", ax=axes[0], show=False, title="Source")
sc.pl.umap(adata_combined, color="cell_type", ax=axes[1], show=False, title="Cell Type")
sc.pl.umap(adata_combined, color="batch", ax=axes[2], show=False, title="Batch")

plt.tight_layout()
```

## 공개 아틀라스 모델 사용

### HuggingFace Model Hub에서

```python
from huggingface_hub import hf_hub_download

# 모델 파일 다운로드
model_dir = hf_hub_download(
    repo_id="scvi-tools/model-name",  # 실제 리포로 교체
    filename="model.pt",
    local_dir="./downloaded_model/"
)

# 모델 로드
atlas_model = scvi.model.SCANVI.load(model_dir)
```

### CellxGene에서

```python
# 많은 CellxGene 데이터셋이 사전 훈련된 모델을 제공합니다
# 모델 가용성에 대해서는 데이터셋 문서를 확인하세요
# https://cellxgene.cziscience.com/

# 예시 워크플로우:
# 1. 참조 데이터셋과 모델 다운로드
# 2. 모델 로드: model = scvi.model.SCANVI.load("cellxgene_model/")
# 3. 위의 단계를 사용하여 쿼리 데이터 매핑
```

## 전체 파이프라인

```python
def map_query_to_reference(
    adata_query,
    reference_model_path,
    model_type="scanvi",
    max_epochs=100,
    confidence_threshold=0.5
):
    """
    쿼리 데이터를 사전 훈련된 참조 모델에 매핑합니다.

    Parameters
    ----------
    adata_query : AnnData
        원시 카운트가 포함된 쿼리 데이터
    reference_model_path : str
        저장된 참조 모델 경로
    model_type : str
        "scvi" 또는 "scanvi"
    max_epochs : int
        미세 조정 에포크 수
    confidence_threshold : float
        최소 예측 신뢰도 (scANVI용)

    Returns
    -------
    예측이 포함된 매핑된 AnnData (scANVI인 경우)
    """
    import scvi

    # 참조 로드
    if model_type == "scanvi":
        reference_model = scvi.model.SCANVI.load(reference_model_path)
        ModelClass = scvi.model.SCANVI
    else:
        reference_model = scvi.model.SCVI.load(reference_model_path)
        ModelClass = scvi.model.SCVI

    # 쿼리 준비
    adata_query = adata_query.copy()
    adata_query = adata_query[:, reference_model.adata.var_names].copy()
    adata_query.layers["counts"] = adata_query.X.copy()

    # 쿼리 매핑
    ModelClass.prepare_query_anndata(adata_query, reference_model)
    query_model = ModelClass.load_query_data(adata_query, reference_model)

    # 미세 조정
    query_model.train(
        max_epochs=max_epochs,
        plan_kwargs={"weight_decay": 0.0}
    )

    # 결과 획득
    rep_key = "X_scANVI" if model_type == "scanvi" else "X_scVI"
    adata_query.obsm[rep_key] = query_model.get_latent_representation()

    if model_type == "scanvi":
        adata_query.obs["predicted_cell_type"] = query_model.predict()
        soft = query_model.predict(soft=True)
        adata_query.obs["prediction_confidence"] = soft.max(axis=1)
        adata_query.obs["confident"] = adata_query.obs["prediction_confidence"] >= confidence_threshold

    # UMAP 계산
    sc.pp.neighbors(adata_query, use_rep=rep_key)
    sc.tl.umap(adata_query)

    return adata_query, query_model


# 사용법
adata_mapped, model = map_query_to_reference(
    adata_query,
    "reference_scanvi_model/",
    model_type="scanvi"
)

# 시각화
sc.pl.umap(adata_mapped, color=['predicted_cell_type', 'prediction_confidence'])
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|-------|-------|----------|
| 유전자 불일치 | 다른 유전자 명명 방식 | 유전자 ID 변환 (Ensembl ↔ Symbol) |
| 낮은 신뢰도가 많음 | 쿼리에 새로운 유형이 있음 | 낮은 신뢰도 세포를 수동으로 주석 달기 |
| 매핑 품질 저하 | 쿼리가 너무 다름 | 결합 데이터로 재훈련 고려 |
| 메모리 오류 | 큰 쿼리 | 배치 단위로 처리 |
| 버전 불일치 | 다른 scvi-tools 버전 | 참조 훈련과 동일한 버전 사용 |

## 주요 참고 문헌

- Lotfollahi et al. (2022) "Mapping single-cell data to reference atlases by transfer learning"
- Xu et al. (2021) "Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models"
