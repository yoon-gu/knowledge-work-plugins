# Operations Plugin

주로 Anthropic의 에이전트 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 비즈니스 운영 플러그인으로, Claude Code에서도 동작합니다. 벤더 관리, 프로세스 문서화, 변경 관리, 역량 계획, 컴플라이언스 추적, 리소스 계획을 지원합니다. 모든 운영 팀에서 사용 가능하며 — 입력만으로도 단독으로 작동하고, ITSM, 프로젝트 트래커 및 기타 도구를 연결하면 더욱 강력하게 활용할 수 있습니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/operations
```

## 명령어

슬래시 명령어로 호출하는 명시적 워크플로우:

| 명령어 | 설명 |
|---|---|
| `/vendor-review` | 벤더 평가 — 비용 분석, 리스크 평가, 계약 요약, 갱신 권고 |
| `/process-doc` | 비즈니스 프로세스 문서화 — 플로우차트, RACI 매트릭스, SOP, 런북 |
| `/change-request` | 변경 관리 요청 생성 — 영향 분석, 롤백 계획, 승인 라우팅 |
| `/capacity-plan` | 리소스 역량 계획 — 워크로드 분석, 인원 모델링, 활용률 예측 |
| `/status-report` | 상태 보고서 생성 — 프로젝트 업데이트, KPI, 리스크, 리더십을 위한 액션 아이템 |
| `/runbook` | 운영 런북 생성 또는 업데이트 — 반복 작업을 위한 단계별 절차 |

모든 명령어는 **단독으로** 작동하며(컨텍스트와 세부 정보 제공) MCP 커넥터 연결 시 **더욱 강력해집니다**.

## Skills

관련 상황에서 Claude가 자동으로 활용하는 도메인 지식:

| Skill | 설명 |
|---|---|
| `vendor-management` | 벤더 관계 평가, 비교, 관리 — 계약, 성과, 리스크 |
| `process-optimization` | 비즈니스 프로세스 분석 및 개선 — 병목 식별, 낭비 제거, 워크플로우 간소화 |
| `change-management` | 조직적 또는 기술적 변경 계획 및 실행 — 커뮤니케이션, 교육, 도입 |
| `risk-assessment` | 운영 리스크 식별, 평가, 완화 — 리스크 레지스터, 영향 분석, 통제 |
| `compliance-tracking` | 컴플라이언스 요건 추적 — 감사, 인증, 규제 기한, 정책 준수 |
| `resource-planning` | 리소스 배분 계획 및 최적화 — 역량, 활용률, 예측, 예산 |

## 예시 워크플로우

### 벤더 평가

```
/vendor-review
```

벤더 이름, 계약 세부 정보를 제공하거나 제안서를 업로드하세요. 비용 분석, 리스크 플래그, 권고사항이 포함된 구조화된 평가를 받을 수 있습니다.

### 프로세스 문서화

```
/process-doc employee offboarding
```

프로세스를 설명하거나 단계별로 안내해 주세요. 플로우차트, RACI 매트릭스, 단계별 절차가 포함된 완전한 SOP를 생성합니다.

### 변경 요청 제출

```
/change-request
```

변경 사항을 설명하세요. 승인을 위한 영향 분석, 리스크 평가, 롤백 계획, 커뮤니케이션 템플릿을 받을 수 있습니다.

### 역량 계획

```
/capacity-plan
```

팀 데이터를 업로드하거나 리소스를 설명하세요. 활용률 분석, 병목 식별, 인원 권고사항을 받을 수 있습니다.

### 리더십 상태 보고서

```
/status-report
```

연결된 도구에서 업데이트를 가져오거나(또는 직접 입력받아) KPI, 리스크, 다음 단계가 포함된 완성도 높은 상태 보고서를 생성합니다.

### 런북 생성

```
/runbook monthly close process
```

프로세스를 한 번 안내해 주세요. 체크리스트, 문제 해결 방법, 에스컬레이션 경로가 포함된 반복 가능한 런북으로 문서화합니다.

## 단독 사용 + 강화된 사용

모든 명령어와 skill은 통합 없이도 작동합니다:

| 기능 | 단독 사용 | 강화 도구 |
|-----------------|------------|-------------------|
| 벤더 리뷰 | 세부 정보 제공, 제안서 업로드 | Procurement, Knowledge base |
| 프로세스 문서화 | 프로세스 설명 | Knowledge base (기존 문서) |
| 변경 요청 | 변경 사항 설명 | ITSM, Project tracker |
| 역량 계획 | 데이터 업로드, 팀 설명 | Project tracker (워크로드 데이터) |
| 상태 보고서 | 수동으로 업데이트 제공 | Project tracker, Chat, Calendar |
| 런북 | 프로세스 단계별 안내 | Knowledge base, ITSM |

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

더 풍부한 경험을 위해 도구를 연결하세요:

| 카테고리 | 예시 | 활성화 기능 |
|---|---|---|
| **ITSM** | ServiceNow, Zendesk | 티켓 관리, 변경 요청, 인시던트 추적 |
| **Project tracker** | Asana, Jira, monday.com | 프로젝트 상태, 리소스 배분, 작업 추적 |
| **Knowledge base** | Notion, Confluence | 프로세스 문서, 런북, 정책 |
| **Chat** | Slack, Teams | 팀 조율, 승인, 상태 업데이트 |
| **Calendar** | Google Calendar, Microsoft 365 | 회의 일정, 마감일 추적 |
| **Email** | Gmail, Microsoft 365 | 벤더 커뮤니케이션, 승인 |

지원되는 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

## 설정

개인화를 위해 `operations/.claude/settings.local.json`에 로컬 설정 파일을 생성하세요:

```json
{
  "company": "Your Company",
  "team": "Operations",
  "reportingCadence": "weekly",
  "approvalChain": ["Manager", "Director", "VP"],
  "complianceFrameworks": ["SOC 2", "ISO 27001"],
  "fiscalYearStart": "January"
}
```

설정이 구성되어 있지 않으면 플러그인이 대화형으로 이 정보를 요청합니다.
