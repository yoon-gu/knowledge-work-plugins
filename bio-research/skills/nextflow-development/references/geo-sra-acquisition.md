# GEO/SRA 데이터 수집

NCBI GEO/SRA에서 원시 시퀀싱 데이터를 다운로드하고 nf-core 파이프라인을 위해 준비합니다.

**다음 경우에 사용하세요.** 게시된 데이터 세트를 재분석하거나, 결과를 검증하거나, 결과를 공개 코호트와 비교하는 경우.

## 목차

- [Workflow Overview](#workflow-overview)
- [Step 1: Fetch Study Information](#step-1-fetch-study-information)
- [Step 2: Review Sample Groups](#step-2-review-sample-groups)
- [Step 3: Download FASTQ Files](#step-3-download-fastq-files)
- [Step 4: Generate Samplesheet](#step-4-generate-samplesheet)
- [Step 5: Run nf-core Pipeline](#step-5-run-nf-core-pipeline)
- [Supported Pipelines](#supported-pipelines)
- [Supported Organisms](#supported-organisms)
- [Complete Example](#complete-example)
- [Troubleshooting](#troubleshooting)

---

## 워크플로 개요

예: "GSE309891(약물 처리 대 대조군)에서 차별적으로 발현된 유전자 찾기"

```
┌─────────────────────────────────────────────────────────────────┐
│                    GEO/SRA DATA ACQUISITION                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │   Fetch study info     │
                 │   • Query NCBI/SRA     │
                 │   • Get metadata       │
                 │   • Detect organism    │
                 │   • Identify data type │
                 └────────────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │   Present summary      │
                 │   • Organism: Human    │
                 │   • Genome: GRCh38     │
                 │   • Type: RNA-Seq      │
                 │   • Pipeline: rnaseq   │
                 │   • Samples: 12        │
                 │     (6 treated,        │
                 │      6 control)        │
                 │   • Size: ~24 GB       │
                 └────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  USER CONFIRMS  │◄──── Decision point
                    │  genome/pipeline│
                    └─────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │   Select samples       │
                 │   • Group by condition │
                 │   • Show treated/ctrl  │
                 └────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  USER SELECTS   │◄──── Decision point
                    │  sample subset  │
                    └─────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │   Download FASTQs      │
                 │   • 24 files (R1+R2)   │
                 │   • Parallel transfers │
                 │   • Auto-resume        │
                 └────────────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │   Generate samplesheet │
                 │   • Map SRR to files   │
                 │   • Pair R1/R2         │
                 │   • Assign conditions  │
                 └────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NF-CORE PIPELINE EXECUTION                   │
│              (Continue with Step 1 of main workflow)            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 클로드를 위한 지침

GEO/SRA 데이터 수집으로 사용자를 지원할 때:

1. **항상 연구 정보를 먼저 가져와** 사용자에게 사용 가능한 데이터를 보여줍니다.
2. **다운로드하기 전에 확인 요청** - 샘플 그룹과 크기를 제시한 다음 AskUserQuestion을 사용하여 다운로드할 하위 집합을 묻습니다.
3. 유기체 및 데이터 유형에 따라 **적절한 게놈 및 파이프라인 제안**
4. 데이터 준비가 완료된 후 **기본 SKILL.md 워크플로**로 돌아갑니다.

확인 질문 예시:
```
Question: "Which sample group would you like to download?"
Options:
  - "RNA-Seq:PAIRED (42 samples, ~87 GB)"
  - "RNA-Seq:SINGLE (7 samples, ~4.5 GB)"
  - "All samples (49 samples, ~92 GB)"
```

---

## 1단계: 연구 정보 가져오기

다운로드하기 전에 GEO 연구에 대한 메타데이터를 얻으세요.

```bash
python scripts/sra_geo_fetch.py info <GEO_ID>
```

**예:**
```bash
python scripts/sra_geo_fetch.py info GSE110004
```

**출력에는 다음이 포함됩니다.**
- 연구 제목 및 요약
- 유기체(자동 제안 게놈 포함)
- 샘플 및 실행 횟수
- 데이터 유형(RNA-Seq, ATAC-seq 등)
- 예상 다운로드 크기
- nf-core 파이프라인 추천

**JSON에 정보 저장:**
```bash
python scripts/sra_geo_fetch.py info GSE110004 -o study_info.json
```

---

## 2단계: 샘플 그룹 검토

데이터 유형 및 레이아웃별로 구성된 샘플 그룹을 봅니다. 이는 혼합된 데이터 유형을 사용하는 연구에 유용합니다.

```bash
python scripts/sra_geo_fetch.py groups <GEO_ID>
```

**예제 출력:**
```
Sample Group          Count Layout     GSM Range                    Est. Size
--------------------------------------------------------------------------------
RNA-Seq                  42 PAIRED     GSM2879618...(42 samples)      87.4 GB
RNA-Seq                   7 SINGLE     GSM2976181-GSM2976187           4.5 GB
--------------------------------------------------------------------------------
TOTAL                    49                                           91.9 GB

Available groups for --subset option:
  1. "RNA-Seq:PAIRED" - 42 samples (~87.4 GB)
  2. "RNA-Seq:SINGLE" - 7 samples (~4.5 GB)
```

**개별 실행 목록:**
```bash
python scripts/sra_geo_fetch.py list <GEO_ID>

# Filter by data type
python scripts/sra_geo_fetch.py list GSE110004 --filter "RNA-Seq:PAIRED"
```

**결정 포인트:** 샘플 그룹을 검토합니다. 연구에 여러 데이터 유형이 있는 경우 다운로드할 하위 집합을 결정합니다.

---

## 3단계: FASTQ 파일 다운로드

ENA에서 FASTQ 파일을 다운로드하세요(SRA보다 빠름).

```bash
python scripts/sra_geo_fetch.py download <GEO_ID> -o <OUTPUT_DIR>
```

**옵션:**
- `-o, --output`: 출력 디렉터리(필수)
- `-i, --interactive`: 다운로드할 샘플 그룹을 대화형으로 선택
- `-s, --subset`: 데이터 유형별로 필터링합니다(예: "RNA-Seq:PAIRED")
- `-p, --parallel`: 병렬 다운로드 (기본값: 4)
- `-t, --timeout`: 다운로드 제한 시간(초)(기본값: 600)

### 대화형 모드(권장)

연구에 여러 데이터 유형이 있는 경우 대화형 샘플 선택을 위해 `-i` 플래그를 사용합니다.

```bash
python scripts/sra_geo_fetch.py download GSE110004 -o ./fastq -i
```

**대화형 출력:**
```
============================================================
  SELECT SAMPLE GROUP TO DOWNLOAD
============================================================

  [1] RNA-Seq (paired)
      Samples: 42
      GSM: GSM2879618...(42 samples)
      Size: ~87.4 GB

  [2] RNA-Seq (single)
      Samples: 7
      GSM: GSM2976181-GSM2976187
      Size: ~4.5 GB

  [0] Download ALL (49 samples)
------------------------------------------------------------

Enter selection (0-2):
```

### 직접 하위 집합 선택

또는 하위 집합을 직접 지정합니다.

```bash
# Download only RNA-Seq paired-end data
python scripts/sra_geo_fetch.py download GSE110004 -o ./fastq \
    --subset "RNA-Seq:PAIRED" --parallel 6
```

**참고:** 다운로드 시 기존 파일을 자동으로 건너뜁니다. 명령을 다시 실행하여 중단된 다운로드를 재개합니다.

---

## 4단계: 샘플시트 생성

nf-core 파이프라인과 호환되는 샘플시트를 만듭니다.

```bash
python scripts/sra_geo_fetch.py samplesheet <GEO_ID> \
    --fastq-dir <FASTQ_DIR> \
    -o samplesheet.csv
```

**옵션:**
- `-f, --fastq-dir`: 다운로드한 FASTQ 파일이 포함된 디렉터리(필수)
- `-o, --output`: 출력 샘플시트 경로 (기본값: Samplesheet.csv)
- `-p, --pipeline`: 대상 파이프라인(지정되지 않은 경우 자동 감지)

**예:**
```bash
python scripts/sra_geo_fetch.py samplesheet GSE110004 \
    --fastq-dir ./fastq \
    -o samplesheet.csv
```

**출력:** 스크립트는 다음을 수행합니다.
1. 대상 파이프라인에 필요한 형식으로 샘플시트를 생성합니다.
2. 제안된 게놈 참조 표시
3. 제안된 nf-core 명령 표시

---

## 5단계: nf-core 파이프라인 실행

샘플시트를 생성한 후 스크립트는 제안된 명령을 제공합니다.

**예제 출력:**
```
Suggested command:
   nextflow run nf-core/rnaseq \
       --input samplesheet.csv \
       --outdir results \
       --genome R64-1-1 \
       -profile docker
```

**결정 포인트:** 검토 및 확인:
1. 제안된 파이프라인이 맞나요?
2. 귀하의 유기체에 대한 게놈 참조가 정확합니까?
3. 추가 파이프라인 옵션이 필요합니까?

그런 다음 기본 SKILL.md 워크플로(1단계: 환경 확인)로 돌아가 파이프라인 실행을 진행합니다.

---

## 지원되는 파이프라인

이 기술은 라이브러리 전략에 따라 적절한 파이프라인을 자동 감지합니다. ★로 표시된 파이프라인은 구성, 샘플 시트 생성 및 문서가 완벽하게 지원됩니다. 다른 것들도 제안되지만 nf-core 문서에 따라 수동 설정이 필요합니다.

| 도서관 전략 | 제안된 파이프라인 | 지원 |
|------|---------|---------|
| RNA-Seq | nf-core/rnaseq | ★ 전체 |
| ATAC-seq | nf-core/atacseq | ★ 전체 |
| WGS/WXS | nf-core/sarek | ★ 전체 |
| 칩-seq | nf-core/칩seq | 매뉴얼 |
| Bisulfite-Seq | nf-core/메틸seq | 매뉴얼 |
| miRNA-Seq | nf-core/smrnaseq | 매뉴얼 |
| 앰플리콘 | nf-core/ampliseq | 매뉴얼 |

---

## 지원되는 유기체

자동 제안 게놈을 가진 일반적인 유기체:

| 유기체 | 게놈 | 메모 |
|----------|---------|-------|
| 호모 사피엔스 | GRCh38 | 인간 참조 |
| 근육 근육 | GRCM39 | 마우스 참조 |
| 사카로미세스 세레비지애 | R64-1-1 | 효모 S288C |
| 초파리 melanogaster | BDGP6 | 초파리 |
| 예쁜꼬마선충 | WBcel235 | C. 예쁜꼬마선충 |
| 다니오 레리오 | GRCz11 | 제브라피시 |
| 애기장대 | TAIR10 | 애기장대 |
| Rattus norvegicus | Rnor_6.0 | 쥐 |

전체 목록은 `scripts/config/genomes.yaml`을 참조하세요.

---

## 완전한 예

GSE110004(효모 RNA-seq) 재분석:

```bash
# 1. Get study info and sample groups
python scripts/sra_geo_fetch.py info GSE110004

# 2. Download with interactive selection
python scripts/sra_geo_fetch.py download GSE110004 -o ./fastq -i
# Select option [1] for RNA-Seq paired-end samples

# 3. Generate samplesheet
python scripts/sra_geo_fetch.py samplesheet GSE110004 \
    --fastq-dir ./fastq \
    -o samplesheet.csv

# 4. Run nf-core/rnaseq (continue with main SKILL.md workflow)
nextflow run nf-core/rnaseq \
    --input samplesheet.csv \
    --outdir results \
    --genome R64-1-1 \
    -profile docker
```

### 대안: 비대화형 다운로드

```bash
# Review sample groups first
python scripts/sra_geo_fetch.py groups GSE110004

# Download specific subset directly
python scripts/sra_geo_fetch.py download GSE110004 \
    --subset "RNA-Seq:PAIRED" \
    -o ./fastq \
    --parallel 4
```

---

## 문제 해결

### ENA 다운로드 실패
ENA 다운로드가 실패하면 SRA에서 직접 데이터를 가져와야 할 수도 있습니다.

```bash
# Create SRA tools environment
conda create -n sra_tools -c bioconda sra-tools

# Download with prefetch + fasterq-dump
conda run -n sra_tools prefetch SRR6357070
conda run -n sra_tools fasterq-dump SRR6357070 -O ./fastq
```

### SRA 실행을 찾을 수 없습니다.
일부 GEO 데이터 세트에는 원시 시퀀싱 읽기가 아닌 처리된 데이터만 있습니다. 확인:
```bash
python scripts/sra_geo_fetch.py info <GEO_ID>
```
"실행: 0"인 경우 데이터 세트의 SRA에 원시 데이터가 없을 수 있습니다.

### SuperSeries 지원
GEO SuperSeries(여러 하위 시리즈 포함)는 자동으로 처리됩니다. 도구는 다음을 수행합니다.
1. GEO ID가 SuperSeries인지 감지
2. 연결된 BioProject 접속 찾기
3. BioProject에서 모든 SRA 실행을 가져옵니다.

예: GSE110004는 BioProject PRJNA432544에 연결되는 SuperSeries입니다.

### 게놈이 인식되지 않음
유기체가 게놈 매핑에 없으면 수동으로 게놈을 지정합니다.
```bash
# Check available iGenomes
python scripts/manage_genomes.py list

# Or provide custom reference files to nf-core
nextflow run nf-core/rnaseq --fasta /path/to/genome.fa --gtf /path/to/genes.gtf
```

---

## 요구사항

- 파이썬 3.8+
- `requests` 라이브러리(선택 사항이지만 권장됨)
- `pyyaml` 라이브러리(선택 사항, 게놈 구성용)
- NCBI 및 ENA에 대한 네트워크 액세스

선택적 종속성을 설치합니다.
```bash
pip install requests pyyaml
```
