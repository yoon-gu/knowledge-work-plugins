# scvi-tools를 위한 데이터 준비

이 레퍼런스는 scvi-tools 모델에서 사용할 AnnData 객체를 올바르게 준비하는 방법을 다룹니다.

## 개요

올바른 데이터 준비는 scvi-tools에 매우 중요합니다. 핵심 요구사항:
1. **원시 카운트** (정규화되지 않은)
2. **고변이 유전자 선택**
3. **적절한 setup_anndata() 호출**

## 1단계: 데이터 로드 및 검사

```python
import scanpy as sc
import scvi
import numpy as np

# 데이터 로드
adata = sc.read_h5ad("data.h5ad")

# adata.X의 내용 확인
print(f"Shape: {adata.shape}")
print(f"X dtype: {adata.X.dtype}")
print(f"X contains integers: {np.allclose(adata.X.data, adata.X.data.astype(int))}")
print(f"X min: {adata.X.min()}, max: {adata.X.max()}")
```

### 원시 카운트 확인

```python
# scvi-tools는 정수 카운트 필요
# X가 정규화된 것처럼 보이면, 원시 카운트 확인

if hasattr(adata, 'raw') and adata.raw is not None:
    print("adata.raw 발견")
    # 원시 카운트 사용
    adata = adata.raw.to_adata()

# 또는 레이어 확인
if 'counts' in adata.layers:
    print("counts 레이어 발견")
    # setup_anndata에서 레이어 지정
```

## 2단계: 기본 필터링

```python
# 세포 필터링 (표준 QC)
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_cells(adata, max_genes=5000)

# 미토콘드리아 비율 계산 (없는 경우)
# 인간 (MT-)과 마우스 (mt-, Mt-) 미토콘드리아 유전자 모두 처리
adata.var['mt'] = (
    adata.var_names.str.startswith('MT-') |
    adata.var_names.str.startswith('mt-') |
    adata.var_names.str.startswith('Mt-')
)
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)
adata = adata[adata.obs['pct_counts_mt'] < 20].copy()

# 유전자 필터링
sc.pp.filter_genes(adata, min_cells=3)

print(f"필터링 후: {adata.shape}")
```

## 3단계: 원시 카운트 저장

**중요**: 정규화 전에 항상 원시 카운트를 보존하세요.

```python
# 레이어에 원시 카운트 저장
adata.layers["counts"] = adata.X.copy()

# 이제 다른 목적으로 정규화 가능 (HVG 선택)
# 하지만 scvi는 counts 레이어를 사용
```

## 4단계: 고변이 유전자 선택

scvi-tools는 1,500-5,000개의 HVG에서 가장 잘 작동합니다.

### 단일 배치 데이터

```python
# HVG 선택만을 위한 정규화
adata_hvg = adata.copy()
sc.pp.normalize_total(adata_hvg, target_sum=1e4)
sc.pp.log1p(adata_hvg)

# HVG 선택
sc.pp.highly_variable_genes(
    adata_hvg,
    n_top_genes=2000,
    flavor="seurat"  # 또는 "cell_ranger"
)

# HVG 주석 전달
adata.var['highly_variable'] = adata_hvg.var['highly_variable']
```

### 다중 배치 데이터 (권장)

```python
# batch_key와 함께 seurat_v3 flavor 사용
# 배치 간 가변적인 유전자 선택
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2000,
    flavor="seurat_v3",
    batch_key="batch",  # 배치 열
    layer="counts"      # 원시 카운트 사용
)
```

### HVG로 서브셋

```python
# 고변이 유전자로 서브셋
adata = adata[:, adata.var['highly_variable']].copy()
print(f"HVG 선택 후: {adata.shape}")
```

## 5단계: AnnData 설정

`setup_anndata()` 함수는 모델을 위한 데이터를 등록합니다.

### 기본 설정

```python
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts"  # 원시 카운트가 있는 레이어 지정
)
```

### 배치 정보 포함

```python
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch"  # adata.obs의 열
)
```

### 세포 유형 레이블 포함 (scANVI용)

```python
scvi.model.SCANVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    labels_key="cell_type"  # 세포 유형 레이블 열
)
```

### 연속 공변량 포함

```python
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    continuous_covariate_keys=["percent_mito", "n_genes"]
)
```

### 범주형 공변량 포함

```python
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    categorical_covariate_keys=["donor", "technology"]
)
```

## 다중 모달 데이터 설정

### CITE-seq (totalVI용)

```python
# adata.obsm에 단백질 데이터
# adata.X에 RNA, 별도 매트릭스에 단백질

# 단백질 데이터 추가
adata.obsm["protein_expression"] = protein_counts  # numpy 배열

# totalVI 설정
scvi.model.TOTALVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    protein_expression_obsm_key="protein_expression"
)
```

### Multiome RNA+ATAC (MultiVI용)

```python
# RNA와 ATAC이 별도 AnnData 또는 MuData에

import mudata as md

# MuData 사용 시
mdata = md.read("multiome.h5mu")

scvi.model.MULTIVI.setup_mudata(
    mdata,
    rna_layer="counts",
    protein_layer=None,
    batch_key="batch",
    modalities={"rna": "rna", "accessibility": "atac"}
)
```

## 전체 준비 파이프라인

전체 준비 함수는 `scripts/model_utils.py`의 `prepare_adata()`를 사용하세요:

```python
from model_utils import prepare_adata

# QC, HVG 선택, 레이어 설정으로 데이터 준비
adata = prepare_adata(
    adata,
    batch_key="batch",
    n_top_genes=2000,
    min_genes=200,
    max_mito_pct=20
)

# 그런 다음 모델 설정
import scvi
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
```

이 함수는 다음을 처리합니다:
- 미토콘드리아 QC 필터링
- 세포 및 유전자 필터링
- 레이어에 카운트 저장
- HVG 선택 (batch_key가 제공되면 배치 인식)
- HVG로 서브셋

## 설정 확인

```python
# 등록된 데이터 확인
print(adata.uns['_scvi_manager_uuid'])
print(adata.uns['_scvi_adata_minify_type'])

# scVI용
scvi.model.SCVI.view_anndata_setup(adata)
```

## 일반적인 문제와 해결 방법

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| "X should contain integers" | X에 정규화된 데이터 | layer="counts" 사용 |
| "batch_key not found" | 잘못된 열 이름 | adata.obs.columns 확인 |
| 희소 매트릭스 오류 | 호환되지 않는 형식 | 변환: adata.X = adata.X.toarray() |
| 메모리 오류 | 유전자 수 너무 많음 | 먼저 HVG로 서브셋 |
| 데이터에 NaN | 결측값 | 필터링 또는 대체 |

## 데이터 형식 참조

### 필수

- `adata.X` 또는 `adata.layers["counts"]`: 원시 정수 카운트 (희소 가능)
- `adata.obs`: 세포 메타데이터 DataFrame
- `adata.var`: 유전자 메타데이터 DataFrame

### 권장

- `adata.obs["batch"]`: 배치/샘플 식별자
- `adata.var["highly_variable"]`: HVG 불리언 마스크

### scANVI용

- `adata.obs["labels"]`: 세포 유형 주석
- 레이블이 없는 세포는 "Unknown" 포함 가능
