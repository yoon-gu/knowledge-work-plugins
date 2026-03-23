---
description: Generate a comprehensive strategic account plan
argument-hint: <company name or domain>
---

"$ARGUMENTS"에 대한 포괄적인 계정 계획을 생성합니다.

## 프로세스

1. **전체 계정 리서치** — account-research skill을 따라 완전한 계정 개요를 작성합니다. 사용 가능한 모든 1st-party(제품), 2nd-party(커뮤니티), 3rd-party(인텐트) 시그널, CRM 데이터, 점수, RoomieAI 리서치를 가져옵니다.

2. **이해관계자 매핑** — 이 회사의 상위 5명의 컨택을 멤버 점수 내림차순으로 가져옵니다. 각각을 Champion, Economic Buyer, Influencer, End User, Unknown으로 분류합니다. 가능한 경우 Spark 페르소나 데이터를 사용하고, Spark를 사용할 수 없는 경우 인게이지먼트 패턴과 활동 최신성에서 추론합니다. 활동 데이터도 없는 경우 Unknown으로 분류합니다.

3. **인게이지먼트 분석** — 지난 90일간의 모든 조직 활동을 가져옵니다(최대 50개 활동). 트렌드를 파악합니다: 인게이지먼트가 증가하고 있는지, 안정적인지, 감소하고 있는지? 어떤 컨택이 가장 활발한지? 어떤 채널을 통해 인게이지하고 있는지?

4. **웹 검색 (보완적)** — CR 데이터가 풍부한 경우 건너뜁니다. 데이터가 부족하거나 사용자가 요청하는 경우, 최근 30일간의 회사 뉴스를 검색합니다: 펀딩, 인수, 제품 출시, 리더십 변화, 경쟁사 동향.

5. **종합** — 모든 데이터를 구조화된 계정 계획으로 결합합니다. 사용자의 회사 컨텍스트가 사용 가능한 경우(참조: `references/my-company-context.md`), 임원 요약, 기회, 액션 아이템을 사용자의 제품 및 ICP에 맞게 조정합니다.

## 출력 형식

```
## Account Plan: [Company Name]

### Executive Summary
[3-4문장: 관계 상태, 핵심 기회, 주요 리스크, 권장 우선순위]

### Account Overview
| Field | Value |
|-------|-------|
| Industry | ... |
| Size | ... |
| Domain | ... |
| CRM Owner | ... |
| Opp Stage | ... |
| ARR | ... |
| Scores | ... |

### Stakeholder Map

**Champions**
- [Name] — [Title] — [핵심 시그널, 마지막 활동 날짜]

**Economic Buyers**
- [Name] — [Title] — [핵심 시그널]

**Influencers**
- [Name] — [Title] — [핵심 시그널]

**End Users**
- [Name] — [Title] — [핵심 시그널]

### Engagement Analysis
[트렌드 요약: 증가/안정/감소, 가장 활발한 컨택, 주요 채널, 가능한 경우 90일 전과 비교]

### Recent News [웹 검색이 실행된 경우]
[소스 및 날짜가 포함된 웹 검색 결과]

### Opportunities
1. [시그널 기반 기회와 구체적인 다음 단계]
2. ...

### Risks
1. [시그널 기반 리스크와 완화 방법]
2. ...

### Prioritized Action Items
1. [구체적인 액션] — [담당자 제안] — [타임라인]
2. ...
3. ...
```

모든 인사이트를 실제 데이터에 근거하여 작성합니다. 데이터가 부족하거나 없는 경우 명시적으로 표시합니다.

**이 계정에 대해 Common Room이 희박한 데이터를 반환하는 경우**, 실제 데이터가 있는 섹션만 포함하는 간략한 계획을 작성합니다. 최소한의 입력으로 전체 계정 계획을 생성하지 마십시오 — 공백이 명확하게 표시된 짧고 솔직한 계획이 조작된 세부 정보로 만들어진 포괄적으로 보이는 계획보다 훨씬 유용합니다. 데이터를 뒷받침할 수 없는 경우 섹션(Stakeholder Map, Engagement Analysis, Opportunities, Risks)을 완전히 생략합니다.
