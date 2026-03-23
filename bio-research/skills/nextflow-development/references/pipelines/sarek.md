# nf-core/sarek

**버전:** 3.7.1

**공식 문서:** https://nf-co.re/sarek/3.7.1/
**GitHub:** https://github.com/nf-core/sarek

> **참고:** 새 버전으로 업데이트할 때 [releases page](https://github.com/nf-core/sarek/releases)에서 주요 변경 사항이 있는지 확인하고 아래 명령으로 버전을 업데이트하세요.

## 내용
- [Test command](#test-command)
- [Samplesheet format](#samplesheet-format)
- [Variant calling modes](#variant-calling-modes)
- [Parameters](#parameters)
- [Output files](#output-files)

## 테스트 명령

```bash
nextflow run nf-core/sarek -r 3.7.1 -profile test,docker --outdir test_sarek
```

예상: ~20분, 정렬된 BAM 및 변형 호출을 생성합니다.

## 샘플시트 형식

### FASTQ에서
```csv
patient,sample,lane,fastq_1,fastq_2
patient1,tumor,L001,/path/to/tumor_L001_R1.fq.gz,/path/to/tumor_L001_R2.fq.gz
patient1,tumor,L002,/path/to/tumor_L002_R1.fq.gz,/path/to/tumor_L002_R2.fq.gz
patient1,normal,L001,/path/to/normal_R1.fq.gz,/path/to/normal_R2.fq.gz
```

### BAM/CRAM에서
```csv
patient,sample,bam,bai
patient1,tumor,/path/to/tumor.bam,/path/to/tumor.bam.bai
patient1,normal,/path/to/normal.bam,/path/to/normal.bam.bai
```

### 종양/정상 상태
```csv
patient,sample,lane,fastq_1,fastq_2,status
patient1,tumor,L001,tumor_R1.fq.gz,tumor_R2.fq.gz,1
patient1,normal,L001,normal_R1.fq.gz,normal_R2.fq.gz,0
```

`status`: 0 = 정상, 1 = 종양

## 다양한 호출 모드

### 생식계열(단일 샘플)
```bash
nextflow run nf-core/sarek -r 3.7.1 -profile docker \
    --input samplesheet.csv --outdir results --genome GRCh38 \
    --tools haplotypecaller,snpeff
```

### 체세포(종양-정상 쌍)
```bash
nextflow run nf-core/sarek -r 3.7.1 -profile docker \
    --input samplesheet.csv --outdir results --genome GRCh38 \
    --tools mutect2,strelka,snpeff
```

### WES(엑솜)
```bash
nextflow run nf-core/sarek -r 3.7.1 -profile docker \
    --input samplesheet.csv --outdir results --genome GRCh38 \
    --wes --intervals /path/to/targets.bed \
    --tools haplotypecaller,snpeff
```

### 공동 생식계열(코호트)
```bash
--tools haplotypecaller --joint_germline
```

## 매개변수

### 사용 가능한 도구

**생식계열 호출자:**
- `haplotypecaller`: GATK HaplotypeCaller
- `freebayes`: 프리베이즈
- `deepvariant`: DeepVariant(GPU 옵션)
- `strelka`: Strelka2 생식계열

**신체 발신자:**
- `mutect2`: GATK Mutect2
- `strelka`: Strelka2 체세포
- `manta`: 구조적 변형

**CNV 발신자:**
- `ascat`: 복사번호
- `controlfreec`: CNV 감지
- `tiddit`: SV 호출

**주석:**
- `snpeff`: 기능 주석
- `vep`: 변형 효과 예측기

### 주요 매개변수

| 매개변수 | 기본값 | 설명 |
|------------|---------|-------------|
| `--tools` | - | 쉼표로 구분된 도구 목록 |
| `--genome` | - | `GRCh38`, `GRCh37` |
| `--wes` | 거짓 | 엑솜 모드(`--intervals` 필요) |
| `--intervals` | - | 대상 지역에 대한 BED 파일 |
| `--joint_germline` | 거짓 | 코호트 공동 소집 |
| `--skip_bqsr` | 거짓 | 기본 품질 재보정 건너뛰기 |

## 출력 파일

```
results/
├── preprocessing/
│   └── recalibrated/           # Analysis-ready BAMs
│       └── *.recal.bam
├── variant_calling/
│   ├── haplotypecaller/        # Germline VCFs
│   ├── mutect2/                # Somatic VCFs (filtered)
│   └── strelka/
├── annotation/
│   └── snpeff/                 # Annotated VCFs
└── multiqc/
```

## 문제 해결

**BQSR 실패**: 게놈에 사용 가능한 알려진 사이트를 확인합니다. 비표준 참조의 경우 `--skip_bqsr`을 사용하여 건너뜁니다.

**Mutect2 변종 없음**: 샘플 시트에서 종양/정상 쌍을 확인합니다(`status` 열 확인).

**메모리 부족**: WGS의 경우 `--max_memory '128.GB'`.

**DeepVariant GPU**: NVIDIA Docker 런타임이 구성되어 있는지 확인하세요.

## 추가 정보

- **전체 매개변수 목록:** https://nf-co.re/sarek/3.7.1/parameters/
- **출력 문서:** https://nf-co.re/sarek/3.7.1/docs/output/
- **사용 문서:** https://nf-co.re/sarek/3.7.1/docs/usage/
