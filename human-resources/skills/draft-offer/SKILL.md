---
name: draft-offer
description: Draft an offer letter with comp details and terms. Use when a candidate is ready for an offer, assembling a total comp package (base, equity, signing bonus), writing the offer letter text itself, or prepping negotiation guidance for the hiring manager.
argument-hint: "<role and level>"
---

# /draft-offer

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우, [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

신입 직원을 위한 완전한 오퍼 레터 초안을 작성합니다.

## 사용법

```
/draft-offer $ARGUMENTS
```

## 필요한 정보

- **역할 및 직함**: 어떤 포지션인가요?
- **레벨**: Junior, Mid, Senior, Staff 등
- **위치**: 어디서 근무하나요? (보상 및 복리후생에 영향)
- **보상**: 기본급, 주식, 사이닝 보너스 (해당하는 경우)
- **시작일**: 언제 시작하나요?
- **채용 관리자**: 누구에게 보고하나요?

모든 세부 정보가 없어도 괜찮습니다. 함께 검토해 드리겠습니다.

## 출력 결과

```markdown
## Offer Letter Draft: [Role] — [Level]

### Compensation Package
| Component | Details |
|-----------|---------|
| **Base Salary** | $[X]/year |
| **Equity** | [X shares/units], [vesting schedule] |
| **Signing Bonus** | $[X] (if applicable) |
| **Target Bonus** | [X]% of base (if applicable) |
| **Total First-Year Comp** | $[X] |

### Terms
- **Start Date**: [Date]
- **Reports To**: [Manager]
- **Location**: [Office / Remote / Hybrid]
- **Employment Type**: [Full-time, Exempt]

### Benefits Summary
[Key benefits highlights relevant to the candidate]

### Offer Letter Text

Dear [Candidate Name],

We are pleased to offer you the position of [Title] at [Company]...

[Complete offer letter text]

### Notes for Hiring Manager
- [Negotiation guidance if needed]
- [Comp band context]
- [Any flags or considerations]
```

## 커넥터 사용 시

**~~HRIS**가 연결된 경우:
- 레벨/역할에 대한 보상 밴드 데이터 조회
- 헤드카운트 승인 확인
- 복리후생 세부 정보 자동 입력

**~~ATS**가 연결된 경우:
- 지원서에서 후보자 정보 조회
- 파이프라인에서 오퍼 상태 업데이트

## 팁

1. **총 보상을 포함하세요** — 후보자는 기본급만이 아니라 총 보상을 비교합니다.
2. **주식을 구체적으로 명시하세요** — 주식 수, 현재 가치 평가 방법, 베스팅 일정.
3. **개인화하세요** — 인터뷰 과정에서 나온 이야기를 언급하면 따뜻한 인상을 줍니다.
