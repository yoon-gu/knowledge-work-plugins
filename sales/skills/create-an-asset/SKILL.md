---
name: create-an-asset
description: 딜 맥락을 바탕으로 맞춤형 영업 자산(랜딩 페이지, 덱, 원페이저, 워크플로 데모)을 생성합니다. 잠재 고객, 대상, 목표를 설명하면 고객과 공유할 수 있는 세련되고 브랜드화된 자산을 얻을 수 있습니다.
---

# 자산 만들기

잠재 고객, 대상, 목표에 맞춘 맞춤형 영업 자산을 생성합니다. 인터랙티브 랜딩 페이지, 프레젠테이션 덱, 임원용 원페이저, 워크플로/아키텍처 데모를 지원합니다.

---

## 트리거

다음 상황에서 이 스킬을 실행합니다.
- 사용자가 `/create-an-asset` 또는 `/create-an-asset [CompanyName]`를 말할 때
- 사용자가 "create an asset", "build a demo", "make a landing page", "mock up a workflow"를 요청할 때
- 사용자가 영업 대화를 위한 고객용 산출물이 필요할 때

---

## 개요

이 스킬은 다음 맥락을 수집해 전문적인 영업 자산을 만듭니다.
- **(a) 잠재 고객** — 회사, 연락처, 대화, 고통 지점
- **(b) 대상** — 누가 보는지, 무엇을 중요하게 보는지
- **(c) 목적** — 자산의 목표, 원하는 다음 행동
- **(d) 형식** — 랜딩 페이지, 덱, 원페이저, 워크플로 데모

그다음 조사, 구조화, 빌드를 거쳐 고객과 공유할 수 있는 세련된 브랜드 자산을 만듭니다.

---

## 0단계: 맥락 감지 및 입력 수집

### 0.1단계: 셀러 맥락 감지

사용자의 이메일 도메인에서 어떤 회사에 다니는지 식별합니다.

**작업:**
1. 사용자 이메일에서 도메인 추출
2. 검색: `"[domain]" company products services site:linkedin.com OR site:crunchbase.com`
3. 셀러 맥락 결정:

| 시나리오 | 작업 |
|----------|--------|
| **단일 제품 회사** | 셀러 맥락 자동 채움 |
| **복수 제품 회사** | 질문: "이 자산은 어떤 제품이나 솔루션용인가요?" |
| **컨설턴트/에이전시/일반 도메인** | 질문: "어떤 회사나 제품을 대표하시나요?" |
| **알 수 없음/스타트업** | 질문: "간단히, 무엇을 판매하나요?" |

**셀러 맥락 저장:**
```yaml
seller:
  company: "[Company Name]"
  product: "[Product/Service]"
  value_props:
    - "[Key value prop 1]"
    - "[Key value prop 2]"
    - "[Key value prop 3]"
  differentiators:
    - "[Differentiator 1]"
    - "[Differentiator 2]"
  pricing_model: "[If publicly known]"
```

향후 세션을 위해 **지식 베이스에 유지**합니다. 다음 실행 때는 "지난번 셀러 맥락을 기억합니다. 아직 [Company]에서 [Product]를 판매하고 계신가요?"라고 확인합니다.

### 0.2단계: 잠재 고객 맥락 수집 (a)

**사용자에게 묻기:**

| 항목 | 질문 | 필수 여부 |
|-------|--------|----------|
| **회사** | "이 자산은 어느 회사를 위한 것인가요?" | ✓ 예 |
| **핵심 연락처** | "핵심 연락처는 누구인가요? (이름, 역할)" | 아니오 |
| **딜 단계** | "이 딜은 어느 단계인가요?" | ✓ 예 |
| **고통 지점** | "어떤 고통 지점이나 우선순위를 공유했나요?" | 아니오 |
| **과거 자료** | "대화 자료(녹취록, 이메일, 메모, 통화 녹음)를 업로드하세요" | 아니오 |

**딜 단계 옵션:**
- Intro / First meeting
- Discovery
- Evaluation / Technical review
- POC / Pilot
- Negotiation
- Close

### 0.3단계: 대상 맥락 수집 (b)

**사용자에게 묻기:**

| 항목 | 질문 | 필수 여부 |
|-------|--------|----------|
| **대상 유형** | "누가 이것을 보나요?" | ✓ 예 |
| **구체적 역할** | "특정 직함에 맞춰야 하나요? (예: CTO, VP Engineering, CFO)" | 아니오 |
| **주요 관심사** | "무엇을 가장 중요하게 보나요?" | ✓ 예 |
| **반론** | "다뤄야 할 우려나 반론이 있나요?" | 아니오 |

**대상 유형 옵션:**
- Executive (C-suite, VPs)
- Technical (Architects, Engineers, Developers)
- Operations (Ops, IT, Procurement)
- Mixed / Cross-functional

**주요 관심사 옵션:**
- ROI / Business impact
- Technical depth / Architecture
- Strategic alignment
- Risk mitigation / Security
- Implementation / Timeline

### 0.4단계: 목적 맥락 수집 (c)

**사용자에게 묻기:**

| 항목 | 질문 | 필수 여부 |
|-------|--------|----------|
| **목표** | "이 자산의 목표는 무엇인가요?" | ✓ 예 |
| **원하는 행동** | "보는 사람이 이것을 본 뒤 무엇을 하길 바라나요?" | ✓ 예 |

**목표 옵션:**
- Intro / First impression
- Discovery follow-up
- Technical deep-dive
- Executive alignment / Business case
- POC proposal
- Deal close

### 0.5단계: 형식 선택 (d)

**사용자에게 묻기:** "어떤 형식이 가장 적합한가요?"

| 형식 | 설명 | 적합한 용도 |
|--------|-------------|----------|
| **인터랙티브 랜딩 페이지** | 데모, 지표, 계산기가 있는 멀티탭 페이지 | 임원 정렬, 소개, 가치 제안 |
| **덱 스타일** | 선형 슬라이드, 발표용 | 공식 미팅, 큰 청중 |
| **원페이저** | 한 번에 스크롤되는 임원용 요약 | 남겨둘 자료, 빠른 요약 |
| **워크플로 / 아키텍처 데모** | 애니메이션 흐름이 있는 인터랙티브 다이어그램 | 기술 심층 분석, POC 데모, 통합 |

### 0.6단계: 형식별 입력

#### "워크플로 / 아키텍처 데모"를 선택한 경우:

**먼저 사용자의 설명을 파싱합니다.** 다음을 찾습니다.
- 언급된 시스템과 구성 요소
- 설명된 데이터 흐름
- 사람의 상호작용 지점
- 예시 시나리오

**그다음 빈 부분을 묻습니다:**

| 누락된 경우... | 물어볼 내용 |
|---------------|--------|
| 구성 요소가 불분명 | "어떤 시스템이나 구성 요소가 관련되나요? (데이터베이스, API, AI, 미들웨어 등)" |
| 흐름이 불분명 | "단계별 흐름을 설명해 주세요" |
| 사람의 접점이 불분명 | "이 워크플로에서 사람은 어디에서 상호작용하나요?" |
| 시나리오가 모호 | "데모할 구체적인 예시 시나리오는 무엇인가요?" |
| 통합 세부사항 | "강조할 특정 도구나 플랫폼이 있나요?" |

---

## 1단계: 조사(적응형)

### 맥락 풍부도 평가

| 수준 | 지표 | 조사 깊이 |
|-------|------------|----------------|
| **풍부** | 녹취록 업로드, 상세한 고통 지점, 명확한 요구사항 | 가볍게 - 빈 부분만 채움 |
| **보통** | 일부 맥락, 녹취록 없음 | 중간 - 회사 + 업종 |
| **빈약** | 회사명만 있음 | 깊게 - 전체 조사 수행 |

### 항상 조사할 항목:

1. **잠재 고객 기본 정보**
   - 검색: `"[Company]" annual report investor presentation 2025 2026`
   - 검색: `"[Company]" CEO strategy priorities 2025 2026`
   - 추출: 매출, 직원 수, 핵심 지표, 전략 우선순위

2. **리더십**
   - 검색: `"[Company]" CEO CTO CIO 2025`
   - 추출: 이름, 직함, 전략/기술에 대한 최근 발언

3. **브랜드 색상**
   - 검색: `"[Company]" brand guidelines`
   - 또는 회사 웹사이트에서 추출
   - 저장: 기본 색상, 보조 색상, 강조색

### 맥락이 보통/빈약한 경우 추가 조사:

4. **업종 맥락**
   - 검색: `"[Industry]" trends challenges 2025 2026`
   - 추출: 흔한 고통 지점, 시장 역학

5. **기술 환경**
   - 검색: `"[Company]" technology stack tools platforms`
   - 추출: 현재 솔루션, 잠재 통합 지점

6. **경쟁 맥락**
   - 검색: `"[Company]" vs [seller's competitors]`
   - 추출: 현재 솔루션, 전환 신호

### 녹취록/자료가 업로드된 경우:

7. **대화 분석**
   - 추출: 언급된 고통 지점, 의사결정 기준, 반론, 일정
   - 식별: 참조할 핵심 인용문(그들의 정확한 표현 사용)
   - 기록: 특정 용어, 약어, 내부 프로젝트명

---

## 2단계: 구조 결정

### 인터랙티브 랜딩 페이지

| 목적 | 권장 섹션 |
|---------|---------------------|
| **소개** | 회사 적합성 → 솔루션 개요 → 핵심 사용 사례 → 우리가 필요한 이유 → 다음 단계 |
| **Discovery 후속** | 그들의 우선순위 → 우리가 돕는 방식 → 관련 예시 → ROI 프레임워크 → 다음 단계 |
| **기술 심층 분석** | 아키텍처 → 보안 및 컴플라이언스 → 통합 → 성능 → 지원 |
| **임원 정렬** | 전략적 적합성 → 비즈니스 영향 → ROI 계산기 → 리스크 완화 → 파트너십 |
| **POC 제안** | 범위 → 성공 기준 → 일정 → 팀 → 투자 → 다음 단계 |
| **딜 종료** | 가치 요약 → 가격 → 구현 계획 → 조건 → 서명 |

**대상별 조정:**
- **임원**: 비즈니스 영향, ROI, 전략적 정렬부터 시작
- **기술**: 아키텍처, 보안, 통합 깊이부터 시작
- **운영**: 워크플로 영향, 변화 관리, 지원부터 시작
- **혼합**: 전략과 전술을 균형 있게; 깊이를 탭으로 분리

### 덱 스타일

같은 섹션을 선형 슬라이드로 구성합니다.

```
1. 제목 슬라이드(잠재 고객 + 셀러 로고, 파트너십 프레이밍)
2. 아젠다
3-N. 슬라이드당 한 섹션(밀도 높은 섹션은 2-3장)
N+1. 요약 / 핵심 시사점
N+2. 다음 단계 / CTA
N+3. 부록(선택 — 상세 사양, 가격 등)
```

**슬라이드 원칙:**
- 슬라이드당 하나의 핵심 메시지
- 시각적 요소를 우선, 텍스트 과다 금지
- 잠재 고객의 지표와 언어 사용
- 발표자 노트 포함

### 원페이저

한 페이지 요약 형식으로 압축합니다.

```
┌─────────────────────────────────────┐
│ HERO: "[Prospect Goal] with [Product]" │
├─────────────────────────────────────┤
│ KEY POINT 1     │ KEY POINT 2     │ KEY POINT 3     │
│ [Icon + 2-3     │ [Icon + 2-3     │ [Icon + 2-3     │
│  sentences]     │  sentences]     │  sentences]     │
├─────────────────────────────────────┤
│ PROOF POINT: [Metric, quote, or case study] │
├─────────────────────────────────────┤
│ CTA: [Clear next action] │ [Contact info] │
└─────────────────────────────────────┘
```

### 워크플로 / 아키텍처 데모

**복잡도에 따른 구조:**

| 복잡도 | 구성 요소 | 구조 |
|------------|------------|-----------|
| **단순** | 3-5 | 단계 주석이 있는 단일 뷰 다이어그램 |
| **중간** | 5-10 | 단계별 안내가 있는 확대 가능한 캔버스 |
| **복잡** | 10+ | 가이드 투어가 있는 다층 뷰(개요 → 상세) |

**표준 요소:**

1. **제목 바**: `[Scenario Name] — Powered by [Seller Product]`
2. **구성 요소 노드**: 각 시스템을 나타내는 시각적 박스/아이콘
3. **흐름 화살표**: 데이터 이동을 보여주는 애니메이션 연결선
4. **단계 패널**: 현재 단계를 쉬운 언어로 설명하는 사이드바
5. **제어**: 재생 / 일시정지 / 한 단계 앞으로 / 한 단계 뒤로 / 초기화
6. **주석**: 핵심 의사결정 지점과 부가 가치를 짚는 콜아웃
7. **데이터 미리보기**: 각 단계의 샘플 payload 또는 변환 결과

---

## 3단계: 콘텐츠 생성

### 일반 원칙

모든 콘텐츠는 다음을 충족해야 합니다.
- 사용자 입력이나 녹취록의 **구체적인 고통 지점**을 참조
- **잠재 고객의 언어** 사용 — 그들의 용어, 그들이 말한 우선순위
- **셀러 제품** → **잠재 고객의 필요**를 명확히 연결
- 가능하면 **증거 포인트** 포함(사례 연구, 지표, 인용문)
- **템플릿이 아니라 맞춤형**처럼 느껴져야 함

### 섹션 템플릿

#### 히어로 / 소개
```
Headline: "[Prospect's Goal] with [Seller's Product]"
Subhead: 그들이 말한 우선순위나 업계의 주요 과제와 연결
Metrics: 잠재 고객에 대한 3-4개의 핵심 사실(조사를 했다는 신호)
```

#### 그들의 우선순위(Discovery 후속인 경우)
```
대화에서 나온 구체적인 고통 지점을 참조:
- 가능하면 그들의 정확한 표현 사용
- 우리가 듣고 이해했다는 것을 보여 줌
- 각각을 우리가 돕는 방식과 연결
```

#### 솔루션 매핑
```
각 고통 지점마다:
├── The challenge (in their words)
├── How [Product] addresses it
├── Proof point or example
└── Outcome / benefit
```

#### 사용 사례 / 데모
```
관련된 3-5개의 사용 사례:
├── Visual mockup or interactive demo
├── Business impact (quantified if possible)
├── "How it works" — 3-4 step summary
└── Relevant to their industry/role
```

#### ROI / 비즈니스 케이스
```
다음이 포함된 인터랙티브 계산기:
├── Inputs relevant to their business (from research)
│   ├── Number of users/developers
│   ├── Current costs or time spent
│   └── Expected improvement %
├── Outputs:
│   ├── Annual value / savings
│   ├── Cost of solution
│   ├── Net ROI
│   └── Payback period
└── Assumptions clearly stated (editable)
```

#### 왜 우리인가 / 차별점
```
├── Differentiators vs. alternatives they might consider
├── Trust, security, compliance positioning
├── Support and partnership model
└── Customer proof points (logos, quotes, case studies)
```

#### 다음 단계 / CTA
```
├── Clear action aligned to Purpose (c)
├── Specific next step (not vague "let's chat")
├── Contact information
├── Suggested timeline
└── What happens after they take action
```

### 워크플로 데모 콘텐츠

#### 구성 요소 정의

각 시스템에 대해 정의합니다:

```yaml
component:
  id: "snowflake"
  label: "Snowflake Data Warehouse"
  type: "database"  # database | api | ai | middleware | human | document | output
  icon: "database"
  description: "Financial performance data"
  brand_color: "#29B5E8"
```

**구성 요소 유형:**
- `human` — 시작하거나 받는 사람
- `document` — PDF, 계약서, 파일
- `ai` — AI/ML 모델, 에이전트
- `database` — 데이터 저장소, 웨어하우스
- `api` — API, 서비스
- `middleware` — 통합 플랫폼, MCP 서버
- `output` — 대시보드, 보고서, 알림

#### 흐름 단계

각 단계에 대해 정의합니다:

```yaml
step:
  number: 1
  from: "human"
  to: "claude"
  action: "Initiates performance review"
  description: "Sarah, a Brand Analyst at [Prospect], kicks off the quarterly review..."
  data_example: "Review request: Nike brand, Q4 2025"
  duration: "~1 second"
  value_note: "No manual data gathering required"
```

#### 시나리오 서사

명확하고 구체적인 walkthrough를 작성합니다.

```
Step 1: Human Trigger
"Sarah, a Brand Performance Analyst at Centric Brands, needs to review
Q4 performance for the Nike license agreement. She opens the review
dashboard and clicks 'Start Review'..."

Step 2: Contract Analysis
"Claude retrieves the Nike contract PDF and extracts the performance
obligations: minimum $50M revenue, 12% margin requirement, quarterly
reporting deadline..."

Step 3: Data Query
"Claude formulates a query and sends it to Workato DataGenie:
'Get Q4 2025 revenue and gross margin for Nike brand from Snowflake'..."

Step 4: Results & Synthesis
"Snowflake returns the data. Claude compares actuals vs. obligations:
Revenue $52.3M ✓ (exceeded by $2.3M)
Margin 11.2% ⚠️ (0.8% below threshold)..."

Step 5: Insight Delivery
"Claude synthesizes findings into an executive summary with
recommendations: 'Review promotional spend allocation to improve
margin performance...'"
```

---

## 4단계: 시각 디자인

### 색상 체계

```css
:root {
    /* === 잠재 고객 브랜드(주요) === */
    --brand-primary: #[extracted from research];
    --brand-secondary: #[extracted];
    --brand-primary-rgb: [r, g, b]; /* For rgba() usage */

    /* === 다크 테마 기본 === */
    --bg-primary: #0a0d14;
    --bg-elevated: #0f131c;
    --bg-surface: #161b28;
    --bg-hover: #1e2536;

    /* === 텍스트 === */
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --text-muted: rgba(255, 255, 255, 0.5);

    /* === 강조색 === */
    --accent: var(--brand-primary);
    --accent-hover: var(--brand-secondary);
    --accent-glow: rgba(var(--brand-primary-rgb), 0.3);

    /* === 상태 === */
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
}
```

### 타이포그래피

```css
/* Primary: 깔끔하고 전문적인 산세리프 */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* 제목 */
h1: 2.5rem, font-weight: 700
h2: 1.75rem, font-weight: 600
h3: 1.25rem, font-weight: 600

/* 본문 */
body: 1rem, font-weight: 400, line-height: 1.6

/* 캡션/라벨 */
small: 0.875rem, font-weight: 500
```

### 시각 요소

**카드:**
- 배경: `var(--bg-surface)`
- 테두리: 1px solid rgba(255,255,255,0.1)
- 테두리 반경: 12px
- 그림자: 은은하고 레이어감 있게
- 호버: 살짝 떠오르고 테두리 글로우

---

## 예시

### 예시 1: 임원 랜딩 페이지

**입력:**
- 잠재 고객: Acme Corp
- 대상: CFO와 COO
- 목적: Discovery 후속
- 형식: 인터랙티브 랜딩 페이지
- 자료: 최근 통화 녹취록, 3개의 핵심 우려, 예산 정보

**출력 구조:**
```
[탭형 랜딩 페이지]

[Hero 탭]
- Acme의 목표와 맥락
- 우리가 그들을 이해하고 있다는 신호

[우선순위 탭]
- Discovery에서 말한 우선순위
- 우리 제품이 해결하는 방식

[ROI 탭]
- 할인 없이 1년 내 가치
- 입력 조정 가능 계산기

[다음 단계 탭]
- 명확한 행동
- 후속 일정
```

### 예시 2: 기술 워크플로 데모

**입력:**
- 잠재 고객: Centric Brands
- 대상: IT 아키텍트
- 목적: POC 제안
- 형식: 워크플로 데모
- 구성 요소: Claude, Workato DataGenie, Snowflake, PDF 계약서

**출력 구조:**
```
[5개 노드의 인터랙티브 캔버스]
Human → Claude → PDF Contracts → Workato → Snowflake
         ↓
    [Results back to Human]

[단계별 샘플 데이터 워크스루]
[제어: Play | Pause | Step | Reset]
```

### 예시 3: 영업 원페이저

**입력:**
- 잠재 고객: TechStart Inc
- 대상: VP Engineering
- 목적: 첫 미팅 후 남겨두는 자료
- 형식: 원페이저

**출력 구조:**
```
Hero: "Accelerate TechStart's Product Velocity"
Point 1: [Dev productivity]
Point 2: [Code quality]
Point 3: [Time to market]
Proof: "Similar companies saw 40% faster releases"
CTA: "Schedule technical deep-dive"
```

---

## 부록: 구성 요소 아이콘

워크플로 데모에서는 다음 아이콘 매핑을 사용합니다.

| 유형 | 아이콘 | 예시 |
|------|------|---------|
| human | 👤 or person SVG | User, Analyst, Admin |
| document | 📄 or file SVG | PDF, Contract, Report |
| ai | 🤖 or brain SVG | Claude, AI Agent |
| database | 🗄️ or cylinder SVG | Snowflake, Postgres |
| api | 🔌 or plug SVG | REST API, GraphQL |
| middleware | ⚡ or hub SVG | Workato, MCP Server |
| output | 📊 or screen SVG | Dashboard, Report |

---

## 부록: 브랜드 색상 대체값

브랜드 색상을 추출할 수 없으면 다음을 사용합니다.

| 업종 | Primary | Secondary |
|----------|---------|-----------|
| Technology | #2563eb | #7c3aed |
| Finance | #0f172a | #3b82f6 |
| Healthcare | #0891b2 | #06b6d4 |
| Manufacturing | #ea580c | #f97316 |
| Retail | #db2777 | #ec4899 |
| Energy | #16a34a | #22c55e |
| Default | #3b82f6 | #8b5cf6 |

---

*일반화된 영업 자산 생성을 위해 만든 스킬입니다. 어떤 셀러, 어떤 제품, 어떤 잠재 고객에도 사용할 수 있습니다.*
