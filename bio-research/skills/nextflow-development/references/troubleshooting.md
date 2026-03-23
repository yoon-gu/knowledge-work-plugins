# 문제 해결

nf-core 파이프라인의 일반적인 문제에 대한 빠른 수정 방법입니다.

## 목차
- [종료 코드](#종료-코드)
- [HPC/Singularity 문제](#hpcsingularity-문제)
- [파이프라인 실패](#파이프라인-실패)
- [RNA-seq 관련](#rna-seq-관련)
- [Sarek 관련](#sarek-관련)
- [ATAC-seq 관련](#atac-seq-관련)
- [리소스 관리](#리소스-관리)
- [도움 받기](#도움-받기)

## 종료 코드

리소스 문제를 나타내는 일반적인 종료 코드 ([nf-core 문서](https://nf-co.re/docs/usage/troubleshooting/crash_halfway) 참조):

| 코드 | 원인 | 해결 방법 |
|------|-------|-----|
| 137 | 메모리 부족 | `--max_memory '32.GB'` 또는 WGS의 경우 `'64.GB'` |
| 143 | 메모리 부족 | `--max_memory '32.GB'` 또는 WGS의 경우 `'64.GB'` |
| 104, 134, 139, 247 | 메모리 부족 | `--max_memory` 증가 |
| 1 | 일반 오류 | `.nextflow.log`에서 세부사항 확인 |

대부분의 파이프라인은 실패 전에 2배, 3배 리소스로 자동 재시도합니다.

## HPC/Singularity 문제

### Singularity 캐시 문제
```bash
export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"
mkdir -p $NXF_SINGULARITY_CACHEDIR
```

### Docker 대신 Singularity 사용
Docker가 없는 HPC 시스템에서는 Singularity를 사용합니다:
```bash
nextflow run nf-core/<pipeline> -profile singularity ...
```

> **참고**: 기본 환경 설정(Docker, Nextflow, Java 설치)은 SKILL.md의 Step 1에 있는 인라인 지침을 참조하세요.

## 파이프라인 실패

### 컨테이너 풀 실패
- 네트워크 연결 확인
- 시도: docker 대신 `-profile singularity`
- 오프라인 사용: `nf-core download <pipeline> -r <version>`

### "No such file" 오류
- 샘플시트에서 **절대 경로** 사용
- 파일 존재 확인: `ls /path/to/file`

### 재개가 작동하지 않음
```bash
# Check work directory exists
ls -la work/

# Force clean restart (loses cache)
rm -rf work/ .nextflow*
nextflow run nf-core/<pipeline> ...
```

## RNA-seq 관련

### STAR 인덱스 실패
- 메모리 증가: `--max_memory '64.GB'`
- 또는 미리 빌드된 인덱스 제공: `--star_index /path/to/star/`

### 낮은 정렬률
- 게놈이 종과 일치하는지 확인
- FastQC에서 어댑터 오염 확인
- 다른 정렬기 시도: `--aligner hisat2`

### 가닥성 감지 실패
- 명시적으로 지정: `--strandedness reverse`
- 일반적인 값: `forward`, `reverse`, `unstranded`

## Sarek 관련

### BQSR 실패
- 게놈의 알려진 사이트 확인
- 비표준 참조의 경우 건너뛰기: `--skip_bqsr`

### Mutect2 변이 없음
- 종양/정상 쌍 확인
- 샘플시트 `status` 컬럼 확인: 0=정상, 1=종양

### WGS 메모리 부족
```bash
--max_memory '128.GB' --max_cpus 16
```

### DeepVariant GPU 문제
- NVIDIA Docker 런타임이 구성되어 있는지 확인
- 또는 CPU 모드 사용 (느림)

## ATAC-seq 관련

### 낮은 FRiP 점수
- `plotFingerprint/`에서 라이브러리 복잡도 확인
- 과도한 트랜스포지션을 나타낼 수 있음

### 적은 피크 호출
- 임계값 낮추기: `--macs_qvalue 0.1`
- 넓은 피크 사용: `--narrow_peak false`

### 높은 중복
- 저입력 샘플에서는 정상
- 파이프라인이 기본적으로 제거
- 더 깊은 시퀀싱 고려

## 리소스 관리

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

1. `.nextflow.log`에서 오류 세부사항 확인
2. nf-core Slack 검색: https://nf-co.re/join
3. GitHub에서 이슈 열기: https://github.com/nf-core/<pipeline>/issues
