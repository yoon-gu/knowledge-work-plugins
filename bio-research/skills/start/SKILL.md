---
name: start
description: Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.
---

# Bio-Research 시작

> 익숙하지 않은 자리 표시자가 보이거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우, [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

생명 과학 연구자가 bio-research 플러그인을 처음 사용할 때 도움을 드립니다. 아래 단계를 순서대로 진행해 주세요.

## 1단계: 환영 메시지

다음 환영 메시지를 표시합니다:

```
Bio-Research 플러그인

생명 과학을 위한 AI 기반 연구 도우미입니다. 이 플러그인은
문헌 검색, 데이터 분석 파이프라인,
과학적 전략을 한 곳에서 통합합니다.
```

## 2단계: 사용 가능한 MCP 서버 확인

사용 가능한 도구를 나열하여 어떤 MCP 서버가 연결되어 있는지 테스트합니다. 결과를 다음과 같이 그룹화합니다:

**문헌 및 데이터 소스:**
- ~~literature database — 생의학 문헌 검색
- ~~literature database — 프리프린트 접근 (생물학 및 의학)
- ~~journal access — 학술 출판물
- ~~data repository — 협업 연구 데이터 (Sage Bionetworks)

**신약 개발 및 임상:**
- ~~chemical database — 생리활성 화합물 데이터베이스
- ~~drug target database — 약물 표적 발견 플랫폼
- ClinicalTrials.gov — 임상 시험 등록부
- ~~clinical data platform — 임상 시험 사이트 순위 및 플랫폼 도움말

**시각화 및 AI:**
- ~~scientific illustration — 과학 그림 및 다이어그램 생성
- ~~AI research platform — 생물학을 위한 AI (조직 병리학, 신약 개발)

연결된 서버와 아직 설정되지 않은 서버를 보고합니다.

## 3단계: 사용 가능한 스킬 조사

이 플러그인에서 사용 가능한 분석 스킬을 나열합니다:

| 스킬 | 기능 |
|-------|-------------|
| **단일세포 RNA QC** | MAD 기반 필터링을 사용한 scRNA-seq 데이터 품질 관리 |
| **scvi-tools** | 단일세포 오믹스를 위한 딥러닝 (scVI, scANVI, totalVI, PeakVI 등) |
| **Nextflow 파이프라인** | nf-core 파이프라인 실행 (RNA-seq, WGS/WES, ATAC-seq) |
| **기기 데이터 변환기** | 실험실 기기 출력을 Allotrope ASM 형식으로 변환 |
| **과학적 문제 선정** | 연구 문제 선택을 위한 체계적인 프레임워크 |

## 4단계: 선택 설정 — 바이너리 MCP 서버

별도로 설치 가능한 두 가지 추가 MCP 서버가 있음을 알려줍니다:

- **~~genomics platform** — 클라우드 분석 데이터 및 워크플로우 접근
  설치: https://github.com/10XGenomics/txg-mcp/releases 에서 `txg-node.mcpb` 다운로드
- **~~tool database** (Harvard MIMS) — 과학적 발견을 위한 AI 도구
  설치: https://github.com/mims-harvard/ToolUniverse/releases 에서 `tooluniverse.mcpb` 다운로드

이 서버들은 바이너리 파일 다운로드가 필요하며 선택 사항입니다.

## 5단계: 도움 요청

연구자가 오늘 무엇을 하고 있는지 물어봅니다. 일반적인 워크플로우를 기반으로 시작점을 제안합니다:

1. **문헌 검토** — "~~literature database에서 [주제]에 관한 최근 논문 검색"
2. **시퀀싱 데이터 분석** — "단일세포 데이터에 대한 QC 실행" 또는 "RNA-seq 파이프라인 설정"
3. **신약 개발** — "~~chemical database에서 [단백질]을 표적으로 하는 화합물 검색" 또는 "[질환]의 약물 표적 찾기"
4. **데이터 표준화** — "기기 데이터를 Allotrope 형식으로 변환"
5. **연구 전략** — "새로운 프로젝트 아이디어 평가 도움"

사용자의 응답을 기다리고 적절한 도구와 스킬로 안내합니다.
