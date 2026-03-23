---
name: contact-research
description: "Common Room 데이터를 사용해 특정 인물을 조사합니다. 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead' 또는 모든 연락처 수준 질문에 반응합니다."
---

# 연락처 조사

Common Room에서 포괄적인 연락처 프로필을 가져옵니다. 이메일, 소셜 핸들, 이름+회사로 조회할 수 있습니다. 활동 이력, Spark, 점수, 웹사이트 방문, CRM 필드를 포함한 보강 데이터를 반환합니다.

## 1단계: 연락처 찾기

Common Room은 여러 조회 방법을 지원합니다. 사용자가 제공한 방식 중 하나를 사용하세요.

| 사용자가 제공한 정보 | 조회 방법 |
|---------------------|--------------|
| 이메일 주소 | 이메일로 조회(가장 신뢰도 높음) |
| LinkedIn, Twitter/X, 또는 GitHub 핸들 | 소셜 핸들로 조회 - 핸들 유형을 명시적으로 지정 |
| 이름 + 회사 | 이름 + 조직 도메인으로 신원 확인; 모호하면 일치 항목을 제시 |
| 이름만 | 이름으로 검색; 여러 일치 항목이 있으면 간단한 목록을 보여 주고 사용자에게 확인 요청 |

일치 항목이 없으면 다음처럼 답하세요: "Common Room에 이 사람의 기록이 없습니다." 추측하거나 프로필 데이터를 만들어내지 마세요.

## 2단계: 연락처 필드 가져오기

Common Room 객체 카탈로그를 사용해 사용 가능한 필드 그룹과 그 내용을 확인하세요. 전체 프로필에는 모든 그룹을 요청하고, 특정 질문에는 관련된 것만 요청하세요.

**알아두어야 할 핵심 필드 그룹:**
- **Scores** - 항상 라벨이 아니라 원시 값 또는 백분위로 반환
- **Recent activity** - `Contact Initiated` 필터(지난 60일)를 사용해 상대의 행동만 확인하고, 우리 팀의 활동은 제외
- **Website visits** - 총 횟수와 특정 페이지(지난 12주)
- **Spark** - 참여 변화 추이를 추적할 때는 모든 Spark를 가져오기

## 3단계: Spark 보강 실행(가능하면)

Spark를 사용할 수 있으면 사용하세요. Spark는 다음을 제공합니다.
- Professional background and job history
- Social presence and influence signals
- Persona classification: Champion, Economic Buyer, Technical Evaluator, End User, or Gatekeeper
- Inferred role in the buying process

Spark가 없지만 실제 활동 데이터(최근 행동, 웹사이트 방문, 커뮤니티 참여)가 있으면 그 신호로 persona를 추론하세요. Spark도 활동 데이터도 없으면 Unknown으로 분류하세요. 직함만 보고 persona를 추정하지 마세요.

사용자가 이 연락처의 참여가 시간에 따라 어떻게 변했는지 알고 싶어 할 때는 가장 최근 것만이 아니라 **모든 Spark**를 가져오세요.

## 4단계: 계정 맥락 평가

이 연락처의 모회사에 대한 축약된 계정 스냅샷을 가져오세요. 다음을 확인합니다.
- Open opportunities, expansion signals, or churn risk at the account level
- Whether other contacts at this company are also active
- How this person's engagement compares to their colleagues

## 5단계: 대화 각도 식별

활동과 신호를 바탕으로 가장 강한 단서 2~3개를 제시하세요.
- A recent `Contact Initiated` activity (community post, product event, support ticket)
- A specific web page they visited recently — especially if it signals evaluation intent
- A job change, promotion, or company news
- Their Spark persona and what that suggests about communication style
- Their role in a known active deal

## 출력 형식

Only include sections where data was actually returned. Omit sections with no data rather than filling them with guesses.

**When data is rich:**

```
## [Contact Name] — Profile

**Overview**
[2 sentences: who they are, their role, and relationship status]

**Details**
- Title: [title]
- Company: [company]
- Email: [email]
- LinkedIn: [URL]
- Other profiles: [Twitter/X, GitHub, CRM link if available]

**Scores** [If scores returned]
[All scores as raw values or percentiles]

**Recent Activity** (last 60 days) [If activity returned]
[3–5 bullets with dates]

**Website Visits** (last 12 weeks) [If visit data exists]
[Total visit count + list of pages visited]

**Spark Profile** [If Spark data is non-null]
[Persona type, background summary, influence signals]

**Segments** [If segments returned]
[List of segment names this contact belongs to]

**Account Context**
[1–2 sentences on their company's status]

**Conversation Starters**
[2–3 specific, signal-backed openers]
```

**When data is sparse (e.g., only name, title, email, tags returned; sparkSummary is null):**

```
## [Contact Name] — Profile (Limited Data)

**Data available:** [List exactly what Common Room returned]

[Present only the returned fields]

**Web Search**
[Any findings from searching their name + company]

**Note:** Common Room has limited data on this contact. No activity history, scores, or Spark profile available. I can run deeper web searches or look up their company for additional context.
```

희소한 데이터로는 대화 시작점, persona 추론, 참여도 평가를 만들지 마세요. 이런 것들은 실제 신호가 필요합니다.

## 품질 기준

- 조회는 입력 유형에 맞는 올바른 방법을 사용해야 합니다. 이메일과 핸들을 추측하지 마세요.
- Scores는 원시 값/백분위만 사용하고 라벨은 쓰지 마세요.
- `Contact Initiated` 활동(지난 60일)이 핵심 참여 신호입니다. 이를 먼저 제시하세요.
- Spark가 없으면 그렇게 말하고, 직함만으로 persona를 꾸며내지 마세요.
- 가장 최근 활동이 30일보다 오래된 연락처는 표시하세요.

## 참고 파일

- **`references/contact-signals-guide.md`** - 전체 필드 설명, Spark persona 가이드, 대화 시작점 원칙
