---
name: journal-entry-prep
description: 월말 마감을 위한 적절한 차변, 대변, 지원 문서를 갖춘 분개를 준비합니다. 미지급비용, 선급비용 상각, 고정자산 감가상각, 급여 분개, 매출 인식, 또는 수동 분개를 기록할 때 사용합니다.
user-invocable: false
---

# Journal Entry Preparation

**Important**: This skill assists with journal entry workflows but does not provide financial advice. All entries should be reviewed by qualified financial professionals before posting.

분개 준비를 위한 모범 사례, 표준 분개 유형, 문서화 요구사항, 검토 워크플로입니다.

## Standard Accrual Types and Their Entries

### Accounts Payable Accruals

기간 말에 인보이스는 받지 않았지만 수령한 재화나 서비스에 대해 비용을 미지급합니다.

**Typical entry:**
- Debit: 비용 계정(자산 요건을 충족하면 자산화)
- Credit: 미지급 부채

**Sources for calculation:**
- 수령이 확인된 열린 구매 주문
- 서비스는 수행되었지만 청구되지 않은 계약
- 정기 공급업체 약정(공과금, 구독, 전문 서비스)
- 제출되었지만 아직 처리되지 않은 직원 경비 보고서

**Key considerations:**
- 다음 기간에 역전(자동 역전 권장)
- 기간 간 일관된 추정 방법 사용
- 추정의 근거(PO 금액, 계약 조건, 과거 실행률) 문서화
- 미래 추정을 개선하기 위해 실제값 vs 미지급액 추적

### Fixed Asset Depreciation

유형 및 무형 자산에 대해 정기적인 감가상각비를 인식합니다.

**Typical entry:**
- Debit: 감가상각/상각 비용(부서 또는 코스트 센터별)
- Credit: 감가상각누계액/상각누계액

**Depreciation methods:**
- **Straight-line:** (Cost - Salvage) / Useful life — 재무보고에서 가장 일반적
- **Declining balance:** 순장부가액에 고정 비율을 적용하는 가속 상각
- **Units of production:** 총 예상 대비 실제 사용량 또는 생산량 기준

**Key considerations:**
- 고정자산 등록부 또는 스케줄에서 감가상각을 실행
- 신규 취득 자산의 내용연수와 방법이 올바르게 설정되었는지 확인
- 상각/손상으로 제거해야 하는 처분 자산 확인
- 장부 감가상각과 세무 감가상각 추적의 일관성 확보

### Prepaid Expense Amortization

선급비용을 효익 기간에 걸쳐 상각합니다.

**Typical entry:**
- Debit: 비용 계정(보험, 소프트웨어, 임대료 등)
- Credit: 선급비용

**Common prepaid categories:**
- 보험료(보통 12개월 계약)
- 소프트웨어 라이선스와 구독
- 선급 임대료(리스 조건에 따라 적용되는 경우)
- 선급 유지보수 계약
- 컨퍼런스 및 행사 보증금

**Key considerations:**
- 시작/종료일과 월별 금액이 포함된 상각 스케줄 유지
- 전액 비용 처리해야 할 선급 항목(중요하지 않은 금액) 검토
- 취소 또는 해지된 계약으로 인한 조기 상각 확인
- 신규 선급비용이 신속히 스케줄에 추가되는지 확인

### Payroll Accruals

기간의 보상과 관련 비용을 미지급합니다.

**Typical entries:**

*Salary accrual (for pay periods not aligned with month-end):*
- Debit: 급여 비용(부서별)
- Credit: 미지급 급여

*Bonus accrual:*
- Debit: 보너스 비용(부서별)
- Credit: 미지급 보너스

*Benefits accrual:*
- Debit: 복리후생 비용
- Credit: 미지급 복리후생

*Payroll tax accrual:*
- Debit: 급여세 비용
- Credit: 미지급 급여세

**Key considerations:**
- 기간의 영업일 대비 급여 기간을 기준으로 급여 미지급액 계산
- 보너스 미지급은 플랜 조건(목표 금액, 성과 지표, 지급 시점)을 반영
- 고용주 부담 세금과 복리후생(FICA, FUTA, 건강보험, 401k 매칭) 포함
- 정책 또는 관할에 따라 필요하면 PTO/휴가 미지급 부채 추적

### Revenue Recognition

성과 의무와 인도에 따라 매출을 인식합니다.

**Typical entries:**

*기존 이연 매출 인식:*
- Debit: 이연 매출
- Credit: 매출

*새 외상매출금과 함께 매출 인식:*
- Debit: 외상매출금
- Credit: 매출

*선수금으로 받은 매출 이연:*
- Debit: 현금 / 외상매출금
- Credit: 이연 매출

**Key considerations:**
- 고객 계약에 대한 ASC 606의 5단계 프레임워크 따르기
- 각 계약의 개별 성과 의무 식별
- 거래 가격 결정(변동 대가 포함)
- 거래 가격을 성과 의무에 배분
- 성과 의무가 충족될 때 매출 인식
- 감사 지원을 위해 계약 단위 세부 정보 유지

## Supporting Documentation Requirements

모든 분개에는 다음이 있어야 합니다:

1. **Entry description/memo:** 분개가 기록하는 내용과 이유를 명확하고 구체적으로 설명
2. **Calculation support:** 금액 산출 방식(공식, 스케줄, 원천 데이터 참조)
3. **Source documents:** 기초 거래나 이벤트에 대한 참조(PO 번호, 인보이스 번호, 계약 참조, 급여 등록부)
4. **Period:** 분개가 적용되는 회계 기간
5. **Preparer identification:** 누가 언제 분개를 준비했는지
6. **Approval:** 승인 매트릭스에 따른 검토 및 승인 증거
7. **Reversal indicator:** 자동 역전 여부와 역전 날짜

## Review and Approval Workflows

### Typical Approval Matrix

| Entry Type | Amount Threshold | Approver |
|-----------|-----------------|----------|
| Standard recurring | Any amount | Accounting manager |
| Non-recurring / manual | < $50K | Accounting manager |
| Non-recurring / manual | $50K - $250K | Controller |
| Non-recurring / manual | > $250K | CFO / VP Finance |
| Top-side / consolidation | Any amount | Controller or above |
| Out-of-period adjustments | Any amount | Controller or above |

*Note: Thresholds should be set based on your organization's materiality and risk tolerance.*

### Review Checklist

분개를 승인하기 전에 검토자는 다음을 확인해야 합니다:

- [ ] 차변과 대변이 일치하는가(분개가 균형을 이루는가)
- [ ] 올바른 회계 기간인가(이미 닫힌 기간에 입력하지 않았는가)
- [ ] 계정 코드가 존재하고 거래에 적절한가
- [ ] 금액이 수학적으로 정확하고 계산으로 뒷받침되는가
- [ ] 설명이 명확하고 구체적이며 감사 목적에 충분한가
- [ ] 부서/코스트 센터/프로젝트 코딩이 올바른가
- [ ] 처리 방식이 이전 기간 및 회계 정책과 일관적인가
- [ ] 자동 역전이 적절히 설정되어 있는가(미지급액은 역전되어야 함)
- [ ] 지원 문서가 완전하고 참조되었는가
- [ ] 분개 금액이 작성자의 권한 수준 내에 있는가
- [ ] 기존 분개와 중복되지 않는가
- [ ] 비정상적이거나 큰 금액이 설명되고 정당화되는가

## Common Errors to Check For

1. **Unbalanced entries:** 차변과 대변이 일치하지 않음(시스템이 막아야 하지만 수동 분개는 확인)
2. **Wrong period:** 잘못된 또는 이미 닫힌 기간에 분개가 게시됨
3. **Wrong sign:** 차변을 대변으로 입력하거나 그 반대
4. **Duplicate entries:** 같은 거래가 두 번 기록됨(게시 전 중복 확인)
5. **Wrong account:** 잘못된 GL 계정에 게시됨(특히 유사한 계정 코드)
6. **Missing reversal:** 미지급액이 자동 역전으로 설정되지 않아 이중 계상 발생
7. **Stale accruals:** 상황 변화에 맞게 반복 미지급액이 업데이트되지 않음
8. **Round-number estimates:** 실제 계산을 반영하지 않을 수 있는 지나치게 반올림된 금액
9. **Incorrect FX rates:** 잘못된 환율 또는 날짜를 사용한 외화 분개
10. **Missing intercompany elimination:** 상응하는 제거 없이 법인 간 분개가 존재
11. **Capitalization errors:** 자산화되어야 할 비용 또는 비용 처리되어야 할 자산화 항목
12. **Cut-off errors:** 인도 또는 서비스 날짜를 기준으로 잘못된 기간에 기록된 거래
