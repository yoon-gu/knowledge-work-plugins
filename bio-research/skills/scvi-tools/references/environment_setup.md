# scvi-tools 환경 설정

이 레퍼런스는 scvi-tools의 설치 및 환경 구성을 다룹니다.

## 설치 옵션

### 옵션 1: Conda 환경 (권장)

```bash
# GPU 지원 환경 생성
conda create -n scvi-env python=3.10
conda activate scvi-env

# scvi-tools 설치
pip install scvi-tools

# GPU 가속 (대규모 데이터셋에 권장)
pip install torch --index-url https://download.pytorch.org/whl/cu118

# 일반 의존성
pip install scanpy leidenalg
```

### 옵션 2: Pip만 사용

```bash
# 가상 환경 생성
python -m venv scvi-env
source scvi-env/bin/activate  # Linux/Mac
# scvi-env\Scripts\activate   # Windows

# 설치
pip install scvi-tools scanpy
```

### 옵션 3: 공간 분석 지원 포함

```bash
conda create -n scvi-spatial python=3.10
conda activate scvi-spatial

pip install scvi-tools scanpy squidpy
```

### 옵션 4: MuData 지원 포함 (Multiome)

```bash
pip install scvi-tools mudata muon
```

## 설치 확인

```python
import scvi
import torch
import scanpy as sc

print(f"scvi-tools version: {scvi.__version__}")
print(f"scanpy version: {sc.__version__}")
print(f"PyTorch version: {torch.__version__}")
print(f"GPU available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU device: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

## GPU 구성

### CUDA 버전 확인

```bash
nvidia-smi
nvcc --version
```

### PyTorch CUDA 버전

| CUDA 버전 | PyTorch 설치 명령 |
|----------|-----------------|
| CUDA 11.8 | `pip install torch --index-url https://download.pytorch.org/whl/cu118` |
| CUDA 12.1 | `pip install torch --index-url https://download.pytorch.org/whl/cu121` |
| CPU 전용 | `pip install torch --index-url https://download.pytorch.org/whl/cpu` |

### 메모리 관리

```python
import torch

# 모델 간 GPU 캐시 해제
torch.cuda.empty_cache()

# 메모리 사용량 모니터링
print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
print(f"Cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")
```

## 일반적인 문제

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| `CUDA out of memory` | GPU 메모리 부족 | batch_size 줄이기, 더 작은 모델 사용 |
| `No GPU detected` | CUDA 미설치 | PyTorch에 맞는 CUDA 툴킷 설치 |
| `Version mismatch` | PyTorch/CUDA 비호환 | 올바른 CUDA 버전으로 PyTorch 재설치 |
| `Import error scvi` | 의존성 누락 | `pip install scvi-tools[all]` |

## Jupyter 설정

```bash
# Jupyter 커널 설치
pip install ipykernel
python -m ipykernel install --user --name scvi-env --display-name "scvi-tools"

# 대화형 그래프용
pip install matplotlib seaborn
```

## 권장 패키지 버전

재현성을 위해 버전 고정:

```bash
pip install \
    scvi-tools>=1.0.0 \
    scanpy>=1.9.0 \
    anndata>=0.9.0 \
    torch>=2.0.0
```

## 버전 호환성 가이드

### scvi-tools 1.x vs 0.x API 변경 사항

1.x 릴리스에서 호환성이 깨지는 변경이 도입되었습니다. 주요 차이점:

| 작업 | 0.x API (더 이상 사용되지 않음) | 1.x API (현재) |
|------|---------------------------|---------------|
| 데이터 설정 | `scvi.data.setup_anndata(adata, ...)` | `scvi.model.SCVI.setup_anndata(adata, ...)` |
| 데이터 등록 | `scvi.data.register_tensor_from_anndata(...)` | `setup_anndata`에 내장 |
| 설정 확인 | `scvi.data.view_anndata_setup(adata)` | `scvi.model.SCVI.view_anndata_setup(adata)` |

### 0.x에서 1.x로 마이그레이션

```python
# 이전 (0.x) - 더 이상 사용되지 않음
import scvi
scvi.data.setup_anndata(adata, layer="counts", batch_key="batch")
model = scvi.model.SCVI(adata)

# 새로운 (1.x) - 현재
import scvi
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
model = scvi.model.SCVI(adata)
```

### 모델별 설정 (1.x)

각 모델은 자체 설정 메서드를 가집니다:

```python
# scVI
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")

# scANVI
scvi.model.SCANVI.setup_anndata(adata, layer="counts", batch_key="batch", labels_key="cell_type")

# totalVI
scvi.model.TOTALVI.setup_anndata(adata, layer="counts", protein_expression_obsm_key="protein")

# MultiVI (MuData 사용)
scvi.model.MULTIVI.setup_mudata(mdata, rna_layer="counts", atac_layer="counts")

# PeakVI
scvi.model.PEAKVI.setup_anndata(adata, batch_key="batch")

# veloVI
scvi.external.VELOVI.setup_anndata(adata, spliced_layer="spliced", unspliced_layer="unspliced")
```

### 최소 버전 요구사항

| 패키지 | 최소 버전 | 비고 |
|--------|---------|------|
| scvi-tools | 1.0.0 | 현재 API에 필수 |
| scanpy | 1.9.0 | HVG 선택 개선 |
| anndata | 0.9.0 | 개선된 MuData 지원 |
| torch | 2.0.0 | 성능 개선 |
| mudata | 0.2.0 | MultiVI에 필수 |
| scvelo | 0.2.5 | veloVI에 필수 |

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

# 1.x API 사용 여부 확인
if hasattr(scvi.model.SCVI, 'setup_anndata'):
    print("scvi-tools 1.x API 사용 중")
else:
    print("경고: 더 이상 사용되지 않는 0.x API 사용 중 - 업그레이드하세요")
```

### 알려진 호환성 문제

| 문제 | 영향받는 버전 | 해결 방법 |
|------|-------------|----------|
| `setup_anndata` 찾을 수 없음 | scvi-tools < 1.0 | 1.0+으로 업그레이드 |
| MuData 오류 | mudata < 0.2 | `pip install mudata>=0.2.0` |
| CUDA 버전 불일치 | 모든 버전 | 사용 중인 CUDA에 맞게 PyTorch 재설치 |
| numpy 2.0 문제 | 2024년 초 빌드 | `pip install numpy<2.0` |

### scvi-tools 업그레이드

```bash
# 최신 버전으로 업그레이드
pip install --upgrade scvi-tools

# 모든 의존성 업그레이드
pip install --upgrade scvi-tools scanpy anndata torch

# 문제 발생 시 클린 설치
pip uninstall scvi-tools
pip cache purge
pip install scvi-tools
```

## 설치 테스트

```python
# 샘플 데이터로 빠른 테스트
import scvi
import scanpy as sc

# 테스트 데이터셋 로드
adata = scvi.data.heart_cell_atlas_subsampled()
print(f"테스트 데이터 로드됨: {adata.shape}")

# 설정 및 모델 생성 (빠른 테스트)
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="cell_source")
model = scvi.model.SCVI(adata, n_latent=10)
print("모델 생성 성공")

# 빠른 학습 테스트 (1 에포크)
model.train(max_epochs=1)
print("학습 작동!")
```
