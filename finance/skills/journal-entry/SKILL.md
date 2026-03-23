---
name: journal-entry
description: 적절한 차변, 대변, 지원 세부 정보를 갖춘 분개를 준비합니다. 월말 미지급비용(AP, 급여, 선급비용), 감가상각/상각 인식, 매출 인식 또는 이연 매출 조정, 감사 검토용 분개 문서화에 사용합니다.
argument-hint: "<entry type> [period]"
---

# Journal Entry Preparation

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

**Important**: This command assists with journal entry workflows but does not provide financial advice. All entries should be reviewed by qualified financial professionals before posting.

적절한 차변, 대변, 지원 세부 정보, 검토 문서를 갖춘 분개를 준비합니다.

## 사용법

```
/je <type> <period>
```

### Arguments

- `type` — 분개 유형. 다음 중 하나:
  - `ap-accrual` — 인보이스는 받지 않았지만 수령한 재화/서비스에 대한 Accounts payable 미지급비용
  - `fixed-assets` — 고정자산과 무형자산의 감가상각 및 상각
  - `prepaid` — 선급비용 상각(보험, 소프트웨어, 임대료 등)
  - `payroll` — 급여, 복리후생, 세금, 보너스 미지급을 포함한 급여 미지급
  - `revenue` — 이연 매출 조정을 포함한 매출 인식 분개
- `period` — 회계 기간(예: `2024-12`, `2024-Q4`, `2024`)

## 워크플로

### 1. 원천 데이터 수집

~~erp 또는 ~~data warehouse가 연결되어 있다면:
- 지정한 기간의 시산표를 가져오기
- 관련 계정의 보조원장 세부 정보 가져오기
- 참고용으로 같은 유형의 이전 기간 분개 가져오기
- 영향을 받는 계정의 현재 GL 잔액 식별

데이터 소스가 연결되어 있지 않다면:
> GL 데이터를 자동으로 가져오려면 ~~erp 또는 ~~data warehouse를 연결하세요. 시산표 데이터를 붙여넣거나 스프레드시트를 업로드할 수도 있습니다.

사용자에게 다음을 제공하도록 요청:
- 영향을 받는 계정의 시산표 또는 GL 잔액
- 보조원장 세부 정보 또는 지원 스케줄
- 참고용 이전 기간 분개(선택 사항)

### 2. 분개 계산

JE 유형에 따라:

**AP Accrual:**
- 기간 말까지 수령했지만 청구되지 않은 재화/서비스 식별
- PO 수령, 계약, 추정에서 미지급액 계산
- Debit: 비용 계정(자본화 가능한 항목은 자산 계정)
- Credit: 미지급 부채

**Fixed Assets:**
- 고정자산 등록부 또는 감가상각 스케줄 불러오기
- 자산 클래스와 방법(정액, 정률법, 생산량 비례)에 따라 기간 감가상각 계산
- Debit: 감가상각 비용(부서/코스트 센터별)
- Credit: 감가상각누계액

**Prepaid:**
- 선급비용 상각 스케줄 불러오기
- 각 선급 항목의 해당 기간 상각 계산
- Debit: 비용 계정(보험, 소프트웨어, 임대료 등 유형별)
- Credit: 선급비용 계정

**Payroll:**
- 아직 지급되지 않은 근무일에 대한 급여 계산
- 복리후생(건강보험, 퇴직기여, PTO) 계산
- 고용주 급여세 미지급액 계산
- 보너스 미지급액 계산(해당 시, 플랜 조건 기반)
- Debit: 급여 비용, 복리후생 비용, 급여세 비용
- Credit: 미지급 급여, 미지급 복리후생, 미지급 급여세

**Revenue:**
- 계약과 성과 의무 검토
- 인도/성과에 따라 인식할 매출 계산
- 이연 매출 잔액 조정
- Debit: 이연 매출(또는 외상매출금)
- Credit: 매출 계정(흐름/카테고리별)

### 3. 분개 생성

표준 형식으로 분개를 제시합니다:

```
Journal Entry: [Type] — [Period]
Prepared by: [User]
Date: [Period end date]

| Line | Account Code | Account Name | Debit | Credit | Department | Memo |
|------|-------------|--------------|-------|--------|------------|------|
| 1    | XXXX        | [Name]       | X,XXX |        | [Dept]     | [Detail] |
| 2    | XXXX        | [Name]       |       | X,XXX  | [Dept]     | [Detail] |
|      |             | **Total**    | X,XXX | X,XXX  |            |      |

Supporting Detail:
- [Calculation basis and assumptions]
- [Reference to supporting schedule or documentation]

Reversal: [Yes/No — if yes, specify reversal date]
```

### 4. 검토 체크리스트

최종 확정 전에 다음을 확인:

- [ ] 차변과 대변이 일치
- [ ] 올바른 회계 기간
- [ ] 계정 코드가 유효하고 올바른 GL 계정에 매핑됨
- [ ] 금액이 정확히 계산되고 지원 세부 정보가 있음
- [ ] 메모/설명이 명확하고 감사에 충분히 구체적
- [ ] 부서/코스트 센터/프로젝트 코딩이 정확
- [ ] 이전 기간 처리와 일관적
- [ ] 역전 플래그가 적절히 설정됨(미지급액은 자동 역전되어야 함)
- [ ] 지원 문서가 참조되거나 첨부됨
- [ ] 분개 금액이 사용자의 승인 권한 내
- [ ] 조사해야 할 비정상적이거나 패턴을 벗어난 금액이 없음

### 5. 출력

다음을 제공합니다:
1. 형식화된 분개
2. 지원 계산
3. 같은 유형의 이전 기간 분개와의 비교(가능한 경우)
4. 검토 또는 후속 조치로 표시할 항목
5. 게시 방법(수동 입력 또는 ERP 업로드 형식) 안내
