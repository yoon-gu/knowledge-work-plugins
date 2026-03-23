# 공간 전사체학 분석

이 참조 문서는 scvi-tools 방법을 사용한 공간 전사체학 분석을 다룹니다: 탈콘볼루션을 위한 DestVI와 공간 모델 구축을 위한 resolVI.

## 개요

Visium과 같은 공간 전사체학 기술은 정의된 공간 위치에서 유전자 발현을 캡처하지만, 많은 플랫폼은 다세포 해상도를 가집니다. scvi-tools는 두 가지 주요 접근 방식을 제공합니다:

- **DestVI**: 탈콘볼루션 - 단일 세포 참조를 사용하여 각 스팟의 세포 유형 비율을 추정
- **resolVI**: 공간 맥락을 고려한 유전자 발현 패턴을 학습하는 공간 모델 구축

## scvi-tools에서 사용 가능한 방법

| 방법 | 설명 | 사용 사례 |
|--------|-------------|----------|
| **DestVI** | 탈콘볼루션을 위한 변분 추론 | 스팟당 세포 유형 비율 추정 |
| **resolVI** | 공간 유전자 발현 모델 | 공간 인식 표현 학습 |
| **CondSCVI** | DestVI를 위한 참조 모델 | DestVI 워크플로우에 필요 |

## 사전 요구 사항

```python
import scvi
import scanpy as sc
import squidpy as sq
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

---

## 파트 1: DestVI 탈콘볼루션

### 1단계: 공간 데이터 로드

```python
# Visium 데이터 로드
adata_spatial = sc.read_visium("spaceranger_output/")

# 구조 확인
print(f"Spots: {adata_spatial.n_obs}")
print(f"Genes: {adata_spatial.n_vars}")
print(f"Spatial coordinates: {adata_spatial.obsm['spatial'].shape}")

# 기본 QC
sc.pp.calculate_qc_metrics(adata_spatial, inplace=True)
adata_spatial = adata_spatial[adata_spatial.obs['n_genes_by_counts'] > 200].copy()

# 카운트 저장
adata_spatial.layers["counts"] = adata_spatial.X.copy()
```

### 2단계: 단일 세포 참조 로드

```python
# 참조 단일 세포 데이터 로드
adata_sc = sc.read_h5ad("reference_scrna.h5ad")

# 요구 사항:
# - 원시 카운트
# - 세포 유형 주석
print(f"Reference cells: {adata_sc.n_obs}")
print(f"Cell types: {adata_sc.obs['cell_type'].nunique()}")
print(adata_sc.obs['cell_type'].value_counts())

# 카운트 저장
adata_sc.layers["counts"] = adata_sc.X.copy()
```

### 3단계: 데이터 준비

```python
# DestVI는 참조와 공간 간의 유전자 겹침이 필요합니다
common_genes = adata_sc.var_names.intersection(adata_spatial.var_names)
print(f"Common genes: {len(common_genes)}")

adata_sc = adata_sc[:, common_genes].copy()
adata_spatial = adata_spatial[:, common_genes].copy()
```

### 4단계: 참조 모델 훈련 (CondSCVI)

```python
# 참조 데이터에 대해 조건부 scVI 훈련
scvi.model.CondSCVI.setup_anndata(
    adata_sc,
    layer="counts",
    labels_key="cell_type"
)

sc_model = scvi.model.CondSCVI(
    adata_sc,
    n_latent=20
)

sc_model.train(max_epochs=200)
sc_model.history['elbo_train'].plot()
```

### 5단계: DestVI 훈련

```python
# 공간 데이터 설정
scvi.model.DestVI.setup_anndata(
    adata_spatial,
    layer="counts"
)

# 참조 모델을 사용하여 DestVI 훈련
spatial_model = scvi.model.DestVI.from_rna_model(
    adata_spatial,
    sc_model
)

spatial_model.train(max_epochs=500)
```

### 6단계: 세포 유형 비율 획득

```python
# 각 스팟에서 세포 유형 비율 추론
proportions = spatial_model.get_proportions()

# adata에 추가
for ct in adata_sc.obs['cell_type'].unique():
    adata_spatial.obs[f'prop_{ct}'] = proportions[ct]

# 시각화
sq.pl.spatial_scatter(
    adata_spatial,
    color=[f'prop_{ct}' for ct in adata_sc.obs['cell_type'].unique()[:6]],
    ncols=3
)
```

---

## 파트 2: resolVI 공간 모델

resolVI는 공간 데이터에서 직접 세포 유형 할당과 공간 인식 표현을 학습하는 반지도 학습 방법으로, 선택적으로 초기 세포 유형 예측을 사용합니다.

**참고**: resolVI는 `scvi.external`에 있습니다 (`scvi.model`이 아님).

### 1단계: 공간 데이터 준비

```python
# 로드 및 전처리
adata = sc.read_visium("spaceranger_output/")

# QC
sc.pp.calculate_qc_metrics(adata, inplace=True)
adata = adata[adata.obs['n_genes_by_counts'] > 200].copy()

# 카운트 저장
adata.layers["counts"] = adata.X.copy()

# HVG 선택
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=4000,
    flavor="seurat_v3",
    layer="counts"
)
adata = adata[:, adata.var['highly_variable']].copy()

# 선택 사항: 초기 세포 유형 예측 획득 (예: 참조로부터)
# adata.obs["predicted_celltype"] = ...
```

### 2단계: resolVI 설정 및 훈련

```python
# resolVI 설정 (참고: scvi.external, scvi.model이 아님)
scvi.external.RESOLVI.setup_anndata(
    adata,
    labels_key="predicted_celltype",  # 초기 세포 유형 예측
    layer="counts"
)

# 모델 생성 (semisupervised=True는 라벨을 사용)
model = scvi.external.RESOLVI(adata, semisupervised=True)

# 훈련
model.train(max_epochs=50)
```

### 3단계: 세포 유형 예측 획득

```python
# 정제된 세포 유형 예측 획득
# soft=True는 확률을 반환, soft=False는 라벨을 반환
cell_type_probs = model.predict(adata, num_samples=3, soft=True)
cell_type_labels = model.predict(adata, num_samples=3, soft=False)

adata.obs["resolvi_celltype"] = cell_type_labels

# 시각화
sq.pl.spatial_scatter(adata, color="resolvi_celltype")
```

### 4단계: 잠재 표현 획득

```python
# 잠재 표현 획득
adata.obsm["X_resolVI"] = model.get_latent_representation(adata)

# 공간 표현 기반 클러스터링
sc.pp.neighbors(adata, use_rep="X_resolVI")
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=0.5)

# 공간적으로 클러스터 시각화
sq.pl.spatial_scatter(adata, color="leiden")
```

### 5단계: 차등 발현 분석

```python
# resolVI를 사용한 세포 유형 간 DE
de_results = model.differential_expression(
    adata,
    groupby="resolvi_celltype",
    group1="T_cell",
    group2="Tumor"
)

print(de_results.head(20))
```

### 6단계: 니체 풍부도 분석

```python
# 조건 간 세포 유형 이웃 관계가 어떻게 다른지 분석
# 공간 이웃 그래프 필요
sq.gr.spatial_neighbors(adata, coord_type="generic")

niche_results = model.differential_niche_abundance(
    groupby="resolvi_celltype",
    group1="T_cell",
    group2="Tumor",
    neighbor_key="spatial_neighbors"
)
```

### 7단계: 쿼리 매핑 (새 데이터로 전이)

```python
# 훈련된 모델에 새 공간 데이터 매핑
query_adata = sc.read_visium("new_sample/")
query_adata.layers["counts"] = query_adata.X.copy()

# 쿼리 준비 및 로드
model.prepare_query_anndata(query_adata, reference_model=model)
query_model = model.load_query_data(query_adata, reference_model=model)

# 쿼리에 대한 미세 조정
query_model.train(max_epochs=20)

# 쿼리에 대한 예측 획득
query_labels = query_model.predict(query_adata, num_samples=3, soft=False)
```

---

## 시각화

### 공간 비율

```python
import matplotlib.pyplot as plt

# 여러 세포 유형 비율 플롯
cell_types = ['T_cell', 'Tumor', 'Fibroblast', 'Macrophage']
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

for ax, ct in zip(axes.flat, cell_types):
    sq.pl.spatial_scatter(
        adata_spatial,
        color=f'prop_{ct}',
        ax=ax,
        title=ct,
        show=False
    )

plt.tight_layout()
```

### 영역별 풍부도

```python
# 공간 데이터 클러스터링
sc.pp.neighbors(adata_spatial)
sc.tl.leiden(adata_spatial, resolution=0.5)

# 영역 간 비율 비교
import pandas as pd

cell_types = adata_sc.obs['cell_type'].unique()
prop_cols = [f'prop_{ct}' for ct in cell_types]
region_props = adata_spatial.obs.groupby('leiden')[prop_cols].mean()
print(region_props)

# 히트맵
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.heatmap(region_props.T, annot=True, cmap='viridis')
plt.title('영역별 세포 유형 비율')
```

### 공간 세포 유형 상호작용

```python
# 세포 유형 할당을 사용한 이웃 풍부도
sq.gr.spatial_neighbors(adata_spatial)

# "우세 세포 유형" 주석 생성
prop_cols = [f'prop_{ct}' for ct in cell_types]
adata_spatial.obs['dominant_type'] = adata_spatial.obs[prop_cols].idxmax(axis=1)
adata_spatial.obs['dominant_type'] = adata_spatial.obs['dominant_type'].str.replace('prop_', '')

# 공존 분석
sq.gr.co_occurrence(adata_spatial, cluster_key='dominant_type')
sq.pl.co_occurrence(adata_spatial, cluster_key='dominant_type')
```

---

## 전체 DestVI 파이프라인

```python
def deconvolve_spatial(
    adata_spatial,
    adata_ref,
    cell_type_key="cell_type",
    n_latent=20,
    max_epochs_ref=200,
    max_epochs_spatial=500
):
    """
    DestVI를 사용한 공간 탈콘볼루션을 수행합니다.

    Parameters
    ----------
    adata_spatial : AnnData
        공간 전사체학 데이터
    adata_ref : AnnData
        세포 유형 주석이 포함된 단일 세포 참조
    cell_type_key : str
        adata_ref.obs에서 세포 유형 라벨이 있는 열
    n_latent : int
        잠재 차원
    max_epochs_ref : int
        참조 모델 훈련 에포크
    max_epochs_spatial : int
        공간 모델 훈련 에포크

    Returns
    -------
    obs에 세포 유형 비율이 포함된 AnnData
    """
    import scvi

    # 공통 유전자 획득
    common_genes = adata_ref.var_names.intersection(adata_spatial.var_names)
    adata_ref = adata_ref[:, common_genes].copy()
    adata_spatial = adata_spatial[:, common_genes].copy()

    # 카운트가 저장되어 있는지 확인
    if "counts" not in adata_ref.layers:
        adata_ref.layers["counts"] = adata_ref.X.copy()
    if "counts" not in adata_spatial.layers:
        adata_spatial.layers["counts"] = adata_spatial.X.copy()

    # 참조 모델 훈련
    scvi.model.CondSCVI.setup_anndata(
        adata_ref,
        layer="counts",
        labels_key=cell_type_key
    )

    ref_model = scvi.model.CondSCVI(adata_ref, n_latent=n_latent)
    ref_model.train(max_epochs=max_epochs_ref)

    # 공간 모델 훈련
    scvi.model.DestVI.setup_anndata(adata_spatial, layer="counts")

    spatial_model = scvi.model.DestVI.from_rna_model(
        adata_spatial,
        ref_model
    )
    spatial_model.train(max_epochs=max_epochs_spatial)

    # 비율 획득
    proportions = spatial_model.get_proportions()

    cell_types = adata_ref.obs[cell_type_key].unique()
    for ct in cell_types:
        adata_spatial.obs[f'prop_{ct}'] = proportions[ct]

    # 우세 유형 추가
    prop_cols = [f'prop_{ct}' for ct in cell_types]
    adata_spatial.obs['dominant_type'] = adata_spatial.obs[prop_cols].idxmax(axis=1)
    adata_spatial.obs['dominant_type'] = adata_spatial.obs['dominant_type'].str.replace('prop_', '')

    return adata_spatial, ref_model, spatial_model

# 사용법
adata_spatial, ref_model, spatial_model = deconvolve_spatial(
    adata_spatial,
    adata_sc,
    cell_type_key="cell_type"
)

# 시각화
sq.pl.spatial_scatter(
    adata_spatial,
    color=['dominant_type', 'prop_T_cell', 'prop_Tumor'],
    ncols=3
)
```

---

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|-------|-------|----------|
| 공통 유전자가 적음 | 다른 유전자 명명 방식 | 유전자 이름 변환 (Ensembl ↔ Symbol) |
| 탈콘볼루션 품질 저하 | 참조가 일치하지 않음 | 조직 매칭 참조 사용 |
| 모든 스팟이 같은 유형 | 과도한 평활화 | 모델 파라미터 조정, 참조 다양성 확인 |
| NaN 비율 | 누락된 세포 유형 | 참조에 예상되는 모든 유형이 포함되어 있는지 확인 |
| 훈련이 느림 | 큰 공간 데이터셋 | max_epochs 감소, batch_size 증가 |

## 주요 참고 문헌

- Lopez et al. (2022) "DestVI identifies continuums of cell types in spatial transcriptomics data"
- [scvi-tools 공간 튜토리얼](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
