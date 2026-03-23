---
name: call-prep
description: "Common Room 신호를 사용해 고객 또는 잠재고객 통화를 준비합니다. 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]' 또는 모든 통화 준비 요청에 반응합니다."
---

# 통화 준비

계정 조사, 연락처 조사, Common Room 신호 종합을 결합해 완전하고 훑어보기 쉬운 통화 준비 브리핑을 만듭니다.

## 준비 프로세스

### 1단계: 계정과 참석자 식별

사용자가 제공한 정보를 해석하세요.
- **Company name** — required; look up the account in Common Room
- **Attendee names** — optional; if provided, research each one

**캘린더 조회:** `~~calendar` 커넥터를 사용할 수 있으면, 지정된 회사와의 예정 미팅을 검색해 참석자 이름, 미팅 시간, 회의 메모나 아젠다를 자동으로 가져옵니다. 사용자가 제공하지 않은 공백을 메우는 데 활용하세요.

참석자도 찾을 수 없고 캘린더 일치 항목도 없으면 다음처럼 묻습니다: "[Company] 쪽에서는 누가 통화에 참여하나요? 각 참석자를 조사해서 준비를 더 유용하게 만들 수 있습니다."

### 2단계: 계정 조사 실행

account-research 스킬 프로세스를 사용해 전체 계정 스냅샷을 만드세요. 통화 준비에서는 다음을 우선시합니다.
- Recent product signals (what are they doing in the product right now?)
- Open opportunities or renewal timeline
- Any risk signals (declining usage, support tickets, churned seats)
- Key recent events (funding, executive change, new hire)

활동 이력을 검토할 때는 Gong 및 통화 녹음 활동을 우선시하세요. 이는 이전 대화의 직접적인 맥락을 제공합니다. 활동 출처를 이유로 통화 녹음을 걸러내지 마세요.

### 3단계: 각 참석자에 대한 연락처 조사 실행

각 외부 참석자에 대해 contact-research 스킬 프로세스를 사용하세요. 통화 준비에서는 다음에 집중합니다.
- Role and influence in the buying process
- Their personal activity and engagement history
- Any recent signals that suggest their current mood/priorities
- Spark persona classification if available

### 4단계: 대화 포인트와 목표 종합

결합된 계정 및 연락처 조사를 바탕으로 다음을 수행합니다.
- Identify the **call objective** (e.g., discovery, demo, expansion conversation, renewal, QBR)
- Generate **3–5 tailored talking points** grounded in specific signal data
- Anticipate **2–3 likely objections or topics** the customer may raise
- Suggest a **recommended outcome** for the call

사용자의 회사 컨텍스트가 가능하면(`references/my-company-context.md` 참고) 대화 포인트를 사용자의 제품과 가치 제안에 맞게 조정하세요.

### 5단계: 최신성 확인(웹 검색)

모든 Common Room 데이터를 모은 뒤 간단한 최신성 확인을 실행해 마지막 CR 동기화 이후에 일어난 일을 잡아냅니다. 이는 보조 단계입니다. 준비의 중심은 CR 데이터이고, 웹 검색은 최신성만 더합니다.

**회사 뉴스:** 최근 14일로 필터한 `"[company name]" news`를 검색합니다. 투자 유치 발표, 제품 출시, 리더십 변화, 구조조정, 파트너십, 보도 노출을 찾습니다.

**참석자 존재감:** 각 외부 참석자에 대해 `"[full name]" "[company name]"`를 검색합니다. 최근 기사, LinkedIn 게시물, 컨퍼런스 발표, 팟캐스트, 공개 의견을 찾습니다.

회사 뉴스가 중요한 경우(예: 최근 투자 유치, 대형 채용 발표) Signal Highlights에 표시하세요. 그렇지 않으면 결과를 짧게만 포함하고, 웹 검색 결과가 CR 신호를 압도하지 않게 하세요.

## 출력 형식

The output adapts to how much data Common Room returned. Only include sections where you have real data. Never fill a section with invented details.

### When data is rich (multiple field groups returned, activity history, scores, signals):

```
## Call Prep: [Company] — [Date/Time if known]

**Meeting Context**
[Attendees, meeting type, and any known agenda]

---

### Company Snapshot
[4–6 bullets: key account status, signals, and recent activity]

---

### Attendee Profiles

**[Attendee Name] — [Title]**
[3–4 bullets: role, recent activity, Spark persona if available, personal hook]

[Repeat for each attendee]

---

### Signal Highlights
[Top 3 signals most relevant to this specific call]

---

### Talking Points
1. [Point tied to a specific signal]
2. [Point tied to a specific signal]
3. [Point tied to a specific signal]

### Likely Topics / Objections to Prepare For
- [Topic or objection + suggested response]
- [Topic or objection + suggested response]

### Recommended Call Outcome
[1–2 sentences: what success looks like for this meeting]
```

### When data is sparse (few fields returned, no activity, null sparkSummary):

```
## Call Prep: [Company] — [Date/Time if known]

**Data available:** [List exactly what Common Room returned — e.g., "Name, title, email, two tags. No activity history, no scores, no Spark data."]

### What I Found
[Only the fields actually returned, presented as-is]

### Web Search Results
[Findings from web search on the company and attendees — or "No significant results"]

### Suggested Next Steps
- I can pull [specific field groups] from Common Room if available
- I can run deeper web searches on [specific topics]
- You may want to check Common Room directly for [what's missing]
```

희소한 데이터로 전체 통화 준비 브리핑을 만들지 마세요. 길지만 허구인 결과보다 짧고 솔직한 결과가 항상 낫습니다.

## 품질 기준

- 모든 대화 포인트는 실제 신호에 근거해야 합니다. 일반적인 채움말은 금지입니다.
- 브리핑은 간결하게 유지하세요. 5분 이내에 읽을 수 있어야 합니다.
- 알 수 없는 부분은 명확히 표시하세요. 참석자 조사가 약하면 그렇게 말하세요.
- 연구에는 시간 제한을 두세요. 속도를 희생하면서 과도하게 파지 마세요.
- **딜 맥락을 절대 지어내지 마세요** - 도구 호출로 반환되지 않은 제안, 경쟁사 비교, 가격, 체험판 조건, 반론은 만들지 않습니다.

## 참고 파일

- **`references/call-types-guide.md`** - 다양한 통화 유형(디스커버리, 확장, 갱신, QBR)에 대한 가이드와 각 상황에 맞게 준비를 조정하는 방법
