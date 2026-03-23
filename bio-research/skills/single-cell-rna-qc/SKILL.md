---
name: single-cell-rna-qc
description: MAD 기반 필터링 및 포괄적인 시각화 기능을 갖춘 scverse 모범 사례를 사용하여 단일 세포 RNA-seq 데이터(.h5ad 또는 .h5 파일)에 대한 품질 관리를 수행합니다. 사용자가 QC 분석을 요청하거나, 품질이 낮은 세포를 필터링하거나, 데이터 품질을 평가하거나, 단일 세포 분석을 위한 scverse/scanpy 모범 사례를 따르는 경우에 사용합니다.
---

# Single-Cell RNA-seq 품질 관리

scverse 모범 사례에 따라 단일 세포 RNA-seq 데이터에 대한 자동화된 QC 워크플로우입니다.

## 이 스킬을 언제 사용해야 할까요?

사용자가 다음과 같은 경우에 사용하세요.
- 단일 세포 RNA-seq 데이터에 대한 품질 관리 또는 QC 요청
- 품질이 낮은 셀을 필터링하거나 데이터 품질을 평가하고 싶습니다.
- QC 시각화 또는 지표가 필요합니다.
- scverse/scanpy 모범 사례를 따르도록 요청하세요.
- MAD 기반 필터링 또는 이상치 감지 요청

**지원되는 입력 형식:**
- `.h5ad` 파일(scanpy/Python 워크플로의 AnnData 형식)
- `.h5` 파일(10X Genomics Cell Ranger 출력)

**기본 권장 사항**: 사용자가 특정 맞춤 요구 사항을 갖고 있거나 비표준 필터링 논리를 명시적으로 요청하지 않는 한 접근 방식 1(완전한 파이프라인)을 사용합니다.

## 접근 방식 1: QC 파이프라인 완료(표준 작업 흐름에 권장)

scverse 모범 사례를 따르는 표준 QC의 경우 편의 스크립트 `scripts/qc_analysis.py`을(를) 사용하십시오.

```bash
python3 scripts/qc_analysis.py input.h5ad
# or for 10X Genomics .h5 files:
python3 scripts/qc_analysis.py raw_feature_bc_matrix.h5
```

스크립트는 자동으로 파일 형식을 감지하고 적절하게 로드합니다.

**이 접근 방식을 사용하는 경우:**
- 조정 가능한 임계값이 있는 표준 QC 작업 흐름(모든 셀이 동일한 방식으로 필터링됨)
- 여러 데이터세트 일괄 처리
- 빠른 탐색적 분석
- 사용자는 "정상적으로 작동하는" 솔루션을 원합니다.

**요구사항:** anndata, scanpy, scipy, matplotlib, seaborn, numpy

**매개변수:**

명령줄 매개변수를 사용하여 필터링 임계값 및 유전자 패턴을 사용자 정의합니다.
- `--output-dir` - 출력 디렉터리
- `--mad-counts`, `--mad-genes`, `--mad-mt` - 개수/유전자/MT%에 대한 MAD 임계값
- `--mt-threshold` - 하드 미토콘드리아 % 컷오프
- `--min-cells` - 유전자 필터링 임계값
- `--mt-pattern`, `--ribo-pattern`, `--hb-pattern` - 다양한 종의 유전자 이름 패턴

현재 기본값을 보려면 `--help`을 사용하세요.

**출력:**

모든 파일은 기본적으로 `<input_basename>_qc_results/` 디렉터리(또는 `--output-dir`에서 지정한 디렉터리)에 저장됩니다.
- `qc_metrics_before_filtering.png` - 사전 필터링 시각화
- `qc_filtering_thresholds.png` - MAD 기반 임계값 오버레이
- `qc_metrics_after_filtering.png` - 필터링 후 품질 측정항목
- `<input_basename>_filtered.h5ad` - 다운스트림 분석을 위해 준비된 깨끗하고 필터링된 데이터세트
- `<input_basename>_with_qc.h5ad` - QC 주석이 보존된 원본 데이터

사용자 액세스를 위해 출력을 복사하는 경우 사용자가 직접 미리 볼 수 있도록 전체 디렉터리가 아닌 개별 파일을 복사합니다.

### 작업 흐름 단계

스크립트는 다음 단계를 수행합니다.

1. **QC 지표 계산** - 카운트 깊이, 유전자 검출, 미토콘드리아/리보솜/헤모글로빈 함량
2. **MAD 기반 필터링 적용** - 개수/유전자/MT%에 대한 MAD 임계값을 사용하여 허용되는 이상값 탐지
3. **필터 유전자** - 소수의 세포에서 검출된 유전자를 제거합니다.
4. **시각화 생성** - 임계값 오버레이가 포함된 포괄적인 전후 플롯

## 접근 방식 2: 모듈식 빌딩 블록(맞춤형 워크플로용)

사용자 정의 분석 워크플로 또는 비표준 요구 사항의 경우 `scripts/qc_core.py` 및 `scripts/qc_plotting.py`의 모듈식 유틸리티 기능을 사용하세요.

```python
# Run from scripts/ directory, or add scripts/ to sys.path if needed
import anndata as ad
from qc_core import calculate_qc_metrics, detect_outliers_mad, filter_cells
from qc_plotting import plot_qc_distributions  # Only if visualization needed

adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)
# ... custom analysis logic here
```

**이 접근 방식을 사용하는 경우:**
- 다양한 작업 흐름 필요(단계 건너뛰기, 순서 변경, 하위 집합에 다른 임계값 적용)
- 조건부 논리(예: 다른 세포와 다르게 뉴런 필터링)
- 부분 실행(메트릭/시각화만, 필터링 없음)
- 더 큰 파이프라인의 다른 분석 단계와 통합
- 명령줄 매개변수가 지원하는 것 이상의 사용자 정의 필터링 기준

**사용 가능한 유틸리티 기능:**

`qc_core.py`(핵심 QC 작업)에서:
- `calculate_qc_metrics(adata, mt_pattern, ribo_pattern, hb_pattern, inplace=True)` - QC 지표를 계산하고 데이터에 주석을 답니다.
- `detect_outliers_mad(adata, metric, n_mads, verbose=True)` - MAD 기반 이상값 감지, 부울 마스크 반환
- `apply_hard_threshold(adata, metric, threshold, operator='>', verbose=True)` - 하드 컷오프를 적용하고 부울 마스크를 반환합니다.
- `filter_cells(adata, mask, inplace=False)` - 필터 셀에 부울 마스크 적용
- `filter_genes(adata, min_cells=20, min_counts=None, inplace=True)` - 검출을 통해 유전자 필터링
- `print_qc_summary(adata, label='')` - 요약 통계 인쇄

`qc_plotting.py`(시각화)에서:
- `plot_qc_distributions(adata, output_path, title)` - 포괄적인 QC 플롯 생성
- `plot_filtering_thresholds(adata, outlier_masks, thresholds, output_path)` - 필터링 임계값 시각화
- `plot_qc_after_filtering(adata, output_path)` - 사후 필터링 플롯 생성

**맞춤형 워크플로의 예:**

**예 1: 측정항목을 계산하고 시각화만 하고 아직 필터링은 하지 않음**
```python
adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)
plot_qc_distributions(adata, 'qc_before.png', title='Initial QC')
print_qc_summary(adata, label='Before filtering')
```

**예 2: MT% 필터링만 적용하고 다른 측정항목은 허용되도록 유지**
```python
adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)

# Only filter high MT% cells
high_mt = apply_hard_threshold(adata, 'pct_counts_mt', 10, operator='>')
adata_filtered = filter_cells(adata, ~high_mt)
adata_filtered.write('filtered.h5ad')
```

**예 3: 다양한 하위 집합에 대한 다양한 임계값**
```python
adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)

# Apply type-specific QC (assumes cell_type metadata exists)
neurons = adata.obs['cell_type'] == 'neuron'
other_cells = ~neurons

# Neurons tolerate higher MT%, other cells use stricter threshold
neuron_qc = apply_hard_threshold(adata[neurons], 'pct_counts_mt', 15, operator='>')
other_qc = apply_hard_threshold(adata[other_cells], 'pct_counts_mt', 8, operator='>')
```

## 모범 사례

1. **필터링을 허용함** - 기본 임계값은 희귀한 개체군의 손실을 방지하기 위해 의도적으로 대부분의 세포를 유지합니다.
2. **시각화 검사** - 필터링이 생물학적으로 적합한지 확인하기 위해 플롯 전/후를 항상 검토합니다.
3. **데이터세트별 요인 고려** - 일부 조직은 자연적으로 미토콘드리아 함량이 더 높습니다(예: 뉴런, 심근세포).
4. **유전자 주석 확인** - 미토콘드리아 유전자 접두사는 종에 따라 다릅니다(마우스의 경우 mt, 인간의 경우 MT-).
5. **필요한 경우 반복** - QC 매개변수는 특정 실험이나 조직 유형에 따라 조정이 필요할 수 있습니다.

## 참고자료

자세한 QC 방법론, 매개변수 근거 및 문제 해결 지침은 `references/scverse_qc_guidelines.md`을 참조하세요. 이 참조는 다음을 제공합니다.
- 각 QC 지표에 대한 자세한 설명과 이것이 중요한 이유
- MAD 기반 임계값의 이론적 근거 및 고정 컷오프보다 나은 이유
- QC 시각화 해석을 위한 지침(히스토그램, 바이올린 플롯, 산점도)
- 유전자 주석에 대한 종별 고려사항
- 필터링 매개변수를 조정하는 시기와 방법
- 고급 QC 고려 사항(주변 RNA 보정, 이중 검출)

사용자가 방법론에 대한 더 깊은 이해가 필요하거나 QC 문제를 해결할 때 이 참조 자료를 로드하세요.

## QC 이후의 다음 단계

일반적인 다운스트림 분석 단계:
- 주변 RNA 보정(SoupX, CellBender)
- 이중선 검출(scDblFinder)
- 정규화(로그 정규화, 스크랜)
- 특징 선택 및 차원 축소
- 클러스터링 및 세포 유형 주석
