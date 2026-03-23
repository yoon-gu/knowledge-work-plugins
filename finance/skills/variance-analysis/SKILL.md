---
name: variance-analysis
description: 재무 차이를 동인으로 분해하고 서술 설명과 워터폴 분석을 제공합니다. 예산 대비 실제, 기간 대비 변화, 매출/비용 차이, 경영진용 차이 코멘터리를 준비할 때 사용합니다.
argument-hint: "<line item> <period> vs <comparison>"
---

# Variance Analysis

**Important**: This skill assists with variance analysis workflows but does not provide financial advice. All analyses should be reviewed by qualified financial professionals before use in reporting.

차이 분해 기법, 중요성 기준, 서술 생성, 워터폴 차트 방법론, 예산 대비 실제 대비 예측 비교를 다룹니다.

## Variance Decomposition Techniques

### Price / Volume Decomposition

가장 기본적인 차이 분해입니다. 매출, 매출원가, 그리고 가격 × 수량으로 표현할 수 있는 지표에 사용합니다.

**Formula:**
```text
Total Variance = Actual - Budget (or Prior)

Volume Effect  = (Actual Volume - Budget Volume) x Budget Price
Price Effect   = (Actual Price - Budget Price) x Actual Volume
Mix Effect     = Residual (interaction term), or allocated proportionally

Verification:  Volume Effect + Price Effect = Total Variance
               (when mix is embedded in the price/volume terms)
```

**Three-way decomposition (separating mix):**
```text
Volume Effect = (Actual Volume - Budget Volume) x Budget Price x Budget Mix
Price Effect  = (Actual Price - Budget Price) x Budget Volume x Actual Mix
Mix Effect    = Budget Price x Budget Volume x (Actual Mix - Budget Mix)
```

**Example — Revenue variance:**
- Budget: 10,000 units at $50 = $500,000
- Actual: 11,000 units at $48 = $528,000
- Total variance: +$28,000 favorable
  - Volume effect: +1,000 units x $50 = +$50,000 (favorable — sold more units)
  - Price effect: -$2 x 11,000 units = -$22,000 (unfavorable — lower ASP)
  - Net: +$28,000

### Rate / Mix Decomposition

서로 다른 단위 경제성을 가진 세그먼트의 혼합 비율을 분석할 때 사용합니다.

**Formula:**
```text
Rate Effect = Sum of (Actual Volume_i x (Actual Rate_i - Budget Rate_i))
Mix Effect  = Sum of (Budget Rate_i x (Actual Volume_i - Expected Volume_i at Budget Mix))
```

**Example — Gross margin variance:**
- Product A: 60% margin, Product B: 40% margin
- Budget mix: 50% A, 50% B → Blended margin 50%
- Actual mix: 40% A, 60% B → Blended margin 48%
- Mix effect explains 2pp of margin compression

### Headcount / Compensation Decomposition

급여와 인건비 차이를 분석할 때 사용합니다.

```text
Total Comp Variance = Actual Compensation - Budget Compensation

Decompose into:
1. Headcount variance    = (Actual HC - Budget HC) x Budget Avg Comp
2. Rate variance         = (Actual Avg Comp - Budget Avg Comp) x Budget HC
3. Mix variance          = Difference due to level/department mix shift
4. Timing variance       = Hiring earlier/later than planned (partial-period effect)
5. Attrition impact      = Savings from unplanned departures (partially offset by backfill costs)
```

### Spend Category Decomposition

가격/수량이 맞지 않는 운영비 분석에 사용합니다.

```text
Total OpEx Variance = Actual OpEx - Budget OpEx

Decompose by:
1. Headcount-driven costs    (salaries, benefits, payroll taxes, recruiting)
2. Volume-driven costs       (hosting, transaction fees, commissions, shipping)
3. Discretionary spend       (travel, events, professional services, marketing programs)
4. Contractual/fixed costs   (rent, insurance, software licenses, subscriptions)
5. One-time / non-recurring  (severance, legal settlements, write-offs, project costs)
6. Timing / phasing          (spend shifted between periods vs plan)
```

## Materiality Thresholds and Investigation Triggers

### 설정 기준

중요성 기준은 어떤 차이를 조사하고 서술해야 하는지 정합니다. 다음에 따라 설정하세요:

1. **재무제표 중요성**: 보통 핵심 기준치(매출, 총자산, 순이익)의 1-5%
2. **라인 항목 크기**: 큰 라인 항목은 더 낮은 백분율 기준이 적절
3. **변동성**: 변동성이 큰 라인 항목은 잡음 방지를 위해 더 높은 기준이 필요할 수 있음
4. **경영진 관심**: 어떤 수준의 차이가 의사결정을 바꾸는가?

### Recommended Threshold Framework

| Comparison Type | Dollar Threshold | Percentage Threshold | Trigger |
|----------------|-----|-----|-----|
| Actual vs Budget | Organization-specific | 10% | Either exceeded |
| Actual vs Prior Year | Organization-specific | 15% | Either exceeded |
| Actual vs Forecast | Organization-specific | 5% | Either exceeded |
| Sequential (MoM) | Organization-specific | 20% | Either exceeded |

*달러 기준은 조직 규모에 맞게 설정하세요. 일반적으로 손익계산서 항목에 대해 매출의 0.5%-1%가 흔한 기준입니다.*

### Investigation Priority

여러 차이가 기준을 넘으면 다음 순서로 조사 우선순위를 정합니다:

1. **가장 큰 절대 금액 차이** — P&L 영향이 가장 큼
2. **가장 큰 퍼센트 차이** — 프로세스 문제나 오류를 시사할 수 있음
3. **예상과 반대 방향** — 추세나 기대와 반대인 차이
4. **새로운 차이** — 정상 궤도였다가 벗어난 항목
5. **누적/추세 차이** — 기간이 지날수록 커지는 항목

## Narrative Generation for Variance Explanations

### 각 차이에 대한 서술 구조

```text
[Line Item]: [Favorable/Unfavorable] variance of $[amount] ([percentage]%)
vs [comparison basis] for [period]

Driver: [Primary driver description]
[2-3 sentences explaining the business reason for the variance, with specific
quantification of contributing factors]

Outlook: [One-time / Expected to continue / Improving / Deteriorating]
Action: [None required / Monitor / Investigate further / Update forecast]
```

### Narrative Quality Checklist

좋은 차이 서술은 다음과 같아야 합니다:

- [ ] **Specific:** "예상보다 높음"이 아니라 실제 동인을 명시
- [ ] **Quantified:** 각 동인의 달러와 퍼센트 영향을 포함
- [ ] **Causal:** 무엇이 일어났는지뿐 아니라 왜 일어났는지 설명
- [ ] **Forward-looking:** 차이가 계속될지 언급
- [ ] **Actionable:** 후속 조치나 결정이 필요한지 식별
- [ ] **Concise:** 채우기 문장이 아닌 2-4문장

### 피해야 할 일반적인 서술 패턴

- "Revenue was higher than budget due to higher revenue" (순환 - 실제 설명 없음)
- "Expenses were elevated this period" (모호 - 어떤 비용인가? 왜인가?)
- "Timing"만 말하고 무엇이 이르거나 늦었는지, 언제 정상화될지 설명하지 않음
- "One-time"이라고만 하고 항목이 무엇인지 설명하지 않음
- "Various small items"라고 하면서 중요한 차이를 대충 넘김
- 가장 큰 동인만 보고 상쇄 항목은 무시

## Waterfall Chart Methodology

### 개념

워터폴(브리지) 차트는 한 값에서 다른 값으로 가는 과정을 여러 양/음 기여 항목을 통해 보여 줍니다. 차이 분해를 시각화할 때 사용합니다.

### 데이터 구조

```text
Starting value:  [Base/Budget/Prior period amount]
Drivers:         [List of contributing factors with signed amounts]
Ending value:    [Actual/Current period amount]

Verification:    Starting value + Sum of all drivers = Ending value
```

### 텍스트 기반 워터폴 형식

차트 도구가 없으면 텍스트 워터폴로 제시합니다:

```text
WATERFALL: Revenue — Q4 Actual vs Q4 Budget

Q4 Budget Revenue                                    $10,000K
  |
  |--[+] Volume growth (new customers)               +$800K
  |--[+] Expansion revenue (existing customers)      +$400K
  |--[-] Price reductions / discounting               -$200K
  |--[-] Churn / contraction                          -$350K
  |--[+] FX tailwind                                  +$50K
  |--[-] Timing (deals slipped to Q1)                 -$150K
  |
Q4 Actual Revenue                                    $10,550K

Net Variance: +$550K (+5.5% favorable)
```

### 브리지 조정 표

워터폴을 조정 표와 함께 보완합니다:

| Driver | Amount | % of Variance | Cumulative |
|--------|--------|---------------|------------|
| Volume growth | +$800K | 145% | +$800K |
| Expansion revenue | +$400K | 73% | +$1,200K |
| Price reductions | -$200K | -36% | +$1,000K |
| Churn / contraction | -$350K | -64% | +$650K |
| FX tailwind | +$50K | 9% | +$700K |
| Timing (deal slippage) | -$150K | -27% | +$550K |
| **Total variance** | **+$550K** | **100%** | |

*참고: 상쇄 항목이 있으면 개별 동인의 퍼센트가 100%를 넘을 수 있습니다.*

### Waterfall Best Practices

1. 동인은 가장 큰 양수부터 가장 큰 음수 순으로(또는 논리적 비즈니스 순서로) 배치
2. 5-8개 동인으로 제한 - 작은 항목은 "Other"로 묶기
3. 워터폴이 조정되는지 확인(시작 + 동인 = 종료)
4. 색상 코드: 유리하면 초록, 불리하면 빨강(시각 차트에서)
5. 각 막대에 금액과 짧은 설명을 함께 라벨링
