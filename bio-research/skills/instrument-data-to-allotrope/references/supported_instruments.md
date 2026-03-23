# 지원되는 기기

## 이 스킬은 무엇을 변환할 수 있나요?

**Allotrope 스키마에 매핑되는 기기 데이터라면 무엇이든 변환할 수 있습니다.** 이 스킬은 계층형 파싱 접근 방식을 사용합니다.

1. **기본 Allotrope 파서**(아래 목록) - 공급업체별 형식에 대해 검증된 가장 높은 충실도의 경로
2. **유연한 대체 파서** - 열을 ASM 필드에 매핑해 CSV, Excel, TXT 같은 표 형식 데이터를 처리합니다.
3. **PDF 추출** - PDF에서 표를 추출한 뒤 유연한 파싱을 적용합니다.

기기가 아래 목록에 없더라도, 데이터에 ASM 기술 스키마에 매핑되는 인식 가능한 측정 필드(샘플 ID, 값, 단위, 타임스탬프 등)가 있다면 이 스킬로 변환할 수 있습니다.

---

## 기본 Allotrope 파서가 있는 기기

다음 기기들은 공급업체 열거형 값을 사용하는 Allotrope 라이브러리의 최적화된 파서를 제공합니다.

## 셀 카운팅

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Beckman Coulter Vi-CELL BLU | `BECKMAN_VI_CELL_BLU` | .csv |
| Beckman Coulter Vi-CELL XR | `BECKMAN_VI_CELL_XR` | .txt, .xls, .xlsx |
| Chemometec NucleoView NC-200 | `CHEMOMETEC_NUCLEOVIEW` | .xlsx |
| Chemometec NC-View | `CHEMOMETEC_NC_VIEW` | .xlsx |
| Revvity Matrix | `REVVITY_MATRIX` | .csv |

## 분광광도법(UV-Vis)

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Thermo Fisher NanoDrop One | `THERMO_FISHER_NANODROP_ONE` | .csv, .xlsx |
| Thermo Fisher NanoDrop Eight | `THERMO_FISHER_NANODROP_EIGHT` | .tsv, .txt |
| Thermo Fisher NanoDrop 8000 | `THERMO_FISHER_NANODROP_8000` | .csv |
| Unchained Labs Lunatic | `UNCHAINED_LABS_LUNATIC` | .csv, .xlsx |
| Thermo Fisher Genesys 30 | `THERMO_FISHER_GENESYS30` | .csv |

## 플레이트 리더(다중 모드, 흡광도, 형광)

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Molecular Devices SoftMax Pro | `MOLDEV_SOFTMAX_PRO` | .txt |
| PerkinElmer EnVision | `PERKIN_ELMER_ENVISION` | .csv |
| Agilent Gen5 (BioTek) | `AGILENT_GEN5` | .xlsx |
| Agilent Gen5 Image | `AGILENT_GEN5_IMAGE` | .xlsx |
| BMG MARS (CLARIOstar) | `BMG_MARS` | .csv, .txt |
| BMG LabTech Smart Control | `BMG_LABTECH_SMART_CONTROL` | .csv |
| Thermo SkanIt | `THERMO_SKANIT` | .xlsx |
| Revvity Kaleido | `REVVITY_KALEIDO` | .csv |
| Tecan Magellan | `TECAN_MAGELLAN` | .xlsx |

## ELISA / 면역분석

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Molecular Devices SoftMax Pro | `MOLDEV_SOFTMAX_PRO` | .txt |
| MSD Discovery Workbench | `MSD_WORKBENCH` | .txt |
| Methodical Mind | `METHODICAL_MIND` | .xlsx |
| BMG MARS | `BMG_MARS` | .csv, .txt |

## qPCR / PCR

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Applied Biosystems QuantStudio | `APPBIO_QUANTSTUDIO` | .xlsx |
| Applied Biosystems QuantStudio Design and Analysis | `APPBIO_QUANTSTUDIO_DESIGNANALYSIS` | .xlsx, .csv |
| Bio-Rad CFX Maestro | `BIORAD_CFX_MAESTRO` | .csv, .xlsx |
| Roche LightCycler | `ROCHE_LIGHTCYCLER` | .txt |

## 크로마토그래피(HPLC, LC)

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Waters Empower | `WATERS_EMPOWER` | .xml |
| Thermo Fisher Chromeleon | `THERMO_FISHER_CHROMELEON` | .xml |
| Agilent ChemStation | `AGILENT_CHEMSTATION` | .csv |

## 전기영동

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Agilent TapeStation | `AGILENT_TAPESTATION` | .csv |
| PerkinElmer LabChip | `PERKIN_ELMER_LABCHIP` | .csv |

## 유세포분석

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| BD Biosciences FACSDiva | `BD_BIOSCIENCES_FACSDIVA` | .xml |
| FlowJo | `FLOWJO` | .wsp |

## 솔루션 분석

| 기기 | 공급업체 열거형 | 파일 형식 |
|------------|-------------|------------|
| Roche Cedex Bio HT | `ROCHE_CEDEX_BIOHT` | .xlsx |
| Beckman Coulter Biomek | `BECKMAN_COULTER_BIOMEK` | .csv |

## 자동 감지 패턴

이 스킬은 다음 패턴을 사용해 파일 내용에서 기기 유형을 식별하려고 시도합니다.

### Vi-CELL BLU
- 열 헤더: "Sample ID", "Viable Cells (x10^6 cells/mL)", "Viability (%)"
- 파일 구조: 특정 열 순서를 가진 CSV

### Vi-CELL XR
- 열 헤더: "Sample", "Total Cells/mL", "Viable Cells/mL"
- 다양한 내보내기 형식 지원

### NanoDrop
- 열 헤더: "Sample Name", "Nucleic Acid Conc.", "A260", "A280"
- 260/280 및 260/230 비율 열

### 일반적인 플레이트 리더
- 웰 식별자(A1-H12 패턴)
- "Plate", "Well", "Sample" 열
- 메타데이터 헤더가 포함된 블록 기반 구조

### ELISA
- 농도가 포함된 표준 곡선 데이터
- OD/흡광도 판독값
- 시료/공백/표준 분류

## 공급업체 열거형 사용

```python
from allotropy.parser_factory import Vendor
from allotropy.to_allotrope import allotrope_from_file

# 지원되는 모든 공급업체를 나열합니다
for v in Vendor:
    print(f"{v.name}: {v.value}")

# 파일 변환
asm = allotrope_from_file("data.csv", Vendor.BECKMAN_VI_CELL_BLU)
```

## 지원 여부 확인

```python
from allotropy.parser_factory import get_parser

# 공급업체/파일 조합이 지원되는지 확인합니다
try:
    parser = get_parser(Vendor.BECKMAN_VI_CELL_BLU)
    print("Supported!")
except Exception as e:
    print(f"Not supported: {e}")
```
