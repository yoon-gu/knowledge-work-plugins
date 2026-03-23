# 제품 관리 플러그인

[Cowork](https://claude.com/product/cowork)을 위해 주로 설계된 제품 관리 플러그인입니다. Anthropic의 에이전틱 데스크톱 애플리케이션을 위한 것이지만 Claude Code에서도 동작합니다. 기능 명세 작성, 로드맵 관리, 이해관계자 커뮤니케이션, 사용자 리서치 종합, 경쟁사 분석, 제품 지표 추적까지 PM 워크플로 전반을 다룹니다.

## 설치

```
claude plugins add knowledge-work-plugins/product-management
```

## 하는 일

이 플러그인은 다음 작업을 도와주는 AI 기반 제품 관리 파트너를 제공합니다.

- **Feature Specs & PRDs** - 문제 정의나 기능 아이디어로부터 구조화된 제품 요구사항 문서를 생성합니다. 사용자 스토리, 요구사항 우선순위, 성공 지표, 범위 관리가 포함됩니다.
- **Roadmap Planning** - 제품 로드맵을 생성, 업데이트, 재우선순위화합니다. Now/Next/Later, 분기별 주제, OKR 연계 형식과 의존성 맵핑을 지원합니다.
- **Stakeholder Updates** - 대상(임원, 엔지니어링, 고객)에 맞는 상태 업데이트를 만듭니다. 연결된 도구에서 맥락을 가져와 주간 업데이트 부담을 줄여 줍니다.
- **User Research Synthesis** - 인터뷰 메모, 설문 데이터, 지원 티켓을 구조화된 인사이트로 바꿉니다. 주제를 식별하고, 페르소나를 만들고, 근거와 함께 기회 영역을 드러냅니다.
- **Competitive Analysis** - 경쟁사를 조사하고 기능 비교, 포지셔닝 분석, 전략적 시사점이 담긴 브리핑을 생성합니다.
- **Metrics Review** - 제품 지표를 분석하고, 추세를 파악하고, 목표와 비교하고, 실행 가능한 인사이트를 도출합니다.
- **Product Brainstorming** - 날카로운 브레인스토밍 파트너와 함께 문제 영역을 탐색하고 아이디어를 생성하며 제품 사고를 검증합니다. How Might We, Jobs-to-be-Done, First Principles, Opportunity Solution Trees 같은 프레임워크를 활용해 발산적 아이데이션, 가정 검증, 전략 탐색을 지원합니다.

## 명령

| Command | What It Does |
|---|---|
| `/write-spec` | Write a feature spec or PRD from a problem statement |
| `/roadmap-update` | Update, create, or reprioritize your roadmap |
| `/stakeholder-update` | Generate a stakeholder update (weekly, monthly, launch) |
| `/synthesize-research` | Synthesize user research from interviews, surveys, and tickets |
| `/competitive-brief` | Create a competitive analysis brief |
| `/metrics-review` | Review and analyze product metrics |
| `/brainstorm` | Brainstorm a product idea, problem space, or strategic question with a thinking partner |

## 스킬

| Skill | What It Covers |
|---|---|
| `feature-spec` | PRD structure, user stories, requirements categorization, acceptance criteria |
| `roadmap-management` | Prioritization frameworks (RICE, MoSCoW), roadmap formats, dependency mapping |
| `stakeholder-comms` | Update templates by audience, risk communication, decision documentation |
| `user-research-synthesis` | Thematic analysis, affinity mapping, persona development, opportunity sizing |
| `competitive-analysis` | Feature comparison matrices, positioning analysis, win/loss analysis |
| `metrics-tracking` | Product metrics hierarchy, goal setting (OKRs), dashboard design, review cadences |
| `product-brainstorming` | Brainstorming modes (problem exploration, solution ideation, assumption testing, strategy), PM frameworks, session structure, thinking partner behaviors |

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

### 경쟁 분석

```
You: /competitive-brief
Claude: Which competitor(s) or feature area do you want to analyze?
You: Compare our onboarding flow to [competitor A] and [competitor B]
Claude: [Researches competitor onboarding approaches]
Claude: [Generates brief with feature comparison, strengths/weaknesses, and strategic implications]
```

## 데이터 소스

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

가장 좋은 경험을 위해 프로젝트 관리 및 커뮤니케이션 도구를 연결하세요. 연결이 없으면 맥락을 수동으로 제공해야 합니다.

**포함된 MCP 연결:**
- Chat (Slack) for team context and stakeholder threads
- Project tracker (Linear, Asana, monday.com, ClickUp, Atlassian) for roadmap integration, ticket context, and status tracking
- Knowledge base (Notion) for existing specs, research, and meeting notes
- Design (Figma) for design context and handoff
- Product analytics (Amplitude, Pendo) for usage data, metrics, and behavioral analysis
- User feedback (Intercom) for support tickets, feature requests, and user conversations
- Meeting transcription (Fireflies) for meeting notes and discussion context

**추가 옵션:**
- 각 범주의 대체 도구는 [CONNECTORS.md](CONNECTORS.md)를 참고하세요
