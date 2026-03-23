---
name: audit-support
description: 통제 테스트 방법론, 샘플 선택, 문서 표준으로 SOX 404 준수를 지원합니다. 테스트 워크페이퍼 생성, 감사 샘플 선택, 통제 결함 분류, 내부 또는 외부 감사 준비 시 사용합니다.
user-invocable: false
---

# Audit Support

**Important**: This skill assists with SOX compliance workflows but does not provide audit or legal advice. All testing workpapers and assessments should be reviewed by qualified financial professionals. While "significance" and "materiality" are context-specific concepts that are ultimately assessed by auditors, this skill is intended to assist professionals in the creation and evaluation of effective internal controls and documentation for audits.

SOX 404 통제 테스트 방법론, 샘플 선택 방식, 테스트 문서 표준, 통제 결함 분류, 일반적인 통제 유형입니다.

## SOX 404 Control Testing Methodology

### Overview

SOX Section 404는 경영진이 재무 보고 내부통제(ICFR)의 효과성을 평가하도록 요구합니다. 이는 다음을 포함합니다:

1. **Scoping:** 중요한 계정과 관련 주장 식별
2. **Risk assessment:** 각 중요한 계정의 중대한 왜곡표시 위험 평가
3. **Control identification:** 각 위험을 다루는 통제 문서화
4. **Testing:** 핵심 통제의 설계와 운영 효과성 테스트
5. **Evaluation:** 결함 존재 여부와 심각도 평가
6. **Reporting:** 평가와 중요한 약점 문서화

### Scoping Significant Accounts

계정이 중요한 것은 개별적으로나 집합적으로 중요한 왜곡표시를 포함할 가능성이 원격 수준보다 높을 때입니다.

**Quantitative factors:**
- 계정 잔액이 중요성 기준치를 초과(보통 핵심 벤치마크의 3-5%)
- 거래량이 높아 오류 위험 증가
- 계정에 중요한 추정이나 판단이 필요

**Qualitative factors:**
- 복잡한 회계가 관여(매출 인식, 파생상품, 연금)
- 사기에 취약(현금, 매출, 특수관계자 거래)
- 과거 왜곡표시나 감사 조정 이력
- 중요한 경영진 판단 또는 추정이 필요
- 신규 계정 또는 크게 변경된 프로세스

### Relevant Assertions by Account Type

| Account Type | Key Assertions |
|-------------|---------------|
| Revenue | Occurrence, Completeness, Accuracy, Cut-off |
| Accounts Receivable | Existence, Valuation (allowance), Rights |
| Inventory | Existence, Valuation, Completeness |
| Fixed Assets | Existence, Valuation, Completeness, Rights |
| Accounts Payable | Completeness, Accuracy, Existence |
| Accrued Liabilities | Completeness, Valuation, Accuracy |
| Equity | Completeness, Accuracy, Presentation |
| Financial Close/Reporting | Presentation, Accuracy, Completeness |

### Design Effectiveness vs Operating Effectiveness

**Design effectiveness:** 통제가 관련 주장에 대한 중요한 왜곡표시를 예방하거나 탐지하도록 적절히 설계되었는가?
- 워크스루를 통해 평가(프로세스를 통해 거래를 처음부터 끝까지 추적)
- 통제가 프로세스의 올바른 지점에 배치되었는지 확인
- 통제가 식별된 위험을 다루는지 확인
- 최소 연 1회, 또는 프로세스가 변경될 때 수행

**Operating effectiveness:** 통제가 테스트 기간 내내 설계대로 실제로 작동했는가?
- 테스트(검사, 관찰, 재수행, 조회)를 통해 평가
- 결론을 뒷받침할 충분한 샘플 크기 필요
- 전체 의존 기간을 포괄해야 함

## Sample Selection Approaches

### Random Selection

**When to use:** 대규모 모집단의 거래 수준 통제에 대한 기본 방법.

**Method:**
1. 모집단 정의(해당 기간 동안 통제 대상이 된 모든 거래)
2. 모집단의 각 항목에 순차 번호 부여
3. 무작위 숫자 생성기로 샘플 항목 선택
4. 선택 편향이 없도록 확인(모든 항목의 확률이 동일)

**Advantages:** 통계적으로 유효하고 방어 가능, 선택 편향 없음
**Disadvantages:** 고위험 항목을 놓칠 수 있고, 완전한 모집단 목록이 필요

### Targeted (Judgmental) Selection

**When to use:** 위험 기반 테스트를 위한 무작위 선택의 보완; 모집단이 작을 때 기본 방법

**Method:**
1. 고위험, 비정상, 기간 말, 큰 금액 등 특정 특성을 가진 항목 선택
2. 선택 이유 문서화
3. 중요한 주장 또는 위험에 집중

**Advantages:** 위험에 민감, 판단을 반영
**Disadvantages:** 통계적으로 대표적이지 않을 수 있음, 특정 위험을 과대표집할 수 있음

### Haphazard Selection

**When to use:** 무작위 선택이 실용적이지 않을 때(순차적 모집단 목록 없음) 그리고 모집단이 비교적 동질적일 때.

**Method:**
1. 특정 패턴이나 편향 없이 항목 선택
2. 선택이 전체 모집단 기간에 걸쳐 퍼지도록 확인
3. 무의식적 편향을 피함(항상 맨 위 항목, 반올림 숫자만 고르지 않기)

**Advantages:** 단순, 기술 불필요
**Disadvantages:** 통계적으로 유효하지 않고 무의식적 편향에 취약

### Systematic Selection

**When to use:** 모집단이 순차적이고 기간 전체를 고르게 커버하고 싶을 때.

**Method:**
1. 샘플링 간격 계산: 모집단 크기 / 샘플 크기
2. 첫 간격 내에서 무작위 시작점 선택
3. 시작점부터 N번째 항목마다 선택

**Example:** 모집단 1,000개, 샘플 25개 → 간격 40. 무작위 시작: 17번 항목. 17, 57, 97, 137, ... 선택

**Advantages:** 모집단 전체를 고르게 커버, 실행이 간단
**Disadvantages:** 모집단의 주기적 패턴이 결과를 편향시킬 수 있음

### Sample Size Guidance

| Control Frequency | Expected Population | Low Risk Sample | Moderate Risk Sample | High Risk Sample |
|------------------|--------------------|-----------------|--------------------|-----------------|
| Annual | 1 | 1 | 1 | 1 |
| Quarterly | 4 | 2 | 2 | 3 |
| Monthly | 12 | 2 | 3 | 4 |
| Weekly | 52 | 5 | 8 | 15 |
| Daily | ~250 | 20 | 30 | 40 |
| Per-transaction (small pop.) | < 250 | 20 | 30 | 40 |
| Per-transaction (large pop.) | 250+ | 25 | 40 | 60 |

**Factors increasing sample size:**
- 계정/프로세스의 고유 위험이 높음
- 통제가 중요한 위험을 다루는 유일한 통제(중복 없음)
- 전기 통제 결함이 식별됨
- 신규 통제(전기에 테스트되지 않음)
- 외부 감사인이 경영진 테스트에 의존

## Testing Documentation Standards

### Workpaper Requirements

모든 통제 테스트는 다음과 같이 문서화해야 합니다:

1. **Control identification:**
   - 통제 번호/ID
   - 통제 설명(무엇을, 누가, 얼마나 자주)
   - 통제 유형(manual, automated, IT-dependent manual)
   - 통제 빈도
   - 다루는 위험과 주장

2. **Test design:**
   - 테스트 목적(무엇을 판단하려는지)
   - 테스트 절차(단계별 지침)
   - 예상 증거(통제가 효과적이라면 무엇이 보여야 하는지)
   - 샘플 선택 방법과 이유

3. **Test execution:**
   - 모집단 설명과 크기
   - 샘플 선택 세부 정보(방법, 선택 항목)
   - 각 샘플 항목 결과(pass/fail와 검토한 구체적 증거)
   - 예외 사항과 상세 설명

4. **Conclusion:**
   - 전체 평가(effective / deficiency / significant deficiency / material weakness)
   - 결론의 근거
   - 예외의 영향 평가
   - 고려한 보완 통제(해당 시)

5. **Sign-off:**
   - 테스트한 사람과 날짜
   - 검토한 사람과 날짜

### Evidence Standards

**Sufficient evidence includes:**
- 시스템 강제 통제를 보여 주는 스크린샷
- 서명/이니셜이 있는 승인 문서
- 승인자와 날짜가 식별되는 이메일 승인
- 누가 언제 조치했는지 보여 주는 시스템 감사 로그
- 결과가 일치하는 재수행 계산
- 관찰 노트(날짜, 장소, 관찰자 포함)

**Insufficient evidence:**
- 구두 확인만(반드시 다른 증거로 보강 필요)
- 날짜 없는 문서
- 수행자/승인자가 식별되지 않는 증거
- 날짜/시간 스탬프가 없는 일반 시스템 리포트
- "[name]과 논의함"만 있고 보강 문서가 없음

### Working Paper Organization

테스트 파일은 통제 영역별로 정리합니다:

```text
SOX Testing/
├── [Year]/
│   ├── Scoping and Risk Assessment/
│   ├── Revenue Cycle/
│   │   ├── Control Matrix
│   │   ├── Walkthrough Documentation
│   │   ├── Test Workpapers (one per control)
│   │   └── Supporting Evidence
│   ├── Procure to Pay/
│   ├── Payroll/
│   ├── Financial Close/
│   ├── Treasury/
│   ├── Fixed Assets/
│   ├── IT General Controls/
│   ├── Entity Level Controls/
│   └── Summary and Conclusions/
│       ├── Deficiency Evaluation
│       └── Management Assessment
```

## Control Deficiency Classification

### Deficiency

내부통제 결함은 통제의 설계 또는 운영이 경영진이나 직원이 맡은 기능을 수행하는 정상 과정에서 중요한 왜곡표시를 적시에 예방하거나 탐지하게 하지 못할 때 존재합니다.

**Evaluation factors:**
- 통제 실패가 왜곡표시로 이어질 가능성은?
- 잠재적 왜곡표시의 규모는?
- 결함을 완화하는 보완 통제가 있는가?

### Significant Deficiency

중요한 약점보다는 덜 심각하지만 감독 책임자가 주의할 필요가 있을 정도의 결함(또는 결함의 조합).

**Indicators:**
- 결함이 중요하지는 않지만 무시할 수 없는 왜곡표시를 낳을 수 있음
- 중요한 왜곡표시가 발생할 가능성이 원격보다는 높지만 합리적으로 가능하다고 보기에는 낮음
- 통제가 핵심 통제이고 보완 통제로 완전히 완화되지 않음
- 개별적으로는 사소하지만 함께 보면 중요한 우려가 되는 결함의 조합

### Material Weakness

재무제표의 중요한 왜곡표시가 적시에 예방되거나 탐지되지 않을 합리적 가능성이 있는 결함(또는 결함의 조합).

**Indicators:**
- 경영진의 사기 식별(규모와 무관)
- 중요한 오류를 수정하기 위한 이전 공시 재무제표 재작성
- 회사 통제로 탐지되지 않았을 중요한 왜곡표시를 감사인이 식별
- 감사위원회의 재무 보고 감독이 비효과적
- 여러 프로세스에 영향을 주는 광범위한 통제(엔터티 레벨, IT 일반 통제)의 결함

### Deficiency Aggregation

개별적으로는 중요하지 않은 결함도 함께 보면 중요할 수 있습니다:

1. 같은 프로세스 또는 같은 주장에 영향을 주는 모든 결함 식별
2. 결합 효과가 중요한 왜곡표시로 이어질 수 있는지 평가
3. 보완 통제의 결함이 다른 결함을 악화시키는지 고려
4. 집계 분석과 결론을 문서화

### Remediation

각 식별된 결함에 대해:

1. **Root cause analysis:** 왜 통제가 실패했는가?(설계 격차, 실행 실패, 인력, 교육, 시스템 이슈)
2. **Remediation plan:** 통제를 고치기 위한 구체적 조치(재설계, 추가 교육, 시스템 개선, 추가 검토)
3. **Timeline:** 개선 완료 목표일
4. **Owner:** 개선을 실행할 책임자
5. **Validation:** 개선된 통제를 언제 어떻게 재테스트해 효과성을 확인할지

## Common Control Types

### IT General Controls (ITGCs)

애플리케이션 통제와 자동화된 프로세스의 신뢰할 수 있는 작동을 지원하는 IT 환경 통제.

**Access Controls:**
- 사용자 접근 권한 부여(새 접근 요청에는 승인 필요)
- 사용자 접근 권한 회수(퇴사자 권한이 적시에 제거됨)
- 특권 접근 관리(관리자/슈퍼유저 접근 제한 및 모니터링)
- 정기적 접근 검토(정해진 일정으로 재인증)
- 비밀번호 정책(복잡성, 변경 주기, 잠금)
- 직무 분리 강제(충돌하는 권한 차단)

**Change Management:**
- 변경 요청이 구현 전에 문서화되고 승인됨
- 변경이 프로덕션 이전에 비프로덕션 환경에서 테스트됨
- 개발과 운영 환경 분리
- 긴급 변경 절차(문서화, 구현 후 승인)
- 변경 검토와 구현 후 검증

**IT Operations:**
- 배치 작업 모니터링과 예외 처리
- 백업 및 복구 절차(정기 백업, 복원 테스트)
- 시스템 가용성 및 성능 모니터링
- 사고 관리와 에스컬레이션 절차
- 재해 복구 계획과 테스트

### Manual Controls

판단이 필요한 사람에 의해 수행되는 통제.

**Examples:**
- 재무제표와 핵심 지표에 대한 경영진 검토
- 임계값을 초과하는 분개에 대한 감독자 승인
- 3-way match 검증(PO, 수령, 인보이스)
- 계정 조정 준비와 검토
- 실물 재고 관찰과 실사
- 공급업체 마스터 데이터 변경 승인
- 고객 신용 승인

**Key attributes to test:**
- 올바른 사람이 통제를 수행했는가(적절한 권한)?
- 적시에 수행되었는가(요구된 시간 내)?
- 검토의 증거가 있는가(서명, 이니셜, 이메일, 시스템 로그)?
- 검토자가 효과적인 검토를 할 충분한 정보를 가졌는가?
- 예외가 식별되었고 적절히 처리되었는가?

### Automated Controls

사람의 개입 없이 IT 시스템이 강제하는 통제.

**Examples:**
- 시스템 강제 승인 워크플로(필수 승인 없이는 진행 불가)
- 3-way match 자동화(PO/수령/인보이스가 일치하지 않으면 시스템이 지급 차단)
- 중복 지급 탐지(중복 인보이스를 시스템이 표시하거나 차단)
- 신용 한도 강제(시스템이 한도를 초과하는 주문을 차단)
- 자동 계산(감가상각, 상각, 이자, 세금)
- 시스템 강제 직무 분리(충돌 역할 차단)
- 입력 검증 통제(필수 필드, 형식 검사, 범위 검사)
- 자동 조정 매칭

**Testing approach:**
- 설계 테스트: 시스템 구성이 의도대로 통제를 강제하는지 확인
- 운영 효과성 테스트: 자동 통제는 시스템 구성이 바뀌지 않았다면 기간당 보통 한 번의 테스트로 충분(변경 관리 ITGC 테스트를 보완)
- 변경 관리 ITGC가 효과적인지 확인(시스템이 바뀌었다면 통제를 다시 테스트)

### IT-Dependent Manual Controls

시스템 생성 정보의 완전성과 정확성에 의존하는 수동 통제.

**Examples:**
- 시스템 생성 예외 리포트에 대한 경영진 검토
- 시스템 생성 aging 리포트를 활용한 충당금 감독자 검토
- 시스템 생성 시산표 데이터를 사용한 조정
- 시스템 생성 워크플로로 식별된 거래 승인

**Testing approach:**
- 수동 통제를 테스트(검토, 승인, 예외 후속 조치)
- AND 기본 리포트/데이터의 완전성과 정확성을 테스트(IPE — Information Produced by the Entity)
- IPE 테스트는 검토자가 의존한 데이터가 완전하고 정확했는지 확인

### Entity-Level Controls

조직 수준에서 작동하고 여러 프로세스에 영향을 주는 광범위한 통제.

**Examples:**
- tone at the top / 행동 강령
- 위험 평가 프로세스
- 재무 보고에 대한 감사위원회 감독
- 내부감사 기능과 활동
- 사기 위험 평가와 반사기 프로그램
- 내부 고발/윤리 핫라인
- 통제 효과성에 대한 경영진 모니터링
- 재무 보고 역량(인력, 교육, 자격)
- 기간 말 재무 보고 프로세스(마감 절차, GAAP 준수 검토)

**Significance:**
- 엔터티 레벨 통제는 완화할 수는 있지만 보통 프로세스 수준 통제를 대체할 수는 없음
- 비효과적인 엔터티 레벨 통제(특히 감사위원회 감독과 tone at the top)는 중요한 약점의 강한 지표
- 효과적인 엔터티 레벨 통제는 프로세스 수준 통제에 필요한 테스트 범위를 줄일 수 있음
