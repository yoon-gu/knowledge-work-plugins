---
name: compose-outreach
description: "Common Room 신호를 사용해 개인화된 아웃리치 메시지를 생성합니다. 'draft outreach to [person]', 'write an email to [name]', 'compose a message for [contact]' 또는 모든 아웃리치 작성 요청에 반응합니다."
---

# 아웃리치 작성

특정 회사나 연락처에 대한 Common Room 신호를 바탕으로 세 가지 개인화된 아웃리치 형식, 즉 이메일, 통화 스크립트, LinkedIn 메시지를 생성합니다.

## 아웃리치 프로세스

### 1단계: 대상 조회

Common Room MCP 도구를 사용해 대상(회사 및/또는 특정 연락처)의 데이터를 찾고 가져옵니다.
- Recent product activity and engagement signals
- Community activity (posts, questions, reactions)
- 3rd-party intent signals (job postings, news, funding)
- Relationship history (prior contact, meetings, email opens)

사용자가 사람을 지정했다면 연락처 수준의 조사를 실행합니다. 회사만 주어졌다면 직함, 참여도, 역할을 바탕으로 가장 적합한 대상을 찾습니다.

### 2단계: 외부 단서용 웹 검색(CR 신호가 얇을 때)

CR이 강한 신호(최근 활동, 참여도, 제품 사용)를 반환했다면 그것이 개인화의 중심이 되어야 하므로 웹 검색은 건너뜁니다. CR 신호가 약하거나 잠재고객의 CR 활동이 거의 없으면 외부 단서를 위해 웹 검색을 실행하세요.

**What to search:**
- `"[company name]" funding OR acquisition OR launch OR announcement` — last 30 days
- `"[contact full name]" "[company name]"` — look for recent articles, interviews, LinkedIn posts, or conference talks

**우선순위를 둘 외부 단서의 조건:**
- 매우 최근 것(< 2주) - 잠재고객이 아직 그 일을 떠올리고 있을 가능성이 큽니다
- 공개적으로 보이는 것 - 당신이 봤을 수 있다는 걸 상대도 압니다
- 변화 신호를 주는 것 - 성장, 새 역할, 새 제품, 새 시장

If the user explicitly asks for web search or external hooks, run it regardless of CR signal richness.

### 3단계: Spark 보강(가능하면)

Spark를 사용할 수 있으면 대상 연락처에 대해 보강을 실행해 persona 분류, 배경, 영향력 신호를 얻습니다. 이를 통해 톤과 메시지 각도를 조정하세요.

### 4단계: 가장 강한 단서 식별

신호 데이터에서 가장 강한 개인화 단서 1~3개를 식별합니다. 다음 기준으로 순위를 매깁니다.
1. **Recency** — happened in the last 7–14 days
2. **Specificity** — a concrete action they took, not a general trend
3. **Relevance** — connects directly to a value your product delivers

좋은 단서: 커뮤니티에서 X에 대해 질문을 올림, 엔지니어 5명을 새로 채용함, 최근 [feature]를 사용하기 시작함, 회사가 방금 Series B를 유치함, 체험판 종료가 임박함, 챔피언이 직장을 옮김.

나쁜 단서: "고객인 걸 봤습니다" 같은 문구, 또는 일반적인 산업 트렌드.

### 5단계: 세 가지 형식 모두 생성

가장 강한 단서를 사용해 세 가지 형식을 모두 작성합니다. 각 형식은 제약과 관례가 다르므로 `references/outreach-formats-guide.md`의 형식별 가이드를 따르세요.

항상 세 가지 모두를 명확히 구분해 작성하세요.

사용자의 회사 컨텍스트가 가능하면(`references/my-company-context.md` 참고) 가치 연결과 피치를 사용자의 구체적인 제품과 포지셔닝에 맞춰 구성하세요.

### 6단계: 선택 이유 주석 달기

세 가지 초안 뒤에는 다음을 설명하는 짧은 메모(2~4문장)를 포함하세요.
- 어떤 신호를 사용했고 왜 선택했는지
- 어떤 가정을 했는지(예: 추정한 통화 목표)
- 주요 단서가 반응을 얻지 못할 경우의 대안 각도

## 출력 형식

```
## Outreach for [Name / Company]

### 📧 Email

**Subject:** [Subject line]

[Email body — 3–5 sentences]

---

### 📞 Call Script

**Opening:**
[Opening line — conversational, 1–2 sentences]

**Value Bridge:**
[Why you're calling and why now — 2–3 sentences tied to a signal]

**Ask:**
[Single, low-friction ask — e.g., 15-minute call, specific question]

---

### 💼 LinkedIn Message

[Under 300 characters. Warm, personal, no pitch.]

---

### Signal Notes
[2–4 sentences: which signals were used, why, and any alternative angles]
```

## 신호 데이터가 희소할 때

If Common Room returns minimal data on the target (e.g., just name, title, tags — no activity, no scores, no Spark):

1. **근거 없이 아웃리치를 쓰지 마세요.** 조작된 신호에 기반한 아웃리치는 아예 없는 것보다 나쁩니다.
2. **먼저 웹 검색을 실행하세요** - 이것이 기본 개인화 소스가 됩니다. 최근 뉴스, LinkedIn 게시물, 컨퍼런스 발표, 회사 공지를 찾으세요.
3. **웹 검색도 거의 결과가 없으면**, 가진 정보를 솔직하게 제시하고 사용자에게 맥락을 요청하세요.

```
## Outreach for [Name / Company] — Limited Data

**What I found:**
[Only the real data from CR and web search]

**I don't have enough signal to draft personalized outreach yet.** To write something strong, I'd need:
- Recent activity or engagement signals
- Context you have from prior conversations
- A specific reason for reaching out now

Can you share any of the above?
```

## 품질 기준

- 모든 메시지는 구체적인 무언가를 참조해야 합니다. 일반론적인 아웃리치는 허용되지 않습니다.
- 톤은 맥락에 맞춰야 합니다. 인바운드/커뮤니티 신호에는 따뜻하고 대화체로, 콜드/임원 대상 아웃리치에는 더 공식적으로 맞추세요.
- LinkedIn 메시지는 반드시 300자 미만이어야 합니다. 예외는 없습니다.
- 통화 스크립트는 자연스럽게 읽힐 수 있어야 합니다. 소리 내어 읽는다고 생각하며 리듬을 점검하세요.
- **신호를 절대 조작하지 마세요** - Common Room 또는 웹 검색에서 가져온 데이터만 참조하세요.

## 참고 파일

- **`references/outreach-formats-guide.md`** - 각 채널의 상세 형식 규칙, 예시, 톤 가이드
