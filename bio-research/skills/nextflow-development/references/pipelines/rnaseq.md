# nf-core/rnaseq

**버전:** 3.22.2

**공식 문서:** https://nf-co.re/rnaseq/3.22.2/
**GitHub:** https://github.com/nf-core/rnaseq

> **참고:** 새 버전으로 업데이트할 때 [릴리스 페이지](https://github.com/nf-core/rnaseq/releases)에서 주요 변경 사항을 확인하고 아래 명령어의 버전을 업데이트하세요.

## 목차
- [테스트 명령어](#테스트-명령어)
- [샘플시트 형식](#샘플시트-형식)
- [파라미터](#파라미터)
- [출력 파일](#출력-파일)
- [다운스트림 분석](#다운스트림-분석)

## 테스트 명령어

```bash
nextflow run nf-core/rnaseq -r 3.22.2 -profile test,docker --outdir test_rnaseq
```

예상 시간: 약 15분, `multiqc/multiqc_report.html`을 생성합니다.

## 샘플시트 형식

```csv
sample,fastq_1,fastq_2,strandedness
CONTROL_REP1,/path/to/ctrl1_R1.fq.gz,/path/to/ctrl1_R2.fq.gz,auto
CONTROL_REP2,/path/to/ctrl2_R1.fq.gz,/path/to/ctrl2_R2.fq.gz,auto
TREATMENT_REP1,/path/to/treat1_R1.fq.gz,/path/to/treat1_R2.fq.gz,auto
```

| 컬럼 | 필수 | 값 |
|--------|----------|--------|
| sample | 예 | 영숫자, 밑줄 허용 |
| fastq_1 | 예 | R1 절대 경로 |
| fastq_2 | 아니오 | R2 절대 경로 (싱글엔드는 비워둠) |
| strandedness | 예 | `auto`, `forward`, `reverse`, `unstranded` |

**가닥성 안내:**
- `auto`: 데이터에서 추론 (권장)
- `forward`: TruSeq Stranded, dUTP 프로토콜
- `reverse`: 결찰 기반 프로토콜
- `unstranded`: 비가닥 프로토콜

## 파라미터

### 최소 실행
```bash
nextflow run nf-core/rnaseq -r 3.22.2 -profile docker \
    --input samplesheet.csv --outdir results --genome GRCh38
```

### 일반적인 파라미터

| 파라미터 | 기본값 | 설명 |
|-----------|---------|-------------|
| `--aligner` | `star_salmon` | 옵션: `star_salmon`, `star_rsem`, `hisat2` |
| `--genome` | - | `GRCh38`, `GRCh37`, `mm10`, `BDGP6` |
| `--pseudo_aligner` | - | 의사정렬만 하려면 `salmon`으로 설정 |
| `--skip_trimming` | false | 어댑터 트리밍 건너뛰기 |
| `--skip_alignment` | false | 의사정렬만 수행 |

### 사용자 정의 참조
```bash
--fasta /path/to/genome.fa \
--gtf /path/to/annotation.gtf \
--star_index /path/to/star/  # Optional, builds if absent
```

## 출력 파일

```
results/
├── star_salmon/
│   ├── salmon.merged.gene_counts.tsv    # DESeq2용 원시 카운트
│   ├── salmon.merged.gene_tpm.tsv       # TPM 값
│   └── *.bam                            # 정렬
├── multiqc/
│   └── multiqc_report.html              # QC 요약
└── pipeline_info/
```

**주요 출력:**
- `salmon.merged.gene_counts.tsv`: DESeq2/edgeR 입력
- `salmon.merged.gene_tpm.tsv`: 정규화된 발현

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

**STAR 인덱스 실패**: `--max_memory '64.GB'`로 메모리를 늘리거나 미리 빌드된 `--star_index`를 제공하세요.

**낮은 정렬률**: 게놈이 종과 일치하는지 확인하고, FastQC에서 어댑터 오염을 확인하세요.

**가닥성 감지 실패**: `--strandedness reverse`로 명시적으로 지정하세요.

## 추가 정보

- **전체 파라미터 목록:** https://nf-co.re/rnaseq/3.22.2/parameters/
- **출력 문서:** https://nf-co.re/rnaseq/3.22.2/docs/output/
- **사용법 문서:** https://nf-co.re/rnaseq/3.22.2/docs/usage/
