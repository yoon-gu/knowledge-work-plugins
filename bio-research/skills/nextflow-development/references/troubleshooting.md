# 문제 해결

일반적인 nf-core 파이프라인 문제에 대한 빠른 수정입니다.

## 내용
- [Exit Codes](#exit-codes)
- [HPC/Singularity Issues](#hpcsingularity-issues)
- [Pipeline Failures](#pipeline-failures)
- [RNA-seq Specific](#rna-seq-specific)
- [sarek Specific](#sarek-specific)
- [ATAC-seq Specific](#atac-seq-specific)
- [Resource Management](#resource-management)
- [Getting Help](#getting-help)

## 종료 코드

리소스 문제를 나타내는 일반적인 종료 코드([nf-core docs](https://nf-co.re/docs/usage/troubleshooting/crash_halfway)당):

| 코드 | 원인 | 수정 |
|------|-------|------|
| 137 | 메모리 부족 | WGS의 경우 `--max_memory '32.GB'` 또는 `'64.GB'` |
| 143 | 메모리 부족 | WGS의 경우 `--max_memory '32.GB'` 또는 `'64.GB'` |
| 104, 134, 139, 247 | 메모리 부족 | `--max_memory` 증가 |
| 1 | 일반 오류 | 자세한 내용은 `.nextflow.log`을 확인하세요 |

대부분의 파이프라인은 실패하기 전에 2배, 3배 리소스를 사용하여 자동 재시도합니다.

## HPC/Singularity 문제

### Singularity 캐시 문제
```bash
export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"
mkdir -p $NXF_SINGULARITY_CACHEDIR
```

### Docker 대신 Singularity 사용
Docker가 없는 HPC 시스템에서는 Singularity를 사용하십시오.
```bash
nextflow run nf-core/<pipeline> -profile singularity ...
```

> **참고**: 기본 환경 설정(Docker, Nextflow, Java 설치)의 경우 SKILL.md의 1단계에 있는 인라인 지침을 참조하세요.

## 파이프라인 실패

### 컨테이너 가져오기 실패
- 네트워크 연결을 확인하세요
- 시도해 보세요: docker 대신 `-profile singularity`
- 오프라인의 경우: `nf-core download <pipeline> -r <version>`

### "해당 파일이 없습니다" 오류
- 샘플 시트에서 **절대 경로** 사용
- 파일이 존재하는지 확인: `ls /path/to/file`

### 이력서가 작동하지 않습니다
```bash
# Check work directory exists
ls -la work/

# Force clean restart (loses cache)
rm -rf work/ .nextflow*
nextflow run nf-core/<pipeline> ...
```

## RNA-seq 특이적

### STAR 인덱스 실패
- 메모리 늘리기: `--max_memory '64.GB'`
- 또는 사전 구축된 제공: `--star_index /path/to/star/`

### 낮은 정렬률
- 게놈이 종과 일치하는지 확인
- FastQC에서 어댑터 오염 여부를 확인하세요.
- 다른 정렬 장치를 사용해 보십시오: `--aligner hisat2`

### 좌초 감지 실패
- 명시적으로 지정: `--strandedness reverse`
- 공통 값: `forward`, `reverse`, `unstranded`

## sarek 특정

### BQSR 실패
- 알려진 게놈 사이트 확인
- 비표준 참조 건너뛰기: `--skip_bqsr`

### Mutect2 변형 없음
- 종양/정상 페어링 확인
- 샘플시트 `status` 열 확인: 0=정상, 1=종양

### WGS 메모리 부족
```bash
--max_memory '128.GB' --max_cpus 16
```

### DeepVariant GPU 문제
- NVIDIA Docker 런타임이 구성되었는지 확인하세요.
- 또는 CPU 모드 사용(느림)

## ATAC-seq 특정

### 낮은 FRiP 점수
- `plotFingerprint/`의 라이브러리 복잡성을 확인하세요.
- 과도한 전치를 나타낼 수 있음

### 몇 개의 봉우리가 호출되었습니다.
- 하한치: `--macs_qvalue 0.1`
- 넓은 피크 사용: `--narrow_peak false`

### 중복이 많음
- 저입력 샘플의 경우 일반
- 파이프라인은 기본적으로 제거됩니다.
- 더 깊은 순서를 고려하세요.

## 자원 관리

### 리소스 제한 설정
```bash
--max_cpus 8 --max_memory '32.GB' --max_time '24.h'
```

### 사용 가능한 리소스 확인
```bash
# CPUs
nproc

# Memory
free -h

# Disk
df -h .
```

## 도움 받기

1. `.nextflow.log`에서 오류 세부정보를 확인하세요.
2. nf-core Slack 검색: https://nf-co.re/join
3. GitHub에서 이슈 열기: https://github.com/nf-core/<pipeline>/issues
