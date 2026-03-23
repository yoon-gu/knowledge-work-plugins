---
name: draft-response
description: 상황과 관계에 맞는 전문적인 고객 응대 초안을 작성하세요. 제품 질문에 답변할 때, 에스컬레이션이나 중단에 응답할 때, 지연이나 수정 불가 같은 나쁜 소식을 전달할 때, 기능 요청을 거부할 때, 청구 문제에 답할 때 사용하세요.
argument-hint: "<situation description>"
---

# /draft-response

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

상황, 고객 관계, 커뮤니케이션 맥락에 맞춰 전문적이고 고객을 향한 대응 초안을 작성하세요.

## 용법

```
/draft-response <context about the customer question, issue, or request>
```

예:
- `/draft-response Acme Corp is asking when the new dashboard feature will ship`
- `/draft-response Customer escalation — their integration has been down for 2 days`
- `/draft-response Responding to a feature request we won't be building`
- `/draft-response Customer hit a billing error and wants a resolution ASAP`

## 작업흐름

### 1. 맥락을 이해하라

사용자 입력을 구문 분석하여 다음을 결정합니다.

- **고객**: 누구를 위한 커뮤니케이션인가요? 가능한 경우 계정 컨텍스트를 찾아보세요.
- **상황 유형**: 질문, 문제, 에스컬레이션, 공지, 협상, 나쁜 소식, 좋은 소식, 후속 조치
- **긴급성**: 시간에 민감한가요? 고객이 얼마나 오랫동안 기다렸나요?
- **채널**: 이메일, 지원 티켓, 채팅 등(적절하게 형식 조정)
- **관계 단계**: 신규 고객, 확립, 좌절/확대
- **이해관계자 수준**: 최종 사용자, 관리자, 임원, 기술, 비즈니스

### 2. 연구 맥락

사용 가능한 소스에서 관련 배경을 수집합니다.

****이메일:**
- 이 주제에 관해 이 고객과의 이전 서신
- 이전에 공유된 모든 약속이나 일정
- 기존 스레드의 톤과 스타일

****채팅:**
- 이 고객 또는 주제에 대한 내부 토론
- 제품, 엔지니어링 또는 리더십의 모든 지침
- 유사한 상황과 처리 방법

****CRM(연결된 경우):**
- 계정 세부정보 및 요금제 수준
- 연락처 정보 및 주요 이해관계자
- 이전 에스컬레이션 또는 민감한 문제

****지원 플랫폼(연결된 경우):**
- 관련 티켓 및 해결 방법
- 알려진 문제 또는 해결 방법
- SLA 상태 및 응답 시간 약속

****지식 기반:**
- 참조할 공식 문서 또는 도움말 문서
- 제품 로드맵 정보(공유 가능한 경우)
- 정책 또는 프로세스 문서

### 3. 초안 생성

상황에 맞는 응답을 생성합니다.

```
## Draft Response

**To:** [Customer contact name]
**Re:** [Subject/topic]
**Channel:** [Email / Ticket / Chat]
**Tone:** [Empathetic / Professional / Technical / Celebratory / Candid]

---

[Draft response text]

---

### Notes for You (internal — do not send)
- **Why this approach:** [Rationale for tone and content choices]
- **Things to verify:** [Any facts or commitments to confirm before sending]
- **Risk factors:** [Anything sensitive about this response]
- **Follow-up needed:** [Actions to take after sending]
- **Escalation note:** [If this should be reviewed by someone else first]
```

### 4. 품질 검사 실행

초안을 발표하기 전에 다음을 확인하십시오.

- [ ] 어조가 상황 및 관계와 일치함
- [ ] 승인된 것 이상으로 약속하지 않음
- [ ] 외부에 공유하면 안 되는 제품 로드맵 세부정보가 없습니다.
- [ ] 이전 대화에 대한 정확한 언급
- [ ] 다음 단계 및 소유권 지우기
- [ ] 이해관계자 수준에 적합(임원에게는 너무 기술적이지 않고 엔지니어에게는 너무 모호하지 않음)
- [ ] 길이가 채널에 적합합니다(채팅의 경우 더 짧고 이메일의 경우 더 큼).

### 5. 제안 반복

초안을 발표한 후:
- "Want me to adjust the tone? (more formal, more casual, more empathetic, more direct)"
- "Should I add or remove any specific points?"
- "Want me to make this shorter/longer?"
- "Should I draft a version for a different stakeholder?"
- "Want me to draft the internal escalation note as well?"
- "Should I prepare a follow-up message to send after [X days] if no response?"

---

## 고객 커뮤니케이션 모범 사례

### 핵심 원칙

1. **공감으로 이끌어주세요**: 해결책을 찾기 전에 고객의 상황을 파악하세요.
2. **직접적으로 설명하세요**: 고객이 바쁘기 때문에 요점을 명확하게 설명하세요. 바텀 라인 업 프론트.
3. **정직하게 행동하세요**: 지나친 약속을 하지 말고, 오해를 불러일으키지도 말고, 나쁜 소식을 전문 용어로 숨기지 마세요.
4. **구체적으로 작성하세요**: 구체적인 세부정보, 타임라인, 이름을 사용하고 모호한 언어는 피하세요.
5. **소유**: 적절한 경우 책임을 집니다. "We"은(는) "the system" 또는 "the process"이 아닙니다.
6. **루프 닫기**: 모든 응답에는 명확한 다음 단계 또는 클릭 유도 문구가 있어야 합니다.
7. **에너지를 일치시키세요**: 그들이're frustrated, be empathetic first. If they'기분이 좋으면 열정을 가지세요.

### 응답 구조

대부분의 고객 커뮤니케이션에서는 다음 구조를 따르십시오.

```
1. Acknowledgment / Context (1-2 sentences)
   - Acknowledge what they said, asked, or are experiencing
   - Show you understand their situation

2. Core Message (1-3 paragraphs)
   - Deliver the main information, answer, or update
   - Be specific and concrete
   - Include relevant details they need

3. Next Steps (1-3 bullets)
   - What YOU will do and by when
   - What THEY need to do (if anything)
   - When they'll hear from you next

4. Closing (1 sentence)
   - Warm but professional sign-off
   - Reinforce you're available if needed
```

### 길이 지침

- **채팅/IM**: 1~4문장. 즉시 요점을 파악하세요.
- **지원 티켓 응답**: 1~3개의 짧은 단락. 구조화되어 있으며 스캔 가능합니다.
- **이메일**: 최대 3~5문단 받은 편지함을 존중하세요.
- **에스컬레이션 응답**: 철저해야 하지만 헤더를 사용하여 체계적으로 구성해야 합니다.
- **경영진 커뮤니케이션**: 짧을수록 좋습니다. 최대 2~3문단 데이터 중심.

## 어조 및 스타일 지침

### 톤 스펙트럼

| 상황 | 음정 | 형질 |
|-----------|------|----------------|
| 좋은 소식 / 승리 | 기념 | 열정적이고, 따뜻하며, 축하하고, 미래 지향적입니다. |
| 정기 업데이트 | 전문적인 | 명확하고 간결하며 유익하고 친절합니다. |
| 기술적 대응 | 정밀한 | 정확하고, 상세하고, 체계적이며, 인내심이 강함 |
| 배송지연 | 책임이 있는 | 정직함, 사과함, 행동지향적, 구체적 |
| 나쁜 소식 | 솔직한 | 직접적, 공감적, 해결 지향적, 존중적 |
| 문제/중단 | 긴급한 | 즉각적이고 투명하며 실행 가능하고 안심할 수 있음 |
| 단계적 확대 | 경영진 | 침착하고, 주인의식을 갖고, 계획을 제시하고, 자신감이 있습니다. |
| 결제/계정 | 정밀한 | 명확하고 사실적이며 공감적이며 해결 중심적입니다. |

### 관계 단계별 톤 조정

**신규 고객(0-3개월):**
- 좀 더 형식적이고 전문적인
- 추가 맥락 및 설명(알고 있다고 가정하지 마세요)
- 도움과 리소스를 적극적으로 제공
- 신뢰성과 대응력을 통해 신뢰 구축

**기존 고객(3개월 이상):**
- 따뜻하고 협력적인
- 공유 기록 및 이전 대화를 참조할 수 있습니다.
- 보다 직접적이고 효율적인 의사소통
- 목표와 우선순위에 대한 인식을 보여줍니다.

**불만했거나 에스컬레이션한 고객:**
- 추가적인 공감과 인정
- 응답 시간의 긴급성
- 구체적인 약속이 포함된 구체적인 실행 계획
- 더 짧은 피드백 루프

### 글쓰기 스타일 규칙

**하다:**
- 능동태 사용("We'll investigate" 아님 "This will be investigated")
- 개인적인 약속에는 "I"을 사용하고 팀 약속에는 "we"을 사용하세요.
- 작업을 할당할 때 특정 사람의 이름을 지정하세요("Sarah from our engineering team will...").
- 내부 전문 용어가 아닌 고객의 용어를 사용하십시오.
- 상대적인 용어가 아닌 특정 날짜 및 시간을 포함합니다("by Friday January 24" 아님 "in a few days").
- 헤더나 글머리 기호로 긴 응답을 나누세요.

**하지 않다:**
- 기업 전문 용어나 유행어를 사용하세요("synergy", "leverage", "paradigm shift").
- 다른 팀, 시스템 또는 프로세스에 대한 비난을 돌리십시오.
- 소유권을 피하기 위해 수동태를 사용하세요("Mistakes were made")
- 신뢰를 훼손하는 불필요한 경고나 위험 회피를 포함합니다.
- 불필요하게 참조 사용자 — 대화에 참여해야 하는 사람만 포함
- 느낌표를 과도하게 사용합니다(있는 경우 이메일당 최대 1개).

## 상황별 접근 방식

**제품 질문에 답변:**
- 직접적인 답변으로 이끌어라
- 관련 문서 링크 제공
- 필요한 경우 적절한 리소스에 연결해 주겠다고 제안하세요.
- 답을 모른다면 솔직하게 말하고, 알아내기 위해 노력하고, 일정을 알려주세요.

**문제 또는 버그에 응답:**
- 업무에 미치는 영향을 인정합니다.
- 문제와 그 상태에 대해 알고 있는 내용을 기술하세요.
- 가능한 경우 해결 방법 제공
- 해결 일정에 대한 기대치 설정
- 정기적인 업데이트를 약속합니다.

**에스컬레이션 처리:**
- 심각성과 좌절감을 인정하십시오.
- 소유권을 가지세요(편향이나 변명 금지)
- 타임라인과 함께 명확한 실행 계획 제공
- 해결 책임이 있는 사람을 식별합니다.
- 심각도에 따라 적절한 경우 회의 또는 전화 제공

**나쁜 소식을 전합니다(기능 종료, 지연, 수정할 수 없음):**
- 직접적으로 말하세요 - 뉴스를 묻어두지 마세요
- 이유를 솔직하게 설명하라
- 구체적으로 그들에게 미치는 영향을 인정하십시오.
- 대안 또는 완화 제안
- 앞으로 나아갈 길을 명확하게 제시하세요

**좋은 소식 공유(기능 출시, 이정표, 인정):**
- 긍정적인 결과로 이끌어라
- 특정 목표나 사용 사례에 연결하세요.
- 좋은 소식을 활용하기 위한 다음 단계 제안
- 진정한 열정을 표현하세요

**요청 거부(기능 요청, 할인, 예외):**
- 요청과 그 이유를 인정합니다.
- 결정에 솔직해지세요
- 무시하지 않고 이유를 설명하세요.
- 가능하다면 대안을 제시하세요
- 미래의 대화를 위해 문을 열어두세요

## 일반적인 시나리오에 대한 응답 템플릿

### 버그 신고 확인

```
Hi [Name],

Thank you for reporting this — I can see how [specific impact] would be
frustrating for your team.

I've confirmed the issue and escalated it to our engineering team as a
[priority level]. Here's what we know so far:
- [What's happening]
- [What's causing it, if known]
- [Workaround, if available]

I'll update you by [specific date/time] with a resolution timeline.
In the meantime, [workaround details if applicable].

Let me know if you have any questions or if this is impacting you in
other ways I should know about.

Best,
[Your name]
```

### 청구 또는 계정 문제 확인

```
Hi [Name],

Thank you for reaching out about this — I understand billing issues
need prompt attention, and I want to make sure this gets resolved
quickly.

I've looked into your account and here's what I'm seeing:
- [What happened — clear factual explanation]
- [Impact on their account — charges, access, etc.]

Here's what I'm doing to fix this:
- [Action 1 — with timeline]
- [Action 2 — if applicable]

[If resolution is immediate: "This has been corrected and you should
see the change reflected within [timeframe]."]
[If needs investigation: "I'm escalating this to our billing team
and will have an update for you by [specific date]."]

I'm sorry for the inconvenience. Let me know if you have any
questions about your account.

Best,
[Your name]
```

### 구축하지 않을 기능 요청에 응답하기

```
Hi [Name],

Thank you for sharing this request — I can see why [capability] would
be valuable for [their use case].

I discussed this with our product team, and this isn't something we're
planning to build in the near term. The primary reason is [honest,
respectful explanation — e.g., it serves a narrow use case, it conflicts
with our architecture direction, etc.].

That said, I want to make sure you can accomplish your goal. Here are
some alternatives:
- [Alternative approach 1]
- [Alternative approach 2]
- [Integration or workaround if applicable]

I've also documented your request in our feedback system, and if our
direction changes, I'll let you know.

Would any of these alternatives work for your team? Happy to dig
deeper into any of them.

Best,
[Your name]
```

### 정전 또는 사고 통신

```
Hi [Name],

I wanted to reach out directly to let you know about an issue affecting
[service/feature] that I know your team relies on.

**What happened:** [Clear, non-technical explanation]
**Impact:** [How it affects them specifically]
**Status:** [Current status — investigating / identified / fixing / resolved]
**ETA for resolution:** [Specific time if known, or "we'll update every X hours"]

[If applicable: "In the meantime, you can [workaround]."]

I'm personally tracking this and will update you as soon as we have a
resolution. You can also check [status page URL] for real-time updates.

I'm sorry for the disruption to your team's work. We take this seriously
and [what you're doing to prevent recurrence if known].

[Your name]
```

### 침묵 후 후속 조치

```
Hi [Name],

I wanted to check in — I sent over [what you sent] on [date] and
wanted to make sure it didn't get lost in the shuffle.

[Brief reminder of what you need from them or what you're offering]

If now isn't a good time, no worries — just let me know when would be
better, and I'm happy to reconnect then.

Best,
[Your name]
```

## 후속 조치 및 에스컬레이션 지침

### 후속 케이던스

| 상황 | 후속 조치 시기 |
|-----------|-----------------|
| 답변되지 않은 질문 | 영업일 기준 2~3일 |
| 공개 지원 문제 | 심각한 문제는 해결될 때까지 매일, 표준의 경우 2~3일 |
| 회의 후 조치 항목 | 24시간 이내(메모보내기) 이후 마감일에 확인 |
| 일반 체크인 | 지속적인 문제에 필요한 경우 |
| 나쁜 소식을 전한 뒤 | 영향과 감정을 확인하는 데 1주일 |

### 에스컬레이션해야 하는 경우

**다음과 같은 경우 관리자에게 에스컬레이션하세요.**
- 고객이 취소하거나 대폭 하향 판매하겠다고 위협함
- 고객이 승인할 수 없는 정책에 대한 예외를 요청합니다.
- SLA가 허용하는 것보다 오랫동안 문제가 해결되지 않았습니다.
- 고객이 경영진과 직접 연락을 요청합니다.
- 해결하려면 고위 관계자가 필요한 오류를 범했습니다.

**다음과 같은 경우 제품/엔지니어링팀으로 에스컬레이션하세요.**
- 버그가 심각하여 고객의 비즈니스를 방해함
- 기능 격차로 인해 경쟁 손실이 발생함
- 고객은 표준 지원 이상의 고유한 기술 요구 사항을 갖고 있습니다.
- 통합 문제에는 엔지니어링 조사가 필요합니다.

**에스컬레이션 형식:**
```
ESCALATION: [Customer Name] — [One-line summary]

Urgency: [Critical / High / Medium]
Customer impact: [What's broken for them]
History: [Brief background — 2-3 sentences]
What I've tried: [Actions taken so far]
What I need: [Specific help or decision needed]
Deadline: [When this needs to be resolved by]
```
