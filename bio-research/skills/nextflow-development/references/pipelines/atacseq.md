# nf-core/atacseq

**버전:** 2.1.2

**공식 문서:** https://nf-co.re/atacseq/2.1.2/
**GitHub:** https://github.com/nf-core/atacseq

> **참고:** 새 버전으로 업데이트할 때 [releases page](https://github.com/nf-core/atacseq/releases)에서 주요 변경 사항이 있는지 확인하고 아래 명령으로 버전을 업데이트하세요.

## 내용
- [Test command](#test-command)
- [Samplesheet format](#samplesheet-format)
- [Parameters](#parameters)
- [Output files](#output-files)
- [Quality metrics](#quality-metrics)

## 테스트 명령

```bash
nextflow run nf-core/atacseq -r 2.1.2 -profile test,docker --outdir test_atacseq
```

예상: ~15분, 피크 및 BigWig 트랙을 생성합니다.

## 샘플시트 형식

```csv
sample,fastq_1,fastq_2,replicate
CONTROL,/path/to/ctrl_rep1_R1.fq.gz,/path/to/ctrl_rep1_R2.fq.gz,1
CONTROL,/path/to/ctrl_rep2_R1.fq.gz,/path/to/ctrl_rep2_R2.fq.gz,2
TREATMENT,/path/to/treat_rep1_R1.fq.gz,/path/to/treat_rep1_R2.fq.gz,1
TREATMENT,/path/to/treat_rep2_R1.fq.gz,/path/to/treat_rep2_R2.fq.gz,2
```

| 칼럼 | 필수 | 설명 |
|---------|------------|-------------|
| 샘플 | 예 | 조건/그룹 식별자 |
| fastq_1 | 예 | R1에 대한 절대 경로 |
| fastq_2 | 예 | R2에 대한 절대 경로(페어링 엔드 필요) |
| 복제 | 예 | 복제 번호(정수) |

### 미분분석을 위한 디자인 파일
```csv
sample,condition
CONTROL,control
TREATMENT,treatment
```

`--deseq2_design design.csv`과 함께 사용하세요.

## 매개변수

### 최소 실행
```bash
nextflow run nf-core/atacseq -r 2.1.2 -profile docker \
    --input samplesheet.csv --outdir results --genome GRCh38 --read_length 50
```

### 공통 매개변수

| 매개변수 | 기본값 | 설명 |
|------------|---------|-------------|
| `--genome` | - | `GRCh38`, `GRCh37`, `mm10` |
| `--read_length` | 50 | MACS2 최적화를 위한 읽기 길이 |
| `--narrow_peak` | 사실 | 좁은 봉우리(넓은 경우 거짓) |
| `--mito_name` | 문자 | 미토콘드리아 염색체 이름 |
| `--keep_mito` | 거짓 | 미토콘드리아 읽기 유지 |
| `--min_reps_consensus` | 1 | 합의 피크에 대한 최소 복제 |

### 차등 접근성
```bash
--deseq2_design design.csv
```

## 출력 파일

```
results/
├── bwa/mergedLibrary/
│   ├── *.mLb.mkD.sorted.bam     # Filtered, deduplicated alignments
│   └── bigwig/
│       └── *.bigWig             # Coverage tracks
├── macs2/narrowPeak/
│   ├── *.narrowPeak             # Peak calls
│   └── consensus/
│       └── consensus_peaks.bed  # Merged peaks across replicates
├── deeptools/
│   ├── plotFingerprint/         # Library complexity
│   └── plotProfile/             # TSS enrichment
├── deseq2/                      # If --deseq2_design provided
└── multiqc/
```

**주요 결과:**
- `*.mLb.mkD.sorted.bam`: 분석 준비 정렬
- `*.narrowPeak`: MACS2 피크 호출(BED 형식)
- `consensus_peaks.bed`: 반복 실험에서 합의 최고점
- `*.bigWig`: 게놈 브라우저 트랙

## 품질 지표

| 미터법 | 좋음 | 허용됨 | 가난한 |
|---------|------|------------|------|
| 매핑된 읽기 | >80% | 60-80% | <60% |
| 미토콘드리아 | <20% | 20-40% | >40% |
| 중복 | <30% | 30-50% | >50% |
| 프립 | >30% | 15-30% | <15% |
| TSS 농축 | >6 | 4-6 | <4 |

**조각 크기**: 뉴클레오솜 주기성을 보여야 합니다(뉴클레오솜 없음 ~50bp, 단뉴클레오솜 ~200bp).

## 다운스트림 분석

```r
library(ChIPseeker)
library(GenomicRanges)
peaks <- import("consensus_peaks.bed")
peakAnno <- annotatePeak(peaks, TxDb = TxDb.Hsapiens.UCSC.hg38.knownGene)
```

**모티프 분석:**
```bash
findMotifsGenome.pl consensus_peaks.bed hg38 motifs/ -size 200
```

## 문제 해결

**낮은 FriP**: `plotFingerprint/`의 라이브러리 복잡성을 확인합니다. 과도하게 전치되었음을 나타낼 수 있습니다.

**몇 가지 피크**: `--macs_qvalue 0.1`을 사용하여 임계값을 낮추거나 더 넓은 피크를 위해 `--narrow_peak false`을 사용합니다.

**중복률 높음**: 입력이 적은 경우 정상입니다. 파이프라인은 기본적으로 제거됩니다.

## 추가 정보

- **전체 매개변수 목록:** https://nf-co.re/atacseq/2.1.2/parameters/
- **출력 문서:** https://nf-co.re/atacseq/2.1.2/docs/output/
- **사용 문서:** https://nf-co.re/atacseq/2.1.2/docs/usage/
