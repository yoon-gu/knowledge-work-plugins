# Bio-Research 플러그인

전임상 연구 도구 및 데이터베이스(문헌 검색, 유전체학 분석, 표적 우선순위화)에 연결하여 초기 단계 생명 과학 R&D를 가속화합니다. [Cowork](https://claude.com/product/cowork)와 함께 사용하거나 Claude Code에 직접 설치할 수 있습니다.

이 플러그인은 생명 과학 연구자를 위한 단일 패키지로 10개의 MCP 서버 통합과 5개의 분석 스킬을 통합합니다.

## 포함된 내용

### MCP 서버 (데이터 소스 및 도구)

> 익숙하지 않은 자리 표시자가 보이거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우, [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

| 제공업체 | 기능 | 카테고리/자리 표시자 |
|----------|-------------|---------------------|
| U.S. National Library of Medicine | 생의학 문헌 및 연구 논문 검색 | `~~literature` |
| deepsense.ai | bioRxiv 및 medRxiv의 프리프린트 접근 | `~~literature` |
| John Wiley & Sons | 학술 연구 및 출판물 접근 | `~~journal access` |
| Sage Bionetworks | 협업 연구 데이터 관리 | `~~data repository` |
| deepsense.ai | 생리활성 약물 유사 화합물 데이터베이스 | `~~chemical database` |
| OpenTargets | 약물 표적 발견 및 우선순위화 | `~~drug targets` |
| deepsense.ai | NIH/NLM 임상 시험 등록부 | `~~clinical trials` |
| BioRender | 과학 일러스트레이션 생성 | `~~scientific illustration` |
| Owkin | 생물학을 위한 AI — 조직 병리학 및 신약 개발 | `~~AI research` |
| Benchling\* | 실험실 데이터 관리 플랫폼 | `~~lab platform` |

### 선택적 바이너리 MCP 서버

다음 서버는 별도의 바이너리 다운로드가 필요합니다:

- **10X Genomics txg-mcp** (`~~genomics platform`) — 클라우드 분석 데이터 및 워크플로우 ([GitHub](https://github.com/10XGenomics/txg-mcp/releases))
- **ToolUniverse** (`~~tool database`) — Harvard MIMS의 과학적 발견을 위한 AI 도구 ([GitHub](https://github.com/mims-harvard/ToolUniverse/releases))

### 스킬 (분석 워크플로우)

#### 단일세포 RNA QC
scverse 모범 사례에 따라 scRNA-seq 데이터에 대한 자동화된 품질 관리. MAD 기반 필터링 및 종합적인 시각화를 통해 `.h5ad` 및 `.h5` 파일을 지원합니다.

#### scvi-tools
단일세포 오믹스를 위한 딥러닝 툴킷. 통합, 배치 보정, 레이블 전이 및 다중 모달 분석을 위한 scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI 모델을 포함합니다.

#### Nextflow 파이프라인
로컬 또는 공개 GEO/SRA 시퀀싱 데이터에 nf-core 생물정보학 파이프라인을 실행합니다:
- **rnaseq** — 유전자 발현 및 차등 발현
- **sarek** — 생식세포 및 체세포 변이 호출 (WGS/WES)
- **atacseq** — 크로마틴 접근성 분석

#### 기기 데이터를 Allotrope로 변환
실험실 기기 출력 파일(PDF, CSV, Excel, TXT)을 Allotrope Simple Model(ASM) 형식으로 변환합니다. 세포 계수기, 분광광도계, 플레이트 리더, qPCR, 크로마토그래피 시스템을 포함한 40가지 이상의 기기 유형을 지원합니다.

#### 과학적 문제 선정
Fischbach & Walsh의 프레임워크에 기반한 연구 문제 선정을 위한 체계적인 프레임워크. 아이디어 발굴, 위험 평가, 최적화, 의사결정 트리, 역경 계획 및 종합을 다루는 9개의 스킬을 포함합니다.

## 시작하기

```bash
# 플러그인 설치
/install anthropics/knowledge-work-plugins bio-research

# 시작 명령어를 실행하여 사용 가능한 도구 확인
/start
```

## 일반적인 워크플로우

**문헌 검토**
논문을 위해 ~~literature 데이터베이스를 검색하고, ~~journal access를 통해 전문을 접근하며, ~~scientific illustration으로 그림을 만듭니다.

**단일세포 분석**
scRNA-seq 데이터에 대해 QC를 실행하고, 통합, 배치 보정 및 세포 유형 주석을 위해 scvi-tools를 사용합니다.

**시퀀싱 파이프라인**
GEO/SRA에서 공개 데이터를 다운로드하고, nf-core 파이프라인(RNA-seq, 변이 호출, ATAC-seq)을 실행하며, 출력을 확인합니다.

**신약 개발**
생리활성 화합물을 위해 ~~chemical database를 검색하고, 표적 우선순위화를 위해 ~~drug target database를 사용하며, 임상 시험 데이터를 검토합니다.

**연구 전략**
새로운 아이디어를 제안하고, 막힌 프로젝트를 해결하거나, 과학적 문제 선정 프레임워크를 사용하여 전략적 결정을 평가합니다.

## 라이선스

스킬은 Apache 2.0 라이선스 하에 있습니다. MCP 서버는 각 저자가 제공합니다 — 이용 약관은 개별 서버 문서를 참조하세요.
