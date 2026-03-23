---
description: 포괄적인 전략 계정 계획을 생성합니다
argument-hint: <company name or domain>
---

`$ARGUMENTS`에 대한 포괄적인 계정 계획을 생성합니다.

## 프로세스

1. **전체 계정 조사** - account-research 스킬을 따라 완전한 계정 개요를 만듭니다. 사용 가능한 모든 1차(제품), 2차(커뮤니티), 3차(의도) 신호, CRM 데이터, 점수, RoomieAI 리서치를 가져옵니다.

2. **이해관계자 매핑** - 이 회사의 상위 5개 연락처를 member score 내림차순으로 가져옵니다. 각 연락처를 Champion, Economic Buyer, Influencer, End User, 또는 Unknown으로 분류합니다. 가능하면 Spark persona 데이터를 사용하고, Spark가 없으면 참여 패턴과 최근 활동으로 추론합니다. 활동 데이터도 없으면 Unknown으로 분류합니다.

3. **참여도 분석** - 지난 90일의 조직 활동을 모두 가져옵니다(최대 50개 활동). 추세를 식별합니다. 참여도가 증가 중인지, 안정적인지, 감소 중인지? 어떤 연락처가 가장 활발한지? 어떤 채널로 참여하는지?

4. **웹 검색(보조)** - CR 데이터가 풍부하면 건너뜁니다. 데이터가 얇거나 사용자가 요청하면 최근 30일의 회사 뉴스(투자 유치, 인수, 제품 출시, 리더십 변화, 경쟁 움직임)를 검색합니다.

5. **종합** - 모든 데이터를 구조화된 계정 계획으로 묶습니다. 사용자의 회사 컨텍스트가 가능하면(`references/my-company-context.md` 참고) 실행 요약, 기회, 실행 항목을 사용자의 제품과 ICP에 맞게 조정합니다.

## 출력 형식

```
## Account Plan: [Company Name]

### Executive Summary
[3-4 sentences: relationship status, key opportunity, primary risk, recommended priority]

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
- [Name] — [Title] — [Key signals, last activity date]

**Economic Buyers**
- [Name] — [Title] — [Key signals]

**Influencers**
- [Name] — [Title] — [Key signals]

**End Users**
- [Name] — [Title] — [Key signals]

### Engagement Analysis
[Trend summary: growing/stable/declining, most active contacts, top channels, comparison to 90 days prior if data available]

### Recent News [If web search was run]
[Web search findings with sources and dates]

### Opportunities
1. [Signal-backed opportunity with specific next step]
2. ...

### Risks
1. [Signal-backed risk with mitigation]
2. ...

### Prioritized Action Items
1. [Specific action] — [Owner suggestion] — [Timeline]
2. ...
3. ...
```

모든 인사이트는 실제 데이터에 근거해야 합니다. 데이터가 부족하거나 없을 때는 반드시 명시하세요.

**이 계정에 대해 Common Room이 희소한 데이터를 반환하면**, 실제 데이터가 있는 섹션만 담은 축약 계획을 작성하세요. 최소한의 입력으로 전체 계정 계획을 만들어 내지 마세요. 허구의 세부사항으로 채운 그럴듯한 문서보다, 공백을 분명히 적은 짧고 솔직한 계획이 훨씬 유용합니다. 이를 뒷받침할 데이터가 없다면 Stakeholder Map, Engagement Analysis, Opportunities, Risks 섹션은 아예 생략하세요.
