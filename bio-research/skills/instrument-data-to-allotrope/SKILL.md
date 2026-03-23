---
name: instrument-data-to-allotrope
description: Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.
---

# 기기 데이터를 Allotrope로 변환

기기 파일을 LIMS 업로드, 데이터 레이크 또는 데이터 엔지니어링 팀에 전달하기 위한 표준화된 Allotrope Simple Model (ASM) 형식으로 변환합니다.

> **참고: 이것은 예시 스킬입니다**
>
> 이 스킬은 스킬이 데이터 엔지니어링 작업(스키마 변환 자동화, 기기 출력 파싱, 프로덕션 준비 코드 생성)을 어떻게 지원할 수 있는지 보여줍니다.
>
> **조직에 맞게 커스터마이징하려면:**
> - 회사별 스키마 또는 온톨로지 매핑을 포함하도록 `references/` 파일을 수정하세요
> - MCP 서버를 사용하여 스키마를 정의하는 시스템(예: LIMS, 데이터 카탈로그, 스키마 레지스트리)에 연결하세요
> - 독점 기기 형식 또는 내부 데이터 표준을 처리하도록 `scripts/`를 확장하세요
>
> 이 패턴은 형식 간 변환 또는 조직 표준에 대한 검증이 필요한 모든 데이터 변환 워크플로우에 적용할 수 있습니다.

## 워크플로우 개요

1. **기기 유형 감지** — 파일 내용에서 기기 유형 감지 (자동 감지 또는 사용자 지정)
2. **파일 파싱** — allotropy 라이브러리(네이티브) 또는 유연한 대체 파서 사용
3. **출력 생성**:
   - ASM JSON (전체 시맨틱 구조)
   - 평탄화된 CSV (2D 표 형식)
   - Python 파서 코드 (데이터 엔지니어 전달용)
4. **전달** — 요약 및 사용 지침과 함께 파일 제공

> **불확실한 경우:** 필드를 ASM에 어떻게 매핑해야 할지 확실하지 않은 경우(예: 이것이 원시 데이터인가 계산된 데이터인가? 장치 설정인가 환경 조건인가?), 사용자에게 명확하게 확인하세요. 지침은 `references/field_classification_guide.md`를 참조하되, 모호한 경우 추측하지 말고 사용자에게 확인하세요.

## 빠른 시작

```python
# 먼저 요구 사항 설치
pip install allotropy pandas openpyxl pdfplumber --break-system-packages

# 핵심 변환
from allotropy.parser_factory import Vendor
from allotropy.to_allotrope import allotrope_from_file

# allotropy로 변환
asm = allotrope_from_file("instrument_data.csv", Vendor.BECKMAN_VI_CELL_BLU)
```

## 출력 형식 선택

**ASM JSON (기본)** - 온톨로지 URI가 포함된 전체 시맨틱 구조
- 적합한 용도: ASM을 기대하는 LIMS 시스템, 데이터 레이크, 장기 보관
- Allotrope 스키마에 대해 검증

**평탄화된 CSV** - 2D 표 형식 표현
- 적합한 용도: 빠른 분석, Excel 사용자, JSON을 지원하지 않는 시스템
- 각 측정이 메타데이터와 함께 하나의 행으로 표현

**둘 다** - 최대 유연성을 위해 두 형식 모두 생성

## 계산된 데이터 처리

**중요:** 원시 측정값과 계산/파생 값을 분리하세요.

- **원시 데이터** → `measurement-document` (직접 기기 판독값)
- **계산된 데이터** → `calculated-data-aggregate-document` (파생 값)

계산된 값은 반드시 `data-source-aggregate-document`를 통한 추적성을 포함해야 합니다:

```json
"calculated-data-aggregate-document": {
  "calculated-data-document": [{
    "calculated-data-identifier": "SAMPLE_B1_DIN_001",
    "calculated-data-name": "DNA integrity number",
    "calculated-result": {"value": 9.5, "unit": "(unitless)"},
    "data-source-aggregate-document": {
      "data-source-document": [{
        "data-source-identifier": "SAMPLE_B1_MEASUREMENT",
        "data-source-feature": "electrophoresis trace"
      }]
    }
  }]
}
```

**기기 유형별 일반적인 계산 필드:**
| 기기 | 계산된 필드 |
|------------|-------------------|
| 세포 계수기 | 생존율 %, 희석 조정된 세포 밀도 값 |
| 분광광도계 | 흡광도에서 농도 계산, 260/280 비율 |
| 플레이트 리더 | 표준 곡선에서 농도, %CV |
| 전기영동 | DIN/RIN, 영역 농도, 평균 크기 |
| qPCR | 상대적 수량, 배수 변화 |

원시 대 계산 분류에 대한 자세한 지침은 `references/field_classification_guide.md`를 참조하세요.

## 검증

사용자에게 전달하기 전에 항상 ASM 출력을 검증하세요:

```bash
python scripts/validate_asm.py output.json
python scripts/validate_asm.py output.json --reference known_good.json  # 참조와 비교
python scripts/validate_asm.py output.json --strict  # 경고를 오류로 처리
```

**검증 규칙:**
- Allotrope ASM 사양 기준 (2024년 12월)
- 마지막 업데이트: 2026-01-07
- 출처: https://gitlab.com/allotrope-public/asm

**소프트 검증 접근 방식:**
알 수 없는 기법, 단위 또는 샘플 역할은 앞으로의 호환성을 위해 **경고**(오류 아님)를 생성합니다. 2024년 12월 이후에 Allotrope가 새로운 값을 추가하는 경우, 검증기는 이를 차단하지 않고 수동 확인을 위해 플래그를 표시합니다. 더 엄격한 검증이 필요한 경우 `--strict` 모드를 사용하세요.

**확인 항목:**
- 올바른 기법 선택 (예: 다중 분석물 프로파일링 대 플레이트 리더)
- 필드 명명 규칙 (하이픈이 아닌 공백 구분)
- 계산된 데이터에 추적성 포함 (`data-source-aggregate-document`)
- 측정 및 계산된 값의 고유 식별자 존재
- 필수 메타데이터 존재
- 유효한 단위 및 샘플 역할 (알 수 없는 값에 대한 소프트 검증 포함)

## 지원 기기

전체 목록은 `references/supported_instruments.md`를 참조하세요. 주요 기기:

| 카테고리 | 기기 |
|----------|-------------|
| 세포 계수 | Vi-CELL BLU, Vi-CELL XR, NucleoCounter |
| 분광광도법 | NanoDrop One/Eight/8000, Lunatic |
| 플레이트 리더 | SoftMax Pro, EnVision, Gen5, CLARIOstar |
| ELISA | SoftMax Pro, BMG MARS, MSD Workbench |
| qPCR | QuantStudio, Bio-Rad CFX |
| 크로마토그래피 | Empower, Chromeleon |

## 감지 및 파싱 전략

### 1계층: 네이티브 allotropy 파싱 (권장)
**항상 allotropy를 먼저 시도하세요.** 사용 가능한 벤더를 직접 확인합니다:

```python
from allotropy.parser_factory import Vendor

# 모든 지원 벤더 나열
for v in Vendor:
    print(f"{v.name}")

# 일반적인 벤더:
# AGILENT_TAPESTATION_ANALYSIS  (TapeStation XML용)
# BECKMAN_VI_CELL_BLU
# THERMO_FISHER_NANODROP_EIGHT
# MOLDEV_SOFTMAX_PRO
# APPBIO_QUANTSTUDIO
# ... 더 많음
```

**사용자가 파일을 제공하면, 수동 파싱으로 대체하기 전에 allotropy가 지원하는지 확인하세요.** `scripts/convert_to_asm.py`의 자동 감지는 allotropy 벤더의 일부만 다룹니다.

### 2계층: 유연한 대체 파싱
**allotropy가 기기를 지원하지 않는 경우에만 사용합니다.** 이 대체 파서는:
- `calculated-data-aggregate-document`를 생성하지 않음
- 전체 추적성을 포함하지 않음
- 단순화된 ASM 구조 생성

유연한 파서 사용:
- 열 이름 퍼지 매칭
- 헤더에서 단위 추출
- 파일 구조에서 메타데이터 추출

### 3계층: PDF 추출
PDF 전용 파일의 경우 pdfplumber를 사용하여 표를 추출한 후 2계층 파싱을 적용합니다.

## 파싱 전 체크리스트

커스텀 파서를 작성하기 전에 항상 다음을 확인하세요:

1. **allotropy 지원 여부 확인** — 가능한 경우 네이티브 파서 사용
2. **참조 ASM 파일 찾기** — `references/examples/` 확인 또는 사용자에게 문의
3. **기기별 가이드 검토** — `references/instrument_guides/` 확인
4. **참조와 비교 검증** — `validate_asm.py --reference <file>` 실행

## 피해야 할 일반적인 실수

| 실수 | 올바른 접근 방식 |
|---------|------------------|
| manifest를 객체로 설정 | URL 문자열 사용 |
| 검출 유형을 소문자로 | "absorbance" 대신 "Absorbance" 사용 |
| "emission wavelength setting" | 방출에는 "detector wavelength setting" 사용 |
| 모든 측정을 하나의 문서에 | 웰/샘플 위치별로 그룹화 |
| 절차 메타데이터 누락 | 측정당 모든 장치 설정 추출 |

## 데이터 엔지니어를 위한 코드 내보내기

과학자가 전달할 수 있는 독립 실행형 Python 스크립트를 생성합니다:

```python
# 파서 코드 내보내기
python scripts/export_parser.py --input "data.csv" --vendor "VI_CELL_BLU" --output "parser_script.py"
```

내보낸 스크립트는:
- pandas/allotropy 이외의 외부 종속성 없음
- 인라인 문서 포함
- Jupyter 노트북에서 실행 가능
- 데이터 파이프라인을 위한 프로덕션 준비 완료

## 파일 구조

```
instrument-data-to-allotrope/
├── SKILL.md                          # 이 파일
├── scripts/
│   ├── convert_to_asm.py            # 메인 변환 스크립트
│   ├── flatten_asm.py               # ASM → 2D CSV 변환
│   ├── export_parser.py             # 독립 실행형 파서 코드 생성
│   └── validate_asm.py              # ASM 출력 품질 검증
└── references/
    ├── supported_instruments.md     # Vendor enum이 포함된 전체 기기 목록
    ├── asm_schema_overview.md       # ASM 구조 참조
    ├── field_classification_guide.md # 다양한 필드 유형 배치 위치
    └── flattening_guide.md          # 평탄화 작동 방식
```

## 사용 예시

### 예시 1: Vi-CELL BLU 파일
```
사용자: "이 세포 계수 데이터를 Allotrope 형식으로 변환해주세요"
[viCell_Results.xlsx 업로드]

Claude:
1. Vi-CELL BLU 감지 (신뢰도 95%)
2. allotropy 네이티브 파서로 변환
3. 출력:
   - viCell_Results_asm.json (전체 ASM)
   - viCell_Results_flat.csv (2D 형식)
   - viCell_parser.py (내보낼 수 있는 코드)
```

### 예시 2: 코드 전달 요청
```
사용자: "데이터 엔지니어에게 NanoDrop 파일을 파싱하는 코드가 필요합니다"

Claude:
1. 독립 실행형 Python 스크립트 생성
2. 샘플 입력/출력 포함
3. 모든 가정 문서화
4. Jupyter 노트북 버전 제공
```

### 예시 3: LIMS 준비 평탄화 출력
```
사용자: "이 ELISA 데이터를 LIMS에 업로드할 수 있는 CSV로 변환해주세요"

Claude:
1. 플레이트 리더 데이터 파싱
2. 다음 열이 포함된 평탄화된 CSV 생성:
   - sample_identifier, well_position, measurement_value, measurement_unit
   - instrument_serial_number, analysis_datetime, assay_type
3. 일반적인 LIMS 가져오기 요구 사항에 대해 검증
```

## 구현 참고 사항

### allotropy 설치
```bash
pip install allotropy --break-system-packages
```

### 파싱 실패 처리
allotropy 네이티브 파싱이 실패하는 경우:
1. 디버깅을 위해 오류 로그 기록
2. 유연한 파서로 대체
3. 사용자에게 메타데이터 완성도 감소 보고
4. 기기에서 다른 형식으로 내보내기 권장

### ASM 스키마 검증
사용 가능한 경우 Allotrope 스키마에 대해 출력을 검증합니다:
```python
import jsonschema
# references/asm_schema_overview.md의 스키마 URL
```
