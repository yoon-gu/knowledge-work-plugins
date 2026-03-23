# HR 플러그인

[Cowork](https://claude.com/product/cowork)를 위해 주로 설계된 인사 운영 플러그인입니다. Anthropic의 에이전틱 데스크톱 애플리케이션이지만 Claude Code에서도 작동합니다. 채용, 온보딩, 성과 관리, 정책 안내, 보상 분석을 돕습니다. 어떤 HR 팀과도 사용할 수 있으며, 입력만으로도 독립적으로 동작하고 HRIS, ATS, 기타 도구를 연결하면 더 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/human-resources
```

## 명령

슬래시 명령으로 직접 호출하는 명시적 워크플로입니다.

| 명령 | 설명 |
|---|---|
| `/draft-offer` | 보상 세부사항, 시작일, 조건이 포함된 오퍼 레터 초안 작성 |
| `/onboarding` | 신규 입사자를 위한 온보딩 체크리스트와 첫 주 계획 생성 |
| `/performance-review` | 자기평가 프롬프트, 관리자 템플릿, 캘리브레이션 준비가 포함된 성과 리뷰 구조화 |
| `/policy-lookup` | 휴가, 복리후생, 경비, 출장, 원격근무 등 회사 정책을 찾고 설명 |
| `/comp-analysis` | 벤치마킹, 밴드 배치, 지분 리프레시 모델링 등 보상 데이터 분석 |
| `/people-report` | 인원수, 이직률, 다양성, 조직 건강 보고서 생성 |

모든 명령은 **독립적으로** 작동하며(맥락과 세부사항을 제공), MCP 커넥터를 연결하면 **더 강력해집니다**.

## 스킬

Claude가 관련될 때 자동으로 사용하는 도메인 지식입니다.

| 스킬 | 설명 |
|---|---|
| `recruiting-pipeline` | 소싱, 스크리닝, 인터뷰, 오퍼 단계의 채용 파이프라인 추적 및 관리 |
| `employee-handbook` | 회사 정책, 복리후생, 절차에 대한 질문 응답 |
| `compensation-benchmarking` | 시장 데이터 대비 보상 벤치마킹 - 기본급, 지분, 총보상 |
| `org-planning` | 인력 계획, 조직 설계, 팀 구조 최적화 |
| `people-analytics` | 이직 추세, 참여 신호, 다양성 지표 등 인력 데이터 분석 |
| `interview-prep` | 역량 기반 질문, 스코어카드, 디브리프 템플릿을 포함한 구조화된 인터뷰 계획 생성 |

## 예시 워크플로

### 오퍼 초안 작성

```
/draft-offer
```

역할, 레벨, 지역, 보상 세부사항을 알려 주세요. 조건, 지분 세부내역, 복리후생 요약이 포함된 완전한 오퍼 레터 초안을 받을 수 있습니다.

### 신규 입사자 온보딩

```
/onboarding
```

신규 입사자의 이름, 역할, 팀, 시작일을 알려 주세요. 포괄적인 온보딩 체크리스트, 첫 주 일정, 도구 접근 목록, 버디 지정 템플릿을 받을 수 있습니다.

### 성과 리뷰 준비

```
/performance-review
```

자기평가, 관리자 리뷰, 캘리브레이션용 템플릿을 받을 수 있습니다. 구체적이고 실행 가능하며 공정한 피드백 구조화를 도와드립니다.

### 복리후생 이해

자연스럽게 질문하세요.
```
우리의 육아휴직 정책은 어떻게 되나요?
```

`employee-handbook` 스킬이 자동으로 실행되어 연결된 지식 베이스에서 답을 검색합니다.

### 보상 벤치마킹

```
/comp-analysis
```

보상 데이터를 업로드하거나 밴드를 설명해 주세요. 시장 비교, 밴드 배치 분석, 조정 권고를 받을 수 있습니다.

## 독립 실행 + 강화 모드

모든 명령과 스킬은 통합 없이도 작동합니다.

| 할 수 있는 일 | 독립 실행 | 연결 시 더 강력한 점 |
|-----------------|------------|-------------------|
| 오퍼 초안 작성 | 세부사항을 수동 입력 | HRIS, ATS로 자동 채움 |
| 온보딩 체크리스트 | 프로세스를 직접 설명 | HRIS, 지식 베이스로 템플릿 제공 |
| 성과 리뷰 | 수동 입력 | 리뷰 이력용 HRIS |
| 정책 조회 | 핸드북 내용을 붙여넣기 | 지식 베이스 |
| 보상 분석 | CSV 업로드, 밴드 설명 | 보상 데이터 MCP |
| 인력 보고서 | 데이터 업로드 | 실시간 데이터용 HRIS |

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

더 풍부한 경험을 위해 도구를 연결하세요.

| 범주 | 예시 | 가능한 기능 |
|---|---|---|
| **HRIS** | Workday, BambooHR, Rippling | 직원 데이터, 조직 구조, PTO 잔액 |
| **ATS** | Greenhouse, Lever, Ashby | 후보자 파이프라인, 인터뷰 일정, 오퍼 추적 |
| **보상** | Pave, Radford | 시장 벤치마크, 보상 밴드 데이터 |
| **채팅** | Slack, Teams | 팀 공지, 후보자 조율 |
| **캘린더** | Google Calendar, Microsoft 365 | 인터뷰 일정, 온보딩 캘린더 |
| **이메일** | Gmail, Microsoft 365 | 오퍼 레터, 후보자 커뮤니케이션 |

지원되는 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

## 설정

개인화하려면 `settings.local.json` 파일을 생성하세요.

- **Cowork**: Cowork와 공유한 폴더(폴더 선택기를 통해) 중 아무 곳에나 저장하면 됩니다. 플러그인이 자동으로 찾습니다.
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

이 정보가 설정되지 않았다면 플러그인이 대화형으로 물어봅니다.
