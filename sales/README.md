# Sales 플러그인

[Cowork](https://claude.com/product/cowork)를 위해 주로 설계된 영업 생산성 플러그인입니다. Anthropic의 에이전틱 데스크톱 애플리케이션용으로 만들었지만 Claude Code에서도 작동합니다. 잠재 고객 발굴, 아웃리치, 파이프라인 관리, 통화 준비, 딜 전략을 돕습니다. 어떤 영업팀과도 함께 사용할 수 있으며, 웹 검색과 사용자 입력만으로도 단독 사용 가능하고 CRM, 이메일, 기타 도구를 연결하면 더 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/sales
```

## 명령

슬래시 명령으로 호출하는 명시적 워크플로입니다.

| 명령 | 설명 |
|---|---|
| `/call-summary` | 통화 메모나 녹취록을 처리합니다. 액션 아이템을 추출하고, 후속 초안을 작성하고, 내부 요약을 생성합니다. |
| `/forecast` | 가중 영업 예측을 생성합니다. CSV를 업로드하거나 파이프라인을 설명하고, 할당량을 설정하면 전망을 얻을 수 있습니다. |
| `/pipeline-review` | 파이프라인 건전성을 분석합니다. 딜 우선순위를 정하고, 리스크를 표시하고, 주간 실행 계획을 얻습니다. |

모든 명령은 **단독으로**도 작동합니다. 메모를 붙여넣거나, CSV를 업로드하거나, 상황을 설명하면 됩니다. MCP 커넥터를 연결하면 **더 강력해집니다**.

## 스킬

Claude가 관련 있을 때 자동으로 사용하는 도메인 지식입니다.

| 스킬 | 설명 |
|---|---|
| `account-research` | 회사나 사람을 조사합니다. 회사 인텔, 핵심 연락처, 최근 뉴스, 채용 신호를 웹 검색합니다. |
| `call-prep` | 영업 통화를 준비합니다. 계정 맥락, 참석자 조사, 제안 아젠다, 발견 질문을 제공합니다. |
| `daily-briefing` | 우선순위가 반영된 일일 영업 브리핑을 제공합니다. 미팅, 파이프라인 알림, 이메일 우선순위, 제안 행동을 담습니다. |
| `draft-outreach` | 조사 우선 아웃리치를 만듭니다. 잠재 고객을 조사한 뒤 개인화된 이메일과 LinkedIn 메시지를 작성합니다. |
| `competitive-intelligence` | 경쟁사를 조사합니다. 제품 비교, 가격 정보, 최근 출시, 차별화 매트릭스, 영업용 토크 트랙을 만듭니다. |
| `create-an-asset` | 맞춤형 영업 자산을 생성합니다. 잠재 고객에 맞춘 랜딩 페이지, 덱, 원페이저, 워크플로 데모를 만듭니다. |

## 예시 워크플로

### 통화 후

```
/call-summary
```

메모나 녹취록을 붙여넣으세요. 구조화된 요약, 담당자가 포함된 액션 아이템, 후속 이메일 초안을 받을 수 있습니다. CRM이 연결되어 있으면 활동 기록과 작업 생성도 제안합니다.

### 주간 예측

```
/forecast
```

CRM에서 CSV를 내보내 업로드하거나 딜을 붙여넣으세요. 목표와 기간을 알려 주면 최상/가능/최악 시나리오가 포함된 가중 예측, 커밋 vs. 업사이드 구분, 갭 분석을 받을 수 있습니다.

### 파이프라인 검토

```
/pipeline-review
```

CSV를 업로드하거나 파이프라인을 설명하세요. 건전성 점수, 딜 우선순위, 리스크 플래그(오래된 딜, 지난 종료일, 단일 접점), 주간 실행 계획을 받을 수 있습니다.

### 잠재 고객 조사

자연스럽게 물어보면 됩니다.
```
Research Acme Corp before my call tomorrow
```

`account-research` 스킬이 자동으로 실행되어 회사 개요, 핵심 연락처, 최근 뉴스, 권장 접근 방식을 제공합니다.

### 아웃리치 초안 작성

```
Draft an email to the VP of Engineering at TechStart
```

`draft-outreach` 스킬이 먼저 잠재 고객을 조사한 뒤, 여러 각도의 개인화된 아웃리치 문안을 생성합니다.

### 경쟁 인텔

```
How do we compare to Competitor X?
```

`competitive-intelligence` 스킬이 양쪽 회사를 조사하고, 차별화 매트릭스와 토크 트랙을 만듭니다.

## 단독 사용 + 강화 사용

모든 명령과 스킬은 통합 없이도 작동합니다.

| 할 수 있는 일 | 단독 사용 | 연결 시 강화 |
|-----------------|------------|-------------------|
| 통화 메모 처리 | 메모/녹취록 붙여넣기 | Transcripts MCP(예: Gong, Fireflies) |
| 파이프라인 예측 | CSV 업로드, 딜 붙여넣기 | CRM MCP |
| 파이프라인 검토 | CSV 업로드, 딜 설명 | CRM MCP |
| 잠재 고객 조사 | 웹 검색 | Enrichment MCP(예: Clay, ZoomInfo) |
| 통화 준비 | 미팅 설명 | CRM, Email, Calendar MCP |
| 아웃리치 초안 작성 | 웹 검색 + 사용자 맥락 | CRM, Email MCP |
| 경쟁 인텔 | 웹 검색 | CRM(win/loss 데이터), Docs(battlecards) |

## MCP 통합

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

더 풍부한 사용 경험을 위해 도구를 연결하세요.

| 범주 | 예시 | 가능해지는 일 |
|---|---|---|
| **CRM** | HubSpot, Close | 파이프라인 데이터, 계정 이력, 연락처 기록 |
| **Transcripts** | Fireflies, Gong, Chorus | 통화 녹음, 녹취록, 핵심 순간 |
| **Enrichment** | Clay, ZoomInfo, Apollo | 회사 및 연락처 데이터 보강 |
| **Chat** | Slack, Teams | 내부 논의, 동료 인텔 |

[CONNECTORS.md](CONNECTORS.md)에서 이메일, 캘린더, 추가 CRM 옵션을 포함한 전체 지원 통합 목록을 확인하세요.

## 설정

개인화를 위해 `settings.local.json` 파일을 만드세요.

- **Cowork**: Cowork와 공유한 폴더(폴더 선택기를 통해)에 저장하세요. 플러그인이 자동으로 찾습니다.
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

구성이 되어 있지 않으면 플러그인이 이 정보를 대화식으로 요청합니다.
