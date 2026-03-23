# ASM을 2D CSV로 평탄화하기

계층적 ASM JSON을 LIMS 가져오기, 스프레드시트 분석 또는 데이터 엔지니어링 파이프라인을 위한 평면 2D 테이블로 변환합니다.

## 왜 평탄화가 필요한가?

ASM은 의미론적으로 풍부하지만 계층적입니다. 많은 시스템에서는 평면 테이블이 필요합니다:
- LIMS 가져오기 (Benchling, STARLIMS, LabWare)
- Excel/CSV 분석
- 데이터베이스 로딩
- 빠른 시각적 검사

## 평탄화 전략

### 핵심 원칙
각 **측정값**은 하나의 **행**이 됩니다. 메타데이터는 행마다 반복됩니다.

### 제외되는 항목
평탄화 과정에서는 다음과 같은 **최상위 ASM 메타데이터**를 의도적으로 **생략**합니다:
- `$asm.manifest` (모델 버전, 스키마 URI)
- 기법 집계 문서 외부의 루트 수준 필드

이를 통해 출력을 실험 데이터에 집중합니다. 규정 준수 또는 감사 목적으로 스키마 버전 추적이 필요한 경우, 원본 ASM JSON을 평탄화된 CSV와 함께 저장하거나 평탄화 스크립트를 수정하여 이러한 필드를 포함시키는 것을 고려하세요.

### 계층 구조에서 컬럼으로
```
ASM Hierarchy                    → Flat Column
─────────────────────────────────────────────────
device-system-document.
  device-identifier              → instrument_serial_number
  model-number                   → instrument_model

measurement-aggregate-document.
  analyst                        → analyst
  measurement-time               → measurement_datetime

measurement-document[].
  sample-identifier              → sample_id
  viable-cell-density.value      → viable_cell_density
  viable-cell-density.unit       → viable_cell_density_unit
  viability.value                → viability_percent
```

## 컬럼 명명 규칙

설명적 접미사가 포함된 snake_case를 사용합니다:

| ASM 필드 | 평면 컬럼 |
|-----------|-------------|
| `viable-cell-density` | `viable_cell_density` |
| `.value` | `_value` (명확한 경우 생략 가능) |
| `.unit` | `_unit` |
| `measurement-time` | `measurement_datetime` |

## 예시: 세포 계수

### ASM 입력 (간소화)
```json
{
  "cell-counting-aggregate-document": {
    "device-system-document": {
      "device-identifier": "VCB001",
      "model-number": "Vi-CELL BLU"
    },
    "cell-counting-document": [{
      "measurement-aggregate-document": {
        "analyst": "jsmith",
        "measurement-time": "2024-01-15T10:30:00Z",
        "measurement-document": [
          {
            "sample-identifier": "Sample_A",
            "viable-cell-density": {"value": 2500000, "unit": "(cell/mL)"},
            "viability": {"value": 95.2, "unit": "%"}
          },
          {
            "sample-identifier": "Sample_B",
            "viable-cell-density": {"value": 1800000, "unit": "(cell/mL)"},
            "viability": {"value": 88.7, "unit": "%"}
          }
        ]
      }
    }]
  }
}
```

### 평탄화된 출력
```csv
sample_id,viable_cell_density,viable_cell_density_unit,viability_percent,analyst,measurement_datetime,instrument_serial_number,instrument_model
Sample_A,2500000,(cell/mL),95.2,jsmith,2024-01-15T10:30:00Z,VCB001,Vi-CELL BLU
Sample_B,1800000,(cell/mL),88.7,jsmith,2024-01-15T10:30:00Z,VCB001,Vi-CELL BLU
```

## 예시: 플레이트 리더

### ASM 입력 (간소화)
```json
{
  "plate-reader-aggregate-document": {
    "plate-reader-document": [{
      "measurement-aggregate-document": {
        "plate-identifier": "ELISA_001",
        "measurement-document": [
          {"well-location": "A1", "absorbance": {"value": 0.125, "unit": "mAU"}},
          {"well-location": "A2", "absorbance": {"value": 0.892, "unit": "mAU"}},
          {"well-location": "A3", "absorbance": {"value": 1.456, "unit": "mAU"}}
        ]
      }
    }]
  }
}
```

### 평탄화된 출력
```csv
plate_id,well_position,absorbance,absorbance_unit
ELISA_001,A1,0.125,mAU
ELISA_001,A2,0.892,mAU
ELISA_001,A3,1.456,mAU
```

## 데이터 큐브 처리

데이터 큐브(시계열, 스펙트럼)는 특별한 처리가 필요합니다:

### 옵션 1: 행으로 확장
각 데이터 포인트가 하나의 행이 됩니다:
```csv
sample_id,time_seconds,absorbance
Sample_A,0,0.100
Sample_A,60,0.125
Sample_A,120,0.150
```

### 옵션 2: 넓은 형식
측정값을 컬럼으로 배치합니다:
```csv
sample_id,abs_0s,abs_60s,abs_120s
Sample_A,0.100,0.125,0.150
```

### 옵션 3: 셀 내 JSON 배열
배열로 유지합니다 (일부 시스템에서 지원):
```csv
sample_id,absorbance_timeseries
Sample_A,"[0.100,0.125,0.150]"
```

## 기법별 표준 컬럼 세트

### 세포 계수
```
sample_id, viable_cell_density, viable_cell_density_unit, total_cell_count,
viability_percent, average_cell_diameter, average_cell_diameter_unit,
analyst, measurement_datetime, instrument_serial_number
```

### 분광광도법
```
sample_id, wavelength_nm, absorbance, pathlength_cm, concentration,
concentration_unit, a260_a280_ratio, a260_a230_ratio,
analyst, measurement_datetime, instrument_serial_number
```

### 플레이트 리더 / ELISA
```
plate_id, well_position, sample_type, sample_id, absorbance, absorbance_unit,
concentration, concentration_unit, dilution_factor, cv_percent,
analyst, measurement_datetime, instrument_serial_number
```

### qPCR
```
sample_id, target_name, well_position, ct_value, ct_mean, ct_sd,
quantity, quantity_unit, amplification_efficiency,
analyst, measurement_datetime, instrument_serial_number
```

## Python 구현

```python
import json
import pandas as pd

def flatten_asm(asm_dict, technique="cell-counting"):
    """
    Flatten ASM JSON to pandas DataFrame.

    Args:
        asm_dict: Parsed ASM JSON
        technique: ASM technique type

    Returns:
        pandas DataFrame with one row per measurement
    """
    rows = []

    # Get aggregate document
    agg_key = f"{technique}-aggregate-document"
    agg_doc = asm_dict.get(agg_key, {})

    # Extract device info
    device = agg_doc.get("device-system-document", {})
    device_info = {
        "instrument_serial_number": device.get("device-identifier"),
        "instrument_model": device.get("model-number")
    }

    # Get technique documents
    doc_key = f"{technique}-document"
    for doc in agg_doc.get(doc_key, []):
        meas_agg = doc.get("measurement-aggregate-document", {})

        # Extract common metadata
        common = {
            "analyst": meas_agg.get("analyst"),
            "measurement_datetime": meas_agg.get("measurement-time"),
            **device_info
        }

        # Extract each measurement
        for meas in meas_agg.get("measurement-document", []):
            row = {**common}

            # Flatten measurement fields
            for key, value in meas.items():
                if isinstance(value, dict) and "value" in value:
                    # Value datum pattern
                    col = key.replace("-", "_")
                    row[col] = value["value"]
                    if "unit" in value:
                        row[f"{col}_unit"] = value["unit"]
                else:
                    row[key.replace("-", "_")] = value

            rows.append(row)

    return pd.DataFrame(rows)

# Usage
with open("asm_output.json") as f:
    asm = json.load(f)

df = flatten_asm(asm, "cell-counting")
df.to_csv("flattened_output.csv", index=False)
```

## LIMS 가져오기 시 고려사항

평탄화된 데이터를 LIMS에 가져올 때:
- 컬럼 이름을 LIMS 스키마 필드 이름과 일치시키세요
- 타임스탬프에는 ISO 8601 날짜 형식을 사용하세요
- 샘플 ID가 기존 LIMS 샘플 식별자와 일치하는지 확인하세요
- LIMS에서 단위를 별도 컬럼으로 기대하는지 값에 포함시키는지 확인하세요
