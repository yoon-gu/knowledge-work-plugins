---
name: single-cell-rna-qc
description: scverse 모범 사례에 따른 MAD 기반 필터링과 포괄적 시각화를 통해 단일 세포 RNA-seq 데이터(.h5ad 또는 .h5 파일)의 품질 관리를 수행합니다. 사용자가 QC 분석, 저품질 세포 필터링, 데이터 품질 평가 또는 scverse/scanpy 모범 사례를 따르는 단일 세포 분석을 요청할 때 사용합니다.
---

# 단일 세포 RNA-seq 품질 관리

scverse 모범 사례에 따른 단일 세포 RNA-seq 데이터의 자동화된 QC 워크플로우입니다.

## 이 스킬을 사용할 때

다음과 같은 경우에 사용합니다:
- 단일 세포 RNA-seq 데이터에 대한 품질 관리 또는 QC를 요청할 때
- 저품질 세포를 필터링하거나 데이터 품질을 평가하고자 할 때
- QC 시각화 또는 지표가 필요할 때
- scverse/scanpy 모범 사례를 따르도록 요청할 때
- MAD 기반 필터링 또는 이상치 탐지를 요청할 때

**지원되는 입력 형식:**
- `.h5ad` 파일 (scanpy/Python 워크플로우의 AnnData 형식)
- `.h5` 파일 (10X Genomics Cell Ranger 출력)

**기본 권장 사항**: 사용자에게 특정 맞춤 요구사항이 있거나 비표준 필터링 로직을 명시적으로 요청하지 않는 한 접근 방식 1(완전한 파이프라인)을 사용합니다.

## 접근 방식 1: 완전한 QC 파이프라인 (표준 워크플로우에 권장)

scverse 모범 사례에 따른 표준 QC를 위해 편의 스크립트 `scripts/qc_analysis.py`를 사용합니다:

```bash
python3 scripts/qc_analysis.py input.h5ad
# 또는 10X Genomics .h5 파일의 경우:
python3 scripts/qc_analysis.py raw_feature_bc_matrix.h5
```

이 스크립트는 자동으로 파일 형식을 감지하고 적절하게 로드합니다.

**이 접근 방식을 사용할 때:**
- 조정 가능한 임계값이 있는 표준 QC 워크플로우 (모든 세포를 동일한 방식으로 필터링)
- 여러 데이터셋의 배치 처리
- 빠른 탐색적 분석
- 사용자가 "바로 작동하는" 솔루션을 원할 때

**요구사항:** anndata, scanpy, scipy, matplotlib, seaborn, numpy

**매개변수:**

명령줄 매개변수를 사용하여 필터링 임계값과 유전자 패턴을 커스터마이즈합니다:
- `--output-dir` - 출력 디렉토리
- `--mad-counts`, `--mad-genes`, `--mad-mt` - counts/genes/MT%에 대한 MAD 임계값
- `--mt-threshold` - 하드 미토콘드리아 % 기준점
- `--min-cells` - 유전자 필터링 임계값
- `--mt-pattern`, `--ribo-pattern`, `--hb-pattern` - 다른 종을 위한 유전자 이름 패턴

현재 기본값을 확인하려면 `--help`를 사용하세요.

**출력:**

모든 파일은 기본적으로 `<입력_기본이름>_qc_results/` 디렉토리에 저장됩니다 (또는 `--output-dir`로 지정된 디렉토리에):
- `qc_metrics_before_filtering.png` - 필터링 전 시각화
- `qc_filtering_thresholds.png` - MAD 기반 임계값 오버레이
- `qc_metrics_after_filtering.png` - 필터링 후 품질 지표
- `<입력_기본이름>_filtered.h5ad` - 하류 분석을 위한 깨끗하고 필터링된 데이터셋
- `<입력_기본이름>_with_qc.h5ad` - QC 주석이 보존된 원본 데이터

사용자 접근을 위해 출력을 복사할 때는 전체 디렉토리가 아닌 개별 파일을 복사하여 사용자가 직접 미리보기할 수 있도록 합니다.

### 워크플로우 단계

이 스크립트는 다음 단계를 수행합니다:

1. **QC 지표 계산** - Count depth, 유전자 탐지, 미토콘드리아/리보솜/헤모글로빈 함량
2. **MAD 기반 필터링 적용** - counts/genes/MT%에 대한 MAD 임계값을 사용한 관대한 이상치 탐지
3. **유전자 필터링** - 소수의 세포에서 탐지된 유전자 제거
4. **시각화 생성** - 임계값 오버레이가 포함된 포괄적인 필터링 전/후 플롯

## 접근 방식 2: 모듈형 구성 요소 (맞춤 워크플로우용)

맞춤 분석 워크플로우나 비표준 요구사항의 경우 `scripts/qc_core.py`와 `scripts/qc_plotting.py`의 모듈형 유틸리티 함수를 사용합니다:

```python
# scripts/ 디렉토리에서 실행하거나, 필요시 scripts/를 sys.path에 추가
import anndata as ad
from qc_core import calculate_qc_metrics, detect_outliers_mad, filter_cells
from qc_plotting import plot_qc_distributions  # 시각화가 필요한 경우에만

adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)
# ... 여기에 맞춤 분석 로직
```

**이 접근 방식을 사용할 때:**
- 다른 워크플로우가 필요한 경우 (단계 건너뛰기, 순서 변경, 하위 집합에 다른 임계값 적용)
- 조건부 로직 (예: 뉴런을 다른 세포와 다르게 필터링)
- 부분 실행 (지표/시각화만, 필터링 없이)
- 더 큰 파이프라인의 다른 분석 단계와 통합
- 명령줄 매개변수가 지원하는 것 이상의 맞춤 필터링 기준

**사용 가능한 유틸리티 함수:**

`qc_core.py`에서 (핵심 QC 작업):
- `calculate_qc_metrics(adata, mt_pattern, ribo_pattern, hb_pattern, inplace=True)` - QC 지표 계산 및 adata에 주석 달기
- `detect_outliers_mad(adata, metric, n_mads, verbose=True)` - MAD 기반 이상치 탐지, 불리언 마스크 반환
- `apply_hard_threshold(adata, metric, threshold, operator='>', verbose=True)` - 하드 기준점 적용, 불리언 마스크 반환
- `filter_cells(adata, mask, inplace=False)` - 불리언 마스크를 적용하여 세포 필터링
- `filter_genes(adata, min_cells=20, min_counts=None, inplace=True)` - 탐지 기준으로 유전자 필터링
- `print_qc_summary(adata, label='')` - 요약 통계 출력

`qc_plotting.py`에서 (시각화):
- `plot_qc_distributions(adata, output_path, title)` - 포괄적 QC 플롯 생성
- `plot_filtering_thresholds(adata, outlier_masks, thresholds, output_path)` - 필터링 임계값 시각화
- `plot_qc_after_filtering(adata, output_path)` - 필터링 후 플롯 생성

**맞춤 워크플로우 예시:**

**예시 1: 지표만 계산하고 시각화, 아직 필터링하지 않음**
```python
adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)
plot_qc_distributions(adata, 'qc_before.png', title='초기 QC')
print_qc_summary(adata, label='필터링 전')
```

**예시 2: MT% 필터링만 적용, 다른 지표는 관대하게 유지**
```python
adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)

# 높은 MT% 세포만 필터링
high_mt = apply_hard_threshold(adata, 'pct_counts_mt', 10, operator='>')
adata_filtered = filter_cells(adata, ~high_mt)
adata_filtered.write('filtered.h5ad')
```

**예시 3: 다른 하위 집합에 대한 다른 임계값**
```python
adata = ad.read_h5ad('input.h5ad')
calculate_qc_metrics(adata, inplace=True)

# 유형별 QC 적용 (cell_type 메타데이터가 존재한다고 가정)
neurons = adata.obs['cell_type'] == 'neuron'
other_cells = ~neurons

# 뉴런은 더 높은 MT%를 허용, 다른 세포는 더 엄격한 임계값 사용
neuron_qc = apply_hard_threshold(adata[neurons], 'pct_counts_mt', 15, operator='>')
other_qc = apply_hard_threshold(adata[other_cells], 'pct_counts_mt', 8, operator='>')
```

## 모범 사례

1. **필터링을 관대하게** - 기본 임계값은 희귀 집단의 손실을 방지하기 위해 의도적으로 대부분의 세포를 유지합니다
2. **시각화 검토** - 필터링이 생물학적으로 의미가 있는지 확인하기 위해 항상 전/후 플롯을 검토합니다
3. **데이터셋 특이적 요인 고려** - 일부 조직은 자연적으로 더 높은 미토콘드리아 함량을 가집니다 (예: 뉴런, 심근세포)
4. **유전자 주석 확인** - 미토콘드리아 유전자 접두사는 종에 따라 다릅니다 (마우스는 mt-, 인간은 MT-)
5. **필요시 반복** - QC 매개변수는 특정 실험이나 조직 유형에 따라 조정이 필요할 수 있습니다

## 참고 자료

자세한 QC 방법론, 매개변수 근거 및 문제 해결 지침은 `references/scverse_qc_guidelines.md`를 참조하세요. 이 참고 자료는 다음을 제공합니다:
- 각 QC 지표가 중요한 이유에 대한 자세한 설명
- MAD 기반 임계값의 근거와 고정 기준점보다 나은 이유
- QC 시각화(히스토그램, 바이올린 플롯, 산점도) 해석 지침
- 유전자 주석에 대한 종별 고려사항
- 필터링 매개변수 조정 시기와 방법
- 고급 QC 고려사항 (주변 RNA 보정, 이중체 탐지)

사용자가 방법론에 대한 더 깊은 이해가 필요하거나 QC 문제를 해결할 때 이 참고 자료를 로드하세요.

## QC 후 다음 단계

일반적인 하류 분석 단계:
- 주변 RNA 보정 (SoupX, CellBender)
- 이중체 탐지 (scDblFinder)
- 정규화 (log-normalize, scran)
- 특징 선택 및 차원 축소
- 클러스터링 및 세포 유형 주석
