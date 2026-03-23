# Sales 플러그인

주로 Anthropic의 에이전트형 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 영업 생산성 플러그인 — Claude Code에서도 동작합니다. 잠재 고객 발굴, 아웃리치, 파이프라인 관리, 통화 준비, 딜 전략을 지원합니다. 모든 영업팀에 적합합니다 — 웹 검색과 직접 입력만으로도 단독으로 사용할 수 있으며, CRM, 이메일 및 기타 도구를 연결하면 훨씬 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/sales
```

## 명령어

슬래시 명령어로 실행하는 명시적 워크플로:

| 명령어 | 설명 |
|---|---|
| `/call-summary` | 통화 메모 또는 전사본 처리 — 액션 아이템 추출, 후속 초안 작성, 내부 요약 생성 |
| `/forecast` | 가중 영업 예측 생성 — CSV 업로드 또는 파이프라인 설명, 할당량 설정, 예측치 획득 |
| `/pipeline-review` | 파이프라인 건강 상태 분석 — 딜 우선순위 지정, 위험 요소 플래그, 주간 실행 계획 수립 |

모든 명령어는 **단독으로** (메모 붙여넣기, CSV 업로드, 또는 상황 설명) 사용할 수 있으며, MCP 커넥터를 연결하면 **더욱 강력해집니다**.

## 스킬

관련성이 있을 때 Claude가 자동으로 사용하는 도메인 지식:

| 스킬 | 설명 |
|---|---|
| `account-research` | 기업 또는 개인 조사 — 기업 정보, 주요 연락처, 최근 뉴스, 채용 신호에 대한 웹 검색 |
| `call-prep` | 영업 통화 준비 — 계정 컨텍스트, 참석자 조사, 제안 안건, 발굴 질문 |
| `daily-briefing` | 우선순위가 지정된 일일 영업 브리핑 — 미팅, 파이프라인 알림, 이메일 우선순위, 제안 행동 |
| `draft-outreach` | 조사 기반 아웃리치 — 잠재 고객 조사 후 개인화된 이메일 및 LinkedIn 메시지 초안 작성 |
| `competitive-intelligence` | 경쟁사 조사 — 제품 비교, 가격 인텔리전스, 최근 출시 정보, 차별화 매트릭스, 영업 토크 트랙 |
| `create-an-asset` | 맞춤형 영업 자료 생성 — 잠재 고객에 맞춘 랜딩 페이지, 덱, 원페이저, 워크플로 데모 |

## 예시 워크플로

### 통화 후

```
/call-summary
```

메모나 전사본을 붙여넣으세요. 구조화된 요약, 담당자가 지정된 액션 아이템, 후속 이메일 초안을 받아보세요. CRM이 연결된 경우, 활동 기록과 태스크 생성을 제안합니다.

### 주간 예측

```
/forecast
```

CRM에서 CSV를 내보내거나 딜 목록을 붙여넣으세요. 할당량과 기간을 알려주세요. 최선/예상/최악 시나리오, 확정 vs. 상향 분류, 갭 분석이 포함된 가중 예측을 받아보세요.

### 파이프라인 검토

```
/pipeline-review
```

CSV를 업로드하거나 파이프라인을 설명하세요. 건강 점수, 딜 우선순위, 위험 플래그(오래된 딜, 지난 클로즈 날짜, 단일 접점), 주간 실행 계획을 받아보세요.

### 잠재 고객 조사

자연스럽게 질문하세요:
```
Research Acme Corp before my call tomorrow
```

`account-research` 스킬이 자동으로 실행되어 기업 개요, 주요 연락처, 최근 뉴스, 권장 접근 방식을 제공합니다.

### 아웃리치 초안 작성

```
Draft an email to the VP of Engineering at TechStart
```

`draft-outreach` 스킬이 먼저 잠재 고객을 조사한 후 다양한 각도의 개인화된 아웃리치를 생성합니다.

### 경쟁 인텔리전스

```
How do we compare to Competitor X?
```

`competitive-intelligence` 스킬이 두 회사를 모두 조사하고 토크 트랙이 포함된 차별화 매트릭스를 구성합니다.

## 단독 사용 + 강화된 사용

모든 명령어와 스킬은 통합 없이도 동작합니다:

| 가능한 작업 | 단독 사용 | 강화 시 필요한 항목 |
|-----------------|------------|-------------------|
| 통화 메모 처리 | 메모/전사본 붙여넣기 | Transcripts MCP (예: Gong, Fireflies) |
| 파이프라인 예측 | CSV 업로드, 딜 붙여넣기 | CRM MCP |
| 파이프라인 검토 | CSV 업로드, 딜 설명 | CRM MCP |
| 잠재 고객 조사 | 웹 검색 | Enrichment MCP (예: Clay, ZoomInfo) |
| 통화 준비 | 미팅 설명 | CRM, Email, Calendar MCPs |
| 아웃리치 초안 | 웹 검색 + 컨텍스트 | CRM, Email MCPs |
| 경쟁 인텔리전스 | 웹 검색 | CRM (승/패 데이터), Docs (배틀카드) |

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인하려면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

더 풍부한 경험을 위해 도구를 연결하세요:

| 카테고리 | 예시 | 활성화되는 기능 |
|---|---|---|
| **CRM** | HubSpot, Close | 파이프라인 데이터, 계정 이력, 연락처 기록 |
| **전사** | Fireflies, Gong, Chorus | 통화 녹음, 전사본, 핵심 순간 |
| **데이터 보강** | Clay, ZoomInfo, Apollo | 기업 및 연락처 데이터 보강 |
| **채팅** | Slack, Teams | 내부 논의, 동료 인텔리전스 |

이메일, 캘린더 및 추가 CRM 옵션을 포함한 지원 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

## 설정

개인화를 위해 `settings.local.json` 파일을 생성하세요:

- **Cowork**: Cowork와 공유한 폴더(폴더 선택기 통해)에 저장하세요. 플러그인이 자동으로 찾습니다.
- **Claude Code**: `sales/.claude/settings.local.json`에 저장하세요.

```json
{
  "name": "Your Name",
  "title": "Account Executive",
  "company": "Your Company",
  "quota": {
    "annual": 1000000,
    "quarterly": 250000
  },
  "product": {
    "name": "Your Product",
    "value_props": [
      "Key value proposition 1",
      "Key value proposition 2"
    ],
    "competitors": [
      "Competitor A",
      "Competitor B"
    ]
  }
}
```

설정이 구성되지 않은 경우 플러그인이 대화형으로 정보를 요청합니다.
