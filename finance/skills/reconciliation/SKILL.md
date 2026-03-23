---
name: reconciliation
description: GL 잔액을 보조원장, 은행 명세서, 제3자 데이터와 비교해 계정을 조정합니다. 은행 조정, GL-보조원장 조정, 인터컴퍼니 조정을 수행하거나 조정 항목을 식별/분류할 때 사용합니다.
argument-hint: "<account> [period]"
---

# Reconciliation

**Important**: This skill assists with reconciliation workflows but does not provide financial advice. All reconciliations should be reviewed by qualified financial professionals before sign-off.

계정 조정 방법론과 베스트 프랙티스입니다. GL-보조원장, 은행 조정, 인터컴퍼니 조정을 포함하고, 조정 항목 분류, aging 분석, 에스컬레이션을 다룹니다.

## Reconciliation Types

### GL to Subledger Reconciliation

총계정원장 통제 계정 잔액과 상세 보조원장 잔액을 비교합니다.

**Common accounts:**
- Accounts receivable (GL control vs AR subledger aging)
- Accounts payable (GL control vs AP subledger aging)
- Fixed assets (GL control vs fixed asset register)
- Inventory (GL control vs inventory valuation report)
- Prepaid expenses (GL control vs prepaid amortization schedule)
- Accrued liabilities (GL control vs accrual detail schedules)

**Process:**
1. 기간 말 기준 통제 계정의 GL 잔액을 가져옵니다
2. 같은 날짜 기준 보조원장 시산표 또는 상세 리포트를 가져옵니다
3. 합계를 비교합니다 - 실시간 게시라면 일치해야 합니다
4. 차이를 조사합니다(게시 타이밍, 반영되지 않은 수동 분개, 인터페이스 오류)

**Common causes of differences:**
- 수동 분개가 통제 계정에만 게시되고 보조원장에는 반영되지 않음
- 보조원장 거래가 아직 GL로 인터페이스되지 않음
- 배치 게시의 타이밍 차이
- GL에서의 재분류 분개가 보조원장 조정 없이 수행됨
- 시스템 인터페이스 오류 또는 게시 실패

### Bank Reconciliation

GL 현금 잔액과 은행 명세서 잔액을 비교합니다.

**Process:**
1. 기간 말 기준 은행 명세서 잔액을 가져옵니다
2. 같은 날짜 기준 GL 현금 계정 잔액을 가져옵니다
3. 미청구 수표(발행되었지만 은행에서 아직 결제되지 않음)를 식별합니다
4. 계좌 이체 중 입금(장부에는 기록되었지만 은행에는 아직 미반영)을 식별합니다
5. GL에 아직 기록되지 않은 은행 수수료, 이자, 조정을 식별합니다
6. 양쪽을 조정된 잔액으로 맞춥니다

**Standard format:**

```text
Balance per bank statement:         $XX,XXX
Add: Deposits in transit            $X,XXX
Less: Outstanding checks           ($X,XXX)
Add/Less: Bank errors               $X,XXX
Adjusted bank balance:              $XX,XXX

Balance per general ledger:         $XX,XXX
Add: Interest/credits not recorded  $X,XXX
Less: Bank fees not recorded       ($X,XXX)
Add/Less: GL errors                 $X,XXX
Adjusted GL balance:                $XX,XXX

Difference:                         $0.00
```

### Intercompany Reconciliation

관련 법인 간 잔액을 조정해 연결 시 0이 되도록 확인합니다.

**Process:**
1. 각 법인 쌍의 인터컴퍼니 채권/채무 잔액을 가져옵니다
2. Entity A의 Entity B에 대한 채권과 Entity B의 Entity A에 대한 채무를 비교합니다
3. 차이를 식별하고 해결합니다
4. 모든 인터컴퍼니 거래가 양쪽에 기록되었는지 확인합니다
5. 연결을 위한 제거 분개가 올바른지 확인합니다

**Common causes of differences:**
- 한 법인에만 기록되고 다른 법인에는 아직 반영되지 않음(타이밍)
- 법인별로 다른 FX 환율 사용
- 잘못된 분류(인터컴퍼니 vs 제3자)
- 분쟁 금액 또는 미적용 지급
- 법인 간 서로 다른 기간 말 컷오프 관행

## Reconciling Item Categorization

### Category 1: Timing Differences

정상적인 처리 타이밍 때문에 존재하고, 조치 없이 해소되는 항목:

- **Outstanding checks:** 수표는 발행되어 GL에 기록되었지만 은행 청산 대기
- **Deposits in transit:** 입금은 GL에 기록되었지만 은행 입금 대기
- **In-transit transactions:** 한 시스템에는 게시되었지만 다른 쪽 인터페이스 대기
- **Pending approvals:** 한 시스템에 게시되기 위해 승인 대기 중인 거래

**Expected resolution:** 정상 처리 사이클(보통 1-5영업일) 내에 해소되어야 합니다. 조정 분개는 필요 없습니다.

### Category 2: Adjustments Required

수정용 분개가 필요한 항목:

- **Unrecorded bank charges:** 은행 수수료, 송금 수수료, 반환 항목 수수료
- **Unrecorded interest:** 은행/대출기관의 이자 수익 또는 비용
- **Recording errors:** 잘못된 금액, 잘못된 계정, 중복
- **Missing entries:** 한 시스템에만 있고 다른 쪽에는 대응 분개가 없음
- **Classification errors:** 올바르게 기록되었지만 잘못된 계정에 있음

**Action:** GL 또는 보조원장을 수정하는 조정 분개 준비

### Category 3: Requires Investigation

즉시 설명되지 않는 항목:

- **Unidentified differences:** 명확한 원인이 없는 차이
- **Disputed items:** 당사자 간 분쟁 금액
- **Aged outstanding items:** 예상 기간 내에 해소되지 않은 항목
- **Recurring unexplained differences:** 매 기간 반복되는 같은 유형의 차이

**Action:** 근본 원인을 조사하고, 결과를 문서화하고, 해결되지 않으면 에스컬레이션

## Aging Analysis for Outstanding Items

조정 항목의 나이를 추적해 오래된 항목을 식별하고 에스컬레이션합니다:

| Age Bucket | Status | Action |
|-----------|--------|--------|
| 0-30 days | Current | Monitor — within normal processing cycle |
| 31-60 days | Aging | Investigate — follow up on why item has not cleared |
| 61-90 days | Overdue | Escalate — notify supervisor, document investigation |
| 90+ days | Stale | Escalate to management — potential write-off or adjustment needed |

### Aging Report Format

| Item # | Description | Amount | Date Originated | Age (Days) | Category | Status | Owner |
|--------|-------------|--------|-----------------|------------|----------|--------|-------|
| 1      | [Detail]    | $X,XXX | [Date]          | XX         | [Type]   | [Status] | [Name] |

### Trending

조정 항목 총액을 시간에 따라 추적해 증가하는 잔액을 식별합니다:

- 총 미해결 항목을 이전 기간과 비교
- 총 조정 항목이 중요성 기준을 넘으면 표시
- 항목 수가 기간별로 증가하면 표시
- 매 기간 반복되는 항목을 식별(프로세스 문제를 시사할 수 있음)

## Escalation Thresholds

조직의 위험 감수 수준에 맞게 에스컬레이션 트리거를 정의합니다:

| Trigger | Threshold (Example) | Escalation |
|---------|---------------------|------------|
| Individual item amount | > $10,000 | Supervisor review |
| Individual item amount | > $50,000 | Controller review |
| Total reconciling items | > $100,000 | Controller review |
| Item age | > 60 days | Supervisor follow-up |
| Item age | > 90 days | Controller / management review |
| Unreconciled difference | Any amount | Cannot close — must resolve or document |
| Growing trend | 3+ consecutive periods | Process improvement investigation |

*Note: Set thresholds based on your organization's materiality level and risk appetite. The examples above are illustrative.*

## Reconciliation Best Practices

1. **Timeliness:** 마감 캘린더 기한 내에 조정을 완료(보통 기간 말 후 T+3~T+5영업일)
2. **Completeness:** 정의된 빈도로 모든 대차대조표 계정을 조정(중요한 계정은 매월, 중요하지 않은 계정은 분기별)
3. **Documentation:** 모든 조정에는 작성자, 검토자, 날짜, 모든 조정 항목에 대한 명확한 설명 포함
4. **Segregation:** 조정한 사람이 같은 계정의 거래를 처리한 사람이면 안 됨
5. **Follow-through:** 항목을 무기한 이월하지 말고 해결까지 추적
6. **Root cause analysis:** 반복되는 조정 항목은 근본 프로세스 문제를 조사하고 수정
7. **Standardization:** 모든 계정에 일관된 템플릿과 절차 사용
8. **Retention:** 조직의 문서 보존 정책에 따라 조정과 지원 세부 정보를 보관
