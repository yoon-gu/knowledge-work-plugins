---
name: customer-research
description: 소스 귀속이 포함된 고객 질문 또는 주제에 대한 다중 소스 연구입니다. 고객이 찾아봐야 할 사항을 물을 때, 이전에 버그가 보고되었는지 조사하거나, 이전에 특정 계정에 전달된 내용을 확인하거나, 응답 초안을 작성하기 전에 배경 정보를 수집할 때 사용하세요.
argument-hint: "<question or topic>"
---

# /customer-research

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

고객 질문, 제품 주제 또는 계정 관련 문의에 대한 다중 소스 조사입니다. 명확한 귀속 및 신뢰도 점수를 통해 사용 가능한 모든 소스에서 얻은 결과를 종합합니다.

## 용법

```
/customer-research <question or topic>
```

## 작업흐름

### 1. 연구 요청 분석

어떤 유형의 연구가 필요한지 확인하십시오.
- **고객 질문**: 고객이 질문했지만 답변이 필요한 내용(예: "Does our product support SSO with Okta?")
- **문제 조사**: 보고된 문제에 대한 배경(예: "Has this bug been reported before? What's the known workaround?")
- **계정 컨텍스트**: 특정 고객과의 기록(예: "What did we tell Acme Corp last time they asked about this?")
- **주제 연구**: 지원 작업과 관련된 일반적인 주제(예: "Best practices for webhook retry logic")

검색하기 전에 실제로 찾으려는 것이 무엇인지 명확히 하세요.
- 이것은 확실한 답이 있는 사실적인 질문입니까?
- 이는 다양한 관점이 필요한 상황별 질문인가요?
- 범위가 아직 정의되고 있는 탐색적 질문인가요?
- 답변의 대상은 누구입니까(내부 팀, 고객, 리더십)?

### 2. 사용 가능한 소스 검색

연결된 항목에 맞춰 아래 소스 계층을 체계적으로 검색하세요. 첫 번째 결과에서 멈추지 마세요. 소스 간 상호 참조가 가능합니다.

**계층 1 — 공식 내부 소스(가장 높은 신뢰도):**
- ~~지식 기반(연결된 경우): 제품 문서, Runbook, FAQ, 정책 문서
- ~~클라우드 스토리지: 내부 문서, 사양, 가이드, 과거 연구
- 제품 로드맵(내부용): 기능 타임라인, 우선순위

**계층 2 — 조직 상황:**
- ~~CRM 메모: 계정 메모, 활동 내역, 이전 답변, 기회 세부정보
- ~~지원 플랫폼(연결된 경우): 이전 해결 방법, 알려진 문제, 해결 방법
- 회의록: 이전 토론, 결정, 약속

**계층 3 - 팀 커뮤니케이션:**
- ~~채팅: 관련 채널에서 주제를 검색합니다. 팀원이 이전에 이에 대해 논의했거나 답변했는지 확인하십시오.
- ~~이메일: 이 주제에 대한 이전 서신 검색
- 캘린더 메모: 회의 안건 및 회의 후 메모

**계층 4 - 외부 소스:**
- 웹 검색: 공식 문서, 블로그 게시물, 커뮤니티 포럼
- 공개 지식 베이스, 도움말 센터, 출시 노트
- 타사 문서: 통합 파트너, 보완 도구

**계층 5 — 추론 또는 유추(직접 소스가 답변을 제공하지 않는 경우 사용):**
- 유사한 상황: 이전에 유사한 질문이 어떻게 처리되었는지
- 유사 고객: 유사 고객에게 효과가 있었던 방법
- 일반 모범 사례: 업계 표준 및 규범

### 3. 결과 종합

결과를 구조화된 연구 요약으로 정리합니다.

```
## Research: [Question/Topic]

### Answer
[Clear, direct answer to the question — lead with the bottom line]

**Confidence:** [High / Medium / Low]
[Explain what drives the confidence level]

### Key Findings

**From [Source 1]:**
- [Finding with specific detail]
- [Finding with specific detail]

**From [Source 2]:**
- [Finding with specific detail]

### Context & Nuance
[Any caveats, edge cases, or additional context that matters]

### Sources
1. [Source name/link] — [what it contributed]
2. [Source name/link] — [what it contributed]
3. [Source name/link] — [what it contributed]

### Gaps & Unknowns
- [What couldn't be confirmed]
- [What might need verification from a subject matter expert]

### Recommended Next Steps
- [Action if the answer needs to go to a customer]
- [Action if further research is needed]
- [Who to consult for verification if needed]
```

### 4. 부족한 소스 처리

연결된 소스가 결과를 생성하지 않는 경우:

- 주제에 대한 웹 조사 수행
- 사용자에게 내부 상황을 물어보세요.
  - "I couldn't find this in connected sources. Do you have internal docs or knowledge base articles about this?"
  - "Has your team discussed this topic before? Any ~~chat channels I should check?"
  - "Is there a subject matter expert who would know the answer?"
- 제한사항을 투명하게 밝히십시오.
  - "This answer is based on web research only — please verify against your internal documentation before sharing with the customer."
  - "I found a possible answer but couldn't confirm it from an authoritative internal source."

### 5. 고객 대면 고려사항

조사가 고객 질문에 답변하는 것인 경우:

- 답변이 검토가 필요할 수 있는 제품 로드맵, 가격, 법률 또는 보안 주제와 관련된 경우 플래그를 지정하세요.
- 답변이 이전에 전달된 내용과 다른 경우 참고하세요.
- 고객 대응에 대한 적절한 주의 사항 제안
- 고객 응답 초안 작성 제안: "Want me to draft a response to the customer based on these findings?"

### 6. 지식 포착

연구가 완료되면 지식을 수집하도록 제안합니다.

- "Should I save these findings to your knowledge base for future reference?"
- "Want me to create a FAQ entry based on this research?"
- "This might be worth documenting — should I draft a runbook entry?"

이는 제도적 지식을 구축하고 팀 전체의 중복된 연구 노력을 줄이는 데 도움이 됩니다.

---

## 소스 우선순위 지정 및 신뢰도

### 소스 계층별 신뢰도

| 층 | 소스 유형 | 신뢰 | 메모 |
|------|-------------|------------|-------|
| 1 | 공식 내부 문서, KB, 정책 | **높은** | 확실히 오래된 것이 아니라면 신뢰하세요 — 날짜를 확인하세요 |
| 2 | CRM, 지원 티켓, 회의록 | **중간 높음** | 주관적이거나 불완전할 수 있음 |
| 3 | 채팅, 이메일, 캘린더 메모 | **중간** | 비공식적, 맥락에 맞지 않거나 추측적일 수 있음 |
| 4 | 웹, 포럼, 타사 문서 | **낮음-중간** | 귀하의 특정 상황을 반영하지 않을 수 있습니다. |
| 5 | 추론, 비유, 모범 사례 | **낮은** | 사실이 아닌 추론으로 명확하게 표시 |

### 신뢰 수준

항상 신뢰 수준을 지정하고 전달하십시오.

**높은 신뢰도:**
- 공식 문서 또는 권위 있는 출처를 통해 확인된 답변
- 여러 소스가 동일한 답변을 확증합니다.
- 정보는 최신 정보입니다(합리적인 기간 내에 확인됨).
- "I'm confident this is accurate based on [source]."

**중간 신뢰도:**
- 공식 문서가 아닌 비공식 소스(채팅, 이메일)에서 답변을 찾았습니다.
- 확증 없는 단일 소스
- 정보가 약간 오래되었을 수 있지만 여전히 유효할 가능성이 높습니다.
- "Based on [source], this appears to be the case, but I'd recommend confirming with [team/person]."

**낮은 신뢰도:**
- 관련 정보에서 답변을 추론합니다.
- 소스가 오래되었거나 잠재적으로 신뢰할 수 없습니다.
- 여러 출처에서 발견된 모순되는 정보
- "I wasn't able to find a definitive answer. Based on [context], my best assessment is [answer], but this should be verified before sharing with the customer."

**결정할 수 없음:**
- 어떤 출처에서도 관련 정보를 찾을 수 없습니다.
- 질문에는 소스에서 사용할 수 없는 전문 지식이 필요합니다.
- "I couldn't find information about this. I recommend reaching out to [suggested expert/team] for a definitive answer."

### 모순 처리

출처가 일치하지 않는 경우:
1. 모순을 명시적으로 주목하라
2. 어느 출처가 더 권위 있고 최신인지 확인하세요.
3. 상황에 맞게 두 관점을 모두 제시
4. 불일치를 해결하는 방법을 권장합니다.
5. 고객에게 문의하는 경우: 문제가 해결될 때까지 가장 보수적이고 신중한 답변을 사용하세요.

## 에스컬레이션해야 하는 경우와 직접 답변해야 하는 경우

### 다음과 같은 경우에는 직접 답변하세요.
- 공식 문서는 질문을 명확하게 다루고 있습니다.
- 신뢰할 수 있는 여러 출처가 답변을 확증합니다.
- 질문이 사실에 근거하고 민감하지 않습니다.
- 대답에는 약속, 일정 또는 가격이 포함되지 않습니다.
- 이전에 비슷한 질문에 정확하게 답변한 적이 있습니다.

### 에스컬레이션 또는 확인 시기:
- 대답은 제품 로드맵 약속 또는 일정과 관련이 있습니다.
- 가격, 법적 조건 또는 계약 관련 질문
- 보안, 규정 준수 또는 데이터 처리 관련 질문
- 대답은 선례를 만들거나 기대를 불러일으킬 수 있습니다.
- 출처에서 모순되는 정보를 발견했습니다.
- 질문은 특정 고객의 사용자 정의 구성과 관련됩니다.
- 답을 얻으려면 귀하가 보유하지 않은 전문 지식이 필요합니다
- 고객이 위험에 처해 있으며 잘못된 답변으로 인해 상황이 악화될 수 있습니다.

### 에스컬레이션 경로:
1. **주제 전문가**: 기술 또는 도메인별 질문
2. **제품팀**: 로드맵, 기능 또는 역량 관련 질문
3. **법률/규정 준수**: 약관, 개인 정보 보호, 보안 또는 규제 관련 질문
4. **청구/금융**: 가격, 송장 또는 결제 관련 질문
5. **엔지니어링**: 맞춤 구성, 버그 또는 기술적인 근본 원인의 경우
6. **리더십**: 전략적 결정, 예외 또는 중대한 위험 상황

## 팀 기술 자료에 대한 연구 문서

연구를 완료한 후 나중에 사용할 수 있도록 지식을 수집합니다.

### 문서화 시기:
- 이전에 질문이 나왔거나 앞으로도 나올 것 같습니다.
- 연구는 컴파일을 위해 상당한 노력을 기울였습니다.
- 여러 소스를 합성하는 데 필요한 답변
- 답변은 일반적인 오해를 바로잡습니다
- 답변에는 오해하기 쉬운 뉘앙스가 포함되어 있습니다.

### 문서 형식:
```
## [Question/Topic]

**Last Verified:** [date]
**Confidence:** [level]

### Answer
[Clear, direct answer]

### Details
[Supporting detail, context, and nuance]

### Sources
[Where this information came from]

### Related Questions
[Other questions this might help answer]

### Review Notes
[When to re-verify, what might change this answer]
```

### 기술 자료 위생:
- 모든 항목에 날짜 스탬프를 찍습니다.
- 특정 제품 버전이나 기능을 참조하는 항목에 플래그를 지정하세요.
- 분기별로 항목을 검토하고 업데이트합니다.
- 더 이상 관련이 없는 항목을 보관하세요.
- 검색 가능성을 위한 태그 항목(주제, 제품 영역, 고객 부문별)
