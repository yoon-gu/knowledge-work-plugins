# 설치

## 목차
- [빠른 설치](#빠른-설치)
- [Docker 설정](#docker-설정)
- [Singularity 설정 (HPC)](#singularity-설정-hpc)
- [nf-core tools (선택 사항)](#nf-core-tools-선택-사항)
- [설치 확인](#설치-확인)
- [일반적인 문제](#일반적인-문제)

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

## Docker 설정

### Linux
```bash
sudo apt-get update && sudo apt-get install docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
# Log out and back in
```

### macOS
Docker Desktop 다운로드: https://docker.com/products/docker-desktop

### 확인
```bash
docker run hello-world
```

## Singularity 설정 (HPC)

```bash
# Ubuntu/Debian
sudo apt-get install singularity-container

# Or via conda
conda install -c conda-forge singularity
```

### 캐시 설정
```bash
export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"
mkdir -p $NXF_SINGULARITY_CACHEDIR
echo 'export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"' >> ~/.bashrc
```

## nf-core tools (선택 사항)

```bash
pip install nf-core
```

유용한 명령어:
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

**Java 버전 오류:**
```bash
export JAVA_HOME=/path/to/java11
```

**Docker 권한 거부:**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

**Nextflow를 찾을 수 없음:**
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
