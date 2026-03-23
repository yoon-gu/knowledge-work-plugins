# sysVI를 이용한 고급 배치 보정

이 레퍼런스는 주요 기술적 또는 연구 차이에 걸쳐 데이터를 통합하기 위해 설계된 sysVI를 사용한 시스템 수준 배치 보정을 다룹니다.

## 개요

sysVI (System Variational Inference)는 다음과 같은 시나리오에서 scVI를 확장합니다:
- 배치 효과가 매우 강한 경우 (다른 기술)
- 표준 scVI가 생물학적 신호를 과도하게 보정하는 경우
- "시스템" 효과를 생물학적 변이에서 분리해야 하는 경우

## sysVI vs scVI 사용 시점

| 시나리오 | 권장 모델 |
|---------|----------|
| 동일 기술, 다른 샘플 | scVI |
| 10x v2 vs 10x v3 | scVI (일반적으로) |
| 10x vs Smart-seq2 | sysVI |
| 다른 시퀀싱 깊이 | 공변량이 포함된 scVI |
| 교차 연구 통합 | sysVI |
| 아틀라스 규모 통합 | sysVI |

## 사전 요구사항

```python
import scvi
import scanpy as sc
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
```

## sysVI 아키텍처 이해

sysVI는 변이를 다음으로 분리합니다:
1. **생물학적 변이**: 세포 유형, 상태, 궤적
2. **시스템 변이**: 기술, 연구, 실험실 효과

```
                    ┌─────────────────┐
입력 카운트 ────────►│    인코더       │
                    │                 │
시스템 정보 ───────►│  (조건부)       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   잠재 변수 z    │
                    │  (생물학적)     │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
시스템 정보 ───────►│    디코더       │
                    │  (조건부)       │
                    └────────┬────────┘
                             │
                    재구성된 카운트
```

## 기본 sysVI 워크플로우

### 1단계: 데이터 준비

```python
# 다른 시스템의 데이터셋 로드
adata1 = sc.read_h5ad("10x_data.h5ad")
adata2 = sc.read_h5ad("smartseq_data.h5ad")

# 시스템 레이블 추가
adata1.obs["system"] = "10x"
adata2.obs["system"] = "Smart-seq2"

# 배치 레이블 추가 (시스템 내)
# 예: 각 기술 내의 다른 샘플

# 연결
adata = sc.concat([adata1, adata2])

# 원시 카운트 저장
adata.layers["counts"] = adata.X.copy()
```

### 2단계: HVG 선택

```python
# 배치와 시스템 모두 고려하여 HVG 선택
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=4000,  # 교차 시스템에는 더 많은 유전자
    flavor="seurat_v3",
    batch_key="system",  # HVG에 시스템 고려
    layer="counts"
)

# 선택사항: 시스템 간 겹침 확인
# HVG가 두 시스템에서 발현되는지 확인
adata = adata[:, adata.var["highly_variable"]].copy()
```

### 3단계: sysVI 설정 및 학습

```python
# AnnData 설정
# 참고: sysVI는 버전에 따라 다르게 접근할 수 있음
# 현재 API는 scvi-tools 문서 확인

scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="sample",           # 시스템 내 배치
    categorical_covariate_keys=["system"]  # 시스템 수준 공변량
)

# 진정한 sysVI (버전에서 사용 가능한 경우)
# scvi.model.SysVI.setup_anndata(...)

# 시스템 인식 모델 생성
model = scvi.model.SCVI(
    adata,
    n_latent=30,
    n_layers=2,
    gene_likelihood="nb"
)

# 학습
model.train(max_epochs=300)
```

### 4단계: 표현 추출

```python
# 잠재 표현 얻기
adata.obsm["X_integrated"] = model.get_latent_representation()

# 클러스터링 및 시각화
sc.pp.neighbors(adata, use_rep="X_integrated")
sc.tl.umap(adata)
sc.tl.leiden(adata)

# 통합 확인
sc.pl.umap(adata, color=["system", "leiden", "cell_type"])
```

## 대안: Harmony + scVI

교차 시스템 통합에서 방법 결합이 잘 작동할 수 있습니다:

```python
import scanpy.external as sce

# 먼저 PCA 실행
sc.pp.pca(adata)

# 초기 정렬을 위해 Harmony 적용
sce.pp.harmony_integrate(adata, key="system")

# 그런 다음 Harmony 보정된 임베딩에서 scVI 학습
# 또는 Harmony 표현을 직접 사용
```

## 대안: scVI에서 공변량 사용

중간 정도의 시스템 효과에 대해:

```python
# 시스템을 범주형 공변량으로 포함
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="sample",
    categorical_covariate_keys=["system", "technology_version"]
)

model = scvi.model.SCVI(adata, n_latent=30)
model.train()
```

## 대안: 별도 모델 + 통합

매우 다른 시스템에 대해:

```python
# 별도 모델 학습
scvi.model.SCVI.setup_anndata(adata1, layer="counts", batch_key="sample")
model1 = scvi.model.SCVI(adata1)
model1.train()

scvi.model.SCVI.setup_anndata(adata2, layer="counts", batch_key="sample")
model2 = scvi.model.SCVI(adata2)
model2.train()

# 잠재 공간 얻기
adata1.obsm["X_scVI"] = model1.get_latent_representation()
adata2.obsm["X_scVI"] = model2.get_latent_representation()

# CCA 또는 Harmony로 정렬
# ... 추가 정렬 단계
```

## 교차 시스템 통합 평가

### 시각적 평가

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 시스템별 색상
sc.pl.umap(adata, color="system", ax=axes[0], show=False, title="시스템별")

# 세포 유형별 색상
sc.pl.umap(adata, color="cell_type", ax=axes[1], show=False, title="세포 유형별")

# 마커 발현별 색상
sc.pl.umap(adata, color="CD3D", ax=axes[2], show=False, title="CD3D 발현")

plt.tight_layout()
```

### 정량적 지표

```python
# scib-metrics 사용
from scib_metrics.benchmark import Benchmarker

bm = Benchmarker(
    adata,
    batch_key="system",
    label_key="cell_type",
    embedding_obsm_keys=["X_integrated"]
)

bm.benchmark()

# 핵심 지표:
# - 배치 혼합 (ASW_batch, Graph connectivity)
# - 생물학적 보존 (NMI, ARI, ASW_label)
```

### LISI 점수

```python
# Local Inverse Simpson's Index
from scib_metrics import lisi

# 배치 LISI (높을수록 좋은 혼합)
batch_lisi = lisi.ilisi_graph(
    adata,
    batch_key="system",
    use_rep="X_integrated"
)

# 세포 유형 LISI (낮을수록 좋은 보존)
ct_lisi = lisi.clisi_graph(
    adata,
    label_key="cell_type",
    use_rep="X_integrated"
)

print(f"배치 LISI: {batch_lisi.mean():.3f}")
print(f"세포 유형 LISI: {ct_lisi.mean():.3f}")
```

## 특정 과제 처리

### 다른 유전자 세트

```python
# 공통 유전자 찾기
common_genes = adata1.var_names.intersection(adata2.var_names)
print(f"공통 유전자: {len(common_genes)}")

# 너무 적으면 유전자 매핑 사용
# 또는 누락 유전자 대체
```

### 다른 시퀀싱 깊이

```python
# 깊이를 연속 공변량으로 추가
adata.obs["log_counts"] = np.log1p(adata.obs["total_counts"])

scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="sample",
    continuous_covariate_keys=["log_counts"]
)
```

### 불균형한 세포 유형

```python
# 시스템별 세포 유형 분포 확인
import pandas as pd

ct_dist = pd.crosstab(adata.obs["system"], adata.obs["cell_type"], normalize="index")
print(ct_dist)

# 매우 불균형하면 다음을 고려:
# 1. 균형을 위해 서브샘플링
# 2. 레이블이 있는 scANVI를 사용하여 희귀 유형 보존
```

## 전체 파이프라인

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
    다른 기술 시스템의 데이터셋 통합.

    Parameters
    ----------
    adatas : dict
        {시스템_이름: AnnData} 딕셔너리
    system_key : str
        시스템 주석 키
    batch_key : str
        시스템 내 배치 키
    cell_type_key : str
        세포 유형 레이블 키 (선택사항)
    n_top_genes : int
        HVG 수
    n_latent : int
        잠재 차원

    Returns
    -------
    모델이 포함된 통합된 AnnData
    """
    import scvi
    import scanpy as sc

    # 시스템 레이블 추가 및 연결
    for system_name, adata in adatas.items():
        adata.obs[system_key] = system_name

    adata = sc.concat(list(adatas.values()))

    # 공통 유전자 찾기
    for name, ad in adatas.items():
        if name == list(adatas.keys())[0]:
            common_genes = set(ad.var_names)
        else:
            common_genes = common_genes.intersection(ad.var_names)

    adata = adata[:, list(common_genes)].copy()
    print(f"공통 유전자: {len(common_genes)}")

    # 카운트 저장
    adata.layers["counts"] = adata.X.copy()

    # HVG 선택
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=n_top_genes,
        flavor="seurat_v3",
        batch_key=system_key,
        layer="counts"
    )
    adata = adata[:, adata.var["highly_variable"]].copy()

    # 시스템을 공변량으로 설정
    scvi.model.SCVI.setup_anndata(
        adata,
        layer="counts",
        batch_key=batch_key if batch_key in adata.obs else None,
        categorical_covariate_keys=[system_key]
    )

    # 학습
    model = scvi.model.SCVI(adata, n_latent=n_latent, n_layers=2)
    model.train(max_epochs=300, early_stopping=True)

    # 표현 얻기
    adata.obsm["X_integrated"] = model.get_latent_representation()

    # 클러스터링
    sc.pp.neighbors(adata, use_rep="X_integrated")
    sc.tl.umap(adata)
    sc.tl.leiden(adata)

    return adata, model

# 사용법
adatas = {
    "10x_v3": sc.read_h5ad("10x_v3_data.h5ad"),
    "Smart-seq2": sc.read_h5ad("smartseq_data.h5ad"),
    "Drop-seq": sc.read_h5ad("dropseq_data.h5ad")
}

adata_integrated, model = integrate_cross_system(adatas)

# 시각화
sc.pl.umap(adata_integrated, color=["system", "leiden"])
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 시스템이 혼합되지 않음 | 효과가 너무 강함 | 더 많은 유전자 사용, n_latent 증가 |
| 과도한 보정 | 모델이 너무 공격적 | n_layers 줄이기, scANVI 사용 |
| 공통 유전자 적음 | 다른 플랫폼 | 유전자 이름 매핑 사용 |
| 한 시스템이 지배적 | 불균형한 크기 | 큰 데이터셋 서브샘플링 |

## 주요 참고문헌

- Lopez et al. (2018) "Deep generative modeling for single-cell transcriptomics"
- Luecken et al. (2022) "Benchmarking atlas-level data integration in single-cell genomics"
