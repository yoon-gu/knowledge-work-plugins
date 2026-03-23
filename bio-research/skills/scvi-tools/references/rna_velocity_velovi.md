# veloVI를 이용한 RNA 속도 분석

이 레퍼런스는 기존 속도 방법을 개선하는 딥러닝 접근법인 veloVI를 사용한 RNA 속도 분석을 다룹니다.

## 개요

RNA 속도는 다음을 모델링하여 세포의 미래 상태를 추정합니다:
- **미접합 RNA**: 새로 전사된, 인트론 포함
- **접합 RNA**: 성숙 mRNA, 인트론 제거됨

미접합 대 접합의 비율은 유전자가 상향 조절되는지 하향 조절되는지를 나타냅니다.

## 왜 veloVI인가?

기존 방법 (velocyto, scVelo)에는 한계가 있습니다:
- 정상 상태 또는 동역학적 모델 가정
- 잡음에 민감
- 배치 효과 처리 불가

veloVI는 다음으로 이를 해결합니다:
- 확률적 모델링
- 더 나은 불확실성 정량화
- scVI 프레임워크와의 통합

## 사전 요구사항

```python
import scvi
import scvelo as scv
import scanpy as sc
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
print(f"scvelo version: {scv.__version__}")
```

## 1단계: 접합/미접합 카운트 생성

### BAM 파일에서 (velocyto)

```bash
# Cell Ranger 출력에서 velocyto 실행
velocyto run10x /path/to/cellranger_output /path/to/genes.gtf

# 출력: 접합/미접합 레이어가 포함된 velocyto.loom 파일
```

### kb-python (kallisto|bustools)에서

```bash
# kallisto를 사용한 더 빠른 대안
kb count \
    --workflow lamanno \
    -i index.idx \
    -g t2g.txt \
    -c1 spliced_t2c.txt \
    -c2 unspliced_t2c.txt \
    -x 10xv3 \
    -o output \
    R1.fastq.gz R2.fastq.gz
```

## 2단계: 속도 데이터 로드

```python
# velocyto에서 loom 파일 로드
adata = scv.read("velocyto_output.loom")

# 또는 kb-python에서 로드
adata = sc.read_h5ad("adata.h5ad")
# adata.layers["spliced"]에 접합
# adata.layers["unspliced"]에 미접합

# 레이어 확인
print("사용 가능한 레이어:", list(adata.layers.keys()))
print(f"접합 shape: {adata.layers['spliced'].shape}")
print(f"미접합 shape: {adata.layers['unspliced'].shape}")
```

### 기존 AnnData와 병합

```python
# 별도 loom과 h5ad가 있는 경우
ldata = scv.read("velocyto.loom")
adata = sc.read_h5ad("processed.h5ad")

# 처리된 adata에 속도 데이터 병합
adata = scv.utils.merge(adata, ldata)
```

## 3단계: 속도를 위한 전처리

```python
# 필터링 및 정규화
scv.pp.filter_and_normalize(
    adata,
    min_shared_counts=20,
    n_top_genes=2000
)

# 모멘트 계산 (scVelo 비교용)
scv.pp.moments(adata, n_pcs=30, n_neighbors=30)
```

## 4단계: veloVI 실행

### AnnData 설정

```python
# veloVI 설정
scvi.model.VELOVI.setup_anndata(
    adata,
    spliced_layer="spliced",
    unspliced_layer="unspliced"
)
```

### 모델 학습

```python
# veloVI 모델 생성 및 학습
vae = scvi.model.VELOVI(adata)

vae.train(
    max_epochs=500,
    early_stopping=True,
    batch_size=256
)

# 학습 확인
vae.history["elbo_train"].plot()
```

### 속도 추정 얻기

```python
# 잠재 시간 얻기
latent_time = vae.get_latent_time(n_samples=25)
adata.obs["veloVI_latent_time"] = latent_time

# 속도 얻기
velocities = vae.get_velocity(n_samples=25)
adata.layers["veloVI_velocity"] = velocities

# 발현 상태 얻기
adata.layers["veloVI_expression"] = vae.get_expression_fit(n_samples=25)
```

## 5단계: 속도 시각화

### 속도 스트림라인

```python
# 속도 그래프 계산
scv.tl.velocity_graph(adata, vkey="veloVI_velocity")

# UMAP에 스트림라인 플롯
scv.pl.velocity_embedding_stream(
    adata,
    basis="umap",
    vkey="veloVI_velocity",
    color="cell_type"
)
```

### 속도 화살표

```python
# 개별 세포 화살표
scv.pl.velocity_embedding(
    adata,
    basis="umap",
    vkey="veloVI_velocity",
    arrow_length=3,
    arrow_size=2,
    color="cell_type"
)
```

### 잠재 시간

```python
# 잠재 시간 플롯 (속도에서의 의사시간)
sc.pl.umap(adata, color="veloVI_latent_time", cmap="viridis")
```

## 6단계: scVelo와 비교

```python
# 비교를 위해 표준 scVelo 실행
scv.tl.velocity(adata, mode="dynamical")
scv.tl.velocity_graph(adata)

# 속도 필드 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

scv.pl.velocity_embedding_stream(
    adata, basis="umap", ax=axes[0],
    title="scVelo", show=False
)

scv.pl.velocity_embedding_stream(
    adata, basis="umap", vkey="veloVI_velocity",
    ax=axes[1], title="veloVI", show=False
)

plt.tight_layout()
```

## 7단계: 유전자 수준 분석

### 속도 위상 초상화

```python
# 특정 유전자의 위상 초상화 플롯
genes = ["SOX2", "PAX6", "DCX", "NEUROD1"]

scv.pl.velocity(
    adata,
    var_names=genes,
    vkey="veloVI_velocity",
    colorbar=True
)
```

### 유전자 동역학

```python
# 잠재 시간에 따른 발현 플롯
for gene in genes:
    fig, ax = plt.subplots(figsize=(6, 4))

    sc.pl.scatter(
        adata,
        x="veloVI_latent_time",
        y=gene,
        color="cell_type",
        ax=ax,
        show=False
    )
    ax.set_xlabel("잠재 시간")
    ax.set_ylabel(f"{gene} 발현")
```

### 구동 유전자

```python
# 속도를 구동하는 유전자 찾기
scv.tl.rank_velocity_genes(
    adata,
    vkey="veloVI_velocity",
    groupby="cell_type"
)

# 클러스터별 상위 유전자
df = scv.get_df(adata, "rank_velocity_genes/names")
print(df.head(10))
```

## 8단계: 불확실성 정량화

veloVI는 불확실성 추정을 제공합니다:

```python
# 불확실성이 포함된 속도 얻기
velocity_mean, velocity_std = vae.get_velocity(
    n_samples=100,
    return_mean=True,
    return_numpy=True
)

# 불확실성 저장
adata.layers["velocity_uncertainty"] = velocity_std

# 불확실성 시각화
adata.obs["mean_velocity_uncertainty"] = velocity_std.mean(axis=1)
sc.pl.umap(adata, color="mean_velocity_uncertainty")
```

## 전체 파이프라인

```python
def run_velocity_analysis(
    adata,
    spliced_layer="spliced",
    unspliced_layer="unspliced",
    n_top_genes=2000,
    max_epochs=500
):
    """
    veloVI를 사용한 전체 RNA 속도 분석.

    Parameters
    ----------
    adata : AnnData
        접합/미접합 레이어가 포함된 데이터
    spliced_layer : str
        접합 카운트의 레이어 이름
    unspliced_layer : str
        미접합 카운트의 레이어 이름
    n_top_genes : int
        속도 유전자 수
    max_epochs : int
        학습 에포크

    Returns
    -------
    속도가 포함된 AnnData와 모델
    """
    import scvi
    import scvelo as scv
    import scanpy as sc

    adata = adata.copy()

    # 전처리
    scv.pp.filter_and_normalize(
        adata,
        min_shared_counts=20,
        n_top_genes=n_top_genes
    )

    # 모멘트 계산 (일부 시각화에 필요)
    scv.pp.moments(adata, n_pcs=30, n_neighbors=30)

    # veloVI 설정
    scvi.model.VELOVI.setup_anndata(
        adata,
        spliced_layer=spliced_layer,
        unspliced_layer=unspliced_layer
    )

    # 학습
    model = scvi.model.VELOVI(adata)
    model.train(max_epochs=max_epochs, early_stopping=True)

    # 결과 얻기
    adata.obs["latent_time"] = model.get_latent_time(n_samples=25)
    adata.layers["velocity"] = model.get_velocity(n_samples=25)

    # 시각화를 위한 속도 그래프 계산
    scv.tl.velocity_graph(adata, vkey="velocity")

    # UMAP이 없으면 계산
    if "X_umap" not in adata.obsm:
        sc.pp.neighbors(adata)
        sc.tl.umap(adata)

    return adata, model

# 사용법
adata_velocity, model = run_velocity_analysis(adata)

# 시각화
scv.pl.velocity_embedding_stream(
    adata_velocity,
    basis="umap",
    vkey="velocity",
    color="cell_type"
)

sc.pl.umap(adata_velocity, color="latent_time")
```

## 고급: 배치 인식 속도

```python
# 다중 배치 데이터의 경우, 모델에 배치 포함
scvi.model.VELOVI.setup_anndata(
    adata,
    spliced_layer="spliced",
    unspliced_layer="unspliced",
    batch_key="batch"
)

model = scvi.model.VELOVI(adata)
model.train()
```

## 결과 해석

### 좋은 속도 신호

- 스트림라인이 예상 분화를 따름
- 잠재 시간이 알려진 생물학과 상관
- 위상 초상화가 명확한 동역학을 보임

### 나쁜 속도 신호

- 무작위/혼란스러운 스트림라인
- 알려진 마커와 상관 없음
- 가능한 원인:
  - 불충분한 미접합 리드
  - 정상 상태의 세포
  - 기술적 문제

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 속도 신호 없음 | 낮은 미접합 카운트 | 시퀀싱 깊이 확인, kb-python 사용 |
| 역방향 | 잘못된 근원 할당 | 수동으로 근원 세포 설정 |
| 잡음 많은 스트림라인 | 유전자 수 너무 많음 | n_top_genes 줄이기 |
| 메모리 오류 | 큰 데이터셋 | batch_size 줄이기 |

## 주요 참고문헌

- Gayoso et al. (2023) "Deep generative modeling of transcriptional dynamics for RNA velocity analysis in single cells"
- La Manno et al. (2018) "RNA velocity of single cells"
- Bergen et al. (2020) "Generalizing RNA velocity to transient cell states through dynamical modeling"
