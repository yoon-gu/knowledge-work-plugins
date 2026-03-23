---
name: competitive-intelligence
description: 경쟁사를 조사하고 인터랙티브 배틀카드를 만듭니다. 클릭 가능한 경쟁사 카드와 비교 매트릭스가 포함된 HTML 산출물을 출력합니다. "competitive intel", "research competitors", "how do we compare to [competitor]", "battlecard for [competitor]", "what's new with [competitor]"을 입력하면 트리거됩니다.
---

# 경쟁 인텔리전스

경쟁사를 폭넓게 조사해 딜에서 활용할 수 있는 **인터랙티브 HTML 배틀카드**를 생성합니다. 출력물은 클릭 가능한 경쟁사 탭과 전체 비교 매트릭스를 갖춘 독립형 산출물입니다.

## 작동 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                  경쟁 인텔리전스                                │
├─────────────────────────────────────────────────────────────────┤
│  항상(웹 검색으로 단독 사용 가능)                               │
│  ✓ 경쟁사 제품 심층 분석: 기능, 가격, 포지셔닝                 │
│  ✓ 최근 출시: 지난 90일 동안 무엇을 출시했는지               │
│  ✓ 우리 회사 출시: 대응을 위해 무엇을 냈는지                  │
│  ✓ 차별화 매트릭스: 우리가 이기는 영역 vs. 그들이 이기는 영역 │
│  ✓ 영업 토크 트랙: 각 경쟁사를 상대로 어떻게 포지셔닝할지     │
│  ✓ 랜드마인 질문: 약점을 자연스럽게 드러내는 질문            │
├─────────────────────────────────────────────────────────────────┤
│  출력: 인터랙티브 HTML 배틀카드                                │
│  ✓ 비교 매트릭스 개요                                           │
│  ✓ 경쟁사별 클릭 가능한 탭                                      │
│  ✓ 다크 테마, 전문적인 스타일링                                 │
│  ✓ 독립형 HTML 파일 — 어디서든 공유하거나 호스팅 가능           │
├─────────────────────────────────────────────────────────────────┤
│  강화 모드(도구를 연결하면)                                      │
│  + CRM: win/loss 데이터, 종료된 딜의 경쟁사 언급               │
│  + Docs: 기존 배틀카드, 경쟁 플레이북                          │
│  + Chat: 내부 인텔, 동료의 현장 보고                           │
│  + Transcripts: 고객 통화에서의 경쟁사 언급                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 시작하기

이 스킬을 실행하면 맥락을 물어봅니다.

**필수:**
- 어떤 회사에서 일하시나요? (또는 이메일에서 감지합니다)
- 주요 경쟁사는 누구인가요? (1-5개 이름)

**선택:**
- 어떤 경쟁사에 먼저 집중할까요?
- 그들과 경쟁 중인 구체적인 딜이 있나요?
- 고객에게서 들은 경쟁사 관련 고통 지점이 있나요?

이전 세션에서 셀러 맥락이 이미 있으면 확인만 하고 질문은 건너뜁니다.

## 연결 도구(선택)

| 연결 도구 | 추가되는 것 |
|-----------|--------------|
| **CRM** | 각 경쟁사에 대한 win/loss 이력, 딜 수준의 경쟁사 추적 |
| **Docs** | 기존 배틀카드, 제품 비교 문서, 경쟁 플레이북 |
| **Chat** | 내부 채팅 인텔(예: Slack) - 팀이 현장에서 듣고 있는 내용 |
| **Transcripts** | 고객 통화의 경쟁사 언급, 제기된 반론 |

> **연결 도구가 없나요?** 웹 검색만으로도 충분히 잘 작동합니다. 제품 페이지, 가격, 블로그, 릴리스 노트, 리뷰, 채용 공고 등 공개 출처에서 모두 가져옵니다.

## 출력: 인터랙티브 HTML 배틀카드

이 스킬은 다음 요소를 가진 **독립형 HTML 파일**을 생성합니다.

### 1. 비교 매트릭스(초기 화면)
당신과 모든 경쟁사를 한눈에 비교하는 개요입니다.
- 기능 비교 그리드
- 가격 비교
- 시장 포지셔닝
- win rate 지표(CRM이 연결된 경우)

### 2. 경쟁사 탭(클릭해서 확장)
각 경쟁사마다 클릭 가능한 카드가 있으며, 펼치면 다음이 보입니다.
- 회사 프로필(규모, 투자, 타깃 시장)
- 무엇을 팔고 어떻게 포지셔닝하는지
- 최근 출시(지난 90일)
- 그들이 이기는 지점 vs. 우리가 이기는 지점
- 가격 정보
- 다양한 시나리오별 토크 트랙
- 반론 대응
- 랜드마인 질문

### 3. 우리 회사 카드
- 우리 출시(지난 90일)
- 핵심 차별점
- 증거 포인트와 고객 인용문

## HTML 구조

```html
<!DOCTYPE html>
<html>
<head>
    <title>배틀카드: [Your Company] vs Competitors</title>
    <style>
        /* 다크 테마, 전문적인 스타일링 */
        /* 탭형 내비게이션 */
        /* 확장 가능한 카드 */
        /* 반응형 디자인 */
    </style>
</head>
<body>
    <!-- 회사명과 날짜가 포함된 헤더 -->
    <header>
        <h1>[Your Company] Competitive Battlecard</h1>
        <p>Generated: [Date] | Competitors: [List]</p>
    </header>

    <!-- 탭 내비게이션 -->
    <nav class="tabs">
        <button class="tab active" data-tab="matrix">비교 매트릭스</button>
        <button class="tab" data-tab="competitor-1">[Competitor 1]</button>
        <button class="tab" data-tab="competitor-2">[Competitor 2]</button>
        <button class="tab" data-tab="competitor-3">[Competitor 3]</button>
    </nav>

    <!-- 비교 매트릭스 탭 -->
    <section id="matrix" class="tab-content active">
        <h2>일대일 비교</h2>
        <table class="comparison-matrix">
            <!-- Feature rows with you vs each competitor -->
        </table>

        <h2>빠른 Win/Loss 가이드</h2>
        <div class="win-loss-grid">
            <!-- Per-competitor: when you win, when you lose -->
        </div>
    </section>

    <!-- 개별 경쟁사 탭 -->
    <section id="competitor-1" class="tab-content">
        <div class="battlecard">
            <div class="profile"><!-- 회사 정보 --></div>
            <div class="differentiation"><!-- 그들이 이기는 지점 / 우리가 이기는 지점 --></div>
            <div class="talk-tracks"><!-- 시나리오 기반 포지셔닝 --></div>
            <div class="objections"><!-- 흔한 반론 + 대응 --></div>
            <div class="landmines"><!-- 물어볼 질문 --></div>
        </div>
    </section>

    <script>
        // 탭 전환 로직
        // 섹션 확장/축소
    </script>
</body>
</html>
```

## 시각 디자인

### 색상 체계
```css
:root {
    /* 다크 테마 기본 */
    --bg-primary: #0a0d14;
    --bg-elevated: #0f131c;
    --bg-surface: #161b28;
    --bg-hover: #1e2536;

    /* 텍스트 */
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --text-muted: rgba(255, 255, 255, 0.5);

    /* 강조색(브랜드 또는 중립 색상) */
    --accent: #3b82f6;
    --accent-hover: #2563eb;

    /* 상태 표시 */
    --you-win: #10b981;
    --they-win: #ef4444;
    --tie: #f59e0b;
}
```

### 카드 디자인
- 둥근 모서리(12px)
- 은은한 테두리(1px, 낮은 불투명도)
- 살짝 떠오르는 호버 상태
- 부드러운 전환(200ms)

### 비교 매트릭스
- 고정 헤더 행
- 색상으로 구분된 승자 표시(초록 = 우리, 빨강 = 그들, 노랑 = 무승부)
- 상세를 볼 수 있는 확장 행

---

## 실행 흐름

### 1단계: 셀러 맥락 수집

```
첫 사용이라면:
1. 질문: "어느 회사에서 일하시나요?"
2. 질문: "무엇을 판매하시나요? (제품/서비스를 한 줄로)"
3. 질문: "주요 경쟁사는 누구인가요? (최대 5개)"
4. 향후 세션을 위해 맥락 저장

기존 사용자라면:
1. 확인: "여전히 [Company]에서 [Product]를 판매하고 계신가요?"
2. 질문: "같은 경쟁사인가요, 추가할 새 경쟁사가 있나요?"
```

### 2단계: 우리 회사 조사(항상)

```
웹 검색:
1. "[Your company] product" — 현재 제공 항목
2. "[Your company] pricing" — 가격 모델
3. "[Your company] news" — 최근 공지(90일)
4. "[Your company] product updates OR changelog OR releases" — 우리가 출시한 것
5. "[Your company] vs [competitor]" — 기존 비교
```

### 3단계: 각 경쟁사 조사(항상)

```
각 경쟁사에 대해 실행:
1. "[Competitor] product features" — 그들이 제공하는 것
2. "[Competitor] pricing" — 과금 방식
3. "[Competitor] news" — 최근 공지
4. "[Competitor] product updates OR changelog OR releases" — 그들이 출시한 것
5. "[Competitor] reviews G2 OR Capterra OR TrustRadius" — 고객 반응
6. "[Competitor] vs [alternatives]" — 어떻게 포지셔닝하는지
7. "[Competitor] customers" — 누가 사용하는지
8. "[Competitor] careers" — 채용 신호(성장 영역)
```

### 4단계: 연결된 출처 가져오기(가능하면)

```
CRM이 연결되어 있으면:
1. closed-won 딜 중 competitor 필드가 [Competitor]인 딜 조회
2. closed-lost 딜 중 competitor 필드가 [Competitor]인 딜 조회
3. win/loss 패턴 추출

Docs가 연결되어 있으면:
1. "battlecard [competitor]" 검색
2. "competitive [competitor]" 검색
3. 기존 포지셔닝 문서 가져오기

Chat이 연결되어 있으면:
1. "[Competitor]" 언급 검색(지난 90일)
2. 현장 인텔과 동료 인사이트 추출

Transcripts가 연결되어 있으면:
1. 통화에서 "[Competitor]" 언급 검색
2. 반론과 고객 인용문 추출
```

### 5단계: HTML 산출물 생성

```
1. 경쟁사별 데이터 구조화
2. 비교 매트릭스 작성
3. 개별 배틀카드 생성
4. 각 시나리오별 토크 트랙 작성
5. 랜드마인 질문 취합
6. 독립형 HTML로 렌더링
7. [YourCompany]-battlecard-[date].html로 저장
```

---

## 경쟁사별 데이터 구조

```yaml
competitor:
  name: "[Name]"
  website: "[URL]"
  profile:
    founded: "[Year]"
    funding: "[Stage + amount]"
    employees: "[Count]"
    target_market: "[Who they sell to]"
    pricing_model: "[Per seat / usage / etc.]"
    market_position: "[Leader / Challenger / Niche]"

  what_they_sell: "[Product summary]"
  their_positioning: "[How they describe themselves]"

  recent_releases:
    - date: "[Date]"
      release: "[Feature/Product]"
      impact: "[Why it matters]"

  where_they_win:
    - area: "[Area]"
      advantage: "[Their strength]"
      how_to_handle: "[Your counter]"

  where_you_win:
    - area: "[Area]"
      advantage: "[Your strength]"
      proof_point: "[Evidence]"

  pricing:
    model: "[How they charge]"
    entry_price: "[Starting price]"
    enterprise: "[Enterprise pricing]"
    hidden_costs: "[Implementation, etc.]"
    talk_track: "[How to discuss pricing]"

  talk_tracks:
    early_mention: "[Strategy if they come up early]"
    displacement: "[Strategy if customer uses them]"
    late_addition: "[Strategy if added late to eval]"

  objections:
    - objection: "[What customer says]"
      response: "[How to handle]"

  landmines:
    - "[Question that exposes their weakness]"

  win_loss: # If CRM connected
    win_rate: "[X]%"
    common_win_factors: "[What predicts wins]"
    common_loss_factors: "[What predicts losses]"
```

---

## 전달

```markdown
## ✓ 배틀카드 생성 완료

[배틀카드 보기](file:///path/to/[YourCompany]-battlecard-[date].html)

---

**요약**
- **Your Company**: [이름]
- **분석한 경쟁사**: [목록]
- **데이터 출처**: 웹 조사 [+ CRM] [+ Docs] [+ Transcripts]

---

**사용 방법**
- **통화 전**: 관련 경쟁사 탭을 열고 토크 트랙을 검토
- **통화 중**: 랜드마인 질문 참조
- **win/loss 후**: 새 인텔로 업데이트

---

**공유 방법**
- **로컬 파일**: 어떤 브라우저에서든 열기
- **호스팅**: Netlify, Vercel, 내부 위키에 업로드
- **직접 공유**: HTML 파일을 동료에게 보내기

---

**최신 상태 유지**
최신 인텔로 갱신하려면 이 스킬을 다시 실행하세요. 권장 주기: 매월 또는 주요 딜 전에.
```

---

## 갱신 주기

경쟁 인텔은 금방 낡습니다. 권장 갱신:

| 트리거 | 작업 |
|---------|--------|
| **매월** | 빠른 갱신 - 새 출시, 뉴스, 가격 변경 |
| **주요 딜 전** | 해당 딜의 특정 경쟁사 심층 갱신 |
| **win/loss 후** | 새 데이터로 패턴 업데이트 |
| **경쟁사 공지** | 해당 경쟁사 즉시 업데이트 |

---

## 더 나은 인텔을 위한 팁

1. **약점에 대해 솔직해지세요** — 경쟁사가 강한 지점을 인정할 때 신뢰가 생깁니다.
2. **기능보다 결과에 집중하세요** — "그들은 X 기능이 있다"보다 "고객이 Y 결과를 얻는다"가 더 중요합니다.
3. **현장에서 업데이트하세요** — 최고의 인텔은 웹사이트가 아니라 실제 고객 대화에서 나옵니다.
4. **랜드마인을 심되 험담하지 마세요** — 약점을 드러내는 질문을 하고, 절대 깎아내리지 마세요.
5. **릴리스를 철저히 추적하세요** — 그들이 무엇을 출시하는지가 전략과 기회를 말해 줍니다.

---

## 관련 스킬

- **account-research** — 연락하기 전에 특정 잠재 고객을 조사
- **call-prep** — 경쟁사가 포함된 통화를 준비
- **create-an-asset** — 특정 딜을 위한 맞춤 비교 페이지 제작
