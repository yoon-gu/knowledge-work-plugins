# scvi-tools 문제 해결 가이드

이 참조는 모든 scvi-tools 모델의 일반적인 문제를 진단하고 해결하기 위한 통합 가이드를 제공합니다.

## 빠른 진단

| 징후 | 가능한 원인 | 빠른 수정 |
|---------|--------------|-----------|
| "X should contain integers" | X의 정규화된 데이터 | 설정에 `layer="counts"` 사용 |
| CUDA 메모리 부족 | GPU 메모리가 소진되었습니다. | `batch_size` 줄이고 더 작은 모델 사용 |
| 훈련 손실은 NaN입니다. | 잘못된 데이터 또는 학습률 | 모두 0인 세포/유전자 확인 |
| 혼합되지 않는 배치 | 공유 기능이 너무 적습니다. | HVG 증가, 유전자 중복 확인 |
| 과잉교정 | 너무 공격적인 통합 | 레이블과 함께 scANVI 사용 |
| 가져오기 오류 | 종속성 누락 | `pip install scvi-tools[all]` |

## 데이터 형식 문제

### 문제: Seurat의 CITE-seq 단백질 데이터가 CLR로 정규화되었습니다.

**원인**: Seurat의 `NormalizeData(normalization.method = "CLR")`은 원시 ADT 수를 변환합니다. totalVI에는 단백질 데이터에 대한 원시 정수 개수가 필요합니다.

**증상**:
- 단백질 값은 정수가 아닙니다.
- 단백질 값에 음수가 포함되어 있습니다.
- 모델 학습 결과가 좋지 않음

**해결책**:
```python
# Check if protein data is normalized
protein = adata.obsm["protein_expression"]
print(f"Min value: {protein.min()}")  # Should be 0 if raw counts
print(f"Contains integers: {np.allclose(protein, protein.astype(int))}")

# If importing from Seurat, use the raw counts assay, not the normalized one
# In R/Seurat, export the RNA assay's counts slot, not the data slot
# GetAssayData(seurat_obj, assay = "ADT", slot = "counts")
```

### 문제: "layer not found" 또는 "X should contain integers"

**원인**: scvi-tools에는 정규화된 데이터가 아닌 원시 정수 개수가 필요합니다.

**해결책**:
```python
# Check if X contains integers
import numpy as np
print(f"X max: {adata.X.max()}")
print(f"Contains integers: {np.allclose(adata.X.data, adata.X.data.astype(int))}")

# If normalized, recover from raw
if hasattr(adata, 'raw') and adata.raw is not None:
    adata = adata.raw.to_adata()

# Or use existing counts layer
adata.layers["counts"] = adata.X.copy()
scvi.model.SCVI.setup_anndata(adata, layer="counts")
```

### 문제: 희소 행렬 오류

**원인**: 호환되지 않는 희소 형식 또는 조밀한 배열이 예상됩니다.

**해결책**:
```python
from scipy.sparse import csr_matrix

# Convert to CSR format (most compatible)
if hasattr(adata.X, 'toarray'):
    adata.X = csr_matrix(adata.X)

# Or convert to dense if small enough
if adata.n_obs * adata.n_vars < 1e8:
    adata.X = adata.X.toarray()
```

### 문제: 데이터의 NaN 또는 Inf 값

**원인**: 값이 누락되었거나 데이터가 손상되었습니다.

**해결책**:
```python
import numpy as np

# Check for issues
X = adata.X.toarray() if hasattr(adata.X, 'toarray') else adata.X
print(f"NaN count: {np.isnan(X).sum()}")
print(f"Inf count: {np.isinf(X).sum()}")
print(f"Negative count: {(X < 0).sum()}")

# Replace NaN/Inf with 0
X = np.nan_to_num(X, nan=0, posinf=0, neginf=0)
X = np.clip(X, 0, None)  # Ensure non-negative
adata.X = csr_matrix(X)
```

### 문제: Batch_key 또는 labels_key를 찾을 수 없습니다.

**원인**: adata.obs의 열 이름이 일치하지 않습니다.

**해결책**:
```python
# List available columns
print(adata.obs.columns.tolist())

# Check for similar names
for col in adata.obs.columns:
    if 'batch' in col.lower() or 'sample' in col.lower():
        print(f"Potential batch column: {col}")
```

## GPU 및 메모리 문제

### 문제: CUDA 메모리 부족

**원인**: 모델 또는 배치가 GPU 메모리에 맞지 않습니다.

**해결책**(순서대로 시도):

```python
# 1. Reduce batch size
model.train(batch_size=64)  # Default is 128

# 2. Use smaller model architecture
model = scvi.model.SCVI(
    adata,
    n_latent=10,   # Default is 10-30
    n_layers=1     # Default is 1-2
)

# 3. Subset to fewer genes
sc.pp.highly_variable_genes(adata, n_top_genes=1500)
adata = adata[:, adata.var['highly_variable']].copy()

# 4. Clear GPU cache between models
import torch
torch.cuda.empty_cache()

# 5. Use CPU if GPU is too small
model.train(accelerator="cpu")
```

### 문제: GPU가 감지되지 않음

**원인**: CUDA가 설치되지 않았거나 버전이 일치하지 않습니다.

**진단**:
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version: {torch.version.cuda}")
```

**해결책**:
```bash
# Check system CUDA
nvidia-smi
nvcc --version

# Reinstall PyTorch with matching CUDA
pip install torch --index-url https://download.pytorch.org/whl/cu118  # For CUDA 11.8
# Or
pip install torch --index-url https://download.pytorch.org/whl/cu121  # For CUDA 12.1
```

### 문제: 대규모 데이터 세트의 메모리 오류

**원인**: 시스템 RAM에 비해 데이터 세트가 너무 큽니다.

**해결책**:
```python
# 1. Process in chunks (for very large data)
# Subsample for initial exploration
adata_sample = adata[np.random.choice(adata.n_obs, 50000, replace=False)].copy()

# 2. Use backed mode for AnnData
adata = sc.read_h5ad("large_data.h5ad", backed='r')

# 3. Reduce gene count aggressively
adata = adata[:, adata.var['highly_variable']].copy()
```

## 훈련 문제

### 문제: 훈련 손실은 NaN입니다.

**원인**: 수치 불안정, 잘못된 데이터 또는 학습률 문제.

**해결책**:
```python
# 1. Check for problematic cells/genes
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# 2. Remove cells with zero counts
adata = adata[adata.X.sum(axis=1) > 0].copy()

# 3. Use gradient clipping (built into scvi-tools)
model.train(max_epochs=200, early_stopping=True)
```

### 문제: 훈련이 수렴되지 않습니다.

**원인**: 충분하지 않은 에포크, 잘못된 하이퍼매개변수 또는 데이터 문제.

**해결책**:
```python
# 1. Train longer
model.train(max_epochs=400)

# 2. Check training curves
import matplotlib.pyplot as plt
plt.plot(model.history['elbo_train'])
plt.plot(model.history['elbo_validation'])
plt.xlabel('Epoch')
plt.ylabel('ELBO')
plt.legend(['Train', 'Validation'])

# 3. Adjust model size for data size
# Small data (<10k cells): smaller model
model = scvi.model.SCVI(adata, n_latent=10, n_layers=1, dropout_rate=0.2)

# Large data (>100k cells): can use larger model
model = scvi.model.SCVI(adata, n_latent=30, n_layers=2)
```

### 문제: 과적합(검증 손실 증가)

**원인**: 모델이 너무 복잡하거나 너무 오랫동안 학습되었습니다.

**해결책**:
```python
# 1. Enable early stopping
model.train(early_stopping=True, early_stopping_patience=10)

# 2. Add regularization
model = scvi.model.SCVI(adata, dropout_rate=0.2)

# 3. Reduce model complexity
model = scvi.model.SCVI(adata, n_layers=1)
```

## 통합 문제

### 문제: 배치가 혼합되지 않음

**원인**: 공유 기능이 너무 적거나 생물학적 차이가 크거나 기술적 문제가 있습니다.

**해결책**:
```python
# 1. Check gene overlap between batches
for batch in adata.obs['batch'].unique():
    batch_genes = adata[adata.obs['batch'] == batch].var_names
    print(f"{batch}: {len(batch_genes)} genes")

# 2. Use more HVGs
sc.pp.highly_variable_genes(adata, n_top_genes=4000, batch_key="batch")

# 3. Train longer
model.train(max_epochs=400)

# 4. Increase latent dimensions
model = scvi.model.SCVI(adata, n_latent=50)
```

### 문제: 과잉 교정(생체 신호 손실)

**원인**: 모델이 너무 많은 변형을 제거했습니다.

**해결책**:
```python
# 1. Use scANVI with cell type labels
scvi.model.SCANVI.from_scvi_model(scvi_model, labels_key="cell_type")

# 2. Reduce model capacity
model = scvi.model.SCVI(adata, n_latent=10)

# 3. Use categorical covariates instead of batch_key
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    categorical_covariate_keys=["batch"]  # Less aggressive than batch_key
)
```

### 문제: 하나의 배치가 클러스터를 지배함

**원인**: 배치 크기가 불균형하거나 통합이 불완전합니다.

**해결책**:
```python
# 1. Check batch distribution
print(adata.obs['batch'].value_counts())

# 2. Subsample to balance
from sklearn.utils import resample
balanced = []
min_size = adata.obs['batch'].value_counts().min()
for batch in adata.obs['batch'].unique():
    batch_data = adata[adata.obs['batch'] == batch]
    balanced.append(batch_data[np.random.choice(len(batch_data), min_size, replace=False)])
adata_balanced = sc.concat(balanced)
```

## 모델별 문제

### scANVI: 라벨 전송 불량

**해결책**:
```python
# 1. Check label distribution
print(adata.obs['cell_type'].value_counts())

# 2. Use Unknown for low-confidence cells
adata.obs.loc[adata.obs['prediction_score'] < 0.5, 'cell_type'] = 'Unknown'

# 3. Train scVI longer before scANVI
scvi_model.train(max_epochs=300)
scanvi_model = scvi.model.SCANVI.from_scvi_model(scvi_model, labels_key="cell_type")
scanvi_model.train(max_epochs=100)
```

### totalVI: 시끄러운 단백질 신호

**해결책**:
```python
# 1. Use denoised protein values
_, protein_denoised = model.get_normalized_expression(return_mean=True)

# 2. Check isotype controls
# Isotype controls should have low expression
for i, name in enumerate(adata.uns["protein_names"]):
    if 'isotype' in name.lower():
        print(f"{name}: mean={adata.obsm['protein_expression'][:, i].mean():.1f}")
```

### PeakVI: 불량한 클러스터링

**해결책**:
```python
# 1. Use more variable peaks
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.05)
adata = adata[:, selector.fit(adata.X).get_support()].copy()

# 2. Binarize data
adata.X = (adata.X > 0).astype(np.float32)
```

### MultiVI: 양식 간 서로 다른 셀 수

**해결책**:
```python
# Ensure same cells in same order
common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
adata_rna = adata_rna[common_cells].copy()
adata_atac = adata_atac[common_cells].copy()
```

### DestVI: 불량한 디콘볼루션

**해결책**:
```python
# 1. Check gene overlap
common_genes = adata_ref.var_names.intersection(adata_spatial.var_names)
print(f"Common genes: {len(common_genes)}")  # Should be >1000

# 2. Use tissue-matched reference
# Reference should contain all cell types expected in spatial data

# 3. Check reference quality
print(adata_ref.obs['cell_type'].value_counts())
```

## 버전 호환성

### scvi-tools 1.x 대 0.x API 변경 사항

주요 차이점:
```python
# 0.x API
scvi.data.setup_anndata(adata, ...)

# 1.x API (current)
scvi.model.SCVI.setup_anndata(adata, ...)
```

### 버전 확인
```python
import scvi
import scanpy as sc
import anndata
import torch

print(f"scvi-tools: {scvi.__version__}")
print(f"scanpy: {sc.__version__}")
print(f"anndata: {anndata.__version__}")
print(f"torch: {torch.__version__}")
```

### 권장 버전(2024년 후반 기준)
```
scvi-tools>=1.0.0
scanpy>=1.9.0
anndata>=0.9.0
torch>=2.0.0
```

## 도움 받기

1. **문서 확인**: https://docs.scvi-tools.org/
2. **GitHub 문제**: https://github.com/scverse/scvi-tools/issues
3. **담론 포럼**: https://discourse.scverse.org/
4. **튜토리얼**: https://docs.scvi-tools.org/en/stable/tutorials/index.html

문제를 보고할 때 다음을 포함하십시오.
- scvi-tools 버전(`scvi.__version__`)
- 파이썬 버전
- 전체 오류 추적
- 재현 가능한 최소 예
