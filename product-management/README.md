# 제품 관리 플러그인

Anthropic의 에이전트 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 주로 설계된 제품 관리 플러그인입니다 — Claude Code에서도 작동합니다. 기능 스펙 작성, 로드맵 관리, 이해관계자 커뮤니케이션, 사용자 리서치 종합, 경쟁사 분석, 제품 지표 추적 등 전체 PM 워크플로를 다룹니다.

## 설치

```
claude plugins add knowledge-work-plugins/product-management
```

## 기능

이 플러그인은 다음을 도울 수 있는 AI 기반 제품 관리 파트너를 제공합니다:

- **기능 스펙 & PRD** — 문제 설명이나 기능 아이디어로부터 구조화된 제품 요구사항 문서를 생성합니다. 사용자 스토리, 요구사항 우선순위 지정, 성공 지표, 범위 관리를 포함합니다.
- **로드맵 계획** — 제품 로드맵을 생성, 업데이트 및 재우선순위화합니다. 의존성 매핑과 함께 Now/Next/Later, 분기별 테마, OKR 정렬 형식을 지원합니다.
- **이해관계자 업데이트** — 대상 청중(경영진, 엔지니어링, 고객)에 맞춘 상태 업데이트를 생성합니다. 연결된 도구에서 컨텍스트를 가져와 주간 업데이트 작업을 절약합니다.
- **사용자 리서치 종합** — 인터뷰 노트, 설문 데이터, 지원 티켓을 구조화된 인사이트로 변환합니다. 테마를 식별하고, 페르소나를 구축하며, 근거와 함께 기회 영역을 도출합니다.
- **경쟁사 분석** — 경쟁사를 조사하고 기능 비교, 포지셔닝 분석 및 전략적 시사점이 포함된 브리프를 생성합니다.
- **지표 검토** — 제품 지표를 분석하고, 트렌드를 파악하며, 목표와 비교하고, 실행 가능한 인사이트를 도출합니다.
- **제품 브레인스토밍** — 문제 공간을 탐색하고, 아이디어를 생성하며, 날카로운 토론 파트너와 함께 제품 아이디어를 검증합니다. How Might We, Jobs-to-be-Done, First Principles, Opportunity Solution Trees와 같은 프레임워크를 사용하여 발산적 아이디어 도출, 가정 검증, 전략 탐색을 지원합니다.

## 명령어

| 명령어 | 기능 |
|---|---|
| `/write-spec` | 문제 설명으로부터 기능 스펙 또는 PRD 작성 |
| `/roadmap-update` | 로드맵 업데이트, 생성 또는 재우선순위화 |
| `/stakeholder-update` | 이해관계자 업데이트 생성 (주간, 월간, 출시) |
| `/synthesize-research` | 인터뷰, 설문조사, 티켓의 사용자 리서치 종합 |
| `/competitive-brief` | 경쟁사 분석 브리프 작성 |
| `/metrics-review` | 제품 지표 검토 및 분석 |
| `/brainstorm` | 사고 파트너와 함께 제품 아이디어, 문제 공간 또는 전략적 질문 브레인스토밍 |

## 스킬

| 스킬 | 다루는 내용 |
|---|---|
| `feature-spec` | PRD 구조, 사용자 스토리, 요구사항 분류, 인수 기준 |
| `roadmap-management` | 우선순위화 프레임워크 (RICE, MoSCoW), 로드맵 형식, 의존성 매핑 |
| `stakeholder-comms` | 청중별 업데이트 템플릿, 리스크 커뮤니케이션, 의사결정 문서화 |
| `user-research-synthesis` | 테마 분석, 친화도 매핑, 페르소나 개발, 기회 규모 산정 |
| `competitive-analysis` | 기능 비교 매트릭스, 포지셔닝 분석, 승/패 분석 |
| `metrics-tracking` | 제품 지표 계층, 목표 설정 (OKRs), 대시보드 설계, 검토 주기 |
| `product-brainstorming` | 브레인스토밍 모드 (문제 탐색, 솔루션 아이디어 도출, 가정 검증, 전략), PM 프레임워크, 세션 구조, 사고 파트너 행동 방식 |

## 예시 워크플로

### PRD 작성

```
You: /write-spec
Claude: What feature or problem are you speccing out?
You: We need to add SSO support for enterprise customers
Claude: [Asks about target users, constraints, success metrics]
Claude: [Generates full PRD with problem statement, user stories, requirements, success metrics, open questions]
```

### 이해관계자 업데이트 준비

```
You: /stakeholder-update
Claude: What type of update? (weekly, monthly, launch, ad-hoc)
You: Weekly update for the exec team
Claude: [Pulls context from project management tool, chat, and docs]
Claude: [Generates executive summary with progress, decisions, risks, and next milestones]
```

### 사용자 리서치 종합

```
You: /synthesize-research
Claude: What research do you want to synthesize? You can paste interview notes, upload files, or I can pull from connected sources.
You: [Pastes 8 interview transcripts]
Claude: [Identifies themes, patterns, and insights across interviews]
Claude: [Generates synthesis with key findings, personas, opportunity areas, and evidence]
```

### 제품 아이디어 브레인스토밍

```
You: /brainstorm Should we add AI-powered search to our product?
Claude: Before we jump to AI search — what problem are your users hitting with search today?
You: They can't find things. Support tickets about "can't find X" are our #2 category.
Claude: That's a discovery problem, not necessarily a search technology problem. Let me push on this...
Claude: [Explores whether the issue is search quality, information architecture, or content discoverability]
Claude: [Generates 5 distinct approaches ranging from better taxonomy to AI search to guided navigation]
Claude: [Challenges assumptions, suggests cheapest experiment to test the riskiest one]
```

### 경쟁사 분석

```
You: /competitive-brief
Claude: Which competitor(s) or feature area do you want to analyze?
You: Compare our onboarding flow to [competitor A] and [competitor B]
Claude: [Researches competitor onboarding approaches]
Claude: [Generates brief with feature comparison, strengths/weaknesses, and strategic implications]
```

## 데이터 소스

> 익숙하지 않은 자리 표시자가 보이거나 어떤 도구가 연결되어 있는지 확인이 필요한 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

최상의 경험을 위해 프로젝트 관리 및 커뮤니케이션 도구를 연결하세요. 연결되지 않은 경우 컨텍스트를 직접 제공하세요.

**포함된 MCP 연결:**
- 채팅 (Slack) — 팀 컨텍스트 및 이해관계자 스레드
- 프로젝트 트래커 (Linear, Asana, monday.com, ClickUp, Atlassian) — 로드맵 통합, 티켓 컨텍스트, 상태 추적
- 지식 베이스 (Notion) — 기존 스펙, 리서치, 미팅 노트
- 디자인 (Figma) — 디자인 컨텍스트 및 핸드오프
- 제품 분석 (Amplitude, Pendo) — 사용 데이터, 지표, 행동 분석
- 사용자 피드백 (Intercom) — 지원 티켓, 기능 요청, 사용자 대화
- 미팅 전사 (Fireflies) — 미팅 노트 및 토론 컨텍스트

**추가 옵션:**
- 각 카테고리의 대체 도구는 [CONNECTORS.md](CONNECTORS.md)를 참조하세요
