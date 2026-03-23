# totalVI를 사용한 CITE-seq 분석

이 참고 자료는 totalVI를 사용한 CITE-seq 데이터(RNA + 표면 단백질)의 다중 모드 분석을 다룹니다.

## 개요

CITE-seq는 다음을 결합합니다.
- scRNA-seq(전사체)
- 단백질 표면마커(항체유래태그, ADT)

totalVI는 두 가지 방식을 공동으로 모델링하여 다음을 수행합니다.
- 여러 배치에 걸쳐 통합
- 단백질 신호 제거
- 공동 잠재 표현 학습
- 교차 모달 대체 활성화

## 전제 조건

```python
import scvi
import scanpy as sc
import mudata as md
import numpy as np
import pandas as pd

print(f"scvi-tools version: {scvi.__version__}")
```

## 1단계: CITE-seq 데이터 로드

### 10x Genomics(셀 레인저)에서

```python
# 10x outputs separate gene expression and feature barcoding
adata_rna = sc.read_10x_h5("filtered_feature_bc_matrix.h5", gex_only=False)

# Separate RNA and protein
adata_protein = adata_rna[:, adata_rna.var['feature_types'] == 'Antibody Capture'].copy()
adata_rna = adata_rna[:, adata_rna.var['feature_types'] == 'Gene Expression'].copy()

print(f"RNA: {adata_rna.shape}")
print(f"Protein: {adata_protein.shape}")
```

### MuData에서

```python
# If data is in MuData format
mdata = md.read_h5mu("cite_seq.h5mu")

adata_rna = mdata['rna'].copy()
adata_protein = mdata['protein'].copy()
```

### 단일 AnnData로 결합

```python
# totalVI expects protein data in obsm
adata = adata_rna.copy()

# Add protein expression to obsm
adata.obsm["protein_expression"] = adata_protein.X.toarray() if hasattr(adata_protein.X, 'toarray') else adata_protein.X

# Store protein names
adata.uns["protein_names"] = list(adata_protein.var_names)
```

## 2단계: 품질 관리

### RNA QC

```python
# Standard RNA QC
# Handle both human (MT-) and mouse (mt-, Mt-) mitochondrial genes
    adata.var['mt'] = (
        adata.var_names.str.startswith('MT-') |
        adata.var_names.str.startswith('mt-') |
        adata.var_names.str.startswith('Mt-')
    )
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)

# Filter cells
adata = adata[adata.obs['n_genes_by_counts'] > 200].copy()
adata = adata[adata.obs['pct_counts_mt'] < 20].copy()

# Filter genes
sc.pp.filter_genes(adata, min_cells=3)
```

### 단백질 QC

```python
# Protein QC
protein_counts = adata.obsm["protein_expression"]
print(f"Protein counts per cell: min={protein_counts.sum(1).min():.0f}, max={protein_counts.sum(1).max():.0f}")

# Check for isotype controls
# Isotype controls should have low counts
protein_names = adata.uns["protein_names"]
for i, name in enumerate(protein_names):
    if 'isotype' in name.lower() or 'control' in name.lower():
        print(f"{name}: mean={protein_counts[:, i].mean():.1f}")
```

## 3단계: 데이터 준비

### 원시 개수 저장

```python
# Store RNA counts
adata.layers["counts"] = adata.X.copy()

# Protein must be raw ADT counts (NOT CLR-normalized)
# WARNING: If importing from Seurat, ensure you use raw counts, not CLR-normalized data
# Seurat's NormalizeData(normalization.method = "CLR") transforms counts - use the original assay
```

### RNA용 HVG 선택

```python
# Select HVGs for RNA
# Note: totalVI uses all proteins regardless of HVG

sc.pp.highly_variable_genes(
    adata,
    n_top_genes=4000,  # Use more for CITE-seq
    flavor="seurat_v3",
    batch_key="batch" if "batch" in adata.obs else None,
    layer="counts"
)

# Subset to HVGs
adata = adata[:, adata.var["highly_variable"]].copy()
```

## 4단계: totalVI 설정 및 교육

```python
# Setup AnnData for totalVI
scvi.model.TOTALVI.setup_anndata(
    adata,
    layer="counts",
    protein_expression_obsm_key="protein_expression",
    batch_key="batch"  # Optional
)

# Create model
model = scvi.model.TOTALVI(
    adata,
    n_latent=20,
    latent_distribution="normal"  # or "ln" for log-normal
)

# Train
model.train(
    max_epochs=200,
    early_stopping=True,
    batch_size=128
)

# Check training
model.history['elbo_train'].plot()
```

## 5단계: 잠재 표현 얻기

```python
# Joint latent space
adata.obsm["X_totalVI"] = model.get_latent_representation()

# Clustering and visualization
sc.pp.neighbors(adata, use_rep="X_totalVI")
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=1.0)

sc.pl.umap(adata, color=['leiden', 'batch'])
```

## 6단계: 잡음 제거된 단백질 발현

```python
# Get denoised protein values
# This removes background noise from protein measurements

_, protein_denoised = model.get_normalized_expression(
    return_mean=True,
    transform_batch="batch1"  # Optional: normalize to specific batch
)

# Add to adata
adata.obsm["protein_denoised"] = protein_denoised

# Visualize denoised proteins
protein_names = adata.uns["protein_names"]
for i, protein in enumerate(protein_names[:5]):
    adata.obs[f"denoised_{protein}"] = protein_denoised[:, i]

sc.pl.umap(adata, color=[f"denoised_{p}" for p in protein_names[:5]])
```

## 7단계: 표준화된 RNA 발현

```python
# Get normalized RNA expression
rna_normalized, _ = model.get_normalized_expression(
    return_mean=True
)

# Store
adata.layers["totalVI_normalized"] = rna_normalized
```

## 8단계: 미분 표현

### RNA 차등 발현

```python
# DE between clusters
de_rna = model.differential_expression(
    groupby="leiden",
    group1="0",
    group2="1"
)

# Filter significant genes
de_sig = de_rna[
    (de_rna['is_de_fdr_0.05']) &
    (abs(de_rna['lfc_mean']) > 1)
]

print(f"Significant DE genes: {len(de_sig)}")
```

### 단백질 차등 발현

```python
# Protein DE
de_protein = model.differential_expression(
    groupby="leiden",
    group1="0",
    group2="1",
    mode="protein"
)

print(de_protein.head(20))
```

## 9단계: 시각화

### UMAP의 단백질 발현

```python
# Denoised protein on UMAP
import matplotlib.pyplot as plt

proteins_to_plot = ["CD3", "CD4", "CD8", "CD19", "CD14"]

fig, axes = plt.subplots(1, len(proteins_to_plot), figsize=(4*len(proteins_to_plot), 4))
for ax, protein in zip(axes, proteins_to_plot):
    idx = adata.uns["protein_names"].index(protein)
    sc.pl.umap(
        adata,
        color=adata.obsm["protein_denoised"][:, idx],
        ax=ax,
        title=protein,
        show=False
    )
plt.tight_layout()
```

### 공동 히트맵

```python
# Heatmap of top genes and proteins per cluster
sc.pl.dotplot(
    adata,
    var_names=de_sig.index[:20].tolist(),
    groupby="leiden",
    layer="totalVI_normalized"
)
```

## 10단계: 셀 유형 주석

```python
# Use both RNA and protein markers for annotation

# RNA markers
rna_markers = {
    'T cells': ['CD3D', 'CD3E'],
    'CD4 T': ['CD4'],
    'CD8 T': ['CD8A', 'CD8B'],
    'B cells': ['CD19', 'MS4A1'],
    'Monocytes': ['CD14', 'LYZ']
}

# Check denoised protein expression
for i, protein in enumerate(adata.uns["protein_names"]):
    if any(m in protein for m in ['CD3', 'CD4', 'CD8', 'CD19', 'CD14']):
        print(f"{protein}: cluster means")
        for cluster in adata.obs['leiden'].unique():
            mask = adata.obs['leiden'] == cluster
            mean_expr = adata.obsm["protein_denoised"][mask, i].mean()
            print(f"  Cluster {cluster}: {mean_expr:.2f}")
```

## 파이프라인 완성

```python
def analyze_citeseq(
    adata_rna,
    adata_protein,
    batch_key=None,
    n_top_genes=4000,
    n_latent=20
):
    """
    Complete CITE-seq analysis with totalVI.
    
    Parameters
    ----------
    adata_rna : AnnData
        RNA expression (raw counts)
    adata_protein : AnnData
        Protein expression (raw counts)
    batch_key : str, optional
        Batch column in obs
    n_top_genes : int
        Number of HVGs
    n_latent : int
        Latent dimensions
        
    Returns
    -------
    Tuple of (processed AnnData, trained model)
    """
    import scvi
    import scanpy as sc
    
    # Ensure same cells
    common_cells = adata_rna.obs_names.intersection(adata_protein.obs_names)
    adata = adata_rna[common_cells].copy()
    adata_protein = adata_protein[common_cells].copy()
    
    # Add protein to obsm
    adata.obsm["protein_expression"] = adata_protein.X.toarray() if hasattr(adata_protein.X, 'toarray') else adata_protein.X
    adata.uns["protein_names"] = list(adata_protein.var_names)
    
    # RNA QC
    # Handle both human (MT-) and mouse (mt-, Mt-) mitochondrial genes
    adata.var['mt'] = (
        adata.var_names.str.startswith('MT-') |
        adata.var_names.str.startswith('mt-') |
        adata.var_names.str.startswith('Mt-')
    )
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)
    adata = adata[adata.obs['pct_counts_mt'] < 20].copy()
    sc.pp.filter_genes(adata, min_cells=3)
    
    # Store counts
    adata.layers["counts"] = adata.X.copy()
    
    # HVG selection
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=n_top_genes,
        flavor="seurat_v3",
        batch_key=batch_key,
        layer="counts"
    )
    adata = adata[:, adata.var["highly_variable"]].copy()
    
    # Setup totalVI
    scvi.model.TOTALVI.setup_anndata(
        adata,
        layer="counts",
        protein_expression_obsm_key="protein_expression",
        batch_key=batch_key
    )
    
    # Train
    model = scvi.model.TOTALVI(adata, n_latent=n_latent)
    model.train(max_epochs=200, early_stopping=True)
    
    # Get representations
    adata.obsm["X_totalVI"] = model.get_latent_representation()
    rna_norm, protein_denoised = model.get_normalized_expression(return_mean=True)
    adata.layers["totalVI_normalized"] = rna_norm
    adata.obsm["protein_denoised"] = protein_denoised
    
    # Clustering
    sc.pp.neighbors(adata, use_rep="X_totalVI")
    sc.tl.umap(adata)
    sc.tl.leiden(adata)
    
    return adata, model

# Usage
adata, model = analyze_citeseq(
    adata_rna,
    adata_protein,
    batch_key="batch"
)

# Visualize
sc.pl.umap(adata, color=['leiden', 'batch'])
```

## 문제 해결

| 이슈 | 원인 | 솔루션 |
|---------|-------|----------|
| 시끄러운 단백질 신호 | 배경이 제거되지 않음 | 잡음 제거와 함께 get_normalized_expression 사용 |
| 일괄 효과가 지속됨 | 배치_키 필요 | Batch_key가 지정되었는지 확인 |
| 메모리 오류 | 유전자가 너무 많습니다 | n_top_genes 감소 |
| 불량한 단백질 클러스터링 | 단백질이 거의 | 일반 - totalVI는 구조에 RNA를 사용합니다 |

## 주요 참고자료

- Gayoso 외. (2021) "totalVI를 사용한 단일 세포 다중 오믹 데이터의 공동 확률 모델링"
