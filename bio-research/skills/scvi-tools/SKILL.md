---
name: scvi-tools
description: scvi-tools를 사용한 단일 세포 분석을 위한 딥 러닝. 이 기술은 사용자가 (1) scVI/scANVI를 사용한 데이터 통합 및 일괄 수정, (2) PeakVI를 사용한 ATAC-seq 분석, (3) totalVI를 사용한 CITE-seq 다중 모드 분석, (4) MultiVI를 사용한 멀티옴 RNA+ATAC 분석, (5) DestVI를 사용한 공간 전사체 디콘볼루션, (6) scANVI/scArches를 사용한 라벨 전송 및 참조 매핑, (7) veloVI를 사용한 RNA 속도 또는 (8) 모든 심층이 필요한 경우에 사용해야 합니다. 학습 기반 단일 세포 방법. 트리거에는 scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, Variational Autoencoder, VAE, 배치 수정, 데이터 통합, 다중 모드, CITE-seq, multiome, 참조 매핑, 잠재 공간에 대한 언급이 포함됩니다.
---

# scvi-tools 딥러닝 기술

이 기술은 단일 세포 유전체학의 확률 모델을 위한 선도적인 프레임워크인 scvi-tools를 사용하여 딥 러닝 기반 단일 세포 분석에 대한 지침을 제공합니다.

## 이 스킬을 사용하는 방법

1. 아래 모델/워크플로 표에서 적절한 워크플로를 식별합니다.
2. 자세한 단계와 코드는 해당 참조 파일을 읽어보세요.
3. 일반적인 코드를 다시 작성하지 않으려면 `scripts/`의 스크립트를 사용하세요.
4. 설치 또는 GPU 문제는 `references/environment_setup.md`에 문의하세요.
5. 디버깅을 위해서는 `references/troubleshooting.md`를 참조하세요.

## 이 스킬을 언제 사용해야 할까요?

- scvi-tools, scVI, scANVI 또는 관련 모델이 언급되는 경우
- 딥러닝 기반의 일괄 수정이나 통합이 필요한 경우
- 다중 모드 데이터(CITE-seq, multiome)로 작업하는 경우
- Reference Mapping이나 Label Transfer가 필요한 경우
- ATAC-seq 또는 공간전사체 데이터를 분석할 때
- 단일 세포 데이터의 잠재 표현을 학습할 때

## 모델 선택 가이드

| 데이터 유형 | 모델 | 기본 사용 사례 |
|------------|-------|------|
| scRNA-seq | **scVI** | 비지도 통합, DE, 대치 |
| scRNA-seq + 라벨 | **scANVI** | 라벨 전송, 준감독 통합 |
| CITE-seq(RNA+단백질) | **totalVI** | 다중 모드 통합, 단백질 노이즈 제거 |
| scATAC-seq | **PeakVI** | 크로마틴 접근성 분석 |
| 멀티옴(RNA+ATAC) | **MultiVI** | 공동 양식 분석 |
| 공간 + scRNA 참조 | **DestVI** | 세포 유형 디콘볼루션 |
| RNA 속도 | **veloVI** | 전사 역학 |
| 교차 기술 | **sysVI** | 시스템 수준 일괄 수정 |

## 워크플로 참조 파일

| 작업 흐름 | 참조 파일 | 설명 |
|------------|---------------|-------------|
| 환경설정 | `references/environment_setup.md` | 설치, GPU, 버전 정보 |
| 데이터 준비 | `references/data_preparation.md` | 모든 모델의 데이터 형식 지정 |
| scRNA 통합 | `references/scrna_integration.md` | scVI/scANVI 일괄 수정 |
| ATAC-seq 분석 | `references/atac_peakvi.md` | 접근성을 위한 PeakVI |
| CITE-seq 분석 | `references/citeseq_totalvi.md` | 단백질+RNA용 totalVI |
| 멀티옴 분석 | `references/multiome_multivi.md` | RNA+ATAC용 MultiVI |
| 공간 디콘볼루션 | `references/spatial_deconvolution.md` | DestVI 공간 분석 |
| 라벨 전송 | `references/label_transfer.md` | scANVI 참조 매핑 |
| scArches 매핑 | `references/scarches_mapping.md` | 쿼리-참조 매핑 |
| 일괄 수정 | `references/batch_correction_sysvi.md` | 고급 배치 방법 |
| RNA 속도 | `references/rna_velocity_velovi.md` | veloVI 역학 |
| 문제 해결 | `references/troubleshooting.md` | 일반적인 문제 및 솔루션 |

## CLI 스크립트

일반적인 작업흐름을 위한 모듈식 스크립트. 필요에 따라 함께 연결하거나 수정하세요.

### 파이프라인 스크립트

| 스크립트 | 목적 | 사용법 |
|---------|---------|-------|
| `prepare_data.py` | QC, 필터, HVG 선택 | `python scripts/prepare_data.py raw.h5ad prepared.h5ad --batch-key batch` |
| `train_model.py` | scvi-tools 모델 훈련 | `python scripts/train_model.py prepared.h5ad results/ --model scvi` |
| `cluster_embed.py` | 이웃, UMAP, 라이덴 | `python scripts/cluster_embed.py adata.h5ad results/` |
| `differential_expression.py` | DE 분석 | `python scripts/differential_expression.py model/ adata.h5ad de.csv --groupby leiden` |
| `transfer_labels.py` | scANVI를 사용한 라벨 전송 | `python scripts/transfer_labels.py ref_model/ query.h5ad results/` |
| `integrate_datasets.py` | 다중 데이터 세트 통합 | `python scripts/integrate_datasets.py results/ data1.h5ad data2.h5ad` |
| `validate_adata.py` | 데이터 호환성 확인 | `python scripts/validate_adata.py data.h5ad --batch-key batch` |

### 워크플로 예시

```bash
# 1. Validate input data
python scripts/validate_adata.py raw.h5ad --batch-key batch --suggest

# 2. Prepare data (QC, HVG selection)
python scripts/prepare_data.py raw.h5ad prepared.h5ad --batch-key batch --n-hvgs 2000

# 3. Train model
python scripts/train_model.py prepared.h5ad results/ --model scvi --batch-key batch

# 4. Cluster and visualize
python scripts/cluster_embed.py results/adata_trained.h5ad results/ --resolution 0.8

# 5. Differential expression
python scripts/differential_expression.py results/model results/adata_clustered.h5ad results/de.csv --groupby leiden
```

### 파이썬 유틸리티

`scripts/model_utils.py`은 사용자 정의 작업 흐름에 대해 가져올 수 있는 기능을 제공합니다.

| 기능 | 목적 |
|------------|---------|
| `prepare_adata()` | 데이터 준비(QC, HVG, 레이어 설정) |
| `train_scvi()` | scVI 또는 scANVI 훈련 |
| `evaluate_integration()` | 컴퓨팅 통합 지표 |
| `get_marker_genes()` | DE 마커 추출 |
| `save_results()` | 모델, 데이터, 플롯 저장 |
| `auto_select_model()` | 최고의 모델 제안 |
| `quick_clustering()` | 이웃 + UMAP + 라이덴 |

## 중요 요구 사항

1. **원시 개수 필요**: scvi-tools 모델에는 정수 개수 데이터가 필요합니다.
   ```python
   adata.layers["counts"] = adata.X.copy()  # Before normalization
   scvi.model.SCVI.setup_anndata(adata, layer="counts")
   ```

2. **HVG 선택**: 2000-4000개의 고도로 가변적인 유전자 사용
   ```python
   sc.pp.highly_variable_genes(adata, n_top_genes=2000, batch_key="batch", layer="counts", flavor="seurat_v3")
   adata = adata[:, adata.var['highly_variable']].copy()
   ```

3. **배치정보** : 통합을 위한 Batch_key 지정
   ```python
   scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
   ```

## 빠른 의사결정 트리

```
Need to integrate scRNA-seq data?
├── Have cell type labels? → scANVI (references/label_transfer.md)
└── No labels? → scVI (references/scrna_integration.md)

Have multi-modal data?
├── CITE-seq (RNA + protein)? → totalVI (references/citeseq_totalvi.md)
├── Multiome (RNA + ATAC)? → MultiVI (references/multiome_multivi.md)
└── scATAC-seq only? → PeakVI (references/atac_peakvi.md)

Have spatial data?
└── Need cell type deconvolution? → DestVI (references/spatial_deconvolution.md)

Have pre-trained reference model?
└── Map query to reference? → scArches (references/scarches_mapping.md)

Need RNA velocity?
└── veloVI (references/rna_velocity_velovi.md)

Strong cross-technology batch effects?
└── sysVI (references/batch_correction_sysvi.md)
```

## 주요 리소스

- [scvi-tools Documentation](https://docs.scvi-tools.org/)
- [scvi-tools Tutorials](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
- [Model Hub](https://huggingface.co/scvi-tools)
- [GitHub Issues](https://github.com/scverse/scvi-tools/issues)
