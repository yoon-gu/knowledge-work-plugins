# 분야 분류 안내

이 가이드는 기기 데이터 필드를 올바른 ASM 문서 위치로 분류하는 데 도움이 됩니다. 원시 기기 출력을 동소체 단순 모델 구조에 매핑할 때 이를 사용합니다.

## ASM 문서 계층 구조```
<technique>-aggregate-document
├── device-system-document          # Instrument hardware info
├── data-system-document            # Software/conversion info
├── <technique>-document[]          # Per-run/sequence data
│   ├── analyst                     # Who performed the analysis
│   ├── measurement-aggregate-document
│   │   ├── measurement-time
│   │   ├── measurement-document[]  # Individual measurements
│   │   │   ├── sample-document
│   │   │   ├── device-control-aggregate-document
│   │   │   └── [measurement fields]
│   │   └── [aggregate-level metadata]
│   ├── processed-data-aggregate-document
│   │   └── processed-data-document[]
│   │       ├── data-processing-document
│   │       └── [processed results]
│   └── calculated-data-aggregate-document
│       └── calculated-data-document[]
```

## 필드 분류 카테고리

### 1. 장치/악기 정보 → `device-system-document`

실제 기기에 대한 하드웨어 및 펌웨어 세부정보입니다.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 악기 이름 | `model-number` | "Vi-CELL BLU", "NanoDrop One" |
| 일련번호 | `equipment-serial-number` | "VCB-12345", "SN001234" |
| 제조업체 | `product-manufacturer` | "베크먼 쿨터", "열 피셔" |
| 펌웨어 버전 | `firmware-version` | "v2.1.3" |
| 장치 ID | `device-identifier` | "악기_01" |
| 브랜드 | `brand-name` | "베크만 쿨터" ​​|

**규칙:** 값이 실제 기기를 설명하고 실행 간에 변경되지 않는 경우 `device-system-document`에 들어갑니다.

---

### 2. 소프트웨어/데이터 시스템 정보 → `data-system-document`

획득, 분석 또는 변환에 사용되는 소프트웨어에 대한 정보입니다.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 소프트웨어 이름 | `software-name` | "크로멜레온", "Gen5" |
| 소프트웨어 버전 | `software-version` | "7.3.2" |
| 파일 이름 | `file-name` | "실험_001.xlsx" |
| 파일 경로 | `file-identifier` | "/데이터/실행/2024-01-15/" |
| 데이터베이스 ID | `ASM-converter-name` | "동소체 v0.1.55" |

**규칙:** 값이 소프트웨어, 파일 메타데이터 또는 데이터 출처를 설명하는 경우 `data-system-document`에 들어갑니다.

---

### 3. 샘플 정보 → `sample-document`

분석 중인 생물학적/화학적 샘플에 대한 메타데이터입니다.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 샘플 ID | `sample-identifier` | "샘플_A", "LIMS-001234" |
| 샘플 이름 | `written-name` | "CHO 세포배양 5일차" |
| 샘플 유형/역할 | `sample-role-type` | "알 수 없는 샘플 역할", "대조 샘플 역할" |
| 배치 ID | `batch-identifier` | "배치-2024-001" |
| 설명 | `description` | "단백질 발현 샘플" |
| 그럼 위치 | `location-identifier` | "A1", "B3" |

**규칙:** 값이 측정된 내용(방법이 아님)을 식별하거나 설명하는 경우 `sample-document`에 들어갑니다.

---

### 4. 장치 제어 설정 → `device-control-aggregate-document`

측정 중에 사용되는 기기 설정 및 매개변수입니다.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 주입량 | `sample-volume-setting` | 10 μL |
| 파장 | `detector-wavelength-setting` | 254nm |
| 온도 | `compartment-temperature` | 37°C |
| 유량 | `flow-rate` | 1.0mL/분 |
| 노출 시간 | `exposure-duration-setting` | 500ms |
| 검출기 이득 | `detector-gain-setting` | 1.5 |
| 조명 | `illumination-setting` | 80% |

**규칙:** 값이 측정에 영향을 미치는 구성 가능한 기기 매개변수인 경우 `device-control-aggregate-document`에 들어갑니다.

---

### 5. 환경 조건 → `device-control-document` 또는 기술별

측정 중 주변 또는 제어된 환경 매개변수.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 주변 온도 | `ambient-temperature` | 22.5°C |
| 습도 | `ambient-relative-humidity` | 45% |
| 컬럼 온도 | `compartment-temperature` | 30°C |
| 샘플 온도 | `sample-temperature` | 4°C |
| 전기영동 온도 | (기술별) | 26.4°C |

**규칙:** 측정 품질에 영향을 미치는 환경 조건은 장치 제어 또는 기술별 위치에 따라 달라집니다.

---

### 6. 원시 측정 데이터 → `measurement-document`

직접적인 기기 판독 - "실측" 데이터입니다.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 흡광도 | `absorbance` | 0.523AU |
| 형광 | `fluorescence` | 12500RFU |
| 세포수 | `total-cell-count` | 2.5e6 셀 |
| 피크 지역 | `peak-area` | 1234.5mAU·분 |
| 보유시간 | `retention-time` | 5.67분 |
| Ct 값 | `cycle-threshold-result` | 24.5 |
| 농도(측정) | `mass-concentration` | 1.5mg/mL |

**규칙:** 값이 이 분석의 다른 값에서 계산되지 않은 직접 기기 판독값인 경우 `measurement-document`에 들어갑니다.

---

### 7. 계산/파생 데이터 → `calculated-data-aggregate-document`

원시 측정에서 계산된 값입니다.

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 생존율 % | `calculated-result` | 95.2% |
| 농도(표준 곡선에서) | `calculated-result` | 125ng/μL |
| 비율 (260/280) | `calculated-result` | 1.89 |
| 상대 수량 | `calculated-result` | 2.5배 |
| % 회복 | `calculated-result` | 98.7% |
| 이력서% | `calculated-result` | 2.3% |

**계산된 데이터 문서 구조:**```json
{
  "calculated-data-name": "viability",
  "calculated-result": {"value": 95.2, "unit": "%"},
  "calculation-description": "viable cells / total cells * 100"
}
```

**규칙:** 이 분석에서 다른 측정값을 통해 값이 계산된 경우 `calculated-data-aggregate-document`에 들어갑니다. 가능하면 `calculation-description`을 포함하세요.

---

### 8. 처리/분석된 데이터 → `processed-data-aggregate-document`

데이터 처리 알고리즘의 결과(피크 통합, 셀 분류 등)

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 피크 목록 | `peak-list` | 통합 피크 결과 |
| 세포 크기 분포 | `cell-diameter-distribution` | 히스토그램 데이터 |
| 기준 수정 데이터 | (처리된 데이터 문서에서) | 수정된 스펙트럼 |
| 적합 곡선 | (처리된 데이터 문서에서) | 표준 곡선 맞춤 |

**연결된 `data-processing-document`:**```json
{
  "cell-type-processing-method": "trypan blue exclusion",
  "cell-density-dilution-factor": {"value": 2, "unit": "(unitless)"},
  "minimum-cell-diameter-setting": {"value": 5, "unit": "µm"},
  "maximum-cell-diameter-setting": {"value": 50, "unit": "µm"}
}
```

**규칙:** 원시 데이터에 적용된 알고리즘이나 처리 방법으로 인해 값이 생성된 경우 해당 값은 `data-processing-document`의 처리 매개변수와 함께 `processed-data-aggregate-document`에 들어갑니다.

---

### 9. 타이밍/타임스탬프 → 다양한 위치

| 타임스탬프 유형 | 위치 | ASM분야 |
|---|----------|------------|
| 측정시간 | `measurement-document` | `measurement-time` |
| 실행 시작 시간 | `analysis-sequence-document` | `analysis-sequence-start-time` |
| 실행 종료 시간 | `analysis-sequence-document` | `analysis-sequence-end-time` |
| 데이터 내보내기 시간 | `data-system-document` | (커스텀) |

**규칙:** ISO 8601 형식 사용: `2024-01-15T10:30:00Z`

---

### 10. 분석가/운영자 정보 → `<technique>-document`

| 필드 유형 | ASM분야 | 예 |
|------------|------------|------------|
| 운영자 이름 | `analyst` | "J스미스" |
| 리뷰어 | (사용자 정의 또는 확장) | "보류 중" |

**규칙:** 분석가는 개별 측정이 아닌 기술 문서 수준에서 진행됩니다.

---

## 의사결정 트리```
Is this field about...

THE INSTRUMENT ITSELF?
├── Hardware specs → device-system-document
└── Software/files → data-system-document

THE SAMPLE?
└── Sample ID, name, type, batch → sample-document

INSTRUMENT SETTINGS?
└── Configurable parameters → device-control-aggregate-document

ENVIRONMENTAL CONDITIONS?
└── Temp, humidity, etc. → device-control-document

A DIRECT READING?
└── Raw instrument output → measurement-document

A COMPUTED VALUE?
├── From other measurements → calculated-data-document
└── From processing algorithm → processed-data-document

TIMING?
├── When measured → measurement-document.measurement-time
└── When run started/ended → analysis-sequence-document

WHO DID IT?
└── Operator/analyst → <technique>-document.analyst
```

## 일반적인 계측기-ASM 매핑

> **참고:** 이러한 매핑은 [Benchling allotropy 라이브러리](https://github.com/Benchling-Open-Source/allotropy/tree/main/src/allotropy/parsers)에서 파생됩니다. 신뢰할 수 있는 매핑을 보려면 특정 기기에 대한 파서 소스 코드를 참조하세요.

### 셀 카운터(Vi-CELL BLU)
*출처: `allotropy/parsers/beckman_vi_cell_blu/vi_cell_blu_structure.py`*

| 계기분야 | ASM분야 |
|----|------------|
| 샘플 ID | `sample_identifier` |
| 분석 날짜/시간 | `measurement_time` |
| 분석 기준 | `analyst` |
| 생존율(%) | `viability` |
| 생존 가능(x10^6) 세포/mL | `viable_cell_density` |
| 총 (x10^6) 셀/mL | `total_cell_density` |
| 세포수 | `total_cell_count` |
| 생존 가능한 세포 | `viable_cell_count` |
| 평균 직경(μm) | `average_total_cell_diameter` |
| 평균 생존 직경(μm) | `average_live_cell_diameter` |
| 평균 순환성 | `average_total_cell_circularity` |
| 세포 유형 | `cell_type_processing_method`(데이터 처리) |
| 희석 | `cell_density_dilution_factor`(데이터 처리) |
| 최소/최대 직경 | `minimum/maximum_cell_diameter_setting`(데이터 처리) |

### 분광광도계(NanoDrop)
| 계기분야 | ASM분야 |
|----|------------|
| 샘플 이름 | `sample_identifier` |
| A260, A280 | `absorbance` (파장 포함) |
| 농도 | `mass_concentration` |
| 260/280 비율 | `a260_a280_ratio` |
| 경로 길이 | `pathlength` |

### 플레이트 리더
| 계기분야 | ASM분야 |
|----|------------|
| 음 | `location_identifier` |
| 샘플 유형 | `sample_role_type` |
| 흡광도/OD | `absorbance` |
| 형광 | `fluorescence` |
| 플레이트 ID | `container_identifier` |

### 크로마토그래피(HPLC)
| 계기분야 | ASM분야 |
|----|------------|
| 샘플 ID | `sample_identifier` |
| 주입량 | `injection_volume` |
| 보유 시간 | `retention_time` |
| 피크 지역 | `peak_area` |
| 피크 높이 | `peak_height` |
| 컬럼 온도 | `column_oven_temperature` |
| 유량 | `flow_rate` |

## 유닛 취급

소스 데이터에 명시적으로 존재하는 단위만 사용하십시오. 값에 단위가 지정되지 않은 경우:
- 단위 값으로 `(unitless)`을 사용합니다.
- 도메인 지식을 기반으로 단위를 추론하지 마십시오.

## 계산된 데이터 추적성

계산된 값을 생성할 때 항상 `data-source-aggregate-document`을 사용하여 소스 데이터에 연결하세요.```json
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

이는 "DIN 5.8은 `TEST_ID_145`의 샘플에서 계산되었습니다."라고 선언합니다.

**이것이 중요한 이유:**
- **감사**: 특정 원시 데이터에서 나온 가치를 증명합니다.
- **디버깅**: 예상치 못한 결과를 소스까지 추적합니다.
- **재처리**: 알고리즘이 변경되면 재분석할 입력을 파악합니다.

**다음에 고유 ID 할당:**
- 측정값, 피크, 영역 및 계산된 값
- 일관된 이름 지정 패턴을 사용합니다(예: `INSTRUMENT_TYPE_TEST_ID_N`).

이를 통해 양방향 순회가 가능합니다. 즉, 계산된 → 원시 또는 원시 → 모든 파생 값을 추적합니다.

---

## 중첩된 문서 구조(중요)

일반적인 실수는 필드를 중첩된 구조로 래핑해야 할 때 측정 문서에 직접 필드를 "평탄화"하는 것입니다. 이로 인해 스키마 준수가 중단되고 의미적 컨텍스트가 손실됩니다.

### 중첩이 중요한 이유

ASM은 의미론적 그룹화를 위해 중첩된 문서를 사용합니다.

| 문서 | 목적 | 포함 |
|------------|---------|----------|
| `sample document` | 측정된 내용 | 샘플 ID, 위치, 플레이트 식별자 |
| `device control aggregate document` | 기기 작동 방식 | 설정, 매개변수, 기술 |
| `custom information document` | 공급업체별 필드 | ASM에 매핑되지 않는 비표준 필드 |

### 샘플 문서 필드

이러한 필드는 `sample document` 내부에 있어야 하며 측정 시 평면화되지 않아야 합니다.```json
// ❌ WRONG - Fields flattened on measurement
{
  "measurement identifier": "TEST_001",
  "sample identifier": "Sample_A",
  "location identifier": "A1",
  "absorbance": {"value": 0.5, "unit": "(unitless)"}
}

// ✅ CORRECT - Fields nested in sample document
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

**샘플 문서에 속하는 필드:**
- `sample identifier` - 샘플 ID/이름
- `written name` - 설명 샘플 이름
- `batch identifier` - 배치/로트 번호
- `sample role type` - 표준, 공백, 제어, 알 수 없음
- `location identifier` - 우물 위치(A1, B3 등)
- `well plate identifier` - 플레이트 바코드
- `description` - 샘플 설명

### 장치 제어 문서 필드

기기 설정은 `device control aggregate document` 내부에 있어야 합니다.```json
// ❌ WRONG - Device settings flattened
{
  "measurement identifier": "TEST_001",
  "device identifier": "Pod1",
  "technique": "Custom",
  "volume": {"value": 26, "unit": "μL"}
}

// ✅ CORRECT - Settings nested in device control
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

**장치 제어에 속하는 필드:**
- `device type` - 장치 유형
- `device identifier` - 장치 ID
- `detector wavelength setting` - 감지 파장
- `compartment temperature` - 온도 설정
- `sample volume setting` - 볼륨 설정
- `flow rate` - 유량 설정

### 맞춤 정보 문서

표준 ASM 용어에 매핑되지 않는 공급업체별 필드는 `custom information document`에 들어갑니다.```json
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

### 액체 처리기: 전송 페어링

액체 처리기의 경우 측정은 별도의 작업이 아닌 완전한 전달(흡인 + 분배)을 나타냅니다.```json
// ❌ WRONG - Separate records for aspirate and dispense
[
  {"measurement identifier": "OP_001", "transfer type": "Aspirate", "volume": {"value": 26, "unit": "μL"}},
  {"measurement identifier": "OP_002", "transfer type": "Dispense", "volume": {"value": 26, "unit": "μL"}}
]

// ✅ CORRECT - Single record with source and destination
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

**페어링 논리:**
1. 프로브 번호에 따라 흡인 및 분배 작업을 일치시킵니다.
2. 일치하는 쌍당 하나의 측정을 생성합니다.
3. 흡인 위치에 `source_*` 필드를 사용합니다.
4. 분배 위치에 `destination_*` 필드를 사용하십시오.
5. `aspiration volume` 및 `transfer volume`을 모두 포함합니다.

### 빠른 참조: 중첩 결정```
Is this field about...

THE SAMPLE BEING MEASURED?
├── Sample ID, name, batch → sample document
├── Well position → sample document.location identifier
├── Plate barcode → sample document.well plate identifier
└── Source/destination locations → sample document (with prefixes)

INSTRUMENT SETTINGS?
├── Standard settings → device control aggregate document
└── Vendor-specific → custom information document

A MEASUREMENT VALUE?
└── Direct on measurement document (e.g., absorbance, volume)

TRANSFER OPERATION TYPE?
└── DON'T use "transfer type" - pair into single measurement
    with source/destination fields instead
```

### 유효성 검사

`validate_asm.py`을 사용하여 중첩 문제를 확인하세요.```bash
python scripts/validate_asm.py output.json --reference known_good.json
```

유효성 검사기는 다음을 확인합니다.
- 측정 시 필드가 잘못 평탄화됨
- `sample document` 래퍼 누락
- `device control aggregate document` 래퍼 누락
- 공급업체 필드에 `custom information document`이 누락되었습니다.
- 액체 처리기: 쌍으로 된 기록 대신 별도의 전송 유형

## 소스

- [동소체 단순 모델 소개](https://www.allotrope.org/introduction-to-allotrope-simple-model)
- [벤칭링 동소체 라이브러리](https://github.com/Benchling-Open-Source/allotropy)
- [Allotrope Foundation ASM 개요](https://www.allotrope.org/asm)