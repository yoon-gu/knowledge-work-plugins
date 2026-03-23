# 지원 기기

## 이 스킬로 무엇을 변환할 수 있나요?

**Allotrope 스키마에 매핑할 수 있는 모든 기기 데이터를 변환할 수 있습니다.** 이 스킬은 계층적 파싱 접근 방식을 사용합니다:

1. **네이티브 allotropy 파서** (아래 목록) - 벤더별 형식에 대해 검증된 최고 충실도
2. **유연한 폴백 파서** - 컬럼을 ASM 필드에 매핑하여 모든 표 형식 데이터(CSV, Excel, TXT) 처리
3. **PDF 추출** - PDF에서 테이블을 추출한 후 유연한 파싱 적용

기기가 아래 목록에 없더라도, 데이터에 ASM 기법 스키마에 매핑할 수 있는 인식 가능한 측정 필드(샘플 ID, 값, 단위, 타임스탬프 등)가 포함되어 있으면 변환할 수 있습니다.

---

## 네이티브 Allotropy 파서가 있는 기기

다음 기기들은 allotropy 라이브러리에 벤더 Enum 값과 함께 최적화된 파서를 갖추고 있습니다.

## 세포 계수

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Beckman Coulter Vi-CELL BLU | `BECKMAN_VI_CELL_BLU` | .csv |
| Beckman Coulter Vi-CELL XR | `BECKMAN_VI_CELL_XR` | .txt, .xls, .xlsx |
| ChemoMetec NucleoView NC-200 | `CHEMOMETEC_NUCLEOVIEW` | .xlsx |
| ChemoMetec NC-View | `CHEMOMETEC_NC_VIEW` | .xlsx |
| Revvity Matrix | `REVVITY_MATRIX` | .csv |

## 분광광도법 (UV-Vis)

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Thermo Fisher NanoDrop One | `THERMO_FISHER_NANODROP_ONE` | .csv, .xlsx |
| Thermo Fisher NanoDrop Eight | `THERMO_FISHER_NANODROP_EIGHT` | .tsv, .txt |
| Thermo Fisher NanoDrop 8000 | `THERMO_FISHER_NANODROP_8000` | .csv |
| Unchained Labs Lunatic | `UNCHAINED_LABS_LUNATIC` | .csv, .xlsx |
| Thermo Fisher Genesys 30 | `THERMO_FISHER_GENESYS30` | .csv |

## 플레이트 리더 (다중모드, 흡광도, 형광)

| 기기 | Vendor Enum | 파일 유형 |
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

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Molecular Devices SoftMax Pro | `MOLDEV_SOFTMAX_PRO` | .txt |
| MSD Discovery Workbench | `MSD_WORKBENCH` | .txt |
| MSD Methodical Mind | `METHODICAL_MIND` | .xlsx |
| BMG MARS | `BMG_MARS` | .csv, .txt |

## qPCR / PCR

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Applied Biosystems QuantStudio | `APPBIO_QUANTSTUDIO` | .xlsx |
| Applied Biosystems QuantStudio Design & Analysis | `APPBIO_QUANTSTUDIO_DESIGNANALYSIS` | .xlsx, .csv |
| Bio-Rad CFX Maestro | `BIORAD_CFX_MAESTRO` | .csv, .xlsx |
| Roche LightCycler | `ROCHE_LIGHTCYCLER` | .txt |

## 크로마토그래피 (HPLC, LC)

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Waters Empower | `WATERS_EMPOWER` | .xml |
| Thermo Fisher Chromeleon | `THERMO_FISHER_CHROMELEON` | .xml |
| Agilent ChemStation | `AGILENT_CHEMSTATION` | .csv |

## 전기영동

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Agilent TapeStation | `AGILENT_TAPESTATION` | .csv |
| PerkinElmer LabChip | `PERKIN_ELMER_LABCHIP` | .csv |

## 유세포 분석

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| BD Biosciences FACSDiva | `BD_BIOSCIENCES_FACSDIVA` | .xml |
| FlowJo | `FLOWJO` | .wsp |

## 용액 분석

| 기기 | Vendor Enum | 파일 유형 |
|------------|-------------|------------|
| Roche Cedex BioHT | `ROCHE_CEDEX_BIOHT` | .xlsx |
| Beckman Coulter Biomek | `BECKMAN_COULTER_BIOMEK` | .csv |

## 자동 감지 패턴

이 스킬은 파일 내용에서 다음 패턴을 사용하여 기기 유형을 식별합니다:

### Vi-CELL BLU
- 컬럼 헤더: "Sample ID", "Viable cells (x10^6 cells/mL)", "Viability (%)"
- 파일 구조: 특정 컬럼 순서의 CSV

### Vi-CELL XR
- 컬럼 헤더: "Sample", "Total cells/ml", "Viable cells/ml"
- 다양한 내보내기 형식 지원

### NanoDrop
- 컬럼 헤더: "Sample Name", "Nucleic Acid Conc.", "A260", "A280"
- 260/280 및 260/230 비율 컬럼

### 플레이트 리더 (일반)
- 웰 식별자 (A1-H12 패턴)
- "Plate", "Well", "Sample" 컬럼
- 메타데이터 헤더가 있는 블록 기반 구조

### ELISA
- 농도가 포함된 표준 곡선 데이터
- OD/흡광도 판독값
- 샘플/블랭크/표준 분류

## Vendor Enum 사용하기

```python
from allotropy.parser_factory import Vendor
from allotropy.to_allotrope import allotrope_from_file

# List all supported vendors
for v in Vendor:
    print(f"{v.name}: {v.value}")

# Convert file
asm = allotrope_from_file("data.csv", Vendor.BECKMAN_VI_CELL_BLU)
```

## 지원 상태 확인하기

```python
from allotropy.parser_factory import get_parser

# Check if a vendor/file combo is supported
try:
    parser = get_parser(Vendor.BECKMAN_VI_CELL_BLU)
    print("Supported!")
except Exception as e:
    print(f"Not supported: {e}")
```
