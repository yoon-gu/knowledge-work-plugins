# scVI 및 scANVI와 scRNA-seq 통합

이 참조 자료에서는 scVI(비지도) 및 scANVI(셀 유형 레이블을 사용한 반지도)를 사용한 일괄 수정 및 데이터 세트 통합을 다룹니다.

## 개요

단일 셀 데이터 세트에는 다음과 같은 일괄 효과가 있는 경우가 많습니다.
- 다양한 기증자/환자
- 다양한 실험 배치
- 다양한 기술(10x v2 대 v3)
- 다양한 연구

scVI 및 scANVI는 생물학적 변이가 보존되는 동안 배치 효과가 제거되는 공유 잠재 공간을 학습합니다.

## 언제 어떤 모델을 사용해야 하는가

| 모델 | 사용 시기 | 필요한 라벨 |
|-------|----------|---------------|
| **scVI** | 사용 가능한 라벨이 없습니다. 탐색적 분석 | 아니요 |
| **scANVI** | 부분/전체 라벨이 있고 더 나은 보존을 원함 | 예(일부 OK) |

## scVI 통합 작업 흐름

### 1단계: 데이터 준비

```python
import scvi
import scanpy as sc

# Load datasets
adata1 = sc.read_h5ad("dataset1.h5ad")
adata2 = sc.read_h5ad("dataset2.h5ad")

# Add batch annotation
adata1.obs["batch"] = "batch1"
adata2.obs["batch"] = "batch2"

# Concatenate
adata = sc.concat([adata1, adata2], label="batch")

# Ensure we have raw counts
# If data is normalized, recover from .raw
if hasattr(adata, 'raw') and adata.raw is not None:
    adata = adata.raw.to_adata()

# Store counts
adata.layers["counts"] = adata.X.copy()
```

### 2단계: 배치 전반에 걸쳐 HVG 선택

```python
# Select HVGs considering batch
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2000,
    flavor="seurat_v3",
    batch_key="batch",
    layer="counts"
)

# Subset to HVGs
adata = adata[:, adata.var["highly_variable"]].copy()
```

### 3단계: scVI 설정 및 교육

```python
# Register data with scVI
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch"
)

# Create model
model = scvi.model.SCVI(
    adata,
    n_latent=30,          # Latent dimensions
    n_layers=2,           # Encoder/decoder depth
    gene_likelihood="nb"  # negative binomial (or "zinb")
)

# Train
model.train(
    max_epochs=200,
    early_stopping=True,
    early_stopping_patience=10,
    batch_size=128
)

# Plot training history
model.history["elbo_train"].plot()
```

### 4단계: 통합 표현 얻기

```python
# Get latent representation
adata.obsm["X_scVI"] = model.get_latent_representation()

# Use for clustering and visualization
sc.pp.neighbors(adata, use_rep="X_scVI", n_neighbors=15)
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=1.0)

# Visualize integration
sc.pl.umap(adata, color=["batch", "leiden"], ncols=2)
```

### 5단계: 모델 저장

```python
# Save model for later use
model.save("scvi_model/")

# Load model
model = scvi.model.SCVI.load("scvi_model/", adata=adata)
```

## scANVI 통합 워크플로

scANVI는 더 나은 생물학적 보존을 위해 세포 유형 라벨로 scVI를 확장합니다.

### 1단계: 라벨을 사용하여 데이터 준비

```python
# Labels should be in adata.obs
# Use "Unknown" for unlabeled cells
print(adata.obs["cell_type"].value_counts())

# For partially labeled data
# Mark unlabeled cells
adata.obs["cell_type_scanvi"] = adata.obs["cell_type"].copy()
# adata.obs.loc[unlabeled_mask, "cell_type_scanvi"] = "Unknown"
```

### 2단계: 옵션 A - 처음부터 scANVI 교육

```python
# Setup for scANVI
scvi.model.SCANVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    labels_key="cell_type"
)

# Create model
scanvi_model = scvi.model.SCANVI(
    adata,
    n_latent=30,
    n_layers=2
)

# Train
scanvi_model.train(max_epochs=200)
```

### 2단계: 옵션 B - scVI에서 scANVI 초기화(권장)

```python
# First train scVI
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
scvi_model = scvi.model.SCVI(adata, n_latent=30)
scvi_model.train(max_epochs=200)

# Initialize scANVI from scVI
scanvi_model = scvi.model.SCANVI.from_scvi_model(
    scvi_model,
    labels_key="cell_type",
    unlabeled_category="Unknown"  # For partially labeled data
)

# Fine-tune scANVI (fewer epochs needed)
scanvi_model.train(max_epochs=50)
```

### 3단계: 결과 얻기

```python
# Latent representation
adata.obsm["X_scANVI"] = scanvi_model.get_latent_representation()

# Predicted labels for unlabeled cells
predictions = scanvi_model.predict()
adata.obs["predicted_cell_type"] = predictions

# Prediction probabilities
soft_predictions = scanvi_model.predict(soft=True)

# Visualization
sc.pp.neighbors(adata, use_rep="X_scANVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color=["batch", "cell_type", "predicted_cell_type"])
```

## 통합 품질 비교

### 시각적 평가

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Before integration (on PCA)
sc.pp.pca(adata)
sc.pl.pca(adata, color="batch", ax=axes[0], title="Before (PCA)", show=False)

# After scVI
sc.pp.neighbors(adata, use_rep="X_scVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color="batch", ax=axes[1], title="After scVI", show=False)

# After scANVI
sc.pp.neighbors(adata, use_rep="X_scANVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color="batch", ax=axes[2], title="After scANVI", show=False)

plt.tight_layout()
```

### 정량적 측정항목(scib)

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

## 미분 표현

scVI는 배치 효과를 설명하는 미분 표현을 제공합니다.

```python
# DE between groups
de_results = model.differential_expression(
    groupby="cell_type",
    group1="T cells",
    group2="B cells"
)

# Filter significant
de_sig = de_results[
    (de_results["is_de_fdr_0.05"] == True) &
    (abs(de_results["lfc_mean"]) > 1)
]

print(de_sig.head(20))
```

## 고급: 다중 범주형 공변량

```python
# Include additional covariates beyond batch
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

### 대규모 데이터 세트의 경우(>100,000개 셀)

```python
model.train(
    max_epochs=100,      # Fewer epochs needed
    batch_size=256,      # Larger batches
    train_size=0.9,      # Less validation
    early_stopping=True
)
```

### 소규모 데이터 세트(<10,000셀)의 경우

```python
model = scvi.model.SCVI(
    adata,
    n_latent=10,         # Smaller latent space
    n_layers=1,          # Simpler model
    dropout_rate=0.2     # More regularization
)

model.train(
    max_epochs=400,
    batch_size=64
)
```

### 모니터링 교육

```python
# Check training curves
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(model.history["elbo_train"], label="Train")
ax.plot(model.history["elbo_validation"], label="Validation")
ax.set_xlabel("Epoch")
ax.set_ylabel("ELBO")
ax.legend()

# Should see convergence without overfitting
```

## 파이프라인 완성

```python
def integrate_datasets(
    adatas,
    batch_key="batch",
    labels_key=None,
    n_top_genes=2000,
    n_latent=30
):
    """
    Integrate multiple scRNA-seq datasets.
    
    Parameters
    ----------
    adatas : dict
        Dictionary of {batch_name: AnnData}
    batch_key : str
        Key for batch annotation
    labels_key : str, optional
        Key for cell type labels (uses scANVI if provided)
    n_top_genes : int
        Number of HVGs
    n_latent : int
        Latent dimensions
        
    Returns
    -------
    AnnData with integrated representation
    """
    import scvi
    import scanpy as sc
    
    # Add batch labels and concatenate
    for batch_name, adata in adatas.items():
        adata.obs[batch_key] = batch_name
    
    adata = sc.concat(list(adatas.values()), label=batch_key)
    
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
    
    # Train model
    if labels_key and labels_key in adata.obs.columns:
        # Use scANVI
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
        # Use scVI
        scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key=batch_key)
        model = scvi.model.SCVI(adata, n_latent=n_latent)
        model.train(max_epochs=200)
        rep_key = "X_scVI"
    
    # Add representation
    adata.obsm[rep_key] = model.get_latent_representation()
    
    # Compute neighbors and UMAP
    sc.pp.neighbors(adata, use_rep=rep_key)
    sc.tl.umap(adata)
    sc.tl.leiden(adata)
    
    return adata, model

# Usage
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

| 문제 | 원인 | 해결책 |
|-------|-------|----------|
| 혼합되지 않는 배치 | 공유 유전자가 너무 적음 | 더 많은 HVG를 사용하고 유전자 중복을 확인하세요. |
| 과잉교정 | 생물학적 변이가 제거됨 | 레이블과 함께 scANVI 사용 |
| 훈련은 다양하다 | 학습률이 너무 높음 | lr을 줄이고 배치 크기를 늘립니다. |
| NaN 손실 | 잘못된 데이터 | 모두 0인 세포/유전자 확인 |
| 메모리 오류 | 셀이 너무 많습니다. | 배치 크기를 줄이고 GPU를 사용하세요. |
