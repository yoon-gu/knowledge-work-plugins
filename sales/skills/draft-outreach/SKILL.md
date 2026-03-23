---
name: draft-outreach
description: 잠재 고객을 조사한 뒤 개인화된 아웃리치를 작성합니다. 기본적으로 웹 검색을 사용하며, 보강 도구와 CRM을 연결하면 더 강력해집니다. "draft outreach to [person/company]", "write cold email to [prospect]", "reach out to [name]"을 입력하면 트리거됩니다.
---

# 아웃리치 초안

먼저 조사하고, 그다음 작성합니다. 이 스킬은 절대 일반적인 아웃리치를 보내지 않습니다. 항상 먼저 잠재 고객을 조사해 메시지를 개인화합니다. 웹 검색으로 단독 사용 가능하며, 도구를 연결하면 더 강력해집니다.

## 연결 도구(선택)

| 연결 도구 | 추가되는 내용 |
|-----------|--------------|
| **Enrichment** | 검증된 이메일, 전화번호, 배경 정보 |
| **CRM** | 이전 관계 맥락, 기존 연락처 |
| **Email** | 받은편지함에 바로 초안 생성 |

> **연결 도구가 없나요?** 웹 조사만으로도 충분히 잘 작동합니다. 복사할 수 있도록 이메일 텍스트를 출력합니다.

## 작동 방식

```
+------------------------------------------------------------------+
|                      아웃리치 초안                               |
|                                                                   |
|  1단계: 조사(항상 먼저)                                          |
|  - 웹 검색(기본)                                                 |
|  - + Enrichment(보강 도구가 연결된 경우)                         |
|  - + CRM(CRM이 연결된 경우)                                      |
|                                                                   |
|  2단계: 작성(조사 기반)                                          |
|  - 개인화된 오프닝(조사 결과)                                    |
|  - 관련 훅(그들의 우선순위)                                      |
|  - 명확한 CTA                                                    |
|                                                                   |
|  3단계: 전달(연결 도구 기반)                                     |
|  - 이메일 초안(이메일이 연결된 경우)                             |
|  - LinkedIn용 문구(항상)                                         |
|  - 사용자에게 출력(항상)                                         |
+------------------------------------------------------------------+
```

## 출력 형식

```markdown
# 아웃리치 초안: [Person] @ [Company]
**생성일:** [Date] | **조사 출처:** [Web, Enrichment, CRM]

---

## 조사 요약

**대상:** [Name], [Title] at [Company]
**훅:** [왜 지금 연락하는지 - 개인화된 각도]
**목표:** [이 아웃리치에서 원하는 것]

---

## 이메일 초안

**받는 사람:** [이메일이 있으면, 없으면 "find email" 메모]
**제목:** [개인화된 제목]

---

[이메일 본문]

---

**제목 대안:**
1. [옵션 2]
2. [옵션 3]

---

## LinkedIn 메시지(이메일이 없을 경우)

**연결 요청(< 300자):**
[짧고 피치 없는 연결 요청]

**후속 메시지(연결 후):**
[가치 우선 메시지]

---

## 왜 이 접근법인가

| 요소 | 근거 |
|---------|----------|
| 오프닝 | [개인화되게 만드는 조사 결과] |
| 훅 | [그들의 우선순위/고통 지점] |
| 증거 | [관련 고객 사례] |
| CTA | [부담이 적은 요청] |

---

## 이메일 초안 상태

[초안 생성됨 - ~~email 확인]
[이메일 미연결 - 위 이메일 복사]
[이메일을 찾지 못함 - LinkedIn 방식 사용]

---

## 후속 시퀀스(선택)

**3일차 - 후속 1:**
[짧은 새 각도]

**7일차 - 후속 2:**
[다른 가치 제안]

**14일차 - 마지막 시도:**
[최종 시도]
```

---

## 실행 흐름

### 1단계: 요청 파싱

```
입력 패턴:
- "draft outreach to John Smith at Acme" → 사람 + 회사
- "write cold email to Acme's CTO" → 역할 + 회사
- "reach out to sarah@acme.com" → 이메일 제공됨
- "LinkedIn message to [LinkedIn URL]" → 프로필 제공됨
```

### 2단계: 먼저 조사(항상)

**내부적으로 research-prospect 스킬 사용:**
```
1. 회사와 사람에 대한 웹 검색
2. Enrichment가 연결된 경우: 검증된 연락처 정보, 배경 가져오기
3. CRM이 연결된 경우: 이전 관계 확인
```

**작성 전에 반드시 찾아야 할 것:**
- 그들이 누구인지(직함, 배경)
- 회사가 하는 일
- 최근 뉴스 또는 트리거
- 개인화 훅

### 3단계: 훅 식별

```
훅의 우선순위:
1. 트리거 이벤트(투자 유치, 채용, 뉴스) → 가장 시의적
2. 상호 연결고리 → 사회적 증거
3. 그들의 콘텐츠(게시물, 글, 발표) → 조사했음을 보여 줌
4. 회사 이니셔티브 → 그들의 우선순위와 관련
5. 역할 기반 고통 지점 → 덜 개인적이지만 여전히 관련
```

### 4단계: 메시지 작성

**이메일 구조(AIDA):**
```
SUBJECT: [개인화, <50자, 스팸 단어 없음]

[오프닝: 개인화 훅 - 조사했다는 점을 보여줌]

[관심: 그들의 문제/기회를 1-2문장으로]

[욕구: 짧은 증거 - 비슷한 회사의 결과]

[행동: 명확하고 부담 없는 CTA]

[서명]
```

**LinkedIn 연결 요청(<300자):**
```
Hi [Name], [상호 연결/공통 관심사/진심 어린 칭찬].
Would love to connect. [No pitch]
```

**LinkedIn 후속 메시지:**
```
Thanks for connecting! [가치 우선: 인사이트, 기사, 관찰]

[왜 연락했는지로 부드럽게 전환]

[피치가 아닌 질문]
```

### 5단계: 이메일 초안 생성

```
이메일 연결이 있으면:
1. 받는 사람, 제목, 본문으로 초안 생성
2. 초안 링크 반환
3. "Draft created - review and send" 메모

연결이 없으면:
1. 이메일 텍스트 출력
2. "Copy to your email client" 메모
```

---

## 연결 도구별 기능

| 기능 | 웹만 | + Enrichment | + CRM | + Email |
|------------|----------|--------------|-------|---------|
| 개인화된 오프닝 | 기본 | 깊이 있음 | 이력 포함 | 동일 |
| 검증된 이메일 | 아니오 | 예 | 예 | 예 |
| 배경 정보 | 공개 정보만 | 전체 | 전체 | 전체 |
| 이전 관계 | 아니오 | 아니오 | 예 | 예 |
| 자동 초안 생성 | 아니오 | 아니오 | 아니오 | 예 |

---

## 시나리오별 메시지 템플릿

### 콜드 아웃리치(이전 관계 없음)

```
Subject: [그들의 이니셔티브] + [당신의 각도]

Hi [Name],

[조사 기반 개인화 훅 - 뉴스, 콘텐츠, 상호 연결].

[역할/회사 기반으로 추정한 1문장 문제].

[짧은 증거: "비슷한 회사에서 [결과]를 달성했습니다".]

관련이 있는지 15분 정도 이야기해 볼 수 있을까요?

[Signature]
```

### 웜 아웃리치(만난 적 있음 / 상호 연결고리)

```
Subject: Following up from [context]

Hi [Name],

[어떻게 알게 되었는지 / 누가 소개했는지].

[왜 지금 연락하는지 - 트리거].

[제공할 수 있는 구체적 가치].

[CTA]
```

### 재접촉(응답 없음)

```
Subject: [짧고 호기심을 자극하는 제목]

Hi [Name],

[시간이 지난 것을 비난 없이 인정].

[다시 연락할 새로운 이유 - 그들의 뉴스 또는 우리의 뉴스].

[대화를 다시 여는 간단한 질문].

[Signature]
```

### 이벤트 후 후속

```
Subject: Great meeting you at [Event]

Hi [Name],

[대화에서의 구체적인 기억].

[가치 추가: 이야기한 내용과 관련된 기사, 소개, 자료].

[다음 대화를 위한 부드러운 CTA].
```

---

## 이메일 스타일 가이드

1. **간결하지만 정보성 있게** — 핵심에 빨리 도달하세요. 바쁜 사람들은 훑어봅니다.
2. **마크다운 형식 금지** — 별표, 굵게(**text**)나 기타 마크다운을 쓰지 마세요. 어떤 이메일 클라이언트에서도 자연스러운 일반 텍스트로 쓰세요.
3. **짧은 문단** — 문단당 최대 2-3문장. 여백은 당신의 친구입니다.
4. **단순한 목록** — 항목을 나열할 때는 단순한 대시를 사용하세요. 화려한 형식은 금지입니다.

**좋은 예:**
```
Here's what I can share:
- Case study from a similar company
- 15-min intro call this week
- Quick demo if helpful
```

**나쁜 예:**
```
**What I Can Offer:**
- **Case study** from a similar company
- **Intro call** this week
```

---

## 하지 말아야 할 것

**평범한 시작 문구:**
- "I hope this email finds you well"
- "I'm reaching out because..."
- "I wanted to introduce myself"

**기능 나열:**
- 제품에 대한 긴 문단
- 여러 가치 제안을 한꺼번에
- 명확한 CTA 없음

**가짜 개인화:**
- "I noticed you work at [Company]"(당연한 내용)
- "Congrats on your role"(맥락 없이)

**이메일에서 마크다운 사용:**
- **굵게**나 *기울임* 별표 사용
- 렌더링되지 않을 헤더나 형식화된 목록

**대신:**
- 조사로 알게 된 구체적인 내용으로 시작
- 하나의 명확한 가치 제안
- 하나의 명확한 요청
- 일반 텍스트 형식만 사용

---

## 채널 선택

```
검증된 이메일이 있으면:
  → 이메일 우선(응답률이 더 높음)
  → LinkedIn 백업도 함께 제공

이메일이 없으면:
  → LinkedIn 연결 요청
  → 연결 후 후속 메시지 템플릿

따뜻한 소개가 가능하면:
  → 먼저 상호 연결을 통한 아웃리치를 제안
```

---

## 회사 설정 [CUSTOMIZE]

```markdown
## 아웃리치 설정

- My name: [Your Name]
- My title: [Your Title]
- My company: [Company Name]
- Value prop: [One sentence - what you help with]

## Signature
[Your preferred email signature]

## Proof Points
- [Customer 1]: [Result]
- [Customer 2]: [Result]
- [Customer 3]: [Result]

## CTA Options
- Default: "Worth a 15-min call?"
- Softer: "Open to learning more?"
- Specific: "Can I send over a quick demo?"

## Tone
- [Professional / Casual / Direct]
- Industry-specific language: [Yes/No]
```

---

## 예시

**입력:** "draft outreach to the Head of Engineering at Notion"

**조사 결과:**
- Name: David Tibbitts
- Recent news: Notion launched AI features
- Hiring: 5 ML engineer roles open
- Background: Ex-Facebook, Stanford CS

**출력:**

```markdown
# Outreach Draft: David Tibbitts @ Notion

## Research Summary
**Target:** David Tibbitts, Head of Engineering at Notion
**Hook:** They're scaling AI features and hiring ML talent
**Goal:** Intro call about AI infrastructure

---

## Email Draft

**To:** david@notion.so
**Subject:** Notion's AI scaling + a thought

---

Hi David,

Saw Notion's AI rollout is gaining serious traction - congrats.
With 5 ML roles open, seems like you're scaling fast.

Curious how you're thinking about inference infrastructure
as usage grows. We helped [Similar Company] cut their AI
serving costs 40% while improving latency.

Worth a 15-min call to see if relevant to your roadmap?

Best,
[Name]

---

**Subject Alternatives:**
1. Notion AI + scaling question
2. Quick thought on Notion's ML hiring

---

## Email Draft Status
Draft created - check ~~email
```
