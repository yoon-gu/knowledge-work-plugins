# 우주공간체학분석

이 참고 자료는 scvi-tools 방법(디콘볼루션을 분리하여 DestVI 및 공간 모델 구축을 resolVI)을 사용하여 공간 압축체 분석을 다뤄집니다.

## 개요

Visium과 같은 공간을 활용하는 기술은 정의된 공간 위치에서 경계심을 포착하지만 많은 플랫폼은 다세포 분리 기능을 갖추고 있습니다. scvi-tools는 두 가지 주요 접근 방식을 제공합니다:

- **DestVI**: Deconvolution - 단일 셀 참조를 사용하여 각 지점에서 세포를 사용합니다.
- **resolVI**: 공간적 소수를 고려한 소수 범위 패턴을 학습하는 공간 모델 구축

## scvi-tools를 사용하는 방법

| 방법 | 설명 | 사용 사례 |
| -------- | ------------- | ---------- |
| **대상VI** | 디콘볼루션을 변형 가능 | 자리에 앉는다면 |
| **해결VI** | 공간 제한 모델 | 공간 표현 학습 |
| **조건SCVI** | DestVI의 참조 사진 | DestVI워크플로우에 필요 |

## 조건

```python
import scvi
import scanpy as sc
import squidpy as sq
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

---

## 1부: DestVI 디컨볼루션

### 1단계: 공간데이터 로드

```python
# Load Visium data
adata_spatial = sc.read_visium("spaceranger_output/")

# Check structure
print(f"Spots: {adata_spatial.n_obs}")
print(f"Genes: {adata_spatial.n_vars}")
print(f"Spatial coordinates: {adata_spatial.obsm['spatial'].shape}")

# Basic QC
sc.pp.calculate_qc_metrics(adata_spatial, inplace=True)
adata_spatial = adata_spatial[adata_spatial.obs['n_genes_by_counts'] > 200].copy()

# Store counts
adata_spatial.layers["counts"] = adata_spatial.X.copy()
```

### 2단계: 단일 셀 참조 로드

```python
# Load reference single-cell data
adata_sc = sc.read_h5ad("reference_scrna.h5ad")

# Requirements:
# - Raw counts
# - Cell type annotations
print(f"Reference cells: {adata_sc.n_obs}")
print(f"Cell types: {adata_sc.obs['cell_type'].nunique()}")
print(adata_sc.obs['cell_type'].value_counts())

# Store counts
adata_sc.layers["counts"] = adata_sc.X.copy()
```

### 3단계: 데이터 준비

```python
# DestVI requires gene overlap between reference and spatial
common_genes = adata_sc.var_names.intersection(adata_spatial.var_names)
print(f"Common genes: {len(common_genes)}")

adata_sc = adata_sc[:, common_genes].copy()
adata_spatial = adata_spatial[:, common_genes].copy()
```

### 4단계: 참조 모델 훈련(CondSCVI)

```python
# Train conditional scVI on reference data
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
# Setup spatial data
scvi.model.DestVI.setup_anndata(
    adata_spatial,
    layer="counts"
)

# Train DestVI using reference model
spatial_model = scvi.model.DestVI.from_rna_model(
    adata_spatial,
    sc_model
)

spatial_model.train(max_epochs=500)
```

### 6단계: 세포활동을 수행한다

```python
# Infer cell type proportions at each spot
proportions = spatial_model.get_proportions()

# Add to adata
for ct in adata_sc.obs['cell_type'].unique():
    adata_spatial.obs[f'prop_{ct}'] = proportions[ct]

# Visualize
sq.pl.spatial_scatter(
    adata_spatial,
    color=[f'prop_{ct}' for ct in adata_sc.obs['cell_type'].unique()[:6]],
    ncols=3
)
```

---

## 2부: resolVI 공간 모델

resolVI는 공간 데이터에서 직접적으로 공간 데이터를 활용하여 공간 인식을 표현하는 방법을 선택적으로 초기에 예측하는 방법입니다.

**참고**: resolVI는 `scvi.external`(`scvi.model`__)에 있습니다.

### 1단계: 공간데이터 준비

```python
# Load and preprocess
adata = sc.read_visium("spaceranger_output/")

# QC
sc.pp.calculate_qc_metrics(adata, inplace=True)
adata = adata[adata.obs['n_genes_by_counts'] > 200].copy()

# Store counts
adata.layers["counts"] = adata.X.copy()

# HVG selection
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=4000,
    flavor="seurat_v3",
    layer="counts"
)
adata = adata[:, adata.var['highly_variable']].copy()

# Optional: Get initial cell type predictions (e.g., from a reference)
# adata.obs["predicted_celltype"] = ...
```

### 2단계: resolvVI 설정 및 교육

```python
# Setup for resolVI (note: scvi.external, not scvi.model)
scvi.external.RESOLVI.setup_anndata(
    adata,
    labels_key="predicted_celltype",  # Initial cell type predictions
    layer="counts"
)

# Create model (semisupervised=True uses the labels)
model = scvi.external.RESOLVI(adata, semisupervised=True)

# Train
model.train(max_epochs=50)
```

### 3단계: 세포를 예측한다

```python
# Get refined cell type predictions
# soft=True returns probabilities, soft=False returns labels
cell_type_probs = model.predict(adata, num_samples=3, soft=True)
cell_type_labels = model.predict(adata, num_samples=3, soft=False)

adata.obs["resolvi_celltype"] = cell_type_labels

# Visualize
sq.pl.spatial_scatter(adata, color="resolvi_celltype")
```

### 4단계: 동작하는 표현

```python
# Get latent representation
adata.obsm["X_resolVI"] = model.get_latent_representation(adata)

# Cluster based on spatial representation
sc.pp.neighbors(adata, use_rep="X_resolVI")
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=0.5)

# Visualize clusters spatially
sq.pl.spatial_scatter(adata, color="leiden")
```

### 5단계: 미분 표현

```python
# DE between cell types using resolVI
de_results = model.differential_expression(
    adata,
    groupby="resolvi_celltype",
    group1="T_cell",
    group2="Tumor"
)

print(de_results.head(20))
```

### 6단계: 연결도 분석

```python
# Analyze how cell type neighborhoods differ between conditions
# Requires spatial neighbor graph
sq.gr.spatial_neighbors(adata, coord_type="generic")

niche_results = model.differential_niche_abundance(
    groupby="resolvi_celltype",
    group1="T_cell",
    group2="Tumor",
    neighbor_key="spatial_neighbors"
)
```

### 7단계: 쿼리 매핑(새 데이터로 전송)

```python
# Map new spatial data to trained model
query_adata = sc.read_visium("new_sample/")
query_adata.layers["counts"] = query_adata.X.copy()

# Prepare and load query
model.prepare_query_anndata(query_adata, reference_model=model)
query_model = model.load_query_data(query_adata, reference_model=model)

# Fine-tune on query
query_model.train(max_epochs=20)

# Get predictions for query
query_labels = query_model.predict(query_adata, num_samples=3, soft=False)
```

---

## 심상

### 공간적으로

```python
import matplotlib.pyplot as plt

# Plot multiple cell type proportions
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

### 지역별로

```python
# Cluster spatial data
sc.pp.neighbors(adata_spatial)
sc.tl.leiden(adata_spatial, resolution=0.5)

# Compare proportions across regions
import pandas as pd

cell_types = adata_sc.obs['cell_type'].unique()
prop_cols = [f'prop_{ct}' for ct in cell_types]
region_props = adata_spatial.obs.groupby('leiden')[prop_cols].mean()
print(region_props)

# Heatmap
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.heatmap(region_props.T, annot=True, cmap='viridis')
plt.title('Cell Type Proportions by Region')
```

### 셀 공간 활용 기능

```python
# Neighborhood enrichment using cell type assignments
sq.gr.spatial_neighbors(adata_spatial)

# Create "dominant cell type" annotation
prop_cols = [f'prop_{ct}' for ct in cell_types]
adata_spatial.obs['dominant_type'] = adata_spatial.obs[prop_cols].idxmax(axis=1)
adata_spatial.obs['dominant_type'] = adata_spatial.obs['dominant_type'].str.replace('prop_', '')

# Co-occurrence analysis
sq.gr.co_occurrence(adata_spatial, cluster_key='dominant_type')
sq.pl.co_occurrence(adata_spatial, cluster_key='dominant_type')
```

---

## DestVI 파이프라인 완성

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
    Perform spatial deconvolution using DestVI.

    Parameters
    ----------
    adata_spatial : AnnData
        Spatial transcriptomics data
    adata_ref : AnnData
        Single-cell reference with cell type annotations
    cell_type_key : str
        Column in adata_ref.obs with cell type labels
    n_latent : int
        Latent dimensions
    max_epochs_ref : int
        Training epochs for reference model
    max_epochs_spatial : int
        Training epochs for spatial model

    Returns
    -------
    AnnData with cell type proportions in obs
    """
    import scvi

    # Get common genes
    common_genes = adata_ref.var_names.intersection(adata_spatial.var_names)
    adata_ref = adata_ref[:, common_genes].copy()
    adata_spatial = adata_spatial[:, common_genes].copy()

    # Ensure counts are stored
    if "counts" not in adata_ref.layers:
        adata_ref.layers["counts"] = adata_ref.X.copy()
    if "counts" not in adata_spatial.layers:
        adata_spatial.layers["counts"] = adata_spatial.X.copy()

    # Train reference model
    scvi.model.CondSCVI.setup_anndata(
        adata_ref,
        layer="counts",
        labels_key=cell_type_key
    )

    ref_model = scvi.model.CondSCVI(adata_ref, n_latent=n_latent)
    ref_model.train(max_epochs=max_epochs_ref)

    # Train spatial model
    scvi.model.DestVI.setup_anndata(adata_spatial, layer="counts")

    spatial_model = scvi.model.DestVI.from_rna_model(
        adata_spatial,
        ref_model
    )
    spatial_model.train(max_epochs=max_epochs_spatial)

    # Get proportions
    proportions = spatial_model.get_proportions()

    cell_types = adata_ref.obs[cell_type_key].unique()
    for ct in cell_types:
        adata_spatial.obs[f'prop_{ct}'] = proportions[ct]

    # Add dominant type
    prop_cols = [f'prop_{ct}' for ct in cell_types]
    adata_spatial.obs['dominant_type'] = adata_spatial.obs[prop_cols].idxmax(axis=1)
    adata_spatial.obs['dominant_type'] = adata_spatial.obs['dominant_type'].str.replace('prop_', '')

    return adata_spatial, ref_model, spatial_model

# Usage
adata_spatial, ref_model, spatial_model = deconvolve_spatial(
    adata_spatial,
    adata_sc,
    cell_type_key="cell_type"
)

# Visualize
sq.pl.spatial_scatter(
    adata_spatial,
    color=['dominant_type', 'prop_T_cell', 'prop_Tumor'],
    ncols=3
)
```

---

## 문제 해결

| 문제 | 원인 | 해결책 |
| ------- | ------- | ---------- |
| 몇 가지 질문이 있습니다. | 다른 이유 | 특수 이름 변환(Ensembl ← Symbol) |
| 불량한 디콘볼루션 | 참조가 일치하지 않습니다. | 조직화 사용 |
| 모든 지역이 비슷한가요? | 엄청나게 평활화 | 다양한 종류의 조정, 선택 절단 |
| NaN | 세포에 존재하는 세포 | 예상되는 모든 유형을 참조하시기 바랍니다. |
| 힘든 훈련 | 우주공간 데이터세트 | max_epochs의 설명, 설명의 증가 |

## 주요 참고자료

- Lopezet al. (2022) "DestVI identifies continuums of cell types in spatial transcriptomics data"
- [scvi-tools spatial tutorials](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
