# Bio-Research 플러그인

전임상 연구 도구와 데이터베이스에 연결해 초기 생명과학 R&D를 가속합니다. 문헌 검색, 유전체 분석, 타깃 우선순위화 같은 작업을 지원하며, [Cowork](https://claude.com/product/cowork)와 함께 사용하거나 Claude Code에 직접 설치할 수 있습니다.

이 플러그인은 생명과학 연구자를 위해 10개의 MCP 서버 연동과 5개의 분석 스킬을 하나의 패키지로 묶어 둡니다.

## 포함 내용

### MCP 서버, 데이터 소스 및 도구

> 익숙하지 않은 자리표시자가 보이거나 어떤 도구가 연결되어 있는지 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

| 제공자 | 하는 일 | 범주/자리표시자 |
|----------|-------------|---------------------|
| U.S. National Library of Medicine | 생의학 문헌과 연구 논문 검색 | `~~literature` |
| deepsense.ai | bioRxiv와 medRxiv의 프리프린트 접근 | `~~literature` |
| John Wiley & Sons | 학술 연구와 출판물 접근 | `~~journal access` |
| Sage Bionetworks | 협업형 연구 데이터 관리 | `~~data repository` |
| deepsense.ai | 생리활성 약물 유사 화합물 데이터베이스 | `~~chemical database` |
| OpenTargets | 약물 타깃 발견과 우선순위화 | `~~drug targets` |
| deepsense.ai | NIH/NLM 임상시험 레지스트리 | `~~clinical trials` |
| BioRender | 과학 일러스트레이션 제작 | `~~scientific illustration` |
| Owkin | 생물학용 AI, 병리학과 신약 발견 | `~~AI research` |
| Benchling\* | 실험실 데이터 관리 플랫폼 | `~~lab platform` |

### 선택적 바이너리 MCP 서버

이 항목들은 별도의 바이너리 다운로드가 필요합니다.

- **10X Genomics txg-mcp** (`~~genomics platform`) - 클라우드 분석 데이터와 워크플로 ([GitHub](https://github.com/10XGenomics/txg-mcp/releases))
- **ToolUniverse** (`~~tool database`) - Harvard MIMS의 과학 발견용 AI 도구 ([GitHub](https://github.com/mims-harvard/ToolUniverse/releases))

### 스킬, 분석 워크플로

#### 단일세포 RNA QC
scverse 모범 사례를 따르는 scRNA-seq 데이터의 자동 품질 관리입니다. MAD 기반 필터링과 포괄적인 시각화를 지원하며 `.h5ad`와 `.h5` 파일을 다룹니다.

#### scvi-tools
단일세포 오믹스를 위한 딥러닝 도구 모음입니다. 통합, 배치 보정, 라벨 전이, 멀티모달 분석을 위한 scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI 모델을 다룹니다.

#### Nextflow 파이프라인
로컬 또는 공개 GEO/SRA 시퀀싱 데이터에 nf-core 생물정보학 파이프라인을 실행합니다.
- **rnaseq** - 유전자 발현과 차등 발현
- **sarek** - 생식계열 및 체세포 변이 호출(WGS/WES)
- **atacseq** - 크로마틴 접근성 분석

#### Instrument Data to Allotrope
실험실 장비 출력 파일(PDF, CSV, Excel, TXT)을 Allotrope Simple Model(ASM) 형식으로 변환합니다. 세포 계수기, 분광광도계, 플레이트 리더, qPCR, 크로마토그래피 시스템을 포함해 40개 이상의 기기 유형을 지원합니다.

#### Scientific Problem Selection
Fischbach & Walsh의 프레임워크를 기반으로 한 연구 문제 선택 체계입니다. 아이데이션, 리스크 평가, 최적화, 의사결정 트리, 역경 대응, 종합을 다루는 9개 스킬을 포함합니다.

## 시작하기

```bash
# 플러그인 설치
/install anthropics/knowledge-work-plugins bio-research

# 사용 가능한 도구를 보려면 시작 명령 실행
/start
```

## 일반 워크플로

**문헌 검토**
`~~literature` 데이터베이스에서 논문을 검색하고, `~~journal access`를 통해 전문을 읽고, `~~scientific illustration`으로 그림을 만듭니다.

**단일세포 분석**
scRNA-seq 데이터에 QC를 수행한 뒤, scvi-tools를 사용해 통합, 배치 보정, 세포 유형 주석을 진행합니다.

**시퀀싱 파이프라인**
공개 GEO/SRA 데이터에서 데이터를 내려받고, nf-core 파이프라인(RNA-seq, 변이 호출, ATAC-seq)을 실행하고, 출력을 검증합니다.

**신약 발견**
`~~chemical database`에서 생리활성 화합물을 찾고, `~~drug target database`를 사용해 타깃을 우선순위화하고, 임상시험 데이터를 검토합니다.

**연구 전략**
새 아이디어를 제안하고, 막힌 프로젝트를 디버그하고, 과학적 문제 선택 프레임워크를 사용해 전략적 결정을 평가합니다.

## 라이선스

스킬은 Apache 2.0으로 라이선스됩니다. MCP 서버는 각 작성자가 제공합니다. 이용 조건은 개별 서버 문서를 참고하세요.
