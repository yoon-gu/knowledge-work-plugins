# totalVI를 이용한 CITE-seq 분석

이 레퍼런스는 totalVI를 사용한 CITE-seq 데이터 (RNA + 표면 단백질)의 다중 모달 분석을 다룹니다.

## 개요

CITE-seq는 다음을 결합합니다:
- scRNA-seq (전사체)
- 단백질 표면 마커 (항체 유래 태그, ADT)

totalVI는 두 모달리티를 공동으로 모델링하여:
- 배치 간 통합
- 단백질 신호 잡음 제거
- 공동 잠재 표현 학습
- 교차 모달 대체 활성화

## 사전 요구사항

```python
import scvi
import scanpy as sc
import mudata as md
import numpy as np
import pandas as pd

print(f"scvi-tools version: {scvi.__version__}")
```

## 1단계: CITE-seq 데이터 로드

### 10x Genomics (Cell Ranger)에서

```python
# 10x는 유전자 발현과 피처 바코딩을 별도로 출력
adata_rna = sc.read_10x_h5("filtered_feature_bc_matrix.h5", gex_only=False)

# RNA와 단백질 분리
adata_protein = adata_rna[:, adata_rna.var['feature_types'] == 'Antibody Capture'].copy()
adata_rna = adata_rna[:, adata_rna.var['feature_types'] == 'Gene Expression'].copy()

print(f"RNA: {adata_rna.shape}")
print(f"Protein: {adata_protein.shape}")
```

### MuData에서

```python
# MuData 형식의 데이터인 경우
mdata = md.read_h5mu("cite_seq.h5mu")

adata_rna = mdata['rna'].copy()
adata_protein = mdata['protein'].copy()
```

### 단일 AnnData로 결합

```python
# totalVI는 단백질 데이터를 obsm에 기대
adata = adata_rna.copy()

# obsm에 단백질 발현 추가
adata.obsm["protein_expression"] = adata_protein.X.toarray() if hasattr(adata_protein.X, 'toarray') else adata_protein.X

# 단백질 이름 저장
adata.uns["protein_names"] = list(adata_protein.var_names)
```

## 2단계: 품질 관리

### RNA QC

```python
# 표준 RNA QC
# 인간 (MT-)과 마우스 (mt-, Mt-) 미토콘드리아 유전자 모두 처리
    adata.var['mt'] = (
        adata.var_names.str.startswith('MT-') |
        adata.var_names.str.startswith('mt-') |
        adata.var_names.str.startswith('Mt-')
    )
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)

# 세포 필터링
adata = adata[adata.obs['n_genes_by_counts'] > 200].copy()
adata = adata[adata.obs['pct_counts_mt'] < 20].copy()

# 유전자 필터링
sc.pp.filter_genes(adata, min_cells=3)
```

### 단백질 QC

```python
# 단백질 QC
protein_counts = adata.obsm["protein_expression"]
print(f"세포당 단백질 카운트: min={protein_counts.sum(1).min():.0f}, max={protein_counts.sum(1).max():.0f}")

# 아이소타입 대조군 확인
# 아이소타입 대조군은 낮은 카운트를 가져야 함
protein_names = adata.uns["protein_names"]
for i, name in enumerate(protein_names):
    if 'isotype' in name.lower() or 'control' in name.lower():
        print(f"{name}: mean={protein_counts[:, i].mean():.1f}")
```

## 3단계: 데이터 준비

### 원시 카운트 저장

```python
# RNA 카운트 저장
adata.layers["counts"] = adata.X.copy()

# 단백질은 원시 ADT 카운트여야 함 (CLR 정규화된 것이 아님)
# 주의: Seurat에서 가져오는 경우, 정규화된 데이터가 아닌 원시 카운트를 사용해야 함
# Seurat의 NormalizeData(normalization.method = "CLR")는 카운트를 변환 - 원래 assay 사용
```

### RNA용 HVG 선택

```python
# RNA용 HVG 선택
# 참고: totalVI는 HVG에 관계없이 모든 단백질을 사용

sc.pp.highly_variable_genes(
    adata,
    n_top_genes=4000,  # CITE-seq에는 더 많이 사용
    flavor="seurat_v3",
    batch_key="batch" if "batch" in adata.obs else None,
    layer="counts"
)

# HVG로 서브셋
adata = adata[:, adata.var["highly_variable"]].copy()
```

## 4단계: totalVI 설정 및 학습

```python
# totalVI용 AnnData 설정
scvi.model.TOTALVI.setup_anndata(
    adata,
    layer="counts",
    protein_expression_obsm_key="protein_expression",
    batch_key="batch"  # 선택사항
)

# 모델 생성
model = scvi.model.TOTALVI(
    adata,
    n_latent=20,
    latent_distribution="normal"  # 또는 로그 정규 분포는 "ln"
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

## 5단계: 잠재 표현 얻기

```python
# 공동 잠재 공간
adata.obsm["X_totalVI"] = model.get_latent_representation()

# 클러스터링 및 시각화
sc.pp.neighbors(adata, use_rep="X_totalVI")
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=1.0)

sc.pl.umap(adata, color=['leiden', 'batch'])
```

## 6단계: 잡음 제거된 단백질 발현

```python
# 잡음 제거된 단백질 값 얻기
# 이것은 단백질 측정에서 배경 잡음을 제거

_, protein_denoised = model.get_normalized_expression(
    return_mean=True,
    transform_batch="batch1"  # 선택사항: 특정 배치로 정규화
)

# adata에 추가
adata.obsm["protein_denoised"] = protein_denoised

# 잡음 제거된 단백질 시각화
protein_names = adata.uns["protein_names"]
for i, protein in enumerate(protein_names[:5]):
    adata.obs[f"denoised_{protein}"] = protein_denoised[:, i]

sc.pl.umap(adata, color=[f"denoised_{p}" for p in protein_names[:5]])
```

## 7단계: 정규화된 RNA 발현

```python
# 정규화된 RNA 발현 얻기
rna_normalized, _ = model.get_normalized_expression(
    return_mean=True
)

# 저장
adata.layers["totalVI_normalized"] = rna_normalized
```

## 8단계: 차등 발현

### RNA 차등 발현

```python
# 클러스터 간 DE
de_rna = model.differential_expression(
    groupby="leiden",
    group1="0",
    group2="1"
)

# 유의미한 유전자 필터링
de_sig = de_rna[
    (de_rna['is_de_fdr_0.05']) &
    (abs(de_rna['lfc_mean']) > 1)
]

print(f"유의미한 DE 유전자: {len(de_sig)}")
```

### 단백질 차등 발현

```python
# 단백질 DE
de_protein = model.differential_expression(
    groupby="leiden",
    group1="0",
    group2="1",
    mode="protein"
)

print(de_protein.head(20))
```

## 9단계: 시각화

### UMAP 위의 단백질 발현

```python
# UMAP 위의 잡음 제거된 단백질
import matplotlib.pyplot as plt

proteins_to_plot = ["CD3", "CD4", "CD8", "CD19", "CD14"]

fig, axes = plt.subplots(1, len(proteins_to_plot), figsize=(4*len(proteins_to_plot), 4))
for ax, protein in zip(axes, proteins_to_plot):
    idx = adata.uns["protein_names"].index(protein)
    sc.pl.umap(
        adata,
        color=adata.obsm["protein_denoised"][:, idx],
        ax=ax,
        title=protein,
        show=False
    )
plt.tight_layout()
```

### 공동 히트맵

```python
# 클러스터별 상위 유전자 및 단백질 히트맵
sc.pl.dotplot(
    adata,
    var_names=de_sig.index[:20].tolist(),
    groupby="leiden",
    layer="totalVI_normalized"
)
```

## 10단계: 세포 유형 주석

```python
# RNA와 단백질 마커 모두 사용하여 주석

# RNA 마커
rna_markers = {
    'T cells': ['CD3D', 'CD3E'],
    'CD4 T': ['CD4'],
    'CD8 T': ['CD8A', 'CD8B'],
    'B cells': ['CD19', 'MS4A1'],
    'Monocytes': ['CD14', 'LYZ']
}

# 잡음 제거된 단백질 발현 확인
for i, protein in enumerate(adata.uns["protein_names"]):
    if any(m in protein for m in ['CD3', 'CD4', 'CD8', 'CD19', 'CD14']):
        print(f"{protein}: 클러스터 평균")
        for cluster in adata.obs['leiden'].unique():
            mask = adata.obs['leiden'] == cluster
            mean_expr = adata.obsm["protein_denoised"][mask, i].mean()
            print(f"  클러스터 {cluster}: {mean_expr:.2f}")
```

## 전체 파이프라인

```python
def analyze_citeseq(
    adata_rna,
    adata_protein,
    batch_key=None,
    n_top_genes=4000,
    n_latent=20
):
    """
    totalVI를 사용한 전체 CITE-seq 분석.

    Parameters
    ----------
    adata_rna : AnnData
        RNA 발현 (원시 카운트)
    adata_protein : AnnData
        단백질 발현 (원시 카운트)
    batch_key : str, optional
        obs의 배치 열
    n_top_genes : int
        HVG 수
    n_latent : int
        잠재 차원

    Returns
    -------
    (처리된 AnnData, 학습된 모델) 튜플
    """
    import scvi
    import scanpy as sc

    # 동일 세포 확인
    common_cells = adata_rna.obs_names.intersection(adata_protein.obs_names)
    adata = adata_rna[common_cells].copy()
    adata_protein = adata_protein[common_cells].copy()

    # obsm에 단백질 추가
    adata.obsm["protein_expression"] = adata_protein.X.toarray() if hasattr(adata_protein.X, 'toarray') else adata_protein.X
    adata.uns["protein_names"] = list(adata_protein.var_names)

    # RNA QC
    # 인간 (MT-)과 마우스 (mt-, Mt-) 미토콘드리아 유전자 모두 처리
    adata.var['mt'] = (
        adata.var_names.str.startswith('MT-') |
        adata.var_names.str.startswith('mt-') |
        adata.var_names.str.startswith('Mt-')
    )
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)
    adata = adata[adata.obs['pct_counts_mt'] < 20].copy()
    sc.pp.filter_genes(adata, min_cells=3)

    # 카운트 저장
    adata.layers["counts"] = adata.X.copy()

    # HVG 선택
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=n_top_genes,
        flavor="seurat_v3",
        batch_key=batch_key,
        layer="counts"
    )
    adata = adata[:, adata.var["highly_variable"]].copy()

    # totalVI 설정
    scvi.model.TOTALVI.setup_anndata(
        adata,
        layer="counts",
        protein_expression_obsm_key="protein_expression",
        batch_key=batch_key
    )

    # 학습
    model = scvi.model.TOTALVI(adata, n_latent=n_latent)
    model.train(max_epochs=200, early_stopping=True)

    # 표현 얻기
    adata.obsm["X_totalVI"] = model.get_latent_representation()
    rna_norm, protein_denoised = model.get_normalized_expression(return_mean=True)
    adata.layers["totalVI_normalized"] = rna_norm
    adata.obsm["protein_denoised"] = protein_denoised

    # 클러스터링
    sc.pp.neighbors(adata, use_rep="X_totalVI")
    sc.tl.umap(adata)
    sc.tl.leiden(adata)

    return adata, model

# 사용법
adata, model = analyze_citeseq(
    adata_rna,
    adata_protein,
    batch_key="batch"
)

# 시각화
sc.pl.umap(adata, color=['leiden', 'batch'])
```

## 문제 해결

| 문제 | 원인 | 해결 방법 |
|------|------|----------|
| 단백질 신호 잡음 | 배경 제거 안 됨 | 잡음 제거와 함께 get_normalized_expression 사용 |
| 배치 효과 지속 | batch_key 필요 | batch_key 지정 확인 |
| 메모리 오류 | 유전자 수 너무 많음 | n_top_genes 줄이기 |
| 단백질 클러스터링 불량 | 단백질 수 적음 | 정상 - totalVI는 구조에 RNA 사용 |

## 주요 참고문헌

- Gayoso et al. (2021) "Joint probabilistic modeling of single-cell multi-omic data with totalVI"
