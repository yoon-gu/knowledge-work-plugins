# HR Plugin

주로 Anthropic의 에이전틱 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 인사 운영 플러그인으로, Claude Code에서도 작동합니다. 채용, 온보딩, 성과 관리, 정책 안내, 보상 분석을 지원합니다. 모든 HR 팀에서 사용할 수 있으며 — 입력 정보만으로도 단독 사용이 가능하고, HRIS, ATS 및 기타 도구를 연결하면 더욱 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/human-resources
```

## 명령어

슬래시 명령어로 실행하는 명시적 워크플로:

| 명령어 | 설명 |
|---|---|
| `/draft-offer` | 보상 세부 정보, 시작일, 조건을 포함한 오퍼 레터 초안 작성 |
| `/onboarding` | 신입 직원을 위한 온보딩 체크리스트 및 첫 주 계획 생성 |
| `/performance-review` | 성과 리뷰 구조화 — 자기 평가 프롬프트, 관리자 템플릿, 조정 준비 |
| `/policy-lookup` | 회사 정책 검색 및 설명 — 휴가, 복리후생, 비용, 출장, 원격 근무 |
| `/comp-analysis` | 보상 데이터 분석 — 벤치마킹, 밴드 배치, 주식 갱신 모델링 |
| `/people-report` | 헤드카운트, 이직률, 다양성 또는 조직 건강 보고서 생성 |

모든 명령어는 **단독으로** (문맥과 세부 정보 제공) 작동하며, MCP 커넥터 연결 시 **더욱 강력해집니다**.

## Skills

관련 상황에서 Claude가 자동으로 활용하는 도메인 지식:

| Skill | 설명 |
|---|---|
| `recruiting-pipeline` | 채용 파이프라인 추적 및 관리 — 소싱, 스크리닝, 인터뷰, 오퍼 단계 |
| `employee-handbook` | 회사 정책, 복리후생, 절차에 관한 질문 답변 |
| `compensation-benchmarking` | 시장 데이터 기준 보상 벤치마킹 — 기본급, 주식, 총 보상 |
| `org-planning` | 헤드카운트 계획, 조직 설계, 팀 구조 최적화 |
| `people-analytics` | 인력 데이터 분석 — 이직 추세, 참여 신호, 다양성 지표 |
| `interview-prep` | 구조화된 인터뷰 계획 생성 — 역량 기반 질문, 스코어카드, 디브리프 템플릿 |

## 예시 워크플로

### 오퍼 초안 작성

```
/draft-offer
```

역할, 레벨, 위치, 보상 세부 정보를 알려주세요. 조건, 주식 내역, 복리후생 요약이 포함된 완전한 오퍼 레터 초안을 받을 수 있습니다.

### 신입 직원 온보딩

```
/onboarding
```

신입 직원의 이름, 역할, 팀, 시작일을 입력하세요. 포괄적인 온보딩 체크리스트, 첫 주 캘린더, 도구 접근 목록, 버디 배정 템플릿을 받을 수 있습니다.

### 성과 리뷰 준비

```
/performance-review
```

자기 평가, 관리자 리뷰, 조정을 위한 템플릿을 받으세요. 구체적이고 실행 가능하며 공정한 피드백을 구조화하도록 도와드립니다.

### 복리후생 이해

자연스럽게 질문하세요:
```
What's our parental leave policy?
```

`employee-handbook` skill이 자동으로 실행되어 연결된 지식 베이스에서 답변을 검색합니다.

### 보상 벤치마킹

```
/comp-analysis
```

보상 데이터를 업로드하거나 밴드를 설명하세요. 시장 비교, 밴드 배치 분석, 조정 권고사항을 받을 수 있습니다.

## 단독 사용 + 강화 사용

모든 명령어와 skill은 통합 없이도 작동합니다:

| 가능한 작업 | 단독 사용 | 다음과 함께 강화 |
|-----------------|------------|-------------------|
| 오퍼 초안 작성 | 세부 정보 수동 입력 | HRIS, ATS로 자동 입력 |
| 온보딩 체크리스트 | 프로세스 직접 설명 | HRIS, 지식 베이스로 템플릿 활용 |
| 성과 리뷰 | 수동 입력 | HRIS로 리뷰 이력 활용 |
| 정책 조회 | 핸드북 내용 붙여넣기 | 지식 베이스 연결 |
| 보상 분석 | CSV 업로드, 밴드 설명 | Compensation data MCP |
| 인원 보고서 | 데이터 업로드 | HRIS로 실시간 데이터 활용 |

## MCP 통합

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우, [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

더 풍부한 경험을 위해 도구를 연결하세요:

| 카테고리 | 예시 | 활성화되는 기능 |
|---|---|---|
| **HRIS** | Workday, BambooHR, Rippling | 직원 데이터, 조직 구조, 휴가 잔여일 |
| **ATS** | Greenhouse, Lever, Ashby | 후보자 파이프라인, 인터뷰 일정, 오퍼 추적 |
| **보상** | Pave, Radford | 시장 벤치마크, 보상 밴드 데이터 |
| **채팅** | Slack, Teams | 팀 공지, 후보자 조율 |
| **캘린더** | Google Calendar, Microsoft 365 | 인터뷰 일정, 온보딩 캘린더 |
| **이메일** | Gmail, Microsoft 365 | 오퍼 레터, 후보자 커뮤니케이션 |

지원되는 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

## 설정

개인화를 위해 `settings.local.json` 파일을 생성하세요:

- **Cowork**: Cowork와 공유한 폴더(폴더 선택기 사용)에 저장하세요. 플러그인이 자동으로 찾습니다.
- **Claude Code**: `human-resources/.claude/settings.local.json`에 저장하세요.

```json
{
  "company": "Your Company",
  "headquarters": "City, State",
  "employeeCount": 500,
  "benefits": {
    "healthInsurance": "Provider Name",
    "pto": "Unlimited / X days",
    "parentalLeave": "X weeks"
  },
  "compensation": {
    "currency": "USD",
    "equityType": "RSU / Options",
    "vestingSchedule": "4 years, 1 year cliff"
  }
}
```

설정이 구성되지 않은 경우 플러그인이 대화 중에 이 정보를 요청합니다.
