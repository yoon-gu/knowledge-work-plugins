---
name: competitive-brief
description: 하나 이상의 경쟁사 또는 기능 영역에 대한 경쟁 분석 브리핑을 만듭니다. 제품 전략이나 기능 우선순위를 정할 때, 세일즈 배틀카드를 만들 때, 이사회나 투자자 자료를 준비할 때, 차별화와 동등화 중 어디에 집중할지 결정할 때 사용합니다.
argument-hint: "<competitor or feature area>"
---

# 경쟁 브리핑

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

하나 이상의 경쟁사 또는 기능 영역에 대한 경쟁 분석 브리핑을 만듭니다.

## 사용법

```
/competitive-brief $ARGUMENTS
```

## 워크플로

### 1. 분석 범위 정하기

Ask the user:
- **Competitor(s)**: 어떤 경쟁사를 분석할까요? 아니면 경쟁사 간 비교할 기능 영역인가요?
- **Focus**: 전체 제품 비교, 특정 기능 영역, 가격/패키징, go-to-market, 포지셔닝 중 무엇인가요?
- **Context**: 이 분석이 어떤 결정을 돕나요? (제품 전략, 세일즈 활성화, 투자자/이사회 자료, 기능 우선순위)

### 2. 조사

**Via web search**:
- Product pages and feature lists
- Pricing pages and packaging
- Recent product launches, blog posts, and changelogs
- Press coverage and analyst reports
- Customer reviews and ratings (G2, Capterra, TrustRadius)
- Job postings (signal of strategic direction)
- Social media and community discussions

If **~~knowledge base** is connected:
- Search for existing competitive analysis documents
- Find win/loss reports or sales battle cards
- Pull prior competitive research

If **~~chat** is connected:
- Search for competitive mentions in sales or product channels
- Find recent deal feedback involving competitors

### 3. 브리핑 생성

#### 경쟁사 개요
For each competitor:
- Company summary: founding, size, funding/revenue if public, target market
- Product positioning: how they describe themselves, who they target
- Recent momentum: launches, funding, partnerships, customer wins

#### 기능 비교
Compare capabilities across key areas relevant to the analysis. See **Feature Comparison Matrices** below for rating scales and matrix templates.

#### 포지셔닝 분석
Analyze how each competitor positions themselves — target customer, category claim, key differentiator, and value proposition. See **Positioning Analysis Frameworks** below for the positioning statement template and message architecture levels.

#### 강점과 약점
For each competitor:
- **Strengths**: Where they genuinely excel. What customers praise.
- **Weaknesses**: Where they fall short. What customers complain about.
- Be honest and evidence-based — do not dismiss competitors or inflate their weaknesses.

#### 기회
Based on the analysis:
- Where are there gaps in competitor offerings we could exploit?
- What are customers asking for that no one provides well?
- Where are competitors making bets we disagree with?
- What market shifts could advantage our approach?

#### 위협
- Where are competitors investing heavily?
- What competitive moves could disrupt our position?
- Where are we most vulnerable?
- What would a "nightmare scenario" competitive move look like?

#### 전략적 시사점
Tie the analysis back to product strategy:
- What should we build, accelerate, or deprioritize based on this analysis?
- Where should we differentiate vs. achieve parity?
- How should we adjust positioning or messaging?
- What should we monitor going forward?

### 4. 후속 조치

After generating the brief:
- Ask if the user wants to dive deeper on any section
- Offer to create a one-page summary for executives
- Offer to create sales battle cards for competitive deals
- Offer to draft a "how to win against [competitor]" guide
- Offer to set up a monitoring plan for competitive moves

## 경쟁 환경 맵핑

### 경쟁 세트 식별
Define competitors at multiple levels:

**직접 경쟁사**: 같은 사용자에게 같은 방식으로 같은 문제를 푸는 제품입니다.
- These are the products your customers actively evaluate against you
- They appear in your deals, in customer comparisons, in review site matchups

**간접 경쟁사**: 같은 문제를 다른 방식으로 푸는 제품입니다.
- Different approach to the same user need (e.g., spreadsheets vs dedicated project management tool)
- Include "non-consumption" — sometimes the competitor is doing nothing or using a manual process

**인접 경쟁사**: 지금은 경쟁하지 않지만 경쟁자가 될 수 있는 제품입니다.
- Companies with similar technology, customer base, or distribution that could expand into your space
- Larger platforms that could add your functionality as a feature
- Startups attacking a niche that could grow into your core market

**대체 솔루션**: 사용자가 근본적인 필요를 해결하는 전혀 다른 방식입니다.
- Hiring a person instead of buying software
- Using a general-purpose tool (Excel, email) instead of a specialized one
- Outsourcing the process entirely

### 환경 맵
Position competitors on meaningful dimensions:

**Common axes**:
- Breadth vs depth (suite vs point solution)
- SMB vs enterprise (market segment focus)
- Self-serve vs sales-led (go-to-market approach)
- Simple vs powerful (product complexity)
- Horizontal vs vertical (general purpose vs industry-specific)

Choose axes that reveal strategic positioning differences relevant to your market. The right axes make competitive dynamics visible.

### 환경 모니터링
Track competitive movements over time:
- Product launches and feature releases (changelogs, blog posts, press releases)
- Pricing and packaging changes
- Funding rounds and acquisitions
- Key hires and job postings (signal strategic direction)
- Customer wins and losses (especially your wins/losses)
- Analyst and review coverage
- Partnership announcements

## 기능 비교 매트릭스

### 기능 비교 만들기
1. **Define capability areas**: Group features into functional categories that matter to buyers (not your internal architecture). Use the categories buyers use when evaluating.
2. **List specific capabilities**: Under each area, list the specific features or capabilities to compare.
3. **Rate each competitor**: Use a consistent rating scale.

### 평가 척도 옵션

**Simple (recommended for most cases)**:
- Strong: Market-leading capability. Deep functionality, well-executed.
- Adequate: Functional capability. Gets the job done but not differentiated.
- Weak: Exists but limited. Significant gaps or poor execution.
- Absent: Does not have this capability.

**Detailed (for deep-dive comparisons)**:
- 5: Best-in-class. Defines the standard others aspire to.
- 4: Strong. Fully-featured and well-executed.
- 3: Adequate. Meets basic needs without differentiation.
- 2: Limited. Exists but with significant gaps.
- 1: Minimal. Barely functional or in early beta.
- 0: Absent. Not available.

### 비교 매트릭스 템플릿
```
| Capability Area | Our Product | Competitor A | Competitor B |
|----------------|-------------|-------------|-------------|
| [Area 1]       |             |             |             |
|   [Feature 1]  | Strong      | Adequate    | Absent      |
|   [Feature 2]  | Adequate    | Strong      | Weak        |
| [Area 2]       |             |             |             |
|   [Feature 3]  | Strong      | Strong      | Adequate    |
```

### 기능 비교 팁
- Rate based on real product experience, customer feedback, and reviews — not just marketing claims
- Features exist on a spectrum. "Has feature X" is less useful than "How well does it do X?"
- Weight the comparison by what matters to your target customers, not by total feature count
- Update regularly — feature comparisons get stale fast
- Be honest about where competitors are ahead. A comparison that always shows you winning is not credible.
- Include the "why it matters" for each capability area. Not all features matter equally to buyers.

## 포지셔닝 분석 프레임워크

### 포지셔닝 문장 분석
For each competitor, extract their positioning:

**Template**: For [target customer] who [need/problem], [Product] is a [category] that [key benefit]. Unlike [competitor/alternative], [Product] [key differentiator].

**Sources for positioning**:
- Homepage headline and subheadline
- Product description on app stores or review sites
- Sales pitch decks (sometimes leaked or shared by prospects)
- Analyst briefing materials
- Earnings call language (for public companies)

### 메시지 아키텍처 분석
How does each competitor communicate value?

**Level 1 — Category**: What category do they claim? (CRM, project management, collaboration platform)
**Level 2 — Differentiator**: What makes them different within that category? (AI-powered, all-in-one, developer-first)
**Level 3 — Value Proposition**: What outcome do they promise? (Close deals faster, ship products faster, never miss a deadline)
**Level 4 — Proof Points**: What evidence do they provide? (Customer logos, metrics, awards, case studies)

### 포지셔닝 공백과 기회
Look for:
- **Unclaimed positions**: Value propositions no competitor owns that matter to buyers
- **Crowded positions**: Claims every competitor makes that have lost meaning
- **Emerging positions**: New value propositions driven by market changes (AI, remote work, compliance)
- **Vulnerable positions**: Claims competitors make that they cannot fully deliver on

## Win/Loss 분석 방법론

### Win/Loss 분석 수행
Win/loss analysis reveals why you actually win and lose deals. It is the most actionable competitive intelligence.

**Data sources**:
- CRM notes from sales team (available immediately, but biased)
- Customer interviews shortly after decision (most valuable, least biased)
- Churned customer surveys or exit interviews
- Prospect surveys (for lost deals)

### Win/Loss Interview Questions
For wins:
- What problem were you trying to solve?
- What alternatives did you evaluate? (Reveals competitive set)
- Why did you choose us over alternatives?
- What almost made you choose someone else?
- What would we need to lose for you to reconsider?

For losses:
- What problem were you trying to solve?
- What did you end up choosing? Why?
- Where did our product fall short?
- What could we have done differently?
- Would you reconsider us in the future? Under what conditions?

### Analyzing Win/Loss Data
- Track win/loss reasons over time. Are patterns changing?
- Segment by deal type: enterprise vs SMB, new vs expansion, industry vertical
- Identify the top 3-5 reasons for wins and losses
- Distinguish between product reasons (features, quality) and non-product reasons (pricing, brand, relationship, timing)
- Calculate competitive win rates by competitor: what % of deals involving each competitor do you win?

### Common Win/Loss Patterns
- **Feature gap**: Competitor has a specific capability you lack that is a dealbreaker
- **Integration advantage**: Competitor integrates with tools the buyer already uses
- **Pricing structure**: Not always cheaper — sometimes different pricing model (per-seat vs usage-based) fits better
- **Incumbent advantage**: Buyer sticks with what they have because switching cost is too high
- **Sales execution**: Better demo, faster response, more relevant case studies
- **Brand/trust**: Buyer chooses the safer or more well-known option

## Market Trend Identification

### Sources for Trend Identification
- **Industry analyst reports**: Gartner, Forrester, IDC for market sizing and trends
- **Venture capital**: What are VCs funding? Investment themes signal where smart money sees opportunity.
- **Conference themes**: What are industry events focusing on? What topics draw the biggest audiences?
- **Technology shifts**: New platforms, APIs, or capabilities that enable new product categories
- **Regulatory changes**: New regulations that create requirements or opportunities
- **Customer behavior changes**: How are user expectations evolving? (e.g., mobile-first, AI-assisted, privacy-conscious)
- **Talent movement**: Where are top people going? What skills are in demand?

### Trend Analysis Framework
For each trend identified:

1. **What is changing?**: Describe the trend clearly and specifically
2. **Why now?**: What is driving this change? (Technology, regulation, behavior, economics)
3. **Who is affected?**: Which customer segments or market categories?
4. **What is the timeline?**: Is this happening now, in 1-2 years, or 3-5 years?
5. **What is the implication for us?**: How should this influence our product strategy?
6. **What are competitors doing?**: How are competitors responding to this trend?

### Separating Signal from Noise
- **Signals**: Trends backed by behavioral data, growing investment, regulatory action, or customer demand
- **Noise**: Trends backed only by media hype, conference buzz, or competitor announcements without customer traction
- Test trends against your own customer data: are YOUR customers asking for this or experiencing this change?
- Be wary of "trend of the year" hype cycles. Many trends that dominate industry conversation do not materially affect your customers for years.

### Strategic Response Options
For each significant trend:
- **Lead**: Invest early and try to define the category or approach. High risk, high reward.
- **Fast follow**: Wait for early signals of customer demand, then move quickly. Lower risk but harder to differentiate.
- **Monitor**: Track the trend but do not invest yet. Set triggers for when to act.
- **Ignore**: Explicitly decide this trend is not relevant to your strategy. Document why.

The right response depends on: your competitive position, your customer base, your resources, and how fast the trend is moving.

## Output Format

Use tables for feature comparisons. Use clear headers for each section. Keep the strategic implications section concise and actionable — this is where the value is for the reader.

## Tips

- Be honest about competitor strengths. Dismissing competitors makes the analysis useless.
- Focus on what matters to customers, not what matters to product teams. Customers do not care about architecture elegance.
- Pricing is hard to compare fairly. Note the caveats (different packaging, usage-based vs seat-based, enterprise custom pricing).
- Job postings are underrated competitive intelligence. A competitor hiring ML engineers signals a strategic direction.
- Customer reviews are gold. They reveal what real users love and hate, unfiltered by marketing.
- The most valuable part of competitive analysis is the "so what" — the strategic implications. Do not skip this.
- Competitive analysis has a shelf life. Note the date and flag areas that change quickly.
