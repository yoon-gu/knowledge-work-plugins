---
name: scvi-tools
description: scvi-tools를 사용한 단일 세포 분석을 위한 딥러닝. 이 스킬은 사용자가 (1) scVI/scANVI를 사용한 데이터 통합 및 배치 보정, (2) PeakVI를 사용한 ATAC-seq 분석, (3) totalVI를 사용한 CITE-seq 다중 모달 분석, (4) MultiVI를 사용한 멀티옴 RNA+ATAC 분석, (5) DestVI를 사용한 공간 전사체학 탈콘볼루션, (6) scANVI/scArches를 사용한 라벨 전이 및 참조 매핑, (7) veloVI를 사용한 RNA 속도, 또는 (8) 딥러닝 기반 단일 세포 방법이 필요할 때 사용해야 합니다. 트리거에는 scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, 변분 오토인코더, VAE, 배치 보정, 데이터 통합, 다중 모달, CITE-seq, 멀티옴, 참조 매핑, 잠재 공간의 언급이 포함됩니다.
---

# scvi-tools 딥러닝 스킬

이 스킬은 단일 세포 유전체학에서 확률 모델의 선도적 프레임워크인 scvi-tools를 사용한 딥러닝 기반 단일 세포 분석에 대한 가이드를 제공합니다.

## 이 스킬 사용 방법

1. 아래의 모델/워크플로우 테이블에서 적절한 워크플로우를 식별합니다
2. 상세한 단계와 코드를 위해 해당 참조 파일을 읽습니다
3. 공통 코드 재작성을 피하기 위해 `scripts/`의 스크립트를 사용합니다
4. 설치 또는 GPU 문제는 `references/environment_setup.md`를 참조합니다
5. 디버깅은 `references/troubleshooting.md`를 참조합니다

## 이 스킬 사용 시기

- scvi-tools, scVI, scANVI 또는 관련 모델이 언급될 때
- 딥러닝 기반 배치 보정 또는 통합이 필요할 때
- 다중 모달 데이터 작업 시 (CITE-seq, 멀티옴)
- 참조 매핑 또는 라벨 전이가 필요할 때
- ATAC-seq 또는 공간 전사체학 데이터 분석 시
- 단일 세포 데이터의 잠재 표현 학습 시

## 모델 선택 가이드

| 데이터 유형 | 모델 | 주요 사용 사례 |
|-----------|-------|------------------|
| scRNA-seq | **scVI** | 비지도 통합, DE, 보간 |
| scRNA-seq + 라벨 | **scANVI** | 라벨 전이, 반지도 통합 |
| CITE-seq (RNA+단백질) | **totalVI** | 다중 모달 통합, 단백질 노이즈 제거 |
| scATAC-seq | **PeakVI** | 크로마틴 접근성 분석 |
| 멀티옴 (RNA+ATAC) | **MultiVI** | 공동 모달리티 분석 |
| 공간 + scRNA 참조 | **DestVI** | 세포 유형 탈콘볼루션 |
| RNA 속도 | **veloVI** | 전사 동역학 |
| 기술 간 | **sysVI** | 시스템 수준 배치 보정 |

## 워크플로우 참조 파일

| 워크플로우 | 참조 파일 | 설명 |
|----------|---------------|-------------|
| 환경 설정 | `references/environment_setup.md` | 설치, GPU, 버전 정보 |
| 데이터 준비 | `references/data_preparation.md` | 모든 모델을 위한 데이터 포맷팅 |
| scRNA 통합 | `references/scrna_integration.md` | scVI/scANVI 배치 보정 |
| ATAC-seq 분석 | `references/atac_peakvi.md` | PeakVI 접근성 분석 |
| CITE-seq 분석 | `references/citeseq_totalvi.md` | totalVI 단백질+RNA 분석 |
| 멀티옴 분석 | `references/multiome_multivi.md` | MultiVI RNA+ATAC 분석 |
| 공간 탈콘볼루션 | `references/spatial_deconvolution.md` | DestVI 공간 분석 |
| 라벨 전이 | `references/label_transfer.md` | scANVI 참조 매핑 |
| scArches 매핑 | `references/scarches_mapping.md` | 쿼리-참조 매핑 |
| 배치 보정 | `references/batch_correction_sysvi.md` | 고급 배치 방법 |
| RNA 속도 | `references/rna_velocity_velovi.md` | veloVI 동역학 |
| 문제 해결 | `references/troubleshooting.md` | 일반적인 문제 및 해결 방법 |

## CLI 스크립트

공통 워크플로우를 위한 모듈식 스크립트. 필요에 따라 체인하거나 수정하세요.

### 파이프라인 스크립트

| 스크립트 | 목적 | 사용법 |
|--------|---------|-------|
| `prepare_data.py` | QC, 필터링, HVG 선택 | `python scripts/prepare_data.py raw.h5ad prepared.h5ad --batch-key batch` |
| `train_model.py` | 모든 scvi-tools 모델 훈련 | `python scripts/train_model.py prepared.h5ad results/ --model scvi` |
| `cluster_embed.py` | 이웃, UMAP, Leiden | `python scripts/cluster_embed.py adata.h5ad results/` |
| `differential_expression.py` | DE 분석 | `python scripts/differential_expression.py model/ adata.h5ad de.csv --groupby leiden` |
| `transfer_labels.py` | scANVI를 사용한 라벨 전이 | `python scripts/transfer_labels.py ref_model/ query.h5ad results/` |
| `integrate_datasets.py` | 다중 데이터셋 통합 | `python scripts/integrate_datasets.py results/ data1.h5ad data2.h5ad` |
| `validate_adata.py` | 데이터 호환성 확인 | `python scripts/validate_adata.py data.h5ad --batch-key batch` |

### 예시 워크플로우

```bash
# 1. 입력 데이터 검증
python scripts/validate_adata.py raw.h5ad --batch-key batch --suggest

# 2. 데이터 준비 (QC, HVG 선택)
python scripts/prepare_data.py raw.h5ad prepared.h5ad --batch-key batch --n-hvgs 2000

# 3. 모델 훈련
python scripts/train_model.py prepared.h5ad results/ --model scvi --batch-key batch

# 4. 클러스터링 및 시각화
python scripts/cluster_embed.py results/adata_trained.h5ad results/ --resolution 0.8

# 5. 차등 발현 분석
python scripts/differential_expression.py results/model results/adata_clustered.h5ad results/de.csv --groupby leiden
```

### Python 유틸리티

`scripts/model_utils.py`는 커스텀 워크플로우를 위한 임포트 가능한 함수를 제공합니다:

| 함수 | 목적 |
|----------|---------|
| `prepare_adata()` | 데이터 준비 (QC, HVG, 레이어 설정) |
| `train_scvi()` | scVI 또는 scANVI 훈련 |
| `evaluate_integration()` | 통합 지표 계산 |
| `get_marker_genes()` | DE 마커 추출 |
| `save_results()` | 모델, 데이터, 플롯 저장 |
| `auto_select_model()` | 최적 모델 제안 |
| `quick_clustering()` | 이웃 + UMAP + Leiden |

## 핵심 요구 사항

1. **원시 카운트 필수**: scvi-tools 모델은 정수 카운트 데이터가 필요합니다
   ```python
   adata.layers["counts"] = adata.X.copy()  # 정규화 전에
   scvi.model.SCVI.setup_anndata(adata, layer="counts")
   ```

2. **HVG 선택**: 2000-4000개의 고변이 유전자 사용
   ```python
   sc.pp.highly_variable_genes(adata, n_top_genes=2000, batch_key="batch", layer="counts", flavor="seurat_v3")
   adata = adata[:, adata.var['highly_variable']].copy()
   ```

3. **배치 정보**: 통합을 위한 batch_key 지정
   ```python
   scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
   ```

## 빠른 의사 결정 트리

```
scRNA-seq 데이터를 통합해야 하나요?
├── 세포 유형 라벨이 있나요? → scANVI (references/label_transfer.md)
└── 라벨이 없나요? → scVI (references/scrna_integration.md)

다중 모달 데이터가 있나요?
├── CITE-seq (RNA + 단백질)? → totalVI (references/citeseq_totalvi.md)
├── 멀티옴 (RNA + ATAC)? → MultiVI (references/multiome_multivi.md)
└── scATAC-seq만? → PeakVI (references/atac_peakvi.md)

공간 데이터가 있나요?
└── 세포 유형 탈콘볼루션이 필요한가요? → DestVI (references/spatial_deconvolution.md)

사전 훈련된 참조 모델이 있나요?
└── 참조에 쿼리를 매핑하나요? → scArches (references/scarches_mapping.md)

RNA 속도가 필요한가요?
└── veloVI (references/rna_velocity_velovi.md)

기술 간 강한 배치 효과가 있나요?
└── sysVI (references/batch_correction_sysvi.md)
```

## 주요 리소스

- [scvi-tools 문서](https://docs.scvi-tools.org/)
- [scvi-tools 튜토리얼](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
- [Model Hub](https://huggingface.co/scvi-tools)
- [GitHub Issues](https://github.com/scverse/scvi-tools/issues)
