# Engineering Plugin

주로 Anthropic의 에이전트형 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 소프트웨어 엔지니어링 플러그인입니다 — Claude Code에서도 동작합니다. 스탠드업, 코드 리뷰, 아키텍처 결정, 인시던트 대응, 디버깅, 기술 문서화를 지원합니다. 모든 엔지니어링 팀에서 사용 가능하며 — 입력만으로도 단독 사용이 가능하고, source control, project tracker, monitoring 도구를 연결하면 더욱 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/engineering
```

## 명령어

슬래시 명령어로 호출하는 명시적 워크플로우:

| 명령어 | 설명 |
|---|---|
| `/standup` | 최근 활동(커밋, PR, 티켓, 채팅)에서 스탠드업 업데이트 생성 |
| `/review` | 코드 변경 사항 리뷰 — 보안, 성능, 스타일, 정확성 |
| `/debug` | 구조화된 디버깅 세션 — 재현, 격리, 진단, 수정 |
| `/architecture` | 아키텍처 결정 생성 또는 평가 — 트레이드오프 분석을 포함한 ADR 형식 |
| `/incident` | 인시던트 대응 워크플로우 실행 — 분류, 소통, 완화, 사후 분석 작성 |
| `/deploy-checklist` | 배포 전 체크리스트 — 테스트 확인, 변경 사항 검토, 의존성 확인, 롤백 계획 확인 |

모든 명령어는 **단독으로** 동작하며(코드 붙여넣기, 시스템 설명, 파일 업로드), MCP 커넥터를 연결하면 **한층 강화**됩니다.

## Skills

관련성이 있을 때 Claude가 자동으로 사용하는 도메인 지식:

| Skill | 설명 |
|---|---|
| `code-review` | 버그, 보안 문제, 성능, 유지보수성 관점에서 코드 리뷰 |
| `incident-response` | 프로덕션 인시던트 분류 및 관리 — 상태 업데이트, runbook, 사후 분석 |
| `system-design` | 시스템 및 서비스 설계 — 아키텍처 다이어그램, API 설계, 데이터 모델링 |
| `tech-debt` | 기술 부채 식별, 분류, 우선순위 지정 — 개선 계획 수립 |
| `testing-strategy` | 테스트 전략 설계 — 단위, 통합, e2e 커버리지, 테스트 계획 작성 |
| `documentation` | 기술 문서 작성 및 유지 — README, API 문서, runbook, 온보딩 가이드 |

## 예시 워크플로우

### 아침 스탠드업

```
/standup
```

도구가 연결되어 있으면 최근 커밋, PR 활동, 티켓 업데이트를 가져옵니다. 연결되지 않은 경우 작업한 내용을 알려주면 형식에 맞게 정리해 드립니다.

### 코드 리뷰

```
/review https://github.com/org/repo/pull/123
```

PR 링크를 공유하거나, diff를 붙여넣거나, 파일을 지정하세요. 보안, 성능, 정확성, 스타일을 다루는 구조화된 리뷰를 받아보세요.

### 이슈 디버깅

```
/debug Users are getting 500 errors on the checkout page
```

구조화된 디버깅 프로세스를 통해 진행합니다: 재현, 격리, 진단, 수정. 체계적으로 생각할 수 있도록 도와드립니다.

### 아키텍처 결정

```
/architecture Should we use a message queue or direct API calls between services?
```

옵션 분석, 트레이드오프, 권장 사항이 포함된 구조화된 ADR을 받아보세요.

### 인시던트 대응

```
/incident The payments service is returning 503s
```

인시던트 워크플로우 시작: 심각도 분류, 소통 초안 작성, 타임라인 추적, 해결 후 사후 분석 생성.

### 배포 전 확인

```
/deploy-checklist auth-service v2.3.0
```

서비스와 변경 사항을 기반으로 맞춤화된 배포 체크리스트를 받아보세요.

## 단독 사용 + 강화 사용

모든 명령어와 skill은 통합 없이도 동작합니다:

| 할 수 있는 것 | 단독 사용 | 강화 사용 (연결 도구) |
|-----------------|------------|-------------------|
| 스탠드업 업데이트 | 작업 내용 설명 | Source control, Project tracker, Chat |
| 코드 리뷰 | diff 또는 코드 붙여넣기 | Source control (PR 자동 가져오기) |
| 디버깅 세션 | 문제 설명 | Monitoring (로그 및 메트릭 가져오기) |
| 아키텍처 결정 | 시스템 설명 | Knowledge base (이전 ADR 검색) |
| 인시던트 대응 | 인시던트 설명 | Monitoring, Incident management, Chat |
| 배포 체크리스트 | 배포 내용 설명 | CI/CD, Source control |

## MCP 통합

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

더 풍부한 경험을 위해 도구를 연결하세요:

| 카테고리 | 예시 | 활성화되는 기능 |
|---|---|---|
| **Source control** | GitHub, GitLab | PR diff, 커밋 히스토리, 브랜치 상태 |
| **Project tracker** | Linear, Jira, Asana | 티켓 상태, 스프린트 데이터, 담당자 |
| **Monitoring** | Datadog, New Relic | 로그, 메트릭, 알림, 대시보드 |
| **Incident management** | PagerDuty, Opsgenie | 온콜 일정, 인시던트 추적, 페이징 |
| **Chat** | Slack, Teams | 팀 토론, 스탠드업 채널 |
| **Knowledge base** | Notion, Confluence | ADR, runbook, 온보딩 문서 |

지원되는 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

## 설정

개인화를 위해 `engineering/.claude/settings.local.json`에 로컬 설정 파일을 만드세요:

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

설정이 구성되지 않은 경우 플러그인이 이 정보를 대화형으로 요청합니다.
