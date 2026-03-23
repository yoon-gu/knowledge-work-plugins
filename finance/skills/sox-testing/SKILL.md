---
name: sox-testing
description: SOX 샘플 선택, 테스트 워크페이퍼, 통제 평가를 생성합니다. 분기 또는 연간 SOX 404 테스트를 계획할 때, 통제(revenue, P2P, ITGC, close)의 샘플을 뽑을 때, 테스트 워크페이퍼 템플릿을 만들 때, 통제 결함을 평가/분류할 때 사용합니다.
argument-hint: "<control area> [period]"
---

# SOX Compliance Testing

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

**Important**: This command assists with SOX compliance workflows but does not provide audit or legal advice. All testing workpapers and assessments should be reviewed by qualified financial professionals before use in audit documentation.

SOX 404 내부 재무보고 통제를 위한 샘플 선택, 테스트 워크페이퍼 생성, 통제 평가 문서화, 테스트 템플릿을 제공합니다.

## 사용법

```
/sox <control-area> <period>
```

### Arguments

- `control-area` — 테스트할 통제 영역:
  - `revenue-recognition` — 매출 사이클 통제(order-to-cash)
  - `procure-to-pay` 또는 `p2p` — 조달 및 AP 통제(purchase-to-pay)
  - `payroll` — 급여 처리 및 보상 통제
  - `financial-close` — 기간 말 마감 및 보고 통제
  - `treasury` — 현금 관리 및 재무 통제
  - `fixed-assets` — 자본자산 생애주기 통제
  - `inventory` — 재고 평가 및 관리 통제
  - `itgc` — IT 일반 통제(접근, 변경 관리, 운영)
  - `entity-level` — 엔터티 레벨 및 모니터링 통제
  - `journal-entries` — 분개 처리 통제
  - 특정 통제 ID 또는 이름
- `period` — 테스트 기간(예: `2024-Q4`, `2024`, `2024-H2`)

## 워크플로

### 1. 테스트할 통제 식별

통제 영역을 바탕으로 핵심 통제를 식별합니다. 통제 매트릭스를 제시:

| Control # | Control Description | Type | Frequency | Key/Non-Key | Risk | Assertion |
|-----------|-------------------|------|-----------|-------------|------|-----------|
| [ID]      | [Description]     | Manual/Automated/IT-Dependent | Daily/Weekly/Monthly/Quarterly/Annual | Key | High/Medium/Low | [CEAVOP] |

**Control types:**
- **Automated:** 수동 개입 없이 시스템이 강제하는 통제
- **Manual:** 판단이 필요한 사람이 수행하는 통제
- **IT-dependent manual:** 시스템 생성 데이터에 의존하는 수동 통제

**Assertions (CEAVOP):**
- **C**ompleteness — 모든 거래가 기록됨
- **E**xistence/Occurrence — 거래가 실제로 발생함
- **A**ccuracy — 금액이 정확하게 기록됨
- **V**aluation — 자산/부채가 적절히 평가됨
- **O**bligations/Rights — 자산에 대한 권리, 부채에 대한 의무가 있음
- **P**resentation/Disclosure — 적절히 분류되고 공시됨

### 2. 샘플 크기 결정

통제 빈도와 위험에 따라 샘플 크기를 계산합니다:

| Control Frequency | Population Size (approx.) | Recommended Sample |
|------------------|--------------------------|-------------------|
| Annual           | 1                        | 1 (test the instance) |
| Quarterly        | 4                        | 2 |
| Monthly          | 12                       | 2-4 (based on risk) |
| Weekly           | 52                       | 5-15 (based on risk) |
| Daily            | ~250                     | 20-40 (based on risk) |
| Per-transaction  | Varies                   | 25-60 (based on risk and volume) |

다음 요인에 따라 조정:
- **Risk level:** 위험이 높을수록 더 큰 샘플 필요
- **Prior year results:** 전기 결함이 있으면 더 큰 샘플 필요
- **Reliance:** 외부 감사인이 의존하는 통제는 더 큰 샘플이 필요할 수 있음

### 3. 샘플 선택 생성

적절한 방법으로 모집단에서 샘플을 선택:

**Random selection** (거래 수준 통제의 기본):
- 무작위 숫자를 생성해 모집단에서 특정 항목을 선택
- 기간 전체에 걸친 커버리지 보장

**Systematic selection** (주기적 통제용):
- 무작위 시작점과 고정 간격으로 항목 선택
- 모든 하위 기간에 대한 대표성 보장

**Targeted selection** (무작위의 보완, 위험 기반 테스트용):
- 고액, 비정상, 기간 말 등 특정 위험 특성을 가진 항목 선택
- 선택 이유 문서화

### 4. 테스트 워크페이퍼 생성

각 통제에 대한 테스트 템플릿을 생성:

```text
SOX CONTROL TESTING WORKPAPER
==============================
Control #: [ID]
Control Description: [Full description of the control activity]
Control Owner: [Role/title — to be filled by tester]
Control Type: [Manual/Automated/IT-Dependent Manual]
Frequency: [How often the control operates]
Key Control: [Yes/No]
Relevant Assertion(s): [CEAVOP]
Testing Period: [Period]

TEST OBJECTIVE:
To determine whether [control description] operated effectively throughout the testing period.

TEST PROCEDURES:
1. [Step 1 — What to inspect, examine, or re-perform]
2. [Step 2 — What evidence to obtain]
3. [Step 3 — What to compare or verify]
4. [Step 4 — How to evaluate completeness of performance]
5. [Step 5 — How to assess timeliness of performance]

EXPECTED EVIDENCE:
- [Document type 1 — e.g., signed approval form]
- [Document type 2 — e.g., system screenshot showing review]
- [Document type 3 — e.g., reconciliation with preparer sign-off]

TEST RESULTS:

| Sample # | Ref | Procedure 1 | Procedure 2 | Procedure 3 | Result | Exception? | Notes |
|----------|-----|-------------|-------------|-------------|--------|------------|-------|
| 1        |     | Pass/Fail   | Pass/Fail   | Pass/Fail   | Pass/Fail | Y/N    |       |
| 2        |     | Pass/Fail   | Pass/Fail   | Pass/Fail   | Pass/Fail | Y/N    |       |

EXCEPTIONS NOTED:
| Sample # | Exception Description | Root Cause | Compensating Control | Impact |
|----------|----------------------|------------|---------------------|--------|
|          |                      |            |                     |        |

CONCLUSION:
[ ] Effective — Control operated effectively with no exceptions
[ ] Effective with exceptions — Control operated effectively; exceptions are isolated
[ ] Deficiency — Control did not operate effectively
[ ] Significant Deficiency — Deficiency is more than inconsequential
[ ] Material Weakness — Reasonable possibility of material misstatement not prevented/detected

Tested by: ________________  Date: ________
Reviewed by: _______________  Date: ________
```

### 5. 일반적인 통제 템플릿 제공

통제 영역에 따라 미리 작성된 테스트 단계 템플릿을 제공합니다:

**Revenue Recognition:**
- 판매 주문 승인과 권한 확인
- 인도/성과 증거 확인
- 계약 조건 대비 매출 인식 시점 테스트
- 계약/가격표 대비 가격 정확성 확인
- 크레딧 메모 승인과 유효성 테스트

**Procure to Pay:**
- 구매 주문 승인과 권한 한도 확인
- 3-way match 확인(PO, 수령, 인보이스)
- 공급업체 마스터 데이터 변경 통제 테스트
- 지급 승인과 직무 분리 확인
- 중복 지급 방지 통제 테스트

**Financial Close:**
- 계정 조정의 완전성과 시의성 확인
- 분개 승인과 직무 분리 테스트
- 재무제표에 대한 경영진 검토 확인
- 연결 및 제거 분개 테스트
- 공시 체크리스트 완료 확인

**ITGC:**
- 사용자 접근 부여와 회수 테스트
- 특권 접근 검토 확인
- 변경 관리 승인과 테스트 확인
- 배치 작업 모니터링과 예외 처리 확인
- 백업 및 복구 절차 테스트

### 6. 통제 평가 문서화

식별된 결함을 분류:

**Deficiency:** 통제가 경영진이나 직원이 중요한 왜곡표시를 적시에 예방하거나 탐지하게 하지 못함. 다음을 고려:
- 왜곡표시 가능성
- 잠재적 왜곡표시의 규모
- 보완 통제가 있는지

**Significant Deficiency:** 중요한 약점보다 덜 심각하지만 감독 책임자가 주의할 필요가 있는 결함(또는 결함의 조합).

**Material Weakness:** 재무제표의 중요한 왜곡표시가 적시에 예방되거나 탐지되지 않을 합리적 가능성이 있는 결함(또는 결함의 조합).

### 7. 출력

다음을 제공합니다:
1. 선택한 영역의 통제 매트릭스
2. 방법론 문서가 포함된 샘플 선택
3. 사전 채워진 테스트 단계가 포함된 테스트 워크페이퍼 템플릿
4. 결과 문서화 템플릿
5. 결함이 식별되었을 때의 결함 평가 프레임워크
6. 식별된 결함에 대한 권고 개선 조치
