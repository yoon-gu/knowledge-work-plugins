# nf-core/rnaseq

**버전:** 3.22.2

**공식 문서:** https://nf-co.re/rnaseq/3.22.2/
**GitHub:** https://github.com/nf-core/rnaseq

> **참고:** 새 버전으로 업데이트할 때 [releases page](https://github.com/nf-core/rnaseq/releases)에서 주요 변경 사항이 있는지 확인하고 아래 명령으로 버전을 업데이트하세요.

## 내용
- [Test command](#test-command)
- [Samplesheet format](#samplesheet-format)
- [Parameters](#parameters)
- [Output files](#output-files)
- [Downstream analysis](#downstream-analysis)

## 테스트 명령

```bash
nextflow run nf-core/rnaseq -r 3.22.2 -profile test,docker --outdir test_rnaseq
```

예상: ~15분, `multiqc/multiqc_report.html`을 생성합니다.

## 샘플시트 형식

```csv
sample,fastq_1,fastq_2,strandedness
CONTROL_REP1,/path/to/ctrl1_R1.fq.gz,/path/to/ctrl1_R2.fq.gz,auto
CONTROL_REP2,/path/to/ctrl2_R1.fq.gz,/path/to/ctrl2_R2.fq.gz,auto
TREATMENT_REP1,/path/to/treat1_R1.fq.gz,/path/to/treat1_R2.fq.gz,auto
```

| 칼럼 | 필수 | 가치 |
|---------|----------|---------|
| 샘플 | 예 | 영숫자, 밑줄 허용 |
| fastq_1 | 예 | R1에 대한 절대 경로 |
| fastq_2 | 아니요 | R2에 대한 절대 경로(단일 엔드의 경우 비어 있음) |
| 좌초 | 예 | `auto`, `forward`, `reverse`, `unstranded` |

**좌초 가이드:**
- `auto`: 데이터에서 추론됨(권장)
- `forward`: TruSeq 좌초, dUTP 프로토콜
- `reverse`: 결찰 기반 프로토콜
- `unstranded`: 비좌초 프로토콜

## 매개변수

### 최소 실행
```bash
nextflow run nf-core/rnaseq -r 3.22.2 -profile docker \
    --input samplesheet.csv --outdir results --genome GRCh38
```

### 공통 매개변수

| 매개변수 | 기본값 | 설명 |
|------------|---------|-------------|
| `--aligner` | `star_salmon` | 옵션: `star_salmon`, `star_rsem`, `hisat2` |
| `--genome` | - | `GRCh38`, `GRCh37`, `mm10`, `BDGP6` |
| `--pseudo_aligner` | - | 의사 정렬에만 `salmon`로 설정 |
| `--skip_trimming` | 거짓 | 어댑터 트리밍 건너뛰기 |
| `--skip_alignment` | 거짓 | 의사 정렬만 |

### 맞춤 참조
```bash
--fasta /path/to/genome.fa \
--gtf /path/to/annotation.gtf \
--star_index /path/to/star/  # Optional, builds if absent
```

## 출력 파일

```
results/
├── star_salmon/
│   ├── salmon.merged.gene_counts.tsv    # Raw counts for DESeq2
│   ├── salmon.merged.gene_tpm.tsv       # TPM values
│   └── *.bam                            # Alignments
├── multiqc/
│   └── multiqc_report.html              # QC summary
└── pipeline_info/
```

**주요 결과:**
- `salmon.merged.gene_counts.tsv`: DESeq2/edgeR에 대한 입력
- `salmon.merged.gene_tpm.tsv`: 정규화된 표현식

## 다운스트림 분석

```r
library(DESeq2)
counts <- read.delim("salmon.merged.gene_counts.tsv", row.names=1)
coldata <- data.frame(
    condition = factor(c("control", "control", "treatment", "treatment"))
)
dds <- DESeqDataSetFromMatrix(
    countData = round(counts),
    colData = coldata,
    design = ~ condition
)
dds <- DESeq(dds)
res <- results(dds, contrast = c("condition", "treatment", "control"))
```

## 문제 해결

**STAR 인덱스 실패**: `--max_memory '64.GB'`으로 메모리를 늘리거나 사전 빌드된 `--star_index`을 제공합니다.

**낮은 정렬 비율**: 게놈이 종과 일치하는지 확인합니다. FastQC에서 어댑터 오염을 확인하세요.

**좌초 감지 실패**: `--strandedness reverse`을 사용하여 명시적으로 지정합니다.

## 추가 정보

- **전체 매개변수 목록:** https://nf-co.re/rnaseq/3.22.2/parameters/
- **출력 문서:** https://nf-co.re/rnaseq/3.22.2/docs/output/
- **사용 문서:** https://nf-co.re/rnaseq/3.22.2/docs/usage/
