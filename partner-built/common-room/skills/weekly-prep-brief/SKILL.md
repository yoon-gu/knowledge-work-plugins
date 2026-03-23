---
name: weekly-prep-brief
description: "앞으로 7일 동안의 모든 외부 통화를 위한 포괄적인 주간 브리핑을 생성합니다. 'weekly prep brief', 'prepare my week', 'what calls do I have this week', 'Monday prep' 또는 모든 주간 계획 요청에 반응합니다."
---

# 주간 준비 브리핑

앞으로 7일 동안의 모든 외부 고객 또는 잠재고객 통화를 다루는 단일 포괄 주간 브리핑을 생성합니다. 각 미팅마다 Common Room의 계정 및 연락처 조사를 포함합니다.

## 브리핑 프로세스

### 1단계: 이번 주 외부 미팅 수집

**옵션 A - 캘린더가 연결된 경우:**
`~~calendar` 커넥터를 사용해 앞으로 7일(또는 사용자가 지정한 범위) 동안 일정이 잡힌 모든 미팅을 가져옵니다. 외부 참석자가 있는 미팅만 남기고 필터링하세요. 내부 전용 미팅, 동료와의 1:1, 반복되는 내부 싱크는 제외합니다.

각 외부 미팅에 대해 다음을 식별하세요.
- Company name
- Meeting date and time
- External attendee names and email addresses

**옵션 B - 캘린더가 연결되지 않은 경우:**
사용자에게 다음처럼 묻습니다: "주간 준비 브리핑을 만들려면 앞으로 있을 외부 통화 정보가 필요합니다. 회사명, 날짜/시간, 참석자 이름을 알려 주세요."

자유 형식 입력을 받아 구조화된 목록으로 파싱한 뒤 진행하세요.

### 2단계: 미팅 목록 확인

조사를 시작하기 전에 식별한 미팅을 사용자에게 보여 주고 확인을 받으세요.

> "Here are the external calls I found for this week. Let me know if anything's missing or should be excluded:
> - [Company] — [Day], [Time] — [Attendees]
> - ..."

이렇게 하면 취소되었거나 잘못된 미팅에 대해 불필요한 조사를 막을 수 있습니다.

### 3단계: 각 미팅 조사

확인된 각 외부 미팅에 대해 가능한 경우 병렬로 다음을 실행하세요.
1. **Account research** — full account snapshot using the account-research skill
2. **Contact research** — profile for each external attendee using the contact-research skill

Common Room 데이터가 기본 소스입니다. CR 조사를 마친 뒤 각 회사에 대해 간단한 **최신성 확인**을 실행하세요. 이는 보조 단계이며 기본은 아닙니다.
- Search `"[company name]" news` scoped to the last 7 days
- For executive attendees, search their name for recent public posts or interviews
- Only include findings that are genuinely noteworthy (funding, leadership changes, major press). Don't pad the brief with generic news.

깊이 조정:
- For high-priority accounts (large accounts, open opportunities, renewal risk), produce full depth research
- For lower-priority or short meetings, produce abbreviated snapshots (3–4 bullets each)

### 4단계: 주간 브리핑 종합

각 미팅별 조사를 미팅 날짜/시간순으로 정렬된 단일 구조화 문서로 묶습니다.

짧은 주간 개요로 시작해 다음 사항을 표시하세요.
- Any accounts with urgent signals (at-risk, trial expiring, expansion opportunity)
- Any meetings that need special preparation or executive involvement
- Total external call count and estimated time commitment

## 출력 형식

```
# Weekly Prep Brief — Week of [Date]

## Week Overview
[2–4 bullets: key themes, flagged priorities, call count]

---

## [Monday / Tuesday / etc.]

### [Company Name] — [Time]
**Attendees:** [Names and titles]
**Meeting type:** [Discovery / QBR / Renewal / Expansion / etc. — inferred if possible]

**Company Snapshot**
[4–5 bullets: account status, top signals, recent activity]

**Attendee Profiles**
- **[Name]** ([Title]): [2–3 bullets on their signals, persona, conversation angle]
- [Repeat per attendee]

**Top Signals This Week**
[2–3 most relevant signals for this specific call]

**This Week's News** [If notable news found]
[Only genuinely noteworthy findings — funding, leadership changes, major press]

**Recommended Objectives**
[1–2 sentences: what to accomplish in this meeting]

---

[Repeat per meeting, sorted by date/time]
```

## When a Meeting Has Sparse Data

If Common Room returns limited data for a particular meeting's account or attendees, use a compressed format for that meeting instead of the full template:

```
### [Company Name] — [Time] ⚠️ Limited Data
**Attendees:** [Names and titles if known]
**Data available:** [What Common Room actually returned]

**Web Search Results**
[Findings from web search — company news, attendee LinkedIn profiles]

**Note:** Common Room has limited data on this account. The rep may want to check directly in CR or gather context from colleagues before this call.
```

희소한 데이터로 전체 미팅 준비 섹션(회사 스냅샷, 신호 하이라이트, 대화 포인트, 권장 목표)을 만들지 마세요. 허구의 전체 섹션보다 짧고 솔직한 섹션이 더 유용합니다.

## 품질 기준

- 각 미팅 섹션은 훑어보기 쉽게 유지하세요. 담당자들은 아침에, 종종 모바일에서 읽습니다.
- 항상 날짜/시간 오름차순으로 정렬하세요.
- 긴급 상황(위험, 체험판 종료, 열린 기회)은 눈에 띄게 표시하고 숨기지 마세요.
- 미팅의 Common Room 데이터가 매우 얇으면 위의 희소 데이터 형식을 사용하세요. 추측으로 전체 템플릿을 채우지 마세요.
- 총 브리핑은 4~6개 미팅 기준 10~15분 안에 읽을 수 있어야 합니다.
- **모든 사실은 도구 호출에서 나와야 합니다** - 지어낸 딜 맥락, 활동, 신호는 없습니다.

## 참고 파일

- **`references/briefing-guide.md`** - 브리핑 구조화, 우선순위 로직, 취소 미팅 및 데이터가 없는 신규 계정 같은 예외 처리 가이드
