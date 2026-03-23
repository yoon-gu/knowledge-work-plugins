# Engineering Plugin

[Cowork](https://claude.com/product/cowork), Anthropic의 에이전트형 데스크톱 애플리케이션을 위해 주로 설계된 소프트웨어 엔지니어링 플러그인입니다. Claude Code에서도 동작합니다. 스탠드업, 코드 리뷰, 아키텍처 결정, 인시던트 대응, 디버깅, 기술 문서를 돕습니다. 어떤 엔지니어링 팀과도 잘 맞으며, 입력만으로도 동작하고 소스 제어, 프로젝트 추적기, 모니터링 도구를 연결하면 더 강력해집니다.

## Installation

```bash
claude plugins add knowledge-work-plugins/engineering
```

## Commands

슬래시 명령으로 호출하는 명시적 워크플로입니다:

| Command | Description |
|---|---|
| `/standup` | 최근 활동(커밋, PR, 티켓, 채팅)을 바탕으로 스탠드업 업데이트 생성 |
| `/review` | 코드 변경 검토 - 보안, 성능, 스타일, 정확성 |
| `/debug` | 구조화된 디버깅 세션 - 재현, 분리, 진단, 수정 |
| `/architecture` | 아키텍처 결정 생성 또는 평가 - 트레이드오프 분석이 포함된 ADR 형식 |
| `/incident` | 인시던트 대응 워크플로 실행 - 트리아지, 커뮤니케이션, 완화, 포스트모템 작성 |
| `/deploy-checklist` | 배포 전 체크리스트 - 테스트 확인, 변경 사항 검토, 의존성 점검, 롤백 계획 확인 |

모든 명령은 **독립 실행형**으로도 동작하며(코드 붙여넣기, 시스템 설명, 파일 업로드), MCP 커넥터를 연결하면 **기능이 강화**됩니다.

## Skills

Claude가 적절할 때 자동으로 사용하는 도메인 지식입니다:

| Skill | Description |
|---|---|
| `code-review` | 버그, 보안 이슈, 성능, 유지보수성을 기준으로 코드 검토 |
| `incident-response` | 프로덕션 인시던트 트리아지 및 관리 - 상태 업데이트, 런북, 포스트모템 |
| `system-design` | 시스템과 서비스 설계 - 아키텍처 다이어그램, API 설계, 데이터 모델링 |
| `tech-debt` | 기술 부채 식별, 분류, 우선순위화 - 개선 계획 수립 |
| `testing-strategy` | 테스트 전략 설계 - 단위, 통합, e2e 커버리지, 테스트 계획 작성 |
| `documentation` | 기술 문서 작성 및 유지 - README, API 문서, 런북, 온보딩 가이드 |

## 예시 워크플로

### Morning Standup

```
/standup
```

도구가 연결되어 있으면 최근 커밋, PR 활동, 티켓 업데이트를 가져옵니다. 그렇지 않으면 무엇을 했는지 알려 주세요. 제가 형식에 맞게 정리하겠습니다.

### Code Review

```
/review https://github.com/org/repo/pull/123
```

PR 링크를 공유하거나 diff를 붙여넣거나 파일을 가리키세요. 보안, 성능, 정확성, 스타일을 포함한 구조화된 리뷰를 받을 수 있습니다.

### Debugging an Issue

```
/debug Users are getting 500 errors on the checkout page
```

재현, 분리, 진단, 수정을 거치는 구조화된 디버깅 과정을 함께 진행합니다. 체계적으로 사고할 수 있도록 도와드리겠습니다.

### Architecture Decision

```
/architecture Should we use a message queue or direct API calls between services?
```

옵션 분석, 트레이드오프, 추천 사항이 포함된 구조화된 ADR을 얻을 수 있습니다.

### Incident Response

```
/incident The payments service is returning 503s
```

인시던트 워크플로를 시작합니다. 심각도 트리아지, 커뮤니케이션 초안 작성, 타임라인 추적, 해결 후 포스트모템 생성을 진행합니다.

### Pre-Deploy Check

```
/deploy-checklist auth-service v2.3.0
```

서비스와 변경 내용을 바탕으로 맞춤형 배포 체크리스트를 받을 수 있습니다.

## 독립 실행형 + 강화 기능

Every command and skill works without any integrations:

| 할 수 있는 일 | 독립 실행형 | 연결 시 강화되는 도구 |
|-----------------|------------|-------------------|
| 스탠드업 업데이트 | 작업 내용을 설명 | 소스 제어, 프로젝트 추적기, 채팅 |
| 코드 리뷰 | diff나 코드를 붙여넣기 | 소스 제어(PR 자동 가져오기) |
| 디버깅 세션 | 문제를 설명 | 모니터링(로그와 지표 가져오기) |
| 아키텍처 결정 | 시스템을 설명 | 지식 베이스(이전 ADR 찾기) |
| 인시던트 대응 | 인시던트를 설명 | 모니터링, 인시던트 관리, 채팅 |
| 배포 체크리스트 | 배포 내용을 설명 | CI/CD, 소스 제어 |

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

더 풍부한 경험을 위해 도구를 연결하세요:

| Category | Examples | What It Enables |
|---|---|---|
| **소스 제어** | GitHub, GitLab | PR diff, 커밋 기록, 브랜치 상태 |
| **프로젝트 추적기** | Linear, Jira, Asana | 티켓 상태, 스프린트 데이터, 할당 |
| **모니터링** | Datadog, New Relic | 로그, 지표, 알림, 대시보드 |
| **인시던트 관리** | PagerDuty, Opsgenie | 온콜 일정, 인시던트 추적, 페이징 |
| **채팅** | Slack, Teams | 팀 토론, 스탠드업 채널 |
| **지식 베이스** | Notion, Confluence | ADR, 런북, 온보딩 문서 |

[CONNECTORS.md](CONNECTORS.md)에서 지원되는 통합의 전체 목록을 확인하세요.

## Settings

개인화하려면 `engineering/.claude/settings.local.json`에 로컬 설정 파일을 만드세요:

```json
{
  "name": "Your Name",
  "title": "Software Engineer",
  "team": "Your Team",
  "company": "Your Company",
  "techStack": ["Python", "TypeScript", "PostgreSQL", "AWS"],
  "defaultBranch": "main",
  "deployProcess": "canary"
}
```

설정되어 있지 않으면 플러그인이 이 정보를 대화형으로 물어봅니다.
