# MultiVI를 이용한 멀티옴 분석

이 참고 자료는 MultiVI를 사용한 멀티옴 실험의 공동 RNA 및 ATAC-seq 분석을 다룹니다.

## 개요

MultiVI는 멀티옴 데이터(동일한 세포의 RNA-seq 및 ATAC-seq 동시)를 분석하기 위한 심층 생성 모델입니다. 그것:
- 양식 전반에 걸쳐 공동 잠재 표현을 학습합니다.
- 누락된 양식 처리(RNA 전용 또는 ATAC 전용 셀)
- 실험 전반에 걸쳐 일괄 수정이 가능합니다.
- 누락된 양식의 대치 지원

## 전제 조건

```python
import scvi
import scanpy as sc
import mudata as md
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

## 데이터 형식

### 옵션 1: MuData(권장)

```python
# Load multiome data as MuData
mdata = md.read("multiome.h5mu")

# Structure:
# mdata.mod['rna']  - AnnData with RNA counts
# mdata.mod['atac'] - AnnData with ATAC counts

print(f"RNA: {mdata.mod['rna'].shape}")
print(f"ATAC: {mdata.mod['atac'].shape}")
```

### 옵션 2: AnnData 개체 분리

```python
# Load separately
adata_rna = sc.read_h5ad("rna.h5ad")
adata_atac = sc.read_h5ad("atac.h5ad")

# Ensure same cells in same order
common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
adata_rna = adata_rna[common_cells].copy()
adata_atac = adata_atac[common_cells].copy()
```

## 1단계: RNA 데이터 준비

```python
# RNA preprocessing (standard scvi-tools pipeline)
adata_rna = mdata.mod['rna'].copy()

# Filter
sc.pp.filter_cells(adata_rna, min_genes=200)
sc.pp.filter_genes(adata_rna, min_cells=3)

# Store counts
adata_rna.layers["counts"] = adata_rna.X.copy()

# HVG selection
sc.pp.highly_variable_genes(
    adata_rna,
    n_top_genes=4000,
    flavor="seurat_v3",
    layer="counts",
    batch_key="batch"  # If multiple batches
)

# Subset to HVGs
adata_rna = adata_rna[:, adata_rna.var['highly_variable']].copy()
```

## 2단계: ATAC 데이터 준비

```python
# ATAC preprocessing
adata_atac = mdata.mod['atac'].copy()

# Filter peaks
sc.pp.filter_genes(adata_atac, min_cells=10)

# Binarize accessibility
adata_atac.X = (adata_atac.X > 0).astype(np.float32)

# Select top accessible peaks (if too many)
if adata_atac.n_vars > 50000:
    peak_accessibility = np.array(adata_atac.X.sum(axis=0)).flatten()
    top_peaks = np.argsort(peak_accessibility)[-50000:]
    adata_atac = adata_atac[:, top_peaks].copy()

# Store in layer
adata_atac.layers["counts"] = adata_atac.X.copy()
```

## 3단계: 결합된 MuData 생성

```python
# Ensure matching cells
common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
adata_rna = adata_rna[common_cells].copy()
adata_atac = adata_atac[common_cells].copy()

# Create MuData
mdata = md.MuData({
    "rna": adata_rna,
    "atac": adata_atac
})

print(f"Combined multiome: {mdata.n_obs} cells")
print(f"RNA features: {mdata.mod['rna'].n_vars}")
print(f"ATAC features: {mdata.mod['atac'].n_vars}")
```

## 4단계: MultiVI 설정

```python
# Setup MuData for MultiVI
scvi.model.MULTIVI.setup_mudata(
    mdata,
    rna_layer="counts",
    atac_layer="counts",
    batch_key="batch",  # Optional
    modalities={
        "rna_layer": "rna",
        "batch_key": "rna",
        "atac_layer": "atac"
    }
)
```

## 5단계: MultiVI 훈련

```python
# Create model
model = scvi.model.MULTIVI(
    mdata,
    n_latent=20,
    n_layers_encoder=2,
    n_layers_decoder=2
)

# Train
model.train(
    max_epochs=300,
    early_stopping=True,
    early_stopping_patience=10,
    batch_size=128
)

# Check training
model.history['elbo_train'].plot()
```

## 6단계: 공동 대표 확보

```python
# Latent representation
latent = model.get_latent_representation()

# Add to MuData
mdata.obsm["X_MultiVI"] = latent

# Clustering on joint space
sc.pp.neighbors(mdata, use_rep="X_MultiVI")
sc.tl.umap(mdata)
sc.tl.leiden(mdata, resolution=1.0)

# Visualize
sc.pl.umap(mdata, color=['leiden', 'batch'], ncols=2)
```

## 7단계: 양식별 분석

### 누락된 양식 대치

```python
# Impute RNA expression for ATAC-only cells
# (Useful when integrating with ATAC-only datasets)
imputed_rna = model.get_normalized_expression(
    modality="rna"
)

# Impute accessibility for RNA-only cells
imputed_atac = model.get_accessibility_estimates()
```

### 차별 분석

```python
# Differential expression (RNA)
de_results = model.differential_expression(
    groupby="leiden",
    group1="0",
    group2="1"
)

# Differential accessibility (ATAC)
da_results = model.differential_accessibility(
    groupby="leiden",
    group1="0",
    group2="1"
)
```

## 부분 데이터 처리

MultiVI는 단 하나의 형식으로 데이터세트를 통합할 수 있습니다:

```python
# Dataset 1: Full multiome
# Dataset 2: RNA only
# Dataset 3: ATAC only

# Mark missing modalities
mdata.obs['modality'] = 'paired'  # For cells with both
# For RNA-only cells, ATAC data should be missing/NaN
# For ATAC-only cells, RNA data should be missing/NaN

# MultiVI handles this automatically during training
```

## 파이프라인 완성

```python
def analyze_multiome(
    adata_rna,
    adata_atac,
    batch_key=None,
    n_top_genes=4000,
    n_top_peaks=50000,
    n_latent=20,
    max_epochs=300
):
    """
    Complete multiome analysis with MultiVI.

    Parameters
    ----------
    adata_rna : AnnData
        RNA count data
    adata_atac : AnnData
        ATAC peak data
    batch_key : str, optional
        Batch column name
    n_top_genes : int
        Number of HVGs for RNA
    n_top_peaks : int
        Number of top peaks for ATAC
    n_latent : int
        Latent dimensions
    max_epochs : int
        Maximum training epochs

    Returns
    -------
    MuData with joint representation
    """
    import scvi
    import scanpy as sc
    import mudata as md
    import numpy as np

    # Get common cells
    common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
    adata_rna = adata_rna[common_cells].copy()
    adata_atac = adata_atac[common_cells].copy()

    # RNA preprocessing
    sc.pp.filter_genes(adata_rna, min_cells=3)
    adata_rna.layers["counts"] = adata_rna.X.copy()

    if batch_key:
        sc.pp.highly_variable_genes(
            adata_rna, n_top_genes=n_top_genes,
            flavor="seurat_v3", layer="counts", batch_key=batch_key
        )
    else:
        sc.pp.normalize_total(adata_rna, target_sum=1e4)
        sc.pp.log1p(adata_rna)
        sc.pp.highly_variable_genes(adata_rna, n_top_genes=n_top_genes)
        adata_rna.X = adata_rna.layers["counts"].copy()

    adata_rna = adata_rna[:, adata_rna.var['highly_variable']].copy()

    # ATAC preprocessing
    sc.pp.filter_genes(adata_atac, min_cells=10)
    adata_atac.X = (adata_atac.X > 0).astype(np.float32)

    if adata_atac.n_vars > n_top_peaks:
        peak_acc = np.array(adata_atac.X.sum(axis=0)).flatten()
        top_idx = np.argsort(peak_acc)[-n_top_peaks:]
        adata_atac = adata_atac[:, top_idx].copy()

    adata_atac.layers["counts"] = adata_atac.X.copy()

    # Create MuData
    mdata = md.MuData({"rna": adata_rna, "atac": adata_atac})

    # Setup and train
    scvi.model.MULTIVI.setup_mudata(
        mdata,
        rna_layer="counts",
        atac_layer="counts",
        batch_key=batch_key,
        modalities={"rna_layer": "rna", "batch_key": "rna", "atac_layer": "atac"}
    )

    model = scvi.model.MULTIVI(mdata, n_latent=n_latent)
    model.train(max_epochs=max_epochs, early_stopping=True)

    # Add representation
    mdata.obsm["X_MultiVI"] = model.get_latent_representation()

    # Cluster
    sc.pp.neighbors(mdata, use_rep="X_MultiVI")
    sc.tl.umap(mdata)
    sc.tl.leiden(mdata)

    return mdata, model


# Usage
mdata, model = analyze_multiome(
    adata_rna,
    adata_atac,
    batch_key="sample"
)

sc.pl.umap(mdata, color=['leiden', 'sample'])
```

## 피크-유전자 연결

```python
# Link ATAC peaks to genes based on correlation in latent space
# This identifies regulatory relationships

def link_peaks_to_genes(model, mdata, distance_threshold=100000):
    """
    Link peaks to nearby genes based on correlation.

    Parameters
    ----------
    model : MULTIVI
        Trained model
    mdata : MuData
        Multiome data
    distance_threshold : int
        Maximum distance (bp) to link peak to gene

    Returns
    -------
    DataFrame of peak-gene links
    """
    # Get imputed values
    rna_imputed = model.get_normalized_expression()
    atac_imputed = model.get_accessibility_estimates()

    # Correlate peak accessibility with gene expression
    # for peaks near gene promoters
    # ... (requires genomic coordinates)

    return peak_gene_links
```

## 문제 해결

| 이슈 | 원인 | 솔루션 |
|---------|-------|----------|
| 다양한 세포 수 | 한 가지 양식에서 세포가 누락됨 | 공통 셀만 사용 |
| 훈련 불안정 | 불균형 양식 | 기능 수 정규화 |
| 불량한 클러스터링 | 기능이 너무 적음 | n_top_genes/peaks 증가 |
| 메모리 오류 | 대형 ATAC 매트릭스 | 피크 수를 줄이고 스파스 사용 |
| 배치가 지배적 | 강력한 기술적 효과 | Batch_key가 설정되어 있는지 확인 |

## 주요 참고자료

- Ashuach 등. (2023) "MultiVI: 다중 모드 데이터 통합을 위한 심층 생성 모델"
