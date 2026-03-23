# veloVI를 사용한 RNA 속도

이 참고 자료는 기존 속도 방법을 개선한 딥 러닝 접근 방식인 veloVI를 사용한 RNA 속도 분석을 다룹니다.

## 개요

RNA 속도는 다음을 모델링하여 세포의 미래 상태를 추정합니다.
- **접합되지 않은 RNA**: 새로 전사되었으며 인트론이 포함되어 있습니다.
- **접합된 RNA**: 성숙한 mRNA, 인트론 제거됨

스플라이싱되지 않은 비율과 스플라이싱된 비율은 유전자가 상향 조절되는지 하향 조절되는지 여부를 나타냅니다.

## 왜 veloVI인가?

기존 방법(velocyto, scVelo)에는 다음과 같은 제한 사항이 있습니다.
- 정상상태 또는 동적 모델 가정
- 소음에 민감함
- 일괄 효과를 처리하지 마세요

veloVI는 다음을 통해 이러한 문제를 해결합니다.
- 확률적 모델링
- 더 나은 불확실성 정량화
- scVI 프레임워크와 통합

## 전제조건

```python
import scvi
import scvelo as scv
import scanpy as sc
import numpy as np

print(f"scvi-tools version: {scvi.__version__}")
print(f"scvelo version: {scv.__version__}")
```

## 1단계: 접합/비접합 개수 생성

### BAM 파일에서(velocyto)

```bash
# Run velocyto on Cell Ranger output
velocyto run10x /path/to/cellranger_output /path/to/genes.gtf

# Output: velocyto.loom file with spliced/unspliced layers
```

### kb-python에서 (kalisto|bustools)

```bash
# Faster alternative using kallisto
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
# Load loom file from velocyto
adata = scv.read("velocyto_output.loom")

# Or load from kb-python
adata = sc.read_h5ad("adata.h5ad")
# Spliced in adata.layers["spliced"]
# Unspliced in adata.layers["unspliced"]

# Check layers
print("Available layers:", list(adata.layers.keys()))
print(f"Spliced shape: {adata.layers['spliced'].shape}")
print(f"Unspliced shape: {adata.layers['unspliced'].shape}")
```

### 기존 AnnData와 병합

```python
# If you have separate loom and h5ad
ldata = scv.read("velocyto.loom")
adata = sc.read_h5ad("processed.h5ad")

# Merge velocity data into processed adata
adata = scv.utils.merge(adata, ldata)
```

## 3단계: 속도 전처리

```python
# Filter and normalize
scv.pp.filter_and_normalize(
    adata,
    min_shared_counts=20,
    n_top_genes=2000
)

# Compute moments (for scVelo comparison)
scv.pp.moments(adata, n_pcs=30, n_neighbors=30)
```

## 4단계: veloVI 실행

### AnnData 설정

```python
# Setup for veloVI
scvi.model.VELOVI.setup_anndata(
    adata,
    spliced_layer="spliced",
    unspliced_layer="unspliced"
)
```

### 모델 훈련

```python
# Create and train veloVI model
vae = scvi.model.VELOVI(adata)

vae.train(
    max_epochs=500,
    early_stopping=True,
    batch_size=256
)

# Check training
vae.history["elbo_train"].plot()
```

### 속도 추정값 얻기

```python
# Get latent time
latent_time = vae.get_latent_time(n_samples=25)
adata.obs["veloVI_latent_time"] = latent_time

# Get velocity
velocities = vae.get_velocity(n_samples=25)
adata.layers["veloVI_velocity"] = velocities

# Get expression states
adata.layers["veloVI_expression"] = vae.get_expression_fit(n_samples=25)
```

## 5단계: 속도 시각화

### 속도 합리화

```python
# Compute velocity graph
scv.tl.velocity_graph(adata, vkey="veloVI_velocity")

# Plot streamlines on UMAP
scv.pl.velocity_embedding_stream(
    adata,
    basis="umap",
    vkey="veloVI_velocity",
    color="cell_type"
)
```

### 속도 화살표

```python
# Individual cell arrows
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
# Plot latent time (pseudotime from velocity)
sc.pl.umap(adata, color="veloVI_latent_time", cmap="viridis")
```

## 6단계: scVelo와 비교

```python
# Run standard scVelo for comparison
scv.tl.velocity(adata, mode="dynamical")
scv.tl.velocity_graph(adata)

# Compare velocity fields
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
# Plot phase portrait for specific genes
genes = ["SOX2", "PAX6", "DCX", "NEUROD1"]

scv.pl.velocity(
    adata,
    var_names=genes,
    vkey="veloVI_velocity",
    colorbar=True
)
```

### 유전자 역학

```python
# Plot expression over latent time
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
    ax.set_xlabel("Latent Time")
    ax.set_ylabel(f"{gene} Expression")
```

### 드라이버 유전자

```python
# Find genes driving velocity
scv.tl.rank_velocity_genes(
    adata,
    vkey="veloVI_velocity",
    groupby="cell_type"
)

# Get top genes per cluster
df = scv.get_df(adata, "rank_velocity_genes/names")
print(df.head(10))
```

## 8단계: 불확실성 정량화

veloVI는 불확실성 추정치를 제공합니다:

```python
# Get velocity with uncertainty
velocity_mean, velocity_std = vae.get_velocity(
    n_samples=100,
    return_mean=True,
    return_numpy=True
)

# Store uncertainty
adata.layers["velocity_uncertainty"] = velocity_std

# Visualize uncertainty
adata.obs["mean_velocity_uncertainty"] = velocity_std.mean(axis=1)
sc.pl.umap(adata, color="mean_velocity_uncertainty")
```

## 파이프라인 완성

```python
def run_velocity_analysis(
    adata,
    spliced_layer="spliced",
    unspliced_layer="unspliced",
    n_top_genes=2000,
    max_epochs=500
):
    """
    Complete RNA velocity analysis with veloVI.
    
    Parameters
    ----------
    adata : AnnData
        Data with spliced/unspliced layers
    spliced_layer : str
        Layer name for spliced counts
    unspliced_layer : str
        Layer name for unspliced counts
    n_top_genes : int
        Number of velocity genes
    max_epochs : int
        Training epochs
        
    Returns
    -------
    AnnData with velocity and model
    """
    import scvi
    import scvelo as scv
    import scanpy as sc
    
    adata = adata.copy()
    
    # Preprocessing
    scv.pp.filter_and_normalize(
        adata,
        min_shared_counts=20,
        n_top_genes=n_top_genes
    )
    
    # Compute moments (needed for some visualizations)
    scv.pp.moments(adata, n_pcs=30, n_neighbors=30)
    
    # Setup veloVI
    scvi.model.VELOVI.setup_anndata(
        adata,
        spliced_layer=spliced_layer,
        unspliced_layer=unspliced_layer
    )
    
    # Train
    model = scvi.model.VELOVI(adata)
    model.train(max_epochs=max_epochs, early_stopping=True)
    
    # Get results
    adata.obs["latent_time"] = model.get_latent_time(n_samples=25)
    adata.layers["velocity"] = model.get_velocity(n_samples=25)
    
    # Compute velocity graph for visualization
    scv.tl.velocity_graph(adata, vkey="velocity")
    
    # Compute UMAP if not present
    if "X_umap" not in adata.obsm:
        sc.pp.neighbors(adata)
        sc.tl.umap(adata)
    
    return adata, model

# Usage
adata_velocity, model = run_velocity_analysis(adata)

# Visualize
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
# For multi-batch data, include batch in model
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

- 합리화는 예상되는 차별화를 따릅니다.
- 잠복기는 알려진 생물학과 상관관계가 있습니다
- 위상 초상화는 명확한 역동성을 보여줍니다.

### 속도 신호 불량

- 무작위/혼란 유선형
- 알려진 마커와 상관관계 없음
- 다음을 나타낼 수 있습니다:
  - 불충분한 스플라이싱되지 않은 읽기
  - 정상 상태의 세포
  - 기술적인 문제

## 문제 해결

| 문제 | 원인 | 해결책 |
|-------|-------|----------|
| 속도 신호 없음 | 낮은 접합되지 않은 개수 | 시퀀싱 깊이를 확인하고 kb-python을 사용하세요. |
| 역방향 | 잘못된 루트 할당 | 수동으로 루트 셀 설정 |
| 시끄러운 유선형 | 유전자가 너무 많아 | n_top_genes 감소 |
| 메모리 오류 | 대규모 데이터 세트 | 배치 크기 줄이기 |

## 주요 참고자료

- Gayosoet al. (2023) "Deep generative modeling of transcriptional dynamics for RNA velocity analysis in single cells"
- La Mannoet al. (2018) "RNA velocity of single cells"
- Bergenet al. (2020) "Generalizing RNA velocity to transient cell states through dynamical modeling"
