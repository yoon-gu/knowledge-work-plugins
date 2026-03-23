# 필드 분류 가이드

이 가이드는 기기 데이터 필드를 올바른 ASM 문서 위치로 분류하는 데 도움을 줍니다. 원시 기기 출력을 Allotrope Simple Model 구조에 매핑할 때 사용하세요.

## ASM 문서 계층 구조

```
<technique>-aggregate-document
├── device-system-document          # 기기 하드웨어 정보
├── data-system-document            # 소프트웨어/변환 정보
├── <technique>-document[]          # 실행/시퀀스별 데이터
│   ├── analyst                     # 분석 수행자
│   ├── measurement-aggregate-document
│   │   ├── measurement-time
│   │   ├── measurement-document[]  # 개별 측정
│   │   │   ├── sample-document
│   │   │   ├── device-control-aggregate-document
│   │   │   └── [측정 필드]
│   │   └── [집계 수준 메타데이터]
│   ├── processed-data-aggregate-document
│   │   └── processed-data-document[]
│   │       ├── data-processing-document
│   │       └── [처리된 결과]
│   └── calculated-data-aggregate-document
│       └── calculated-data-document[]
```

## 필드 분류 카테고리

### 1. 장치/기기 정보 → `device-system-document`

물리적 기기에 대한 하드웨어 및 펌웨어 세부 정보.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 기기 이름 | `model-number` | "Vi-CELL BLU", "NanoDrop One" |
| 일련 번호 | `equipment-serial-number` | "VCB-12345", "SN001234" |
| 제조업체 | `product-manufacturer` | "Beckman Coulter", "Thermo Fisher" |
| 펌웨어 버전 | `firmware-version` | "v2.1.3" |
| 장치 ID | `device-identifier` | "Instrument_01" |
| 브랜드 | `brand-name` | "Beckman Coulter" |

**규칙:** 값이 물리적 기기를 설명하고 실행 간에 변경되지 않는 경우 `device-system-document`에 넣습니다.

---

### 2. 소프트웨어/데이터 시스템 정보 → `data-system-document`

수집, 분석 또는 변환에 사용된 소프트웨어에 대한 정보.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 소프트웨어 이름 | `software-name` | "Chromeleon", "Gen5" |
| 소프트웨어 버전 | `software-version` | "7.3.2" |
| 파일 이름 | `file-name` | "experiment_001.xlsx" |
| 파일 경로 | `file-identifier` | "/data/runs/2024-01-15/" |
| 데이터베이스 ID | `ASM-converter-name` | "allotropy v0.1.55" |

**규칙:** 값이 소프트웨어, 파일 메타데이터 또는 데이터 출처를 설명하는 경우 `data-system-document`에 넣습니다.

---

### 3. 샘플 정보 → `sample-document`

분석되는 생물학적/화학적 샘플에 대한 메타데이터.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 샘플 ID | `sample-identifier` | "Sample_A", "LIMS-001234" |
| 샘플 이름 | `written-name` | "CHO Cell Culture Day 5" |
| 샘플 유형/역할 | `sample-role-type` | "unknown sample role", "control sample role" |
| 배치 ID | `batch-identifier` | "Batch-2024-001" |
| 설명 | `description` | "단백질 발현 샘플" |
| 웰 위치 | `location-identifier` | "A1", "B3" |

**규칙:** 값이 측정된 대상을 식별하거나 설명하는 경우(방법이 아닌) `sample-document`에 넣습니다.

---

### 4. 장치 제어 설정 → `device-control-aggregate-document`

측정 중에 사용된 기기 설정 및 파라미터.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 주입 부피 | `sample-volume-setting` | 10 µL |
| 파장 | `detector-wavelength-setting` | 254 nm |
| 온도 | `compartment-temperature` | 37°C |
| 유속 | `flow-rate` | 1.0 mL/min |
| 노출 시간 | `exposure-duration-setting` | 500 ms |
| 검출기 이득 | `detector-gain-setting` | 1.5 |
| 조명 | `illumination-setting` | 80% |

**규칙:** 값이 측정에 영향을 미치는 구성 가능한 기기 파라미터인 경우 `device-control-aggregate-document`에 넣습니다.

---

### 5. 환경 조건 → `device-control-document` 또는 기법별

측정 중 주변 또는 제어된 환경 파라미터.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 주변 온도 | `ambient-temperature` | 22.5°C |
| 습도 | `ambient-relative-humidity` | 45% |
| 컬럼 온도 | `compartment-temperature` | 30°C |
| 샘플 온도 | `sample-temperature` | 4°C |
| 전기영동 온도 | (기법별) | 26.4°C |

**규칙:** 측정 품질에 영향을 미치는 환경 조건은 장치 제어 또는 기법별 위치에 넣습니다.

---

### 6. 원시 측정 데이터 → `measurement-document`

직접 기기 판독값 — "지실" 데이터.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 흡광도 | `absorbance` | 0.523 AU |
| 형광 | `fluorescence` | 12500 RFU |
| 세포 수 | `total-cell-count` | 2.5e6 cells |
| 피크 면적 | `peak-area` | 1234.5 mAU·min |
| 머무름 시간 | `retention-time` | 5.67 min |
| Ct 값 | `cycle-threshold-result` | 24.5 |
| 농도 (측정) | `mass-concentration` | 1.5 mg/mL |

**규칙:** 값이 이 분석에서 다른 값으로부터 계산되지 않은 직접 기기 판독값인 경우 `measurement-document`에 넣습니다.

---

### 7. 계산/파생 데이터 → `calculated-data-aggregate-document`

원시 측정값으로부터 계산된 값.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 생존율 % | `calculated-result` | 95.2% |
| 농도 (표준 곡선에서) | `calculated-result` | 125 ng/µL |
| 비율 (260/280) | `calculated-result` | 1.89 |
| 상대적 수량 | `calculated-result` | 2.5x |
| % 회수율 | `calculated-result` | 98.7% |
| CV% | `calculated-result` | 2.3% |

**계산된 데이터 문서 구조:**
```json
{
  "calculated-data-name": "viability",
  "calculated-result": {"value": 95.2, "unit": "%"},
  "calculation-description": "viable cells / total cells * 100"
}
```

**규칙:** 값이 이 분석의 다른 측정값으로부터 계산된 경우 `calculated-data-aggregate-document`에 넣습니다. 가능한 경우 `calculation-description`을 포함하세요.

---

### 8. 처리/분석된 데이터 → `processed-data-aggregate-document`

데이터 처리 알고리즘(피크 적분, 세포 분류 등)의 결과.

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 피크 목록 | `peak-list` | 적분된 피크 결과 |
| 세포 크기 분포 | `cell-diameter-distribution` | 히스토그램 데이터 |
| 기준선 보정 데이터 | (processed-data-document 내) | 보정된 스펙트럼 |
| 적합 곡선 | (processed-data-document 내) | 표준 곡선 적합 |

**관련 `data-processing-document`:**
```json
{
  "cell-type-processing-method": "trypan blue exclusion",
  "cell-density-dilution-factor": {"value": 2, "unit": "(unitless)"},
  "minimum-cell-diameter-setting": {"value": 5, "unit": "µm"},
  "maximum-cell-diameter-setting": {"value": 50, "unit": "µm"}
}
```

**규칙:** 값이 원시 데이터에 알고리즘이나 처리 방법을 적용하여 생성된 경우 처리 파라미터와 함께 `processed-data-aggregate-document`에 넣습니다.

---

### 9. 타이밍/타임스탬프 → 다양한 위치

| 타임스탬프 유형 | 위치 | ASM 필드 |
|----------------|----------|-----------|
| 측정 시간 | `measurement-document` | `measurement-time` |
| 실행 시작 시간 | `analysis-sequence-document` | `analysis-sequence-start-time` |
| 실행 종료 시간 | `analysis-sequence-document` | `analysis-sequence-end-time` |
| 데이터 내보내기 시간 | `data-system-document` | (커스텀) |

**규칙:** ISO 8601 형식 사용: `2024-01-15T10:30:00Z`

---

### 10. 분석가/운영자 정보 → `<technique>-document`

| 필드 유형 | ASM 필드 | 예시 |
|------------|-----------|----------|
| 운영자 이름 | `analyst` | "jsmith" |
| 검토자 | (커스텀 또는 확장) | "Pending" |

**규칙:** 분석가는 개별 측정이 아닌 기법-문서 수준에 넣습니다.

---

## 의사결정 트리

```
이 필드가 다음에 관한 것인가?

기기 자체?
├── 하드웨어 사양 → device-system-document
└── 소프트웨어/파일 → data-system-document

샘플?
└── 샘플 ID, 이름, 유형, 배치 → sample-document

기기 설정?
└── 구성 가능한 파라미터 → device-control-aggregate-document

환경 조건?
└── 온도, 습도 등 → device-control-document

직접 판독값?
└── 원시 기기 출력 → measurement-document

계산된 값?
├── 다른 측정값으로부터 → calculated-data-document
└── 처리 알고리즘으로부터 → processed-data-document

타이밍?
├── 측정 시간 → measurement-document.measurement-time
└── 실행 시작/종료 시간 → analysis-sequence-document

수행자?
└── 운영자/분석가 → <technique>-document.analyst
```

## 일반적인 기기-ASM 매핑

> **참고:** 이 매핑은 [Benchling allotropy 라이브러리](https://github.com/Benchling-Open-Source/allotropy/tree/main/src/allotropy/parsers)에서 파생되었습니다. 권위 있는 매핑을 위해 특정 기기의 파서 소스 코드를 참조하세요.

### 세포 계수기 (Vi-CELL BLU)
*출처: `allotropy/parsers/beckman_vi_cell_blu/vi_cell_blu_structure.py`*

| 기기 필드 | ASM 필드 |
|-----------------|-----------|
| Sample ID | `sample_identifier` |
| 분석 날짜/시간 | `measurement_time` |
| 분석 담당자 | `analyst` |
| 생존율 (%) | `viability` |
| 생존 (x10^6) cells/mL | `viable_cell_density` |
| 전체 (x10^6) cells/mL | `total_cell_density` |
| 세포 수 | `total_cell_count` |
| 생존 세포 | `viable_cell_count` |
| 평균 직경 (μm) | `average_total_cell_diameter` |
| 평균 생존 직경 (μm) | `average_live_cell_diameter` |
| 평균 원형도 | `average_total_cell_circularity` |
| 세포 유형 | `cell_type_processing_method` (data-processing) |
| 희석 | `cell_density_dilution_factor` (data-processing) |
| 최소/최대 직경 | `minimum/maximum_cell_diameter_setting` (data-processing) |

### 분광광도계 (NanoDrop)
| 기기 필드 | ASM 필드 |
|-----------------|-----------|
| 샘플 이름 | `sample_identifier` |
| A260, A280 | `absorbance` (파장 포함) |
| 농도 | `mass_concentration` |
| 260/280 비율 | `a260_a280_ratio` |
| 광로 길이 | `pathlength` |

### 플레이트 리더
| 기기 필드 | ASM 필드 |
|-----------------|-----------|
| 웰 | `location_identifier` |
| 샘플 유형 | `sample_role_type` |
| 흡광도/OD | `absorbance` |
| 형광 | `fluorescence` |
| 플레이트 ID | `container_identifier` |

### 크로마토그래피 (HPLC)
| 기기 필드 | ASM 필드 |
|-----------------|-----------|
| 샘플 ID | `sample_identifier` |
| 주입 부피 | `injection_volume` |
| 머무름 시간 | `retention_time` |
| 피크 면적 | `peak_area` |
| 피크 높이 | `peak_height` |
| 컬럼 온도 | `column_oven_temperature` |
| 유속 | `flow_rate` |

## 단위 처리

원본 데이터에 명시적으로 있는 단위만 사용하세요. 단위가 지정되지 않은 값의 경우:
- 단위 값으로 `(unitless)` 사용
- 도메인 지식을 기반으로 단위를 추론하지 마세요

## 계산된 데이터 추적성

계산된 값을 생성할 때 항상 `data-source-aggregate-document`를 사용하여 원본 데이터에 연결하세요:

```json
{
    "calculated-data-name": "DIN",
    "calculated-result": {"value": 5.8, "unit": "(unitless)"},
    "calculated-data-identifier": "TEST_ID_147",
    "data-source-aggregate-document": {
        "data-source-document": [{
            "data-source-identifier": "TEST_ID_145",
            "data-source-feature": "sample"
        }]
    }
}
```

이는 다음을 선언합니다: "DIN 5.8은 `TEST_ID_145`의 샘플에서 계산되었습니다."

**이것이 중요한 이유:**
- **감사**: 값이 특정 원시 데이터에서 나왔음을 증명
- **디버깅**: 예상치 못한 결과를 원본으로 역추적
- **재처리**: 알고리즘이 변경된 경우 재분석할 입력 파악

**다음에 고유 ID를 할당하세요:**
- 측정, 피크, 영역 및 계산된 값
- 일관된 명명 패턴 사용 (예: `INSTRUMENT_TYPE_TEST_ID_N`)

이를 통해 계산됨 → 원시로의, 또는 원시 → 모든 파생 값으로의 양방향 탐색이 가능합니다.

---

## 중첩 문서 구조 (중요)

일반적인 실수는 중첩 구조로 래핑해야 하는 필드를 측정 문서에 직접 "평탄화"하는 것입니다. 이는 스키마 준수를 위반하고 시맨틱 컨텍스트를 잃습니다.

### 중첩이 중요한 이유

ASM은 시맨틱 그룹화를 위해 중첩 문서를 사용합니다:

| 문서 | 목적 | 포함 내용 |
|----------|---------|----------|
| `sample document` | 측정된 대상 | 샘플 ID, 위치, 플레이트 식별자 |
| `device control aggregate document` | 기기 작동 방식 | 설정, 파라미터, 기법 |
| `custom information document` | 벤더별 필드 | ASM에 매핑되지 않는 비표준 필드 |

### 샘플 문서 필드

이 필드들은 반드시 측정에 평탄화되지 않고 `sample document` 내에 있어야 합니다:

```json
// ❌ 잘못된 예 — 측정에 필드가 평탄화됨
{
  "measurement identifier": "TEST_001",
  "sample identifier": "Sample_A",
  "location identifier": "A1",
  "absorbance": {"value": 0.5, "unit": "(unitless)"}
}

// ✅ 올바른 예 — 필드가 sample document에 중첩됨
{
  "measurement identifier": "TEST_001",
  "sample document": {
    "sample identifier": "Sample_A",
    "location identifier": "A1",
    "well plate identifier": "96WP001"
  },
  "absorbance": {"value": 0.5, "unit": "(unitless)"}
}
```

**sample document에 속하는 필드:**
- `sample identifier` — 샘플 ID/이름
- `written name` — 설명적 샘플 이름
- `batch identifier` — 배치/로트 번호
- `sample role type` — 표준, 블랭크, 대조군, 알 수 없음
- `location identifier` — 웰 위치 (A1, B3 등)
- `well plate identifier` — 플레이트 바코드
- `description` — 샘플 설명

### 장치 제어 문서 필드

기기 설정은 반드시 `device control aggregate document` 내에 있어야 합니다:

```json
// ❌ 잘못된 예 — 장치 설정이 평탄화됨
{
  "measurement identifier": "TEST_001",
  "device identifier": "Pod1",
  "technique": "Custom",
  "volume": {"value": 26, "unit": "μL"}
}

// ✅ 올바른 예 — 설정이 device control에 중첩됨
{
  "measurement identifier": "TEST_001",
  "device control aggregate document": {
    "device control document": [{
      "device type": "liquid handler",
      "device identifier": "Pod1"
    }]
  },
  "aspiration volume": {"value": 26, "unit": "μL"}
}
```

**device control에 속하는 필드:**
- `device type` — 장치 유형
- `device identifier` — 장치 ID
- `detector wavelength setting` — 검출 파장
- `compartment temperature` — 온도 설정
- `sample volume setting` — 부피 설정
- `flow rate` — 유속 설정

### 커스텀 정보 문서

표준 ASM 용어에 매핑되지 않는 벤더별 필드는 `custom information document`에 넣습니다:

```json
"device control document": [{
  "device type": "liquid handler",
  "custom information document": {
    "probe": "2",
    "pod": "Pod1",
    "source labware name": "Inducer",
    "destination labware name": "GRP1"
  }
}]
```

### 액체 취급기: 이송 쌍 처리

액체 취급기의 경우, 측정은 별도의 작업이 아닌 완전한 이송(흡인 + 분배)을 나타냅니다:

```json
// ❌ 잘못된 예 — 흡인과 분배에 대한 별도 레코드
[
  {"measurement identifier": "OP_001", "transfer type": "Aspirate", "volume": {"value": 26, "unit": "μL"}},
  {"measurement identifier": "OP_002", "transfer type": "Dispense", "volume": {"value": 26, "unit": "μL"}}
]

// ✅ 올바른 예 — 소스와 목적지를 포함한 단일 레코드
{
  "measurement identifier": "TRANSFER_001",
  "sample document": {
    "source well location identifier": "1",
    "destination well location identifier": "2",
    "source well plate identifier": "96WP001",
    "destination well plate identifier": "96WP002"
  },
  "aspiration volume": {"value": 26, "unit": "μL"},
  "transfer volume": {"value": 26, "unit": "μL"}
}
```

**쌍 처리 로직:**
1. 프로브 번호로 흡인과 분배 작업 매칭
2. 각 매칭된 쌍당 하나의 측정 생성
3. 흡인 위치에는 `source_*` 필드 사용
4. 분배 위치에는 `destination_*` 필드 사용
5. `aspiration volume`과 `transfer volume` 모두 포함

### 빠른 참조: 중첩 결정

```
이 필드가 다음에 관한 것인가?

측정된 샘플?
├── 샘플 ID, 이름, 배치 → sample document
├── 웰 위치 → sample document.location identifier
├── 플레이트 바코드 → sample document.well plate identifier
└── 소스/목적지 위치 → sample document (접두사 포함)

기기 설정?
├── 표준 설정 → device control aggregate document
└── 벤더별 → custom information document

측정값?
└── measurement document에 직접 (예: absorbance, volume)

이송 작업 유형?
└── "transfer type" 사용 금지 — 소스/목적지 필드로 단일 측정으로 쌍 처리
```

### 검증

중첩 문제를 확인하기 위해 `validate_asm.py` 사용:
```bash
python scripts/validate_asm.py output.json --reference known_good.json
```

검증기는 다음을 확인합니다:
- 측정에 잘못 평탄화된 필드
- `sample document` 래퍼 누락
- `device control aggregate document` 래퍼 누락
- 벤더 필드의 `custom information document` 누락
- 액체 취급기: 쌍 처리 대신 별도 이송 유형

## 출처

- [Allotrope Simple Model 소개](https://www.allotrope.org/introduction-to-allotrope-simple-model)
- [Benchling allotropy 라이브러리](https://github.com/Benchling-Open-Source/allotropy)
- [Allotrope Foundation ASM 개요](https://www.allotrope.org/asm)
