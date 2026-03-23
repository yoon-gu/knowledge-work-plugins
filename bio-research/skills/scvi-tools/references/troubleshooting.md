# scvi-tools 문제 해결 가이드

이 참조 문서는 모든 scvi-tools 모델에서 발생하는 일반적인 문제를 진단하고 해결하기 위한 통합 가이드를 제공합니다.

## 빠른 진단

| 증상 | 가능한 원인 | 빠른 해결 |
|---------|--------------|-----------|
| "X should contain integers" | X에 정규화된 데이터 | setup에서 `layer="counts"` 사용 |
| CUDA out of memory | GPU 메모리 부족 | `batch_size` 줄이기, 더 작은 모델 사용 |
| 훈련 손실이 NaN | 불량 데이터 또는 학습률 | 카운트가 0인 세포/유전자 확인 |
| 배치가 혼합되지 않음 | 공유 피처가 너무 적음 | HVG 증가, 유전자 겹침 확인 |
| 과보정 | 너무 공격적인 통합 | 라벨과 함께 scANVI 사용 |
| Import 오류 | 종속성 누락 | `pip install scvi-tools[all]` |

## 데이터 형식 문제

### 문제: Seurat의 CITE-seq 단백질 데이터가 CLR 정규화되어 있음

**원인**: Seurat의 `NormalizeData(normalization.method = "CLR")`이 원시 ADT 카운트를 변환합니다. totalVI는 단백질 데이터에 원시 정수 카운트가 필요합니다.

**증상**:
- 단백질 값이 정수가 아님
- 단백질 값에 음수가 포함됨
- 모델 훈련 결과가 좋지 않음

**해결 방법**:
```python
# 단백질 데이터가 정규화되었는지 확인
protein = adata.obsm["protein_expression"]
print(f"Min value: {protein.min()}")  # 원시 카운트라면 0이어야 함
print(f"Contains integers: {np.allclose(protein, protein.astype(int))}")

# Seurat에서 가져올 때 정규화된 것이 아닌 원시 카운트 assay를 사용
# R/Seurat에서 data 슬롯이 아닌 RNA assay의 counts 슬롯을 내보내기
# GetAssayData(seurat_obj, assay = "ADT", slot = "counts")
```

### 문제: "layer not found" 또는 "X should contain integers"

**원인**: scvi-tools는 정규화된 데이터가 아닌 원시 정수 카운트가 필요합니다.

**해결 방법**:
```python
# X에 정수가 포함되어 있는지 확인
import numpy as np
print(f"X max: {adata.X.max()}")
print(f"Contains integers: {np.allclose(adata.X.data, adata.X.data.astype(int))}")

# 정규화된 경우 raw에서 복구
if hasattr(adata, 'raw') and adata.raw is not None:
    adata = adata.raw.to_adata()

# 또는 기존 counts 레이어 사용
adata.layers["counts"] = adata.X.copy()
scvi.model.SCVI.setup_anndata(adata, layer="counts")
```

### 문제: 희소 행렬 오류

**원인**: 호환되지 않는 희소 형식 또는 밀집 배열이 필요함.

**해결 방법**:
```python
from scipy.sparse import csr_matrix

# CSR 형식으로 변환 (가장 호환성 좋음)
if hasattr(adata.X, 'toarray'):
    adata.X = csr_matrix(adata.X)

# 충분히 작다면 밀집으로 변환
if adata.n_obs * adata.n_vars < 1e8:
    adata.X = adata.X.toarray()
```

### 문제: 데이터에 NaN 또는 Inf 값

**원인**: 누락된 값 또는 손상된 데이터.

**해결 방법**:
```python
import numpy as np

# 문제 확인
X = adata.X.toarray() if hasattr(adata.X, 'toarray') else adata.X
print(f"NaN count: {np.isnan(X).sum()}")
print(f"Inf count: {np.isinf(X).sum()}")
print(f"Negative count: {(X < 0).sum()}")

# NaN/Inf를 0으로 대체
X = np.nan_to_num(X, nan=0, posinf=0, neginf=0)
X = np.clip(X, 0, None)  # 비음수 보장
adata.X = csr_matrix(X)
```

### 문제: batch_key 또는 labels_key를 찾을 수 없음

**원인**: adata.obs의 열 이름 불일치.

**해결 방법**:
```python
# 사용 가능한 열 나열
print(adata.obs.columns.tolist())

# 유사한 이름 확인
for col in adata.obs.columns:
    if 'batch' in col.lower() or 'sample' in col.lower():
        print(f"Potential batch column: {col}")
```

## GPU 및 메모리 문제

### 문제: CUDA out of memory

**원인**: 모델 또는 배치가 GPU 메모리에 맞지 않음.

**해결 방법** (순서대로 시도):

```python
# 1. 배치 크기 줄이기
model.train(batch_size=64)  # 기본값은 128

# 2. 더 작은 모델 아키텍처 사용
model = scvi.model.SCVI(
    adata,
    n_latent=10,   # 기본값은 10-30
    n_layers=1     # 기본값은 1-2
)

# 3. 더 적은 유전자로 서브셋
sc.pp.highly_variable_genes(adata, n_top_genes=1500)
adata = adata[:, adata.var['highly_variable']].copy()

# 4. 모델 간 GPU 캐시 비우기
import torch
torch.cuda.empty_cache()

# 5. GPU가 너무 작으면 CPU 사용
model.train(accelerator="cpu")
```

### 문제: GPU가 감지되지 않음

**원인**: CUDA가 설치되지 않았거나 버전 불일치.

**진단**:
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version: {torch.version.cuda}")
```

**해결 방법**:
```bash
# 시스템 CUDA 확인
nvidia-smi
nvcc --version

# 일치하는 CUDA로 PyTorch 재설치
pip install torch --index-url https://download.pytorch.org/whl/cu118  # CUDA 11.8용
# 또는
pip install torch --index-url https://download.pytorch.org/whl/cu121  # CUDA 12.1용
```

### 문제: 대규모 데이터셋의 메모리 오류

**원인**: 데이터셋이 시스템 RAM에 비해 너무 큼.

**해결 방법**:
```python
# 1. 청크 단위로 처리 (매우 큰 데이터의 경우)
# 초기 탐색을 위한 서브샘플링
adata_sample = adata[np.random.choice(adata.n_obs, 50000, replace=False)].copy()

# 2. AnnData의 backed 모드 사용
adata = sc.read_h5ad("large_data.h5ad", backed='r')

# 3. 유전자 수를 적극적으로 줄이기
adata = adata[:, adata.var['highly_variable']].copy()
```

## 훈련 문제

### 문제: 훈련 손실이 NaN

**원인**: 수치적 불안정성, 불량 데이터 또는 학습률 문제.

**해결 방법**:
```python
# 1. 문제가 있는 세포/유전자 확인
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# 2. 카운트가 0인 세포 제거
adata = adata[adata.X.sum(axis=1) > 0].copy()

# 3. 그래디언트 클리핑 사용 (scvi-tools에 내장)
model.train(max_epochs=200, early_stopping=True)
```

### 문제: 훈련이 수렴하지 않음

**원인**: 에포크 부족, 잘못된 하이퍼파라미터 또는 데이터 문제.

**해결 방법**:
```python
# 1. 더 오래 훈련
model.train(max_epochs=400)

# 2. 훈련 곡선 확인
import matplotlib.pyplot as plt
plt.plot(model.history['elbo_train'])
plt.plot(model.history['elbo_validation'])
plt.xlabel('Epoch')
plt.ylabel('ELBO')
plt.legend(['Train', 'Validation'])

# 3. 데이터 크기에 맞게 모델 크기 조정
# 소규모 데이터 (<10k 세포): 더 작은 모델
model = scvi.model.SCVI(adata, n_latent=10, n_layers=1, dropout_rate=0.2)

# 대규모 데이터 (>100k 세포): 더 큰 모델 사용 가능
model = scvi.model.SCVI(adata, n_latent=30, n_layers=2)
```

### 문제: 과적합 (검증 손실 증가)

**원인**: 모델이 너무 복잡하거나 너무 오래 훈련됨.

**해결 방법**:
```python
# 1. 조기 종료 활성화
model.train(early_stopping=True, early_stopping_patience=10)

# 2. 정규화 추가
model = scvi.model.SCVI(adata, dropout_rate=0.2)

# 3. 모델 복잡성 감소
model = scvi.model.SCVI(adata, n_layers=1)
```

## 통합 문제

### 문제: 배치가 혼합되지 않음

**원인**: 공유 피처가 너무 적거나, 강한 생물학적 차이 또는 기술적 문제.

**해결 방법**:
```python
# 1. 배치 간 유전자 겹침 확인
for batch in adata.obs['batch'].unique():
    batch_genes = adata[adata.obs['batch'] == batch].var_names
    print(f"{batch}: {len(batch_genes)} genes")

# 2. 더 많은 HVG 사용
sc.pp.highly_variable_genes(adata, n_top_genes=4000, batch_key="batch")

# 3. 더 오래 훈련
model.train(max_epochs=400)

# 4. 잠재 차원 증가
model = scvi.model.SCVI(adata, n_latent=50)
```

### 문제: 과보정 (생물학적 신호 손실)

**원인**: 모델이 너무 많은 변이를 제거함.

**해결 방법**:
```python
# 1. 세포 유형 라벨과 함께 scANVI 사용
scvi.model.SCANVI.from_scvi_model(scvi_model, labels_key="cell_type")

# 2. 모델 용량 감소
model = scvi.model.SCVI(adata, n_latent=10)

# 3. batch_key 대신 범주형 공변량 사용
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    categorical_covariate_keys=["batch"]  # batch_key보다 덜 공격적
)
```

### 문제: 한 배치가 클러스터를 지배함

**원인**: 불균형한 배치 크기 또는 불완전한 통합.

**해결 방법**:
```python
# 1. 배치 분포 확인
print(adata.obs['batch'].value_counts())

# 2. 균형을 맞추기 위한 서브샘플링
from sklearn.utils import resample
balanced = []
min_size = adata.obs['batch'].value_counts().min()
for batch in adata.obs['batch'].unique():
    batch_data = adata[adata.obs['batch'] == batch]
    balanced.append(batch_data[np.random.choice(len(batch_data), min_size, replace=False)])
adata_balanced = sc.concat(balanced)
```

## 모델별 문제

### scANVI: 라벨 전이 품질 저하

**해결 방법**:
```python
# 1. 라벨 분포 확인
print(adata.obs['cell_type'].value_counts())

# 2. 낮은 신뢰도 세포에 Unknown 사용
adata.obs.loc[adata.obs['prediction_score'] < 0.5, 'cell_type'] = 'Unknown'

# 3. scANVI 전에 scVI를 더 오래 훈련
scvi_model.train(max_epochs=300)
scanvi_model = scvi.model.SCANVI.from_scvi_model(scvi_model, labels_key="cell_type")
scanvi_model.train(max_epochs=100)
```

### totalVI: 단백질 신호 잡음

**해결 방법**:
```python
# 1. 노이즈 제거된 단백질 값 사용
_, protein_denoised = model.get_normalized_expression(return_mean=True)

# 2. 아이소타입 대조군 확인
# 아이소타입 대조군은 낮은 발현을 가져야 합니다
for i, name in enumerate(adata.uns["protein_names"]):
    if 'isotype' in name.lower():
        print(f"{name}: mean={adata.obsm['protein_expression'][:, i].mean():.1f}")
```

### PeakVI: 클러스터링 품질 저하

**해결 방법**:
```python
# 1. 더 많은 가변 피크 사용
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.05)
adata = adata[:, selector.fit(adata.X).get_support()].copy()

# 2. 데이터 이진화
adata.X = (adata.X > 0).astype(np.float32)
```

### MultiVI: 모달리티 간 세포 수가 다름

**해결 방법**:
```python
# 동일한 세포가 같은 순서인지 확인
common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
adata_rna = adata_rna[common_cells].copy()
adata_atac = adata_atac[common_cells].copy()
```

### DestVI: 탈콘볼루션 품질 저하

**해결 방법**:
```python
# 1. 유전자 겹침 확인
common_genes = adata_ref.var_names.intersection(adata_spatial.var_names)
print(f"Common genes: {len(common_genes)}")  # >1000이어야 함

# 2. 조직 매칭 참조 사용
# 참조에 공간 데이터에서 예상되는 모든 세포 유형이 포함되어야 함

# 3. 참조 품질 확인
print(adata_ref.obs['cell_type'].value_counts())
```

## 버전 호환성

### scvi-tools 1.x vs 0.x API 변경 사항

주요 차이점:
```python
# 0.x API
scvi.data.setup_anndata(adata, ...)

# 1.x API (현재)
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

### 권장 버전 (2024년 후반 기준)
```
scvi-tools>=1.0.0
scanpy>=1.9.0
anndata>=0.9.0
torch>=2.0.0
```

## 도움 받기

1. **문서 확인**: https://docs.scvi-tools.org/
2. **GitHub 이슈**: https://github.com/scverse/scvi-tools/issues
3. **Discourse 포럼**: https://discourse.scverse.org/
4. **튜토리얼**: https://docs.scvi-tools.org/en/stable/tutorials/index.html

이슈 보고 시 포함할 항목:
- scvi-tools 버전 (`scvi.__version__`)
- Python 버전
- 전체 오류 트레이스백
- 최소 재현 가능 예제
