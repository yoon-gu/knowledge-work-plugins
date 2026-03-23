# scANVI를 이용한 레이블 전달 및 참조 매핑

이 레퍼런스는 scANVI를 사용하여 참조 아틀라스에서 쿼리 데이터로 세포 유형 주석을 전달하는 방법을 다룹니다.

## 개요

참조 매핑("레이블 전달"이라고도 함)은 주석이 달린 참조 데이터에 대해 사전 학습된 모델을 사용하여 새로운 미주석 쿼리 데이터의 세포 유형을 예측합니다. 이는 재클러스터링보다 빠르고 연구 간에 더 일관적입니다.

scANVI는 다음을 수행하기에 탁월합니다:
- 참조와 쿼리를 공유 공간에 공동 임베딩
- 확률적으로 레이블 전달
- 참조와 쿼리 간의 배치 효과 처리

## 참조 매핑 사용 시점

- 기존 아틀라스를 사용하여 새 데이터셋 주석
- 여러 연구에 걸친 일관된 주석
- 속도: 재클러스터링 및 수동 주석 불필요
- 품질: 전문가가 큐레이션한 참조 주석 활용

## 워크플로우 옵션

1. **새 모델 학습**: 참조에서 scANVI 학습 후 쿼리 매핑
2. **사전 학습된 모델 사용**: 기존 모델 로드 (예: Model Hub에서)
3. **scArches**: 쿼리 데이터로 기존 모델 확장 (참조 보존)

## 옵션 1: 참조에서 scANVI 학습

### 1단계: 참조 데이터 준비

```python
import scvi
import scanpy as sc

# 참조 아틀라스 로드
adata_ref = sc.read_h5ad("reference_atlas.h5ad")

# 주석 확인
print(f"참조 세포 수: {adata_ref.n_obs}")
print(f"세포 유형 수: {adata_ref.obs['cell_type'].nunique()}")
print(adata_ref.obs['cell_type'].value_counts())

# 원시 카운트 확인
adata_ref.layers["counts"] = adata_ref.raw.X.copy() if adata_ref.raw else adata_ref.X.copy()

# HVG 선택
sc.pp.highly_variable_genes(
    adata_ref,
    n_top_genes=3000,
    flavor="seurat_v3",
    batch_key="batch" if "batch" in adata_ref.obs else None,
    layer="counts"
)
adata_ref = adata_ref[:, adata_ref.var["highly_variable"]].copy()
```

### 2단계: 참조에서 scANVI 학습

```python
# 먼저 scVI 학습 (비지도)
scvi.model.SCVI.setup_anndata(
    adata_ref,
    layer="counts",
    batch_key="batch"
)

scvi_ref = scvi.model.SCVI(adata_ref, n_latent=30)
scvi_ref.train(max_epochs=200)

# scVI에서 scANVI 초기화
scanvi_ref = scvi.model.SCANVI.from_scvi_model(
    scvi_ref,
    labels_key="cell_type",
    unlabeled_category="Unknown"
)

# scANVI 학습
scanvi_ref.train(max_epochs=50)

# 나중 사용을 위해 저장
scanvi_ref.save("scanvi_reference_model/")
```

### 3단계: 쿼리 데이터 준비

```python
# 쿼리 데이터 로드
adata_query = sc.read_h5ad("query_data.h5ad")

# 중요: 참조와 동일한 유전자 사용
common_genes = adata_ref.var_names.intersection(adata_query.var_names)
print(f"공통 유전자: {len(common_genes)}")

# 쿼리를 참조 유전자로 서브셋
adata_query = adata_query[:, adata_ref.var_names].copy()

# 누락 유전자 처리 (0으로 설정)
missing_genes = set(adata_ref.var_names) - set(adata_query.var_names)
if missing_genes:
    # 0 발현으로 누락 유전자 추가
    import numpy as np
    from scipy.sparse import csr_matrix

    zero_matrix = csr_matrix((adata_query.n_obs, len(missing_genes)))
    # ... 연결 및 참조와 일치하도록 재정렬

# 카운트 저장
adata_query.layers["counts"] = adata_query.X.copy()
```

### 4단계: 쿼리를 참조에 매핑

```python
# 매핑을 위한 쿼리 데이터 준비
scvi.model.SCANVI.prepare_query_anndata(adata_query, scanvi_ref)

# 참조에서 쿼리 모델 생성
scanvi_query = scvi.model.SCANVI.load_query_data(
    adata_query,
    scanvi_ref
)

# 쿼리에서 미세 조정 (선택사항이지만 권장)
scanvi_query.train(
    max_epochs=100,
    plan_kwargs={"weight_decay": 0.0}
)

# 예측 얻기
adata_query.obs["predicted_cell_type"] = scanvi_query.predict()

# 예측 확률 얻기
soft_predictions = scanvi_query.predict(soft=True)
adata_query.obs["prediction_score"] = soft_predictions.max(axis=1)
```

### 5단계: 예측 평가

```python
# 신뢰도 점수
print(f"평균 예측 신뢰도: {adata_query.obs['prediction_score'].mean():.3f}")

# 낮은 신뢰도 예측
low_conf = adata_query.obs['prediction_score'] < 0.5
print(f"낮은 신뢰도 세포: {low_conf.sum()} ({low_conf.mean()*100:.1f}%)")

# 시각화
sc.pp.neighbors(adata_query, use_rep="X_scANVI")
sc.tl.umap(adata_query)
sc.pl.umap(adata_query, color=['predicted_cell_type', 'prediction_score'])
```

## 옵션 2: 사전 학습된 모델 사용

### Model Hub에서

```python
# scvi-tools는 HuggingFace에서 모델 유지
# 확인: https://huggingface.co/scvi-tools

# 예시: 사전 학습된 모델 로드
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="scvi-tools/example-model",
    filename="model.pt"
)

# 모델 로드
model = scvi.model.SCANVI.load(model_path, adata=adata_query)
```

### 출판된 아틀라스에서

```python
# 많은 아틀라스가 사전 학습된 모델 제공
# CellTypist 스타일 모델 사용 예시 워크플로우

# 참조 모델 다운로드
# model = scvi.model.SCANVI.load("atlas_model/", adata=adata_query)
```

## 옵션 3: 증분 업데이트를 위한 scArches

scArches는 처음부터 재학습 없이 참조 모델을 확장합니다:

```python
# 기존 참조 모델 로드
scanvi_ref = scvi.model.SCANVI.load("reference_model/")

# 수술: 쿼리 통합 준비
scanvi_ref.freeze_layers()

# 쿼리 데이터 매핑
scvi.model.SCANVI.prepare_query_anndata(adata_query, scanvi_ref)
scanvi_query = scvi.model.SCANVI.load_query_data(adata_query, scanvi_ref)

# 쿼리 전용 매개변수만 학습
scanvi_query.train(
    max_epochs=200,
    plan_kwargs={"weight_decay": 0.0}
)
```

## 참조와 쿼리 함께 시각화

```python
# 공동 시각화를 위해 연결
adata_ref.obs["dataset"] = "reference"
adata_query.obs["dataset"] = "query"

# 잠재 표현 얻기
adata_ref.obsm["X_scANVI"] = scanvi_ref.get_latent_representation()
adata_query.obsm["X_scANVI"] = scanvi_query.get_latent_representation()

# 결합
adata_combined = sc.concat([adata_ref, adata_query])

# 결합 UMAP 계산
sc.pp.neighbors(adata_combined, use_rep="X_scANVI")
sc.tl.umap(adata_combined)

# 플롯
sc.pl.umap(
    adata_combined,
    color=["dataset", "cell_type", "predicted_cell_type"],
    ncols=2
)
```

## 예측 품질 관리

### 신뢰도 필터링

```python
# 신뢰도로 예측 필터링
confidence_threshold = 0.7

high_conf = adata_query[adata_query.obs['prediction_score'] >= confidence_threshold].copy()
low_conf = adata_query[adata_query.obs['prediction_score'] < confidence_threshold].copy()

print(f"높은 신뢰도: {len(high_conf)} ({len(high_conf)/len(adata_query)*100:.1f}%)")
print(f"낮은 신뢰도: {len(low_conf)} ({len(low_conf)/len(adata_query)*100:.1f}%)")
```

### 마커 검증

```python
# 알려진 마커로 예측 검증
markers = {
    'T cells': ['CD3D', 'CD3E'],
    'B cells': ['CD19', 'MS4A1'],
    'Monocytes': ['CD14', 'LYZ']
}

for ct, genes in markers.items():
    ct_cells = adata_query[adata_query.obs['predicted_cell_type'] == ct]
    if len(ct_cells) > 0:
        for gene in genes:
            if gene in adata_query.var_names:
                expr = ct_cells[:, gene].X.mean()
                print(f"{ct} - {gene}: {expr:.3f}")
```

## 전체 파이프라인

```python
def transfer_labels(
    adata_ref,
    adata_query,
    cell_type_key="cell_type",
    batch_key=None,
    n_top_genes=3000,
    confidence_threshold=0.5
):
    """
    참조에서 쿼리로 세포 유형 레이블 전달.

    Parameters
    ----------
    adata_ref : AnnData
        주석이 달린 참조 데이터
    adata_query : AnnData
        미주석 쿼리 데이터
    cell_type_key : str
        참조의 세포 유형 주석 열
    batch_key : str, optional
        배치 열
    n_top_genes : int
        HVG 수
    confidence_threshold : float
        예측의 최소 신뢰도

    Returns
    -------
    예측이 포함된 AnnData
    """
    import scvi
    import scanpy as sc

    # 참조 준비
    adata_ref = adata_ref.copy()
    adata_ref.layers["counts"] = adata_ref.X.copy()

    sc.pp.highly_variable_genes(
        adata_ref,
        n_top_genes=n_top_genes,
        flavor="seurat_v3",
        batch_key=batch_key,
        layer="counts"
    )
    adata_ref = adata_ref[:, adata_ref.var["highly_variable"]].copy()

    # 참조 모델 학습
    scvi.model.SCVI.setup_anndata(adata_ref, layer="counts", batch_key=batch_key)
    scvi_ref = scvi.model.SCVI(adata_ref, n_latent=30)
    scvi_ref.train(max_epochs=200)

    scanvi_ref = scvi.model.SCANVI.from_scvi_model(
        scvi_ref,
        labels_key=cell_type_key,
        unlabeled_category="Unknown"
    )
    scanvi_ref.train(max_epochs=50)

    # 쿼리 준비
    adata_query = adata_query[:, adata_ref.var_names].copy()
    adata_query.layers["counts"] = adata_query.X.copy()

    # 쿼리 매핑
    scvi.model.SCANVI.prepare_query_anndata(adata_query, scanvi_ref)
    scanvi_query = scvi.model.SCANVI.load_query_data(adata_query, scanvi_ref)
    scanvi_query.train(max_epochs=100, plan_kwargs={"weight_decay": 0.0})

    # 예측 얻기
    adata_query.obs["predicted_cell_type"] = scanvi_query.predict()
    soft = scanvi_query.predict(soft=True)
    adata_query.obs["prediction_score"] = soft.max(axis=1)

    # 낮은 신뢰도 표시
    adata_query.obs["confident_prediction"] = adata_query.obs["prediction_score"] >= confidence_threshold

    # 잠재 표현 추가
    adata_query.obsm["X_scANVI"] = scanvi_query.get_latent_representation()

    return adata_query, scanvi_ref, scanvi_query

# 사용법
adata_annotated, ref_model, query_model = transfer_labels(
    adata_ref,
    adata_query,
    cell_type_key="cell_type"
)

# 시각화
sc.pp.neighbors(adata_annotated, use_rep="X_scANVI")
sc.tl.umap(adata_annotated)
sc.pl.umap(adata_annotated, color=['predicted_cell_type', 'prediction_score'])
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 낮은 신뢰도 예측 많음 | 쿼리에 새로운 세포 유형 | 낮은 신뢰도 세포 수동 주석 |
| 잘못된 예측 | 참조가 조직과 불일치 | 조직에 적합한 참조 사용 |
| 유전자 불일치 | 다른 유전자 명명 | 유전자 ID 변환 |
| 모두 동일한 예측 | 쿼리가 너무 다름 | 데이터 품질 확인, 다른 참조 시도 |

## 주요 참고문헌

- Xu et al. (2021) "Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models"
- Lotfollahi et al. (2022) "Mapping single-cell data to reference atlases by transfer learning"
