# PeakVI를 이용한 scATAC-seq 분석

이 레퍼런스는 PeakVI를 사용한 단일세포 ATAC-seq 분석의 차원 축소, 배치 보정, 차등 접근성 분석을 다룹니다.

## 개요

PeakVI는 scATAC-seq 데이터를 위한 심층 생성 모델로 다음을 수행합니다:
- 이진 접근성 모델링 (피크 열림/닫힘)
- 배치 효과 처리
- 클러스터링을 위한 잠재 표현 제공
- 차등 접근성 분석 활성화

## 사전 요구사항

```python
import scvi
import scanpy as sc
import numpy as np
import anndata as ad

print(f"scvi-tools version: {scvi.__version__}")
```

## 1단계: ATAC 데이터 로드 및 준비

### 10x Genomics (Cell Ranger ATAC)에서

```python
# fragments에서 피크-세포 매트릭스
# 일반적으로 filtered_peak_bc_matrix 형식

adata = sc.read_10x_h5("filtered_peak_bc_matrix.h5")

# 또는 mtx 형식에서
adata = sc.read_10x_mtx("filtered_peak_bc_matrix/")

# 구조 확인
print(f"Cells: {adata.n_obs}, Peaks: {adata.n_vars}")
print(f"Sparsity: {1 - adata.X.nnz / (adata.n_obs * adata.n_vars):.2%}")
```

### ArchR/Signac에서

```python
# ArchR에서 내보내기 (R에서)
# saveArchRProject(proj, outputDirectory="atac_export", load=FALSE)
# 그런 다음 Python에서 내보낸 파일 읽기

# Signac에서:
# 피크 매트릭스와 메타데이터 내보내기
```

## 2단계: 품질 관리

```python
# QC 지표 계산
sc.pp.calculate_qc_metrics(adata, inplace=True)

# ATAC의 핵심 지표:
# - n_genes_by_counts: 세포당 피크 수 (이름 변경 필요)
# - total_counts: 세포당 단편 수
adata.obs['n_peaks'] = adata.obs['n_genes_by_counts']
adata.obs['total_fragments'] = adata.obs['total_counts']

# 세포 필터링
adata = adata[adata.obs['n_peaks'] > 500].copy()
adata = adata[adata.obs['n_peaks'] < 50000].copy()  # 잠재적 이중체 제거

# 피크 필터링 (최소 n개 세포에서 접근 가능)
sc.pp.filter_genes(adata, min_cells=10)

print(f"QC 후: {adata.shape}")
```

### 데이터 이진화

```python
# PeakVI는 이진 접근성으로 작동
# 아직 이진이 아니면 이진화
adata.X = (adata.X > 0).astype(np.float32)

# 확인
print(f"Unique values: {np.unique(adata.X.data)}")
```

## 3단계: 피처 선택

RNA-seq와 달리, ATAC의 피크 선택은 덜 확립되어 있습니다. 옵션:

### 옵션 A: 가장 접근 가능한 피크

```python
# 접근성 빈도로 상위 피크 선택
peak_accessibility = np.array(adata.X.sum(axis=0)).flatten()
top_peaks = np.argsort(peak_accessibility)[-50000:]  # 상위 50k 피크

adata = adata[:, top_peaks].copy()
```

### 옵션 B: 가변 피크

```python
# 높은 분산을 가진 피크 선택
# (클러스터링에 가장 유익)
from sklearn.feature_selection import VarianceThreshold

selector = VarianceThreshold(threshold=0.05)
selector.fit(adata.X)
adata = adata[:, selector.get_support()].copy()
```

### 옵션 C: 유전자 근처 피크

```python
# 프로모터 영역이나 유전자 본체 내의 피크 유지
# 피크 주석이 필요
# gene_peaks = 유전자 주석이 있는 피크
# adata = adata[:, adata.var['near_gene']].copy()
```

## 4단계: 배치 정보 추가

```python
# 여러 샘플인 경우 배치 주석 추가
adata.obs['batch'] = adata.obs['sample_id']  # 또는 적절한 열

print(adata.obs['batch'].value_counts())
```

## 5단계: PeakVI 설정 및 학습

```python
# AnnData 설정
scvi.model.PEAKVI.setup_anndata(
    adata,
    batch_key="batch"  # 선택사항, 단일 배치면 생략
)

# 모델 생성
model = scvi.model.PEAKVI(
    adata,
    n_latent=20,      # 잠재 차원
    n_layers_encoder=2,
    n_layers_decoder=2
)

# 학습
model.train(
    max_epochs=200,
    early_stopping=True,
    batch_size=128
)

# 학습 확인
model.history['elbo_train'].plot()
```

## 6단계: 잠재 표현 얻기

```python
# 다운스트림 분석을 위한 잠재 공간
adata.obsm["X_PeakVI"] = model.get_latent_representation()

# 클러스터링 및 시각화
sc.pp.neighbors(adata, use_rep="X_PeakVI", n_neighbors=15)
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=0.5)

# 시각화
sc.pl.umap(adata, color=['leiden', 'batch'], ncols=2)
```

## 7단계: 차등 접근성

```python
# 클러스터 간 차등 접근성
da_results = model.differential_accessibility(
    groupby='leiden',
    group1='0',
    group2='1'
)

# 유의미한 피크 필터링
da_sig = da_results[
    (da_results['is_da_fdr_0.05']) &
    (abs(da_results['lfc_mean']) > 1)
]

print(f"유의미한 DA 피크: {len(da_sig)}")
print(da_sig.head())
```

### 조건 간 DA

```python
# 세포 유형 내에서 조건 비교
adata_subset = adata[adata.obs['cell_type'] == 'CD4 T cells'].copy()

da_condition = model.differential_accessibility(
    groupby='condition',
    group1='treated',
    group2='control'
)
```

## 8단계: 피크 주석

```python
# 가장 가까운 유전자로 피크 주석
# pybedtools 또는 유사 도구 사용

# 피크 이름 형식 예: chr1:1000-2000
# 주석을 위해 bed 형식으로 파싱

import pandas as pd

def parse_peak_names(peak_names):
    """피크 이름을 bed 형식으로 파싱."""
    records = []
    for peak in peak_names:
        chrom, coords = peak.split(':')
        start, end = coords.split('-')
        records.append({
            'chrom': chrom,
            'start': int(start),
            'end': int(end),
            'peak': peak
        })
    return pd.DataFrame(records)

peak_bed = parse_peak_names(adata.var_names)
```

## 9단계: 모티프 분석

```python
# 유의미한 피크를 모티프 분석을 위해 내보내기
# HOMER, MEME 또는 chromVAR 사용

# 피크 서열 내보내기
sig_peaks = da_sig.index.tolist()
peak_bed_sig = peak_bed[peak_bed['peak'].isin(sig_peaks)]
peak_bed_sig.to_csv("significant_peaks.bed", sep='\t', index=False, header=False)

# 그런 다음 HOMER 실행:
# findMotifsGenome.pl significant_peaks.bed hg38 motif_output/ -size 200
```

## 10단계: 유전자 활성도 점수

```python
# 피크 접근성에서 유전자 활성도 계산
# (피크-유전자 주석 필요)

def compute_gene_activity(adata, peak_gene_map):
    """
    피크 접근성에서 유전자 활성도 점수 계산.

    Parameters
    ----------
    adata : AnnData
        피크가 포함된 ATAC 데이터
    peak_gene_map : dict
        피크를 유전자에 매핑

    Returns
    -------
    유전자 활성도 점수가 포함된 AnnData
    """
    from scipy.sparse import csr_matrix

    genes = list(set(peak_gene_map.values()))
    gene_matrix = np.zeros((adata.n_obs, len(genes)))

    for i, gene in enumerate(genes):
        gene_peaks = [p for p, g in peak_gene_map.items() if g == gene]
        if gene_peaks:
            peak_idx = [list(adata.var_names).index(p) for p in gene_peaks if p in adata.var_names]
            if peak_idx:
                gene_matrix[:, i] = np.array(adata.X[:, peak_idx].sum(axis=1)).flatten()

    adata_gene = ad.AnnData(
        X=csr_matrix(gene_matrix),
        obs=adata.obs.copy(),
        var=pd.DataFrame(index=genes)
    )

    return adata_gene
```

## 전체 파이프라인

```python
def analyze_scatac(
    adata,
    batch_key=None,
    n_top_peaks=50000,
    n_latent=20,
    resolution=0.5
):
    """
    PeakVI를 사용한 전체 scATAC-seq 분석.

    Parameters
    ----------
    adata : AnnData
        원시 피크-세포 매트릭스
    batch_key : str, optional
        배치 주석 열
    n_top_peaks : int
        사용할 상위 피크 수
    n_latent : int
        잠재 차원
    resolution : float
        Leiden 클러스터링 해상도

    Returns
    -------
    (처리된 AnnData, 학습된 모델) 튜플
    """
    import scvi
    import scanpy as sc
    import numpy as np

    adata = adata.copy()

    # QC
    sc.pp.calculate_qc_metrics(adata, inplace=True)
    adata = adata[adata.obs['n_genes_by_counts'] > 500].copy()
    sc.pp.filter_genes(adata, min_cells=10)

    # 이진화
    adata.X = (adata.X > 0).astype(np.float32)

    # 상위 피크 선택
    if adata.n_vars > n_top_peaks:
        peak_accessibility = np.array(adata.X.sum(axis=0)).flatten()
        top_peaks = np.argsort(peak_accessibility)[-n_top_peaks:]
        adata = adata[:, top_peaks].copy()

    # PeakVI 설정
    scvi.model.PEAKVI.setup_anndata(adata, batch_key=batch_key)

    # 학습
    model = scvi.model.PEAKVI(adata, n_latent=n_latent)
    model.train(max_epochs=200, early_stopping=True)

    # 잠재 표현
    adata.obsm["X_PeakVI"] = model.get_latent_representation()

    # 클러스터링
    sc.pp.neighbors(adata, use_rep="X_PeakVI")
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=resolution)

    return adata, model

# 사용법
adata, model = analyze_scatac(
    adata,
    batch_key="sample",
    n_top_peaks=50000
)

# 시각화
sc.pl.umap(adata, color=['leiden', 'sample'])

# 차등 접근성
da_results = model.differential_accessibility(
    groupby='leiden',
    group1='0',
    group2='1'
)
```

## scRNA-seq와의 통합

멀티오믹 데이터 또는 동일 세포의 별도 RNA/ATAC:

```python
# 공동 RNA+ATAC 분석은 MultiVI 참조
# 또는 WNN (weighted nearest neighbors) 접근법 사용

# 공유 잠재 공간을 사용하여 RNA에서 ATAC으로 레이블 전달
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 학습 느림 | 피크 수가 너무 많음 | 상위 50k 피크로 서브셋 |
| 클러스터링 불량 | 유익한 피크 부족 | 가변 피크 사용 |
| 배치가 지배적 | 강한 기술적 효과 | batch_key 설정 확인 |
| 메모리 오류 | 큰 피크 매트릭스 | 희소 형식 사용, 피크 축소 |

## 주요 참고문헌

- Ashuach et al. (2022) "PeakVI: A deep generative model for single-cell chromatin accessibility analysis"
