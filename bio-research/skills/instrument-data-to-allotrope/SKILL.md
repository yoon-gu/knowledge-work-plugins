---
name: instrument-data-to-allotrope
description: 실험실 장비 출력 파일(PDF, CSV, Excel, TXT)을 ASM(Allotrope Simple Model) JSON 또는 평면화된 2차원 CSV로 변환합니다. 과학자가 기기 데이터를 LIMS 시스템, 데이터 레이크 또는 후속 분석용으로 표준화해야 할 때 사용하세요. 기기 유형의 자동 감지를 지원하며, 출력에는 전체 ASM JSON, 가져오기 쉬운 평면화된 CSV, 데이터 엔지니어용으로 내보낼 수 있는 Python 코드가 포함됩니다. 일반적인 사용 사례는 기기 파일 변환, 실험실 데이터 표준화, LIMS/ELN 업로드 준비, 생산 파이프라인용 파서 코드 생성입니다.
---
# 기기 데이터를 Allotrope ASM으로 변환하기

LIMS 업로드, 데이터 레이크, 또는 데이터 엔지니어링 팀에 전달할 수 있도록 기기 파일을 표준화된 ASM 형식으로 변환합니다.

> **참고: 예시 스킬입니다**
>
> 이 스킬은 스키마 변환 자동화, 장비 출력 파싱, 바로 사용할 수 있는 코드 생성 같은 데이터 엔지니어링 작업을 어떻게 지원할 수 있는지 보여주는 예시입니다.
>
> **조직에 맞게 사용자 정의하려면:**
> - 회사의 특정 스키마나 온톨로지 매핑을 반영하도록 `references/` 파일을 수정하세요.
> - MCP 서버를 사용해 스키마를 정의하는 시스템(예: LIMS, 데이터 카탈로그, 스키마 레지스트리)에 연결하세요.
> - `scripts/`를 확장해 독점 기기 형식이나 내부 데이터 표준을 처리하세요.
>
> 이 패턴은 형식 간 변환이나 조직 표준에 따른 검증이 필요한 모든 데이터 변환 워크플로에 맞게 조정할 수 있습니다.

## 워크플로 개요

1. 파일 내용에서 **기기 유형 감지**(자동 감지 또는 사용자 지정)
2. Allotrope 라이브러리(기본 제공) 또는 유연한 대체 파서를 사용해 **파일 파싱**
3. **출력 생성**:
   - ASM JSON(전체 의미 구조)
   - 평면화된 CSV(2차원 표 형식)
   - Python 파서 코드(데이터 엔지니어 전달용)
4. 요약과 사용 지침이 포함된 **전달용** 파일

> **불확실한 경우:** 필드를 ASM에 어떻게 매핑해야 할지 확신이 서지 않으면(예: 이 값은 원시 데이터인가요, 계산된 데이터인가요? 장비 설정인가요, 환경 조건인가요?) 사용자에게 확인하세요. 자세한 지침은 `references/field_classification_guide.md`를 참고하세요. 그래도 애매하다면 추측하지 말고 사용자에게 다시 물어보세요.

## 빠른 시작

```python
# 먼저 필요한 패키지를 설치합니다
pip install allotropy pandas openpyxl pdfplumber --break-system-packages

# 핵심 변환
from allotropy.parser_factory import Vendor
from allotropy.to_allotrope import allotrope_from_file

# allotropy로 변환
asm = allotrope_from_file("instrument_data.csv", Vendor.BECKMAN_VI_CELL_BLU)
```

## 출력 형식 선택

**ASM JSON(기본값)** - 온톨로지 URI가 포함된 전체 의미 구조
- 가장 적합한 용도: ASM, 데이터 레이크, 장기 보관이 필요한 LIMS 시스템
- Allotrope 스키마에 대해 검증합니다.

**평면화된 CSV** - 2차원 표 형식 표현
- 가장 적합한 대상: 빠른 분석, Excel 사용자, JSON을 지원하지 않는 시스템
- 각 측정값은 메타데이터가 반복된 하나의 행이 됩니다.

**둘 다** - 유연성을 최대화하기 위해 두 형식을 모두 생성합니다.

## 계산된 데이터 처리

**중요:** 계산/파생값과 원시 측정값을 구분하세요.

- **원시 데이터** → `measurement-document`(직접 기기 판독값)
- **계산된 데이터** → `calculated-data-aggregate-document` (파생값)

계산된 값에는 `data-source-aggregate-document`를 통한 추적 가능성이 포함되어야 합니다.

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
|------------|------|
| 셀 카운터 | 생존율(%), 세포 밀도 희석 조정 값 |
| 분광 광도계 | 농도(흡광도 기준), 260/280 비율 |
| 플레이트 리더 | 표준 곡선의 농도, %CV |
| 전기영동 | DIN/RIN, 지역 농도, 평균 크기 |
| qPCR | 상대 수량, 배수 변경 |

원시 분류와 계산된 분류에 대한 자세한 지침은 `references/field_classification_guide.md`를 참고하세요.

## 검증

사용자에게 전달하기 전에 항상 ASM 출력을 검증하세요.

```bash
python scripts/validate_asm.py output.json
python scripts/validate_asm.py output.json --reference known_good.json  # Compare to reference
python scripts/validate_asm.py output.json --strict  # Treat warnings as errors
```

**검증 규칙:**
- Allotrope ASM 사양 기준(2024년 12월)
- 최종 업데이트 날짜: 2026-01-07
- 출처: https://gitlab.com/allotrope-public/asm

**부드러운 검증 방식:**
알 수 없는 기술, 단위, 샘플 역할은 향후 호환성을 위해 **경고**(오류 아님)로 처리됩니다. Allotrope가 2024년 12월 이후 새 값을 추가하더라도 검증기는 이를 막지 않고, 수동 확인이 필요하다는 표시만 남깁니다. 더 엄격한 검증이 필요하면 `--strict` 모드를 사용해 경고를 오류로 취급하세요.

**검사 항목:**
- 올바른 기술 선택(예: 다중 분석물 프로파일링 대 플레이트 리더)
- 필드 명명 규칙(하이픈 대신 공백 사용)
- 계산된 데이터에 추적성이 있는지 확인(`data-source-aggregate-document`)
- 측정값과 계산값에 대한 고유 식별자가 있는지 확인
- 필수 메타데이터 존재
- 유효한 단위와 샘플 역할(알 수 없는 값에 대한 부드러운 검증 포함)

## 지원되는 기기

전체 목록은 `references/supported_instruments.md`를 참고하세요. 주요 기기는 다음과 같습니다.

| 카테고리 | 기기 |
|----------|-------------|
| 세포 계수 | Vi-CELL BLU, Vi-CELL XR, NucleoCounter |
| 분광광도계 | NanoDrop One/Eight/8000, 루나틱 |
| 플레이트 리더 | SoftMax Pro, EnVision, Gen5, CLARIOstar |
| 엘리사 | 소프트맥스 프로, BMG MARS, MSD 워크벤치 |
| qPCR | QuantStudio, Bio-Rad CFX |
| 크로마토그래피 | Empower, Chromeleon |

## 탐지 및 구문 분석 전략

### 계층 1: 기본 Allotrope 파싱(선호)
**항상 Allotrope 파서를 먼저 시도하세요.** 사용 가능한 공급업체를 직접 확인하세요.

```python
from allotropy.parser_factory import Vendor

# 지원되는 모든 공급업체를 나열합니다
for v in Vendor:
    print(f"{v.name}")

# 대표적인 공급업체:
# AGILENT_TAPESTATION_ANALYSIS  (for TapeStation XML)
# BECKMAN_VI_CELL_BLU
# THERMO_FISHER_NANODROP_EIGHT
# MOLDEV_SOFTMAX_PRO
# APPBIO_QUANTSTUDIO
# ... many more
```

**사용자가 파일을 제공하면 수동 파싱으로 돌아가기 전에 Allotrope가 이를 지원하는지 확인하세요.** `scripts/convert_to_asm.py`의 자동 감지는 Allotrope 공급업체의 일부에만 적용됩니다.

### 계층 2: 유연한 대체 구문 분석
**Allotrope가 기기를 지원하지 않을 때만 사용하세요.** 이 대체 방식은 다음과 같습니다.
- `calculated-data-aggregate-document`을 생성하지 않습니다.
- 전체 추적성을 포함하지 않습니다.
- 단순화된 ASM 구조를 생성합니다.

다음과 함께 유연한 파서를 사용하세요.
- 열 이름 퍼지 매칭
- 헤더에서 단위 추출
- 파일 구조에서 메타데이터 추출

### 계층 3: PDF 추출
PDF 전용 파일은 pdfplumber로 표를 추출한 뒤, 2단계 파싱을 적용하세요.

## 사전 파싱 체크리스트

사용자 정의 파서를 작성하기 전에 항상 다음을 확인하세요.

1. **Allotrope 지원 여부 확인** - 가능하면 기본 파서를 사용하세요.
2. **참조 ASM 파일 찾기** - `references/examples/`를 확인하거나 사용자에게 물어보세요.
3. **기기별 가이드 검토** - `references/instrument_guides/`를 확인하세요.
4. **참조 파일로 검증** - `validate_asm.py --reference <file>`를 실행하세요.

## 피해야 할 일반적인 실수

| 실수 | 올바른 접근 |
|---------|------|
| 객체로 매니페스트 | URL 문자열 사용 |
| 기기명과 기술명을 지나치게 번역함 | 원래 제품명과 기술명을 유지 |
| "발광 파장 설정" | 방출에는 "검출기 파장 설정" 사용 |
| 하나의 문서에 모든 측정값 | 웰/샘플 위치별로 그룹화 |
| 프로시저 메타데이터 누락 | 측정별로 모든 장치 설정 추출 |

## 데이터 엔지니어를 위한 코드 내보내기

과학자가 넘겨줄 수 있는 독립형 Python 스크립트를 생성합니다.

```python
# 파서 코드 내보내기
python scripts/export_parser.py --input "data.csv" --vendor "VI_CELL_BLU" --output "parser_script.py"
```

내보낸 스크립트:
- pandas/Allotrope 외에 외부 종속성이 없습니다.
- 인라인 문서가 포함됩니다.
- Jupyter Notebook에서 실행할 수 있습니다.
- 데이터 파이프라인에서 바로 사용할 수 있도록 준비됩니다.

## 파일 구조

```
instrument-data-to-allotrope/
├── SKILL.md                          # This file
├── scripts/
│   ├── convert_to_asm.py            # 메인 변환 스크립트
│   ├── flatten_asm.py               # ASM → 2차원 CSV 변환
│   ├── export_parser.py             # 독립형 파서 코드 생성
│   └── validate_asm.py              # ASM 출력 품질 검증
└── references/
    ├── supported_instruments.md     # Vendor 열거형이 포함된 전체 기기 목록
    ├── asm_schema_overview.md       # ASM 구조 참고 자료
    ├── field_classification_guide.md # 각 필드 유형을 어디에 넣는지 설명
    └── flattening_guide.md          # 평면화 방식 설명
```

## 사용 예

### 예시 1: Vi-CELL BLU 파일

```
User: "Convert this cell counting data to Allotrope format"
[uploads viCell_Results.xlsx]

Claude:
1. Detects Vi-CELL BLU (95% confidence)
2. Converts using allotropy native parser
3. Outputs:
   - viCell_Results_asm.json (full ASM)
   - viCell_Results_flat.csv (2D format)
   - viCell_parser.py (exportable code)
```

### 예시 2: 코드 전달 요청

```
User: "I need to give our data engineer code to parse NanoDrop files"

Claude:
1. Generates self-contained Python script
2. Includes sample input/output
3. Documents all assumptions
4. Provides Jupyter notebook version
```

### 예 3: LIMS 지원 평면화된 출력

```
User: "Convert this ELISA data to a CSV I can upload to our LIMS"

Claude:
1. Parses plate reader data
2. Generates flattened CSV with columns:
   - sample_identifier, well_position, measurement_value, measurement_unit
   - instrument_serial_number, analysis_datetime, assay_type
3. Validates against common LIMS import requirements
```

## 구현 참고 사항

### Allotrope 설치

```bash
pip install allotropy --break-system-packages
```

### 구문 분석 실패 처리
Allotrope 기본 파싱이 실패하는 경우:
1. 디버깅을 위해 오류를 기록합니다.
2. 유연한 파서로 돌아가기
3. 감소된 메타데이터 완전성을 사용자에게 보고
4. 기기에서 다른 형식으로 내보내기 제안

### ASM 스키마 검증
가능하면 Allotrope 스키마를 기준으로 출력을 검증합니다.

```python
import jsonschema
# Schema URLs in references/asm_schema_overview.md
```
