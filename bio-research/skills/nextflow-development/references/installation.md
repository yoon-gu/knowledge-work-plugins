# 설치

## 내용
- [Quick install](#quick-install)
- [Docker setup](#docker-setup)
- [Singularity setup (HPC)](#singularity-setup-hpc)
- [nf-core tools (optional)](#nf-core-tools-optional)
- [Verify installation](#verify-installation)
- [Common issues](#common-issues)

## 빠른 설치

```bash
# Nextflow
curl -s https://get.nextflow.io | bash
mv nextflow ~/bin/
export PATH="$HOME/bin:$PATH"

# Verify
nextflow -version
java -version  # Requires 11+
```

## 도커 설정

### 리눅스
```bash
sudo apt-get update && sudo apt-get install docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
# Log out and back in
```

### 맥OS
Docker 데스크탑 다운로드: https://docker.com/products/docker-desktop

### 확인
```bash
docker run hello-world
```

## Singularity 설정(HPC)

```bash
# Ubuntu/Debian
sudo apt-get install singularity-container

# Or via conda
conda install -c conda-forge singularity
```

### 캐시 구성
```bash
export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"
mkdir -p $NXF_SINGULARITY_CACHEDIR
echo 'export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"' >> ~/.bashrc
```

## nf-core 도구(선택 사항)

```bash
pip install nf-core
```

유용한 명령:
```bash
nf-core list                    # Available pipelines
nf-core launch rnaseq           # Interactive parameter selection
nf-core download rnaseq -r 3.14.0  # Download for offline use
```

## 설치 확인

```bash
nextflow run nf-core/demo -profile test,docker --outdir test_demo
ls test_demo/
```

## 일반적인 문제

**Java 버전이 잘못되었습니다:**
```bash
export JAVA_HOME=/path/to/java11
```

**Docker 권한이 거부되었습니다:**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

**Nextflow를 찾을 수 없습니다:**
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
