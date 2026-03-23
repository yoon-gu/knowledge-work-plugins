# sysVI를 사용한 고급 일괄 수정

이 참조 자료는 주요 기술 또는 연구 차이점에 걸쳐 데이터를 통합하기 위해 설계된 sysVI를 사용한 시스템 수준 배치 수정을 다룹니다.

## 개요

sysVI(시스템 변형 추론)는 다음과 같은 시나리오에 대해 scVI를 확장합니다.
- 배치 효과가 매우 강함(다른 기술)
- 표준 scVI는 생물학적 신호를 과도하게 수정합니다.
- 생물학적 변이와 "시스템" 효과를 분리해야 합니다.

## sysVI와 scVI를 언제 사용해야 할까요?

| 시나리오 | 추천 모델 |
|------------|------|
| 동일한 기술, 다른 샘플 | scVI |
| 10x v2 대 10x v3 | scVI (보통) |
| 10x 대 Smart-seq2 | 시스템VI |
| 다양한 시퀀싱 깊이 | 공변량이 있는 scVI |
| 연구 간 통합 | 시스템VI |
| Atlas 규모의 통합 | 시스템VI |

## 전제 조건

```python
import scvi
import scanpy as sc
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

## sysVI 아키텍처 이해

sysVI는 변형을 다음과 같이 분리합니다.
1. **생물학적 변이**: 세포 유형, 상태, 궤적
2. **시스템 변형**: 기술, 연구, 실험실 효과

```
                    ┌─────────────────┐
Input counts ──────►│    Encoder      │
                    │                 │
System info ───────►│  (conditioned)  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Latent z      │
                    │  (biological)   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
System info ───────►│    Decoder      │
                    │  (conditioned)  │
                    └────────┬────────┘
                             │
                    Reconstructed counts
```

## 기본 sysVI 작업 흐름

### 1단계: 데이터 준비

```python
# Load datasets from different systems
adata1 = sc.read_h5ad("10x_data.h5ad")
adata2 = sc.read_h5ad("smartseq_data.h5ad")

# Add system labels
adata1.obs["system"] = "10x"
adata2.obs["system"] = "Smart-seq2"

# Add batch labels (within system)
# e.g., different samples within each technology

# Concatenate
adata = sc.concat([adata1, adata2])

# Store raw counts
adata.layers["counts"] = adata.X.copy()
```

### 2단계: HVG 선택

```python
# Select HVGs considering both batch and system
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=4000,  # More genes for cross-system
    flavor="seurat_v3",
    batch_key="system",  # Consider system for HVG
    layer="counts"
)

# Optionally: ensure overlap between systems
# Check HVGs are expressed in both systems
adata = adata[:, adata.var["highly_variable"]].copy()
```

### 3단계: sysVI 설정 및 교육

```python
# Setup AnnData
# Note: sysVI may be accessed differently depending on version
# Check scvi-tools documentation for current API

scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="sample",           # Within-system batches
    categorical_covariate_keys=["system"]  # System-level covariate
)

# For true sysVI (if available in your version)
# scvi.model.SysVI.setup_anndata(...)

# Create model with system awareness
model = scvi.model.SCVI(
    adata,
    n_latent=30,
    n_layers=2,
    gene_likelihood="nb"
)

# Train
model.train(max_epochs=300)
```

### 4단계: 표현 추출

```python
# Get latent representation
adata.obsm["X_integrated"] = model.get_latent_representation()

# Clustering and visualization
sc.pp.neighbors(adata, use_rep="X_integrated")
sc.tl.umap(adata)
sc.tl.leiden(adata)

# Check integration
sc.pl.umap(adata, color=["system", "leiden", "cell_type"])
```

## 대안: 하모니 + scVI

시스템 간 통합의 경우 방법을 결합하는 것이 효과적일 수 있습니다.

```python
import scanpy.external as sce

# First run PCA
sc.pp.pca(adata)

# Apply Harmony for initial alignment
sce.pp.harmony_integrate(adata, key="system")

# Then train scVI on Harmony-corrected embedding
# Or use Harmony representation directly
```

## 대안: scVI에서 공변량 사용

적당한 시스템 효과의 경우:

```python
# Include system as categorical covariate
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="sample",
    categorical_covariate_keys=["system", "technology_version"]
)

model = scvi.model.SCVI(adata, n_latent=30)
model.train()
```

## 대안: 별도의 모델 + 통합

매우 다른 시스템의 경우:

```python
# Train separate models
scvi.model.SCVI.setup_anndata(adata1, layer="counts", batch_key="sample")
model1 = scvi.model.SCVI(adata1)
model1.train()

scvi.model.SCVI.setup_anndata(adata2, layer="counts", batch_key="sample")
model2 = scvi.model.SCVI(adata2)
model2.train()

# Get latent spaces
adata1.obsm["X_scVI"] = model1.get_latent_representation()
adata2.obsm["X_scVI"] = model2.get_latent_representation()

# Align with CCA or Harmony
# ... additional alignment step
```

## 시스템 간 통합 평가

### 시각적 평가

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Color by system
sc.pl.umap(adata, color="system", ax=axes[0], show=False, title="By System")

# Color by cell type
sc.pl.umap(adata, color="cell_type", ax=axes[1], show=False, title="By Cell Type")

# Color by expression of marker
sc.pl.umap(adata, color="CD3D", ax=axes[2], show=False, title="CD3D Expression")

plt.tight_layout()
```

### 정량적 지표

```python
# Using scib-metrics
from scib_metrics.benchmark import Benchmarker

bm = Benchmarker(
    adata,
    batch_key="system",
    label_key="cell_type",
    embedding_obsm_keys=["X_integrated"]
)

bm.benchmark()

# Key metrics:
# - Batch mixing (ASW_batch, Graph connectivity)
# - Bio conservation (NMI, ARI, ASW_label)
```

### LISI 점수

```python
# Local Inverse Simpson's Index
from scib_metrics import lisi

# Batch LISI (higher = better mixing)
batch_lisi = lisi.ilisi_graph(
    adata,
    batch_key="system",
    use_rep="X_integrated"
)

# Cell type LISI (lower = better preservation)
ct_lisi = lisi.clisi_graph(
    adata,
    label_key="cell_type", 
    use_rep="X_integrated"
)

print(f"Batch LISI: {batch_lisi.mean():.3f}")
print(f"Cell type LISI: {ct_lisi.mean():.3f}")
```

## 특정 과제 처리

### 다양한 유전자 세트

```python
# Find common genes
common_genes = adata1.var_names.intersection(adata2.var_names)
print(f"Common genes: {len(common_genes)}")

# If too few, use gene mapping
# Or impute missing genes
```

### 다양한 시퀀싱 깊이

```python
# Add depth as continuous covariate
adata.obs["log_counts"] = np.log1p(adata.obs["total_counts"])

scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="sample",
    continuous_covariate_keys=["log_counts"]
)
```

### 불균형 세포 유형

```python
# Check cell type distribution per system
import pandas as pd

ct_dist = pd.crosstab(adata.obs["system"], adata.obs["cell_type"], normalize="index")
print(ct_dist)

# If very unbalanced, consider:
# 1. Subsample to balance
# 2. Use scANVI with labels to preserve rare types
```

## 파이프라인 완성

```python
def integrate_cross_system(
    adatas: dict,
    system_key: str = "system",
    batch_key: str = "batch",
    cell_type_key: str = "cell_type",
    n_top_genes: int = 4000,
    n_latent: int = 30
):
    """
    Integrate datasets from different technological systems.
    
    Parameters
    ----------
    adatas : dict
        Dictionary of {system_name: AnnData}
    system_key : str
        Key for system annotation
    batch_key : str
        Key for within-system batch
    cell_type_key : str
        Key for cell type labels (optional)
    n_top_genes : int
        Number of HVGs
    n_latent : int
        Latent dimensions
        
    Returns
    -------
    Integrated AnnData with model
    """
    import scvi
    import scanpy as sc
    
    # Add system labels and concatenate
    for system_name, adata in adatas.items():
        adata.obs[system_key] = system_name
    
    adata = sc.concat(list(adatas.values()))
    
    # Find common genes
    for name, ad in adatas.items():
        if name == list(adatas.keys())[0]:
            common_genes = set(ad.var_names)
        else:
            common_genes = common_genes.intersection(ad.var_names)
    
    adata = adata[:, list(common_genes)].copy()
    print(f"Common genes: {len(common_genes)}")
    
    # Store counts
    adata.layers["counts"] = adata.X.copy()
    
    # HVG selection
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=n_top_genes,
        flavor="seurat_v3",
        batch_key=system_key,
        layer="counts"
    )
    adata = adata[:, adata.var["highly_variable"]].copy()
    
    # Setup with system as covariate
    scvi.model.SCVI.setup_anndata(
        adata,
        layer="counts",
        batch_key=batch_key if batch_key in adata.obs else None,
        categorical_covariate_keys=[system_key]
    )
    
    # Train
    model = scvi.model.SCVI(adata, n_latent=n_latent, n_layers=2)
    model.train(max_epochs=300, early_stopping=True)
    
    # Get representation
    adata.obsm["X_integrated"] = model.get_latent_representation()
    
    # Clustering
    sc.pp.neighbors(adata, use_rep="X_integrated")
    sc.tl.umap(adata)
    sc.tl.leiden(adata)
    
    return adata, model

# Usage
adatas = {
    "10x_v3": sc.read_h5ad("10x_v3_data.h5ad"),
    "Smart-seq2": sc.read_h5ad("smartseq_data.h5ad"),
    "Drop-seq": sc.read_h5ad("dropseq_data.h5ad")
}

adata_integrated, model = integrate_cross_system(adatas)

# Visualize
sc.pl.umap(adata_integrated, color=["system", "leiden"])
```

## 문제 해결

| 이슈 | 원인 | 솔루션 |
|---------|-------|----------|
| 시스템은 혼합되지 않습니다 | 효과가 너무 강함 | 더 많은 유전자를 사용하고 n_latent를 늘리세요 |
| 과잉교정 | 너무 공격적인 모델 | n_layers를 줄이고 scANVI |
| 몇 가지 공통 유전자 | 다양한 플랫폼 | 유전자 이름 매핑 사용 |
| 하나의 시스템이 지배적 | 불균형한 크기 | 더 큰 데이터 세트 서브샘플 |

## 주요 참고자료

- 로페즈 외. (2018) "단일 세포 전사체학을 위한 심층 생성 모델링"
- Luecken 외. (2022) "단일 세포 유전체학의 아틀라스 수준 데이터 통합 ​​벤치마킹"
