---
name: nextflow-development
description: 시퀀싱 데이터에 대해 nf-core 생물정보학 파이프라인(rnaseq, sarek, atacseq)을 실행합니다. RNA-seq, WGS/WES 또는 ATAC-seq 데이터(로컬 FASTQ 또는 GEO/SRA의 공개 데이터 세트)를 분석할 때 사용합니다. nf-core, Nextflow, FASTQ 분석, 변이체 호출, 유전자 발현, 차등 발현, GEO 재분석, GSE/GSM/SRR 가입 또는 샘플시트 생성을 트리거합니다.
---

# nf-core 파이프라인 배포

로컬 또는 공개 시퀀싱 데이터에 대해 nf-core 생물정보학 파이프라인을 실행합니다.

**대상 사용자:** 대규모 오믹스 분석(미분 발현, 변형 호출 또는 염색질 접근성 분석)을 실행해야 하는 전문 생물정보학 교육을 받지 않은 벤치 과학자 및 연구원.

## 워크플로 체크리스트

```
- [ ] Step 0: Acquire data (if from GEO/SRA)
- [ ] Step 1: Environment check (MUST pass)
- [ ] Step 2: Select pipeline (confirm with user)
- [ ] Step 3: Run test profile (MUST pass)
- [ ] Step 4: Create samplesheet
- [ ] Step 5: Configure & run (confirm genome with user)
- [ ] Step 6: Verify outputs
```

---

## 0단계: 데이터 수집(GEO/SRA에만 해당)

**사용자에게 로컬 FASTQ 파일이 있는 경우 이 단계를 건너뛰세요.**

공개 데이터 세트의 경우 먼저 GEO/SRA에서 가져옵니다. 전체 작업 흐름은 [references/geo-sra-acquisition.md](references/geo-sra-acquisition.md)을 참조하세요.

**빠른 시작:**

```bash
# 1. Get study info
python scripts/sra_geo_fetch.py info GSE110004

# 2. Download (interactive mode)
python scripts/sra_geo_fetch.py download GSE110004 -o ./fastq -i

# 3. Generate samplesheet
python scripts/sra_geo_fetch.py samplesheet GSE110004 --fastq-dir ./fastq -o samplesheet.csv
```

**결정 포인트:** 연구 정보를 가져온 후 사용자에게 확인합니다.
- 다운로드할 샘플 하위 집합(데이터 유형이 여러 개인 경우)
- 제안하는 게놈 및 파이프라인

그런 다음 1단계를 계속합니다.

---

## 1단계: 환경 확인

**먼저 실행하세요. 환경을 전달하지 않으면 파이프라인이 실패합니다.**

```bash
python scripts/check_environment.py
```

모든 중요 점검을 통과해야 합니다. 실패한 경우 수정 지침을 제공합니다.

### 도커 문제

| 문제 | 수정 |
|---------|-----|
| 설치되지 않음 | https://docs.docker.com/get-docker/에서 설치 |
| 허가가 거부되었습니다 | `sudo usermod -aG docker $USER` 그런 다음 다시 로그인 |
| 데몬이 실행되지 않음 | `sudo systemctl start docker` |

### Nextflow 문제

| 문제 | 수정 |
|---------|-----|
| 설치되지 않음 | `curl -s https://get.nextflow.io \| bash && mv nextflow ~/bin/` |
| 버전 < 23.04 | `nextflow self-update` |

### 자바 문제

| 문제 | 수정 |
|---------|-----|
| 설치되지 않음 / < 11 | `sudo apt install openjdk-11-jdk` |

**모든 검사가 통과될 때까지 진행하지 마십시오.** HPC/Singularity의 경우 [references/troubleshooting.md](references/troubleshooting.md)을 참조하세요.

---

## 2단계: 파이프라인 선택

**결정 사항: 계속하기 전에 사용자에게 확인하세요.**

| 데이터 유형 | 파이프라인 | 버전 | 목표 |
|------------|----------|---------|------|
| RNA-seq | `rnaseq` | 3.22.2 | 유전자 발현 |
| WGS/WES | `sarek` | 3.7.1 | 변형 호출 |
| ATAC-seq | `atacseq` | 2.1.2 | 크로마틴 접근성 |

데이터에서 자동 감지:
```bash
python scripts/detect_data_type.py /path/to/data
```

파이프라인별 세부정보:
- [references/pipelines/rnaseq.md](references/pipelines/rnaseq.md)
- [references/pipelines/sarek.md](references/pipelines/sarek.md)
- [references/pipelines/atacseq.md](references/pipelines/atacseq.md)

---

## 3단계: 테스트 프로필 실행

**작은 데이터로 환경을 검증합니다. 실제 데이터보다 먼저 통과해야 합니다.**

```bash
nextflow run nf-core/<pipeline> -r <version> -profile test,docker --outdir test_output
```

| 파이프라인 | 명령 |
|------------|---------|
| rnaseq | `nextflow run nf-core/rnaseq -r 3.22.2 -profile test,docker --outdir test_rnaseq` |
| sarek | `nextflow run nf-core/sarek -r 3.7.1 -profile test,docker --outdir test_sarek` |
| atacseq | `nextflow run nf-core/atacseq -r 2.1.2 -profile test,docker --outdir test_atacseq` |

확인:
```bash
ls test_output/multiqc/multiqc_report.html
grep "Pipeline completed successfully" .nextflow.log
```

테스트가 실패하면 [references/troubleshooting.md](references/troubleshooting.md)을 참조하세요.

---

## 4단계: 샘플시트 만들기

### 자동 생성

```bash
python scripts/generate_samplesheet.py /path/to/data <pipeline> -o samplesheet.csv
```

스크립트:
- FASTQ/BAM/CRAM 파일 검색
- R1/R2 쌍 읽기
- 샘플 메타데이터를 추론합니다.
- 쓰기 전에 유효성을 검사합니다.

**sarek의 경우:** 자동 감지되지 않는 경우 스크립트에서 종양/정상 상태를 묻는 메시지를 표시합니다.

### 기존 샘플시트 유효성 검사

```bash
python scripts/generate_samplesheet.py --validate samplesheet.csv <pipeline>
```

### 샘플 시트 형식

**rnaseq:**
```csv
sample,fastq_1,fastq_2,strandedness
SAMPLE1,/abs/path/R1.fq.gz,/abs/path/R2.fq.gz,auto
```

**sarek:**
```csv
patient,sample,lane,fastq_1,fastq_2,status
patient1,tumor,L001,/abs/path/tumor_R1.fq.gz,/abs/path/tumor_R2.fq.gz,1
patient1,normal,L001,/abs/path/normal_R1.fq.gz,/abs/path/normal_R2.fq.gz,0
```

**atacseq:**
```csv
sample,fastq_1,fastq_2,replicate
CONTROL,/abs/path/ctrl_R1.fq.gz,/abs/path/ctrl_R2.fq.gz,1
```

---

## 5단계: 구성 및 실행

### 5a. 게놈 가용성 확인

```bash
python scripts/manage_genomes.py check <genome>
# If not installed:
python scripts/manage_genomes.py download <genome>
```

공통 게놈: GRCh38(인간), GRCh37(레거시), GRCm39(마우스), R64-1-1(효모), BDGP6(파리)

### 5b. 결정 포인트

**결정 사항: 사용자에게 확인:**

1. **게놈:** 사용할 참조
2. **파이프라인별 옵션:**
   - **rnaseq:** 정렬기(star_salmon 권장, 메모리 부족의 경우 hisat2)
   - **sarek:** 도구(생식계열의 경우 haplotypecaller, 체세포의 경우 mutect2)
   - **atacseq:** read_length(50, 75, 100 또는 150)

### 5c. 파이프라인 실행

```bash
nextflow run nf-core/<pipeline> \
    -r <version> \
    -profile docker \
    --input samplesheet.csv \
    --outdir results \
    --genome <genome> \
    -resume
```

**주요 플래그:**
- `-r`: 핀 버전
- `-profile docker`: Docker(또는 HPC의 경우 `singularity`)를 사용합니다.
- `--genome`: iGenomes 키
- `-resume`: 체크포인트에서 계속

**리소스 제한(필요한 경우):**
```bash
--max_cpus 8 --max_memory '32.GB' --max_time '24.h'
```

---

## 6단계: 출력 확인

### 완료 확인

```bash
ls results/multiqc/multiqc_report.html
grep "Pipeline completed successfully" .nextflow.log
```

### 파이프라인별 주요 출력

**rnaseq:**
- `results/star_salmon/salmon.merged.gene_counts.tsv` - 유전자 수
- `results/star_salmon/salmon.merged.gene_tpm.tsv` - TPM 값

**sarek:**
- `results/variant_calling/*/` - VCF 파일
- `results/preprocessing/recalibrated/` - BAM 파일

**atacseq:**
- `results/macs2/narrowPeak/` - 피크 호출
- `results/bwa/mergedLibrary/bigwig/` - 커버리지 트랙

---

## 빠른 참조

일반적인 종료 코드 및 수정 사항은 [references/troubleshooting.md](references/troubleshooting.md)을 참조하세요.

### 실패한 실행 재개

```bash
nextflow run nf-core/<pipeline> -resume
```

---

## 참고자료

- [references/geo-sra-acquisition.md](references/geo-sra-acquisition.md) - 공개 GEO/SRA 데이터 다운로드
- [references/troubleshooting.md](references/troubleshooting.md) - 일반적인 문제 및 수정 사항
- [references/installation.md](references/installation.md) - 환경 설정
- [references/pipelines/rnaseq.md](references/pipelines/rnaseq.md) - RNA-seq 파이프라인 세부정보
- [references/pipelines/sarek.md](references/pipelines/sarek.md) - 다양한 호출 세부정보
- [references/pipelines/atacseq.md](references/pipelines/atacseq.md) - ATAC-seq 세부정보

---

## 면책조항

이 기술은 자동화된 분석 워크플로우를 위해 nf-core 생물정보학 파이프라인을 Claude Code에 통합하는 방법을 보여주는 프로토타입 예제로 제공됩니다. 현재 구현에서는 세 가지 파이프라인(rnaseq, sarek 및 atacseq)을 지원하며 커뮤니티가 전체 nf-core 파이프라인 세트에 대한 지원을 확장할 수 있는 기반 역할을 합니다.

이는 교육 및 연구 목적으로 만들어졌으며 특정 사용 사례에 대한 적절한 검증 없이 프로덕션 준비가 완료된 것으로 간주되어서는 안 됩니다. 사용자는 자신의 컴퓨팅 환경이 파이프라인 요구 사항을 충족하는지 확인하고 분석 결과를 확인할 책임이 있습니다.

Anthropic은 생물정보학 출력의 정확성을 보장하지 않으며 사용자는 전산 분석 검증을 위한 표준 관행을 따라야 합니다. 이 통합은 nf-core 커뮤니티에 의해 공식적으로 승인되거나 제휴되지 않습니다.

## 속성

결과를 게시할 때 적절한 파이프라인을 인용하세요. 인용은 각 nf-core 저장소의 CITATIONS.md 파일(예: https://github.com/nf-core/rnaseq/blob/3.22.2/CITATIONS.md).)에서 확인할 수 있습니다.

## 라이선스

- **nf-core 파이프라인:** MIT 라이선스(https://nf-co.re/about)
- **Nextflow:** Apache 라이센스, 버전 2.0(https://www.nextflow.io/about-us.html)
- **NCBI SRA 툴킷:** 공개 도메인(https://github.com/ncbi/sra-tools/blob/master/LICENSE)
