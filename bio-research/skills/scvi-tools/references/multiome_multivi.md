# MultiVI를 이용한 Multiome 분석

이 레퍼런스는 MultiVI를 사용한 멀티오믹 실험 (동일 세포에서 동시 RNA-seq 및 ATAC-seq)의 공동 RNA 및 ATAC-seq 분석을 다룹니다.

## 개요

MultiVI는 멀티오믹 데이터 분석을 위한 심층 생성 모델로:
- 모달리티 간 공동 잠재 표현 학습
- 누락된 모달리티 처리 (RNA 전용 또는 ATAC 전용 세포)
- 실험 간 배치 보정
- 누락 모달리티의 대체 지원

## 사전 요구사항

```python
import scvi
import scanpy as sc
import mudata as md
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

## 데이터 형식

### 옵션 1: MuData (권장)

```python
# MuData로 멀티오믹 데이터 로드
mdata = md.read("multiome.h5mu")

# 구조:
# mdata.mod['rna']  - RNA 카운트가 포함된 AnnData
# mdata.mod['atac'] - ATAC 카운트가 포함된 AnnData

print(f"RNA: {mdata.mod['rna'].shape}")
print(f"ATAC: {mdata.mod['atac'].shape}")
```

### 옵션 2: 별도 AnnData 객체

```python
# 별도로 로드
adata_rna = sc.read_h5ad("rna.h5ad")
adata_atac = sc.read_h5ad("atac.h5ad")

# 동일한 세포가 동일한 순서인지 확인
common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
adata_rna = adata_rna[common_cells].copy()
adata_atac = adata_atac[common_cells].copy()
```

## 1단계: RNA 데이터 준비

```python
# RNA 전처리 (표준 scvi-tools 파이프라인)
adata_rna = mdata.mod['rna'].copy()

# 필터링
sc.pp.filter_cells(adata_rna, min_genes=200)
sc.pp.filter_genes(adata_rna, min_cells=3)

# 카운트 저장
adata_rna.layers["counts"] = adata_rna.X.copy()

# HVG 선택
sc.pp.highly_variable_genes(
    adata_rna,
    n_top_genes=4000,
    flavor="seurat_v3",
    layer="counts",
    batch_key="batch"  # 여러 배치인 경우
)

# HVG로 서브셋
adata_rna = adata_rna[:, adata_rna.var['highly_variable']].copy()
```

## 2단계: ATAC 데이터 준비

```python
# ATAC 전처리
adata_atac = mdata.mod['atac'].copy()

# 피크 필터링
sc.pp.filter_genes(adata_atac, min_cells=10)

# 접근성 이진화
adata_atac.X = (adata_atac.X > 0).astype(np.float32)

# 상위 접근 가능 피크 선택 (너무 많은 경우)
if adata_atac.n_vars > 50000:
    peak_accessibility = np.array(adata_atac.X.sum(axis=0)).flatten()
    top_peaks = np.argsort(peak_accessibility)[-50000:]
    adata_atac = adata_atac[:, top_peaks].copy()

# 레이어에 저장
adata_atac.layers["counts"] = adata_atac.X.copy()
```

## 3단계: 결합 MuData 생성

```python
# 일치하는 세포 확인
common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
adata_rna = adata_rna[common_cells].copy()
adata_atac = adata_atac[common_cells].copy()

# MuData 생성
mdata = md.MuData({
    "rna": adata_rna,
    "atac": adata_atac
})

print(f"결합 멀티오믹: {mdata.n_obs}개 세포")
print(f"RNA 피처: {mdata.mod['rna'].n_vars}")
print(f"ATAC 피처: {mdata.mod['atac'].n_vars}")
```

## 4단계: MultiVI 설정

```python
# MultiVI용 MuData 설정
scvi.model.MULTIVI.setup_mudata(
    mdata,
    rna_layer="counts",
    atac_layer="counts",
    batch_key="batch",  # 선택사항
    modalities={
        "rna_layer": "rna",
        "batch_key": "rna",
        "atac_layer": "atac"
    }
)
```

## 5단계: MultiVI 학습

```python
# 모델 생성
model = scvi.model.MULTIVI(
    mdata,
    n_latent=20,
    n_layers_encoder=2,
    n_layers_decoder=2
)

# 학습
model.train(
    max_epochs=300,
    early_stopping=True,
    early_stopping_patience=10,
    batch_size=128
)

# 학습 확인
model.history['elbo_train'].plot()
```

## 6단계: 공동 표현 얻기

```python
# 잠재 표현
latent = model.get_latent_representation()

# MuData에 추가
mdata.obsm["X_MultiVI"] = latent

# 공동 공간에서 클러스터링
sc.pp.neighbors(mdata, use_rep="X_MultiVI")
sc.tl.umap(mdata)
sc.tl.leiden(mdata, resolution=1.0)

# 시각화
sc.pl.umap(mdata, color=['leiden', 'batch'], ncols=2)
```

## 7단계: 모달리티별 분석

### 누락 모달리티 대체

```python
# ATAC 전용 세포의 RNA 발현 대체
# (ATAC 전용 데이터셋과 통합 시 유용)
imputed_rna = model.get_normalized_expression(
    modality="rna"
)

# RNA 전용 세포의 접근성 대체
imputed_atac = model.get_accessibility_estimates()
```

### 차등 분석

```python
# 차등 발현 (RNA)
de_results = model.differential_expression(
    groupby="leiden",
    group1="0",
    group2="1"
)

# 차등 접근성 (ATAC)
da_results = model.differential_accessibility(
    groupby="leiden",
    group1="0",
    group2="1"
)
```

## 부분 데이터 처리

MultiVI는 하나의 모달리티만 있는 데이터셋을 통합할 수 있습니다:

```python
# 데이터셋 1: 전체 멀티오믹
# 데이터셋 2: RNA 전용
# 데이터셋 3: ATAC 전용

# 누락 모달리티 표시
mdata.obs['modality'] = 'paired'  # 두 모달리티 모두 있는 세포
# RNA 전용 세포의 경우, ATAC 데이터가 누락/NaN
# ATAC 전용 세포의 경우, RNA 데이터가 누락/NaN

# MultiVI는 학습 중 자동 처리
```

## 전체 파이프라인

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
    MultiVI를 사용한 전체 멀티오믹 분석.

    Parameters
    ----------
    adata_rna : AnnData
        RNA 카운트 데이터
    adata_atac : AnnData
        ATAC 피크 데이터
    batch_key : str, optional
        배치 열 이름
    n_top_genes : int
        RNA용 HVG 수
    n_top_peaks : int
        ATAC용 상위 피크 수
    n_latent : int
        잠재 차원
    max_epochs : int
        최대 학습 에포크

    Returns
    -------
    공동 표현이 포함된 MuData
    """
    import scvi
    import scanpy as sc
    import mudata as md
    import numpy as np

    # 공통 세포 얻기
    common_cells = adata_rna.obs_names.intersection(adata_atac.obs_names)
    adata_rna = adata_rna[common_cells].copy()
    adata_atac = adata_atac[common_cells].copy()

    # RNA 전처리
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

    # ATAC 전처리
    sc.pp.filter_genes(adata_atac, min_cells=10)
    adata_atac.X = (adata_atac.X > 0).astype(np.float32)

    if adata_atac.n_vars > n_top_peaks:
        peak_acc = np.array(adata_atac.X.sum(axis=0)).flatten()
        top_idx = np.argsort(peak_acc)[-n_top_peaks:]
        adata_atac = adata_atac[:, top_idx].copy()

    adata_atac.layers["counts"] = adata_atac.X.copy()

    # MuData 생성
    mdata = md.MuData({"rna": adata_rna, "atac": adata_atac})

    # 설정 및 학습
    scvi.model.MULTIVI.setup_mudata(
        mdata,
        rna_layer="counts",
        atac_layer="counts",
        batch_key=batch_key,
        modalities={"rna_layer": "rna", "batch_key": "rna", "atac_layer": "atac"}
    )

    model = scvi.model.MULTIVI(mdata, n_latent=n_latent)
    model.train(max_epochs=max_epochs, early_stopping=True)

    # 표현 추가
    mdata.obsm["X_MultiVI"] = model.get_latent_representation()

    # 클러스터링
    sc.pp.neighbors(mdata, use_rep="X_MultiVI")
    sc.tl.umap(mdata)
    sc.tl.leiden(mdata)

    return mdata, model


# 사용법
mdata, model = analyze_multiome(
    adata_rna,
    adata_atac,
    batch_key="sample"
)

sc.pl.umap(mdata, color=['leiden', 'sample'])
```

## 피크-유전자 연결

```python
# 잠재 공간에서의 상관관계를 기반으로 ATAC 피크를 유전자에 연결
# 이것은 조절 관계를 식별

def link_peaks_to_genes(model, mdata, distance_threshold=100000):
    """
    상관관계를 기반으로 피크를 근처 유전자에 연결.

    Parameters
    ----------
    model : MULTIVI
        학습된 모델
    mdata : MuData
        멀티오믹 데이터
    distance_threshold : int
        피크를 유전자에 연결하는 최대 거리 (bp)

    Returns
    -------
    피크-유전자 연결 DataFrame
    """
    # 대체값 얻기
    rna_imputed = model.get_normalized_expression()
    atac_imputed = model.get_accessibility_estimates()

    # 유전자 프로모터 근처 피크의 접근성과 유전자 발현 상관
    # ... (게놈 좌표 필요)

    return peak_gene_links
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 세포 수 다름 | 한 모달리티에 세포 누락 | 공통 세포만 사용 |
| 학습 불안정 | 불균형 모달리티 | 피처 카운트 정규화 |
| 클러스터링 불량 | 피처 수 부족 | n_top_genes/피크 증가 |
| 메모리 오류 | 큰 ATAC 매트릭스 | 피크 수 줄이기, 희소 형식 사용 |
| 배치가 지배적 | 강한 기술적 효과 | batch_key 설정 확인 |

## 주요 참고문헌

- Ashuach et al. (2023) "MultiVI: deep generative model for the integration of multimodal data"
