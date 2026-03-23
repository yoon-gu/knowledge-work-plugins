# Customer Support Plugin

주로 Anthropic의 에이전틱 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 고객 지원 플러그인입니다 — Claude Code에서도 작동합니다. 지원 팀을 위한 티켓 트리아지, 에스컬레이션 관리, 응답 초안 작성, 고객 조사, 그리고 지식 베이스 작성 기능을 제공합니다.

## 설치

```
claude plugins add knowledge-work-plugins/customer-support
```

## 기능

이 플러그인은 Claude를 고객 지원 코파일럿으로 전환합니다. 다음 작업을 도와줍니다:

- **수신 티켓 트리아지**: 구조화된 분류, 우선순위 평가, 라우팅 권장 사항
- **고객 문의 조사**: 신뢰도 점수와 함께 여러 출처의 정보를 종합
- **전문적인 응답 초안 작성**: 상황, 긴급성, 커뮤니케이션 채널에 맞게 조정
- **에스컬레이션 패키징**: 엔지니어링 또는 제품팀을 위한 전체 컨텍스트, 재현 단계, 비즈니스 영향 포함
- **KB 문서 작성**: 해결된 이슈로부터 미래 티켓 볼륨을 줄이기 위한 문서 작성

## 명령어

| 명령어 | 설명 |
|---|---|
| `/triage` | 지원 티켓 또는 고객 이슈를 분류, 우선순위 지정, 라우팅 |
| `/research` | 고객 문의 또는 주제에 대한 다중 소스 조사 |
| `/draft-response` | 모든 상황에 대한 고객용 응답 초안 작성 |
| `/escalate` | 엔지니어링, 제품, 또는 리더십을 위한 에스컬레이션 패키징 |
| `/kb-article` | 해결된 이슈로부터 지식 베이스 문서 초안 작성 |

## 스킬

| 스킬 | 설명 |
|---|---|
| `ticket-triage` | 카테고리 분류 체계, 우선순위 프레임워크 (P1-P4), 라우팅 규칙, 중복 감지 |
| `customer-research` | 다중 소스 조사 방법론, 소스 우선순위, 답변 종합 |
| `response-drafting` | 커뮤니케이션 모범 사례, 톤 가이드라인, 일반적인 시나리오 템플릿 |
| `escalation` | 에스컬레이션 단계, 구조화된 에스컬레이션 형식, 영향 평가, 후속 조치 주기 |
| `knowledge-management` | 문서 구조 표준, 검색 가능성을 위한 작성, 검토 주기, 유지 관리 |

## 데이터 소스

> 낯선 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

최상의 경험을 위해 지원 플랫폼, 지식 베이스, 커뮤니케이션 도구를 연결하세요. 연결 없이는 고객 컨텍스트를 수동으로 제공해야 합니다.

**포함된 MCP 연결:**
- 채팅 (Slack) — 내부 토론 및 고객 채널 컨텍스트
- 지원 플랫폼 (Intercom) — 티켓 이력 및 고객 대화
- CRM (HubSpot) — 계정 세부 정보 및 연락처 정보
- 지식 베이스 (Guru, Notion) — 내부 문서 및 런북
- 프로젝트 트래커 (Atlassian) — 버그 리포트 및 기능 요청
- 이메일 및 클라우드 스토리지 (Microsoft 365) — 고객 서신

**추가 옵션:**
- 각 카테고리의 대안 도구는 [CONNECTORS.md](CONNECTORS.md)를 참조하세요

## 예시 워크플로우

### 수신 티켓 트리아지

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

### 고객 문의 조사

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

### KB 문서 작성

```
You: /kb-article How to configure webhook notifications —
     just resolved this for the third customer this month

Claude: [Generates a structured how-to article with prerequisites,
 step-by-step instructions, verification steps, and common
 issues — optimized for search]
```

## 구성

플러그인은 포함된 MCP 연결로 즉시 작동합니다. 가장 풍부한 경험을 위해 Claude 설정을 통해 추가 데이터 소스를 연결하세요:

1. **지원 플랫폼**: 티켓 이력 및 고객 컨텍스트를 위한 티켓팅 시스템 추가
2. **지식 베이스**: 내부 문서 및 기존 KB 문서를 위한 위키 추가
3. **프로젝트 트래커**: 버그 리포트 및 기능 요청을 위한 이슈 트래커 추가
4. **CRM**: 계정 세부 정보 및 연락처 정보를 위한 CRM 추가

이러한 연결 없이는 플러그인이 컨텍스트를 수동으로 제공하도록 요청하고, 직접 데이터를 채울 수 있는 프레임워크와 템플릿을 제공합니다.
