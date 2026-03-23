# 운영 플러그인

[Cowork](https://claude.com/product/cowork)를 위해 주로 설계된 비즈니스 운영 플러그인입니다. Anthropic의 에이전틱 데스크톱 앱이지만 Claude Code에서도 작동합니다. 벤더 관리, 프로세스 문서화, 변경 관리, 용량 계획, 컴플라이언스 추적, 리소스 계획을 돕습니다. 어떤 운영 팀에도 맞으며, 입력만으로도 동작하고 ITSM, 프로젝트 추적기, 기타 도구를 연결하면 더 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/operations
```

## 명령

슬래시 명령으로 직접 실행하는 워크플로입니다.

| 명령 | 설명 |
|---|---|
| `/vendor-review` | 벤더를 평가합니다 - 비용 분석, 리스크 평가, 계약 요약, 갱신 권고 |
| `/process-doc` | 비즈니스 프로세스를 문서화합니다 - 플로우차트, RACI 매트릭스, SOP, runbook |
| `/change-request` | 변경 관리 요청을 만듭니다 - 영향 분석, 롤백 계획, 승인 라우팅 |
| `/capacity-plan` | 리소스 용량을 계획합니다 - 업무량 분석, 인원 모델링, 활용도 예측 |
| `/status-report` | 상태 보고서를 생성합니다 - 프로젝트 업데이트, KPI, 리스크, 리더십용 실행 항목 |
| `/runbook` | 운영 runbook을 만들거나 업데이트합니다 - 반복 작업을 위한 단계별 절차 |

모든 명령은 **독립적으로** 동작하며(맥락과 세부 정보를 제공하면 됨), MCP 커넥터를 연결하면 **더 강력해집니다**.

## 스킬

관련성이 있을 때 Claude가 자동으로 활용하는 도메인 지식입니다.

| 스킬 | 설명 |
|---|---|
| `vendor-management` | 벤더 관계를 평가, 비교, 관리합니다 - 계약, 성과, 리스크 |
| `process-optimization` | 비즈니스 프로세스를 분석하고 개선합니다 - 병목 식별, 낭비 감소, 워크플로 간소화 |
| `change-management` | 조직적 또는 기술적 변경을 계획하고 실행합니다 - 커뮤니케이션, 교육, 도입 |
| `risk-assessment` | 운영 리스크를 식별, 평가, 완화합니다 - 리스크 등록부, 영향 분석, 통제 |
| `compliance-tracking` | 컴플라이언스 요구사항을 추적합니다 - 감사, 인증, 규제 마감일, 정책 준수 |
| `resource-planning` | 리소스 배분을 계획하고 최적화합니다 - 용량, 활용도, 예측, 예산 |

## 예시 워크플로

### 벤더 평가

```
/vendor-review
```

벤더 이름, 계약 세부 정보, 또는 제안서를 업로드하세요. 비용 분석, 리스크 표시, 권고가 포함된 구조화된 평가를 받을 수 있습니다.

### 프로세스 문서화

```
/process-doc employee offboarding
```

프로세스를 설명하거나 처음부터 끝까지 안내해 주세요. 플로우차트, RACI 매트릭스, 단계별 절차가 포함된 완전한 SOP를 제공합니다.

### 변경 요청 제출

```
/change-request
```

변경 사항을 설명하세요. 승인용으로 준비된 영향 분석, 리스크 평가, 롤백 계획, 커뮤니케이션 템플릿을 받을 수 있습니다.

### 용량 계획

```
/capacity-plan
```

팀 데이터를 업로드하거나 리소스를 설명하세요. 활용도 분석, 병목 식별, 인원 권고를 제공합니다.

### 리더십 상태 보고서

```
/status-report
```

연결된 도구에서 업데이트를 가져오거나 입력을 요청해, KPI, 리스크, 다음 단계가 포함된 세련된 상태 보고서를 생성합니다.

### Runbook 만들기

```
/runbook monthly close process
```

프로세스를 한 번만 안내해 주세요. 체크리스트, 문제 해결, 에스컬레이션 경로가 포함된 반복 가능한 runbook으로 문서화합니다.

## 독립 실행 + 강화 모드

모든 명령과 스킬은 어떤 연동 없이도 작동합니다.

| 할 수 있는 일 | 독립 실행 | 연결 시 더 강력해지는 대상 |
|-----------------|------------|-------------------|
| 벤더 검토 | 세부 정보 제공, 제안서 업로드 | Procurement, Knowledge base |
| 프로세스 문서화 | 프로세스 설명 | Knowledge base(기존 문서) |
| 변경 요청 | 변경 사항 설명 | ITSM, Project tracker |
| 용량 계획 | 데이터 업로드, 팀 설명 | Project tracker(업무량 데이터) |
| 상태 보고서 | 수동으로 업데이트 제공 | Project tracker, Chat, Calendar |
| Runbook | 프로세스 안내 | Knowledge base, ITSM |

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

도구를 연결하면 더 풍부한 경험을 얻을 수 있습니다.

| 범주 | 예시 | 가능해지는 일 |
|---|---|---|
| **ITSM** | ServiceNow, Zendesk | 티켓 관리, 변경 요청, 인시던트 추적 |
| **Project tracker** | Asana, Jira, monday.com | 프로젝트 상태, 리소스 배분, 작업 추적 |
| **Knowledge base** | Notion, Confluence | 프로세스 문서, runbook, 정책 |
| **Chat** | Slack, Teams | 팀 조율, 승인, 상태 업데이트 |
| **Calendar** | Google Calendar, Microsoft 365 | 회의 일정 조율, 마감일 추적 |
| **Email** | Gmail, Microsoft 365 | 벤더 커뮤니케이션, 승인 |

지원되는 전체 통합 목록은 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

## 설정

개인화를 위해 `operations/.claude/settings.local.json`에 로컬 설정 파일을 만드세요.

```json
{
  "company": "귀사",
  "team": "운영",
  "reportingCadence": "weekly",
  "approvalChain": ["Manager", "Director", "VP"],
  "complianceFrameworks": ["SOC 2", "ISO 27001"],
  "fiscalYearStart": "January"
}
```

이 정보가 설정되어 있지 않으면 플러그인이 대화형으로 물어봅니다.
