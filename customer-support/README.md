# 고객 지원 플러그인

주로 Anthropic의 에이전트 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)용으로 설계된 고객 지원 플러그인입니다. 단, Claude Code에서도 작동합니다. 지원 팀을 위한 티켓 분류, 에스컬레이션 관리, 응답 초안 작성, 고객 조사 및 지식 기반 작성 기능을 제공합니다.

## 설치

```
claude plugins add knowledge-work-plugins/customer-support
```

## 그것이 하는 일

이 플러그인은 Claude를 고객 지원 부조종사로 바꿔줍니다. 도움이 됩니다:

- **수신 티켓 분류** 구조화된 분류, 우선순위 평가, 라우팅 권장사항을 통해
- 신뢰도 점수를 통해 여러 소스의 정보를 종합하여 **고객 질문 조사**
- **상황, 긴급성, 커뮤니케이션 채널에 맞춰 전문적인 답변 초안** 작성
- 엔지니어링 또는 제품에 대한 전체 컨텍스트, 재현 단계, 비즈니스 영향을 포함하는 **패키지 에스컬레이션**
- 향후 티켓 양을 줄이기 위해 해결된 문제에 대한 **KB 문서 작성**

## 명령

| 명령 | 설명 |
|---|---|
| `/triage` | 지원 티켓 또는 고객 문제를 분류하고, 우선순위를 지정하고 전달합니다. |
| `/research` | 고객 질문 또는 주제에 대한 다중 소스 연구 |
| `/draft-response` | 어떤 상황에도 고객 대응 초안 작성 |
| `/escalate` | 엔지니어링, 제품 또는 리더십에 대한 에스컬레이션 패키지 |
| `/kb-article` | 해결된 문제에서 기술 자료 문서 초안 작성 |

## 기술

| 기능 | 설명 |
|---|---|
| `ticket-triage` | 카테고리 분류, 우선순위 프레임워크(P1-P4), 라우팅 규칙, 중복 감지 |
| `customer-research` | 다중 소스 연구 방법론, 소스 우선 순위 지정, 답변 종합 |
| `response-drafting` | 커뮤니케이션 모범 사례, 어조 지침, 일반 시나리오용 템플릿 |
| `escalation` | 에스컬레이션 계층, 구조화된 에스컬레이션 형식, 영향 평가, 후속 조치 흐름 |
| `knowledge-management` | 기사 구조 표준, 검색 가능성을 위한 작성, 검토 흐름, 유지 관리 |

## 데이터 소스

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)을 참조하세요.

최고의 경험을 위해 지원 플랫폼, 지식 기반, 커뮤니케이션 도구를 연결하세요. 이러한 정보가 없으면 고객 상황을 수동으로 제공하세요.

**포함된 MCP 연결:**
- 내부 토론 및 고객 채널 컨텍스트를 위한 채팅(Slack)
- 티켓 내역 및 고객 대화 지원 플랫폼(인터콤)
- 계정 세부정보 및 연락처 정보를 위한 CRM(HubSpot)
- 내부 문서 및 Runbook을 위한 기술 자료(Guru, Notion)
- 버그 보고서 및 기능 요청을 위한 프로젝트 트래커(Atlassian)
- 고객 서신을 위한 이메일 및 클라우드 저장소(Microsoft 365)

**추가 옵션:**
- 각 카테고리의 대체 도구는 [CONNECTORS.md](CONNECTORS.md)을 참조하세요.

## 예시 워크플로

### 들어오는 티켓 분류

```
You: /triage Customer says their dashboard has been showing a blank
     page since this morning — they're on the Enterprise plan

Claude: Analyzing the issue...

## Triage: Dashboard blank page — Enterprise customer

**Category:** Bug
**Priority:** P2 — High (core feature broken, enterprise customer)
**Product area:** Dashboard / Frontend

### Routing Recommendation
Route to: Tier 2 Support (investigate browser/account specifics,
then escalate to Engineering if reproducible)

### Suggested Initial Response
[Draft acknowledging the issue, asking clarifying questions
about browser and any recent changes, offering status page link]
```

### 고객 질문 조사

```
You: /research Does our platform support SSO with Okta?

Claude: Let me check across available sources...

[Searches docs, knowledge base, previous conversations,
 and web sources — synthesizes answer with confidence
 level and source attribution]
```

### 에스컬레이션 패키징

```
You: /escalate API returning 500 errors intermittently — 3
     Enterprise customers reported this week

Claude: I'll gather context and build the escalation brief...

[Pulls ticket history, identifies affected accounts,
 structures reproduction steps, assesses business impact,
 and generates a structured escalation for engineering]
```

### 응답 초안 작성

```
You: /draft-response Customer escalation — their integration
     has been down for 2 days and they're frustrated

Claude: [Generates empathetic, professional response acknowledging
 the frustration, taking ownership, providing a clear action
 plan with timeline, and offering a call]
```

### KB 기사 작성

```
You: /kb-article How to configure webhook notifications —
     just resolved this for the third customer this month

Claude: [Generates a structured how-to article with prerequisites,
 step-by-step instructions, verification steps, and common
 issues — optimized for search]
```

## 구성

플러그인은 포함된 MCP 연결을 사용하여 즉시 작동합니다. 가장 풍부한 경험을 위해 Claude 설정을 통해 추가 데이터 소스를 연결하세요.

1. **지원 플랫폼**: 티켓 내역 및 고객 상황에 대한 티켓팅 시스템을 추가하세요.
2. **기술 기반**: 내부 문서 및 기존 KB 기사에 대한 위키 추가
3. **프로젝트 트래커**: 버그 보고서 및 기능 요청을 위한 이슈 트래커를 추가하세요.
4. **CRM**: 계정 세부정보 및 연락처 정보를 보려면 CRM을 추가하세요.

이러한 연결이 없으면 플러그인은 컨텍스트를 수동으로 제공하고 사용자가 자신의 데이터로 채울 수 있는 프레임워크와 템플릿을 제공하도록 요청합니다.
