# ASM 스키마 개요

ASM(Allotrope Simple Model)은 의미적 일관성을 유지하면서 실험실 장비 데이터를 표현하기 위한 JSON 기반 표준입니다.

## 핵심 개념

### 구조
ASM은 계층형 문서 구조를 사용합니다.
- **매니페스트** - 온톨로지와 스키마로 연결되는 참조
- **데이터** - 기술별로 정리된 실제 측정 데이터

### 주요 구성 요소

```json
{
  "$asm.manifest": {
    "vocabulary": ["http://purl.allotrope.org/voc/afo/REC/2023/09/"],
    "contexts": ["http://purl.allotrope.org/json-ld/afo-context-REC-2023-09.jsonld"]
  },
  "<technique>-aggregate-document": {
    "device-system-document": { ... },
    "<technique>-document": [
      {
        "measurement-aggregate-document": {
          "measurement-document": [ ... ]
        }
      }
    ]
  }
}
```

## 필수 메타데이터 문서

### 데이터 시스템 문서
모든 ASM 출력에는 다음 항목을 포함한 이 문서가 있어야 합니다.
- `ASM file identifier`: 출력 파일 이름
- `data system instance identifier`: 시스템 ID 또는 "N/A"
- `file name`: 소스 입력 파일 이름
- `UNC path`: 소스 파일 경로
- `ASM converter name`: 파서 식별자(예: "allotropy_beckman_coulter_biomek")
- `ASM converter version`: 버전 문자열
- `software name`: 소스 파일을 생성한 장비 소프트웨어

### 장치 시스템 문서
모든 ASM 출력에는 다음 항목을 포함한 이 문서가 있어야 합니다.
- `equipment serial number`: 주요 장비의 일련번호
- `product manufacturer`: 공급업체 이름
- `device document`: 하위 구성 요소 배열(프로브, 포드 등)
  - `device type`: 표준화된 유형(예: "액체 핸들러 프로브 헤드")
  - `device identifier`: 논리적 이름(예: 일련번호가 아닌 "Pod1")
  - `equipment serial number`: 구성 요소의 일련번호
  - `product manufacturer`: 구성 요소 공급업체

## 사용 가능한 ASM 기술

공식 ASM 저장소에는 **65개의 기술 스키마**가 포함되어 있습니다.

```
absorbance, automated-reactors, balance, bga, binding-affinity, bulk-density,
cell-counting, cell-culture-analyzer, chromatography, code-reader, conductance,
conductivity, disintegration, dsc, dvs, electronic-lab-notebook,
electronic-spectrometry, electrophoresis, flow-cytometry, fluorescence,
foam-height, foam-qualification, fplc, ftir, gas-chromatography, gc-ms, gloss,
hot-tack, impedance, lc-ms, light-obscuration, liquid-chromatography,
loss-on-drying, luminescence, mass-spectrometry, metabolite-analyzer,
multi-analyte-profiling, nephelometry, nmr, optical-imaging, optical-microscopy,
osmolality, oven-kf, pcr, ph, plate-reader, pressure-monitoring, psd, pumping,
raman, rheometry, sem, solution-analyzer, specific-rotation, spectrophotometry,
stirring, surface-area-analysis, tablet-hardness, temperature-monitoring,
tensile-test, thermogravimetric-analysis, titration, ultraviolet-absorbance,
x-ray-powder-diffraction
```

참조: https://gitlab.com/allotrope-public/asm/-/tree/main/json-schemas/adm

## 기술별 일반적인 ASM 스키마

자주 사용되는 기술에 대한 자세한 내용은 다음과 같습니다.

### 셀 카운팅
스키마: `cell-counting/REC/2024/09/cell-counting.schema.json`

주요 필드:
- `viable-cell-density` (셀/mL)
- `viability`(백분율)
- `total-cell-count`
- `dead-cell-count`
- `cell-diameter-distribution-datum`

### 분광광도법(UV-Vis)
스키마: `spectrophotometry/REC/2024/06/spectrophotometry.schema.json`

주요 필드:
- `absorbance`(무차원)
- `wavelength`(nm)
- `transmittance`(백분율)
- `pathlength`(cm)
- `concentration`(단위 포함)

### 플레이트 리더
스키마: `plate-reader/REC/2024/06/plate-reader.schema.json`

주요 필드:
- `absorbance`
- `fluorescence`
- `luminescence`
- `well-location` (A1-H12)
- `plate-identifier`

### qPCR
스키마: `pcr/REC/2024/06/pcr.schema.json`

주요 필드:
- `cycle-threshold-result`
- `amplification-efficiency`
- `melt-curve-datum`
- `target-DNA-description`

### 크로마토그래피
스키마: `liquid-chromatography/REC/2023/09/liquid-chromatography.schema.json`

주요 필드:
- `retention-time`(분)
- `peak-area`
- `peak-height`
- `peak-width`
- `chromatogram-data-cube`

## 데이터 패턴

### 값 예시
단위가 포함된 단순 값:

```json
{
  "value": 1.5,
  "unit": "mL"
}
```

### 집계 데이텀
관련 값 묶음:

```json
{
  "measurement-aggregate-document": {
    "measurement-document": [
      { "viable-cell-density": {"value": 2.5e6, "unit": "(cell/mL)"} },
      { "viability": {"value": 95.2, "unit": "%"} }
    ]
  }
}
```

### 데이터 큐브
다차원 배열 데이터:

```json
{
  "cube-structure": {
    "dimensions": [{"@componentDatatype": "double", "concept": "elapsed time"}],
    "measures": [{"@componentDatatype": "double", "concept": "absorbance"}]
  },
  "data": {
    "dimensions": [[0, 1, 2, 3, 4]],
    "measures": [[0.1, 0.2, 0.3, 0.4, 0.5]]
  }
}
```

## 검증

공식 스키마를 기준으로 ASM 출력을 검증합니다.

```python
import json
import jsonschema
from urllib.request import urlopen

# ASM 출력 불러오기
with open("output.json") as f:
    asm = json.load(f)

# 매니페스트에서 스키마 URL 가져오기
schema_url = asm.get("$asm.manifest", {}).get("$ref")

# 검증(간단화한 예시입니다. 실제 검증은 더 복잡합니다.)
# 참고: 전체 검증에는 $ref 참조 해석이 필요합니다.
```

## 스키마 저장소

공식 스키마: https://gitlab.com/allotrope-public/asm/-/tree/main/json-schemas/adm

스키마 구조:

```
json-schemas/adm/
├── cell-counting/
│   └── REC/2024/09/
│       └── cell-counting.schema.json
├── spectrophotometry/
│   └── REC/2024/06/
│       └── spectrophotometry.schema.json
├── plate-reader/
│   └── REC/2024/06/
│       └── plate-reader.schema.json
└── ...
```

## 일반적인 문제

### 누락된 필드
모든 장비 출력에 모든 ASM 필드가 들어 있는 것은 아닙니다. 보고서 완성도:

```python
def report_completeness(asm, expected_fields):
    found = set(extract_all_fields(asm))
    missing = expected_fields - found
    return len(found) / len(expected_fields) * 100
```

### 단위 변형
기기마다 단위 형식이 다를 수 있습니다. Allotrope 라이브러리는 다음 형식을 정규화합니다.
- "세포/mL" → "(세포/mL)"
- "%" → "%"
- "nm" → "nm"

### 날짜 형식
ASM은 ISO 8601 형식을 사용합니다: `2024-01-15T10:30:00Z`
