---
name: account-research
description: "Common Room 데이터를 사용해 회사를 조사합니다. 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]' 또는 계정 수준 질문에 반응합니다."
---

# 계정 조사

Common Room에서 계정 정보를 가져와 종합합니다. 전체 개요, 특정 필드 질문, 희소 데이터 상황, MCP 데이터와 LLM 추론을 결합한 네 가지 상호작용 패턴을 처리합니다.

## 0단계: 사용자 컨텍스트( Me ) 불러오기

어떤 계정을 조사하든 먼저 Common Room에서 `Me` 객체를 가져오세요. 이를 통해 다음 정보를 얻습니다.
- The user's profile, title, role, and Persona in CR
- The user's segments ("My Segments")

사용자가 더 넓은 범위를 명시적으로 요청하지 않는 한 모든 쿼리는 기본적으로 사용자의 세그먼트로 제한하세요. 이렇게 하면 결과가 담당 구역에 맞게 유지됩니다.

## 1단계: 상호작용 패턴 식별

얼마나 많은 데이터를 가져올지 정하기 전에 사용자가 실제로 무엇을 원하는지 파악하세요.

**패턴 1 - 전체 개요:** "Datadog에 대해 알려줘" / "cloudflare.com 요약해줘"
→ 전체 필드 집합을 가져와 구조화된 브리핑을 만듭니다.

**패턴 2 - 특정 질문:** "Snowflake 계정 담당자는 누구야?" / "acme.io에서 구매 신호가 보이나?" / "notion.so의 직원 수는 얼마야?"
→ 관련 필드만 가져옵니다. 간단한 질문에는 전체 브리핑을 만들지 말고 직접적이고 간결한 답변을 반환하세요.

**패턴 3 - 희소 데이터:** "tiny-startup.io에 대해 알려줘"
→ Common Room에 해당 계정 데이터가 제한적이면 솔직하게 말하세요: "이 계정에 대해서는 제한된 정보만 उपलब्ध합니다." 절대 추측하거나 일반론으로 공백을 채우지 마세요.

**패턴 4 - 결합 추론:** 구조화된 MCP 데이터를 가져온 뒤 LLM 분석을 더합니다. 예: "Stripe는 직원이 8,000명이고 AI 직군 채용을 많이 하고 있습니다. 귀사의 ICP가 1천~1만 명 규모의 핀테크 회사라면, 이는 강한 적합 대상입니다."

## 2단계: 계정 조회

도메인 또는 회사명으로 Common Room에서 계정을 검색하세요. 먼저 정확히 일치하는 항목을 찾고, 결과가 없으면 부분 일치를 시도한 뒤 진행 전에 사용자에게 확인하세요.

## 3단계: 올바른 필드 가져오기

Common Room 객체 카탈로그를 사용해 사용 가능한 필드 그룹과 그 내용을 확인하세요. 전체 개요에서는 모든 필드 그룹을 요청하고, 특정 질문에서는 관련된 것만 요청하세요.

**알아두어야 할 핵심 필드 그룹:**
- **Scores** - 항상 라벨이 아니라 원시 값 또는 백분위로 반환
- **Summary research** - RoomieAI 출력; 보통 가장 풍부한 정성 신호
- **Top contacts** - 점수 내림차순으로 정렬; 전체 조회에는 communityMemberID 사용

**가져올 내용 선택하기:**

| 사용자 질의 유형 | 요청할 필드 |
|-----------------|------------------|
| 전체 계정 개요 | 모든 필드 그룹 |
| "이 계정 담당자는 누구야?" | 회사 프로필 및 링크, CRM 필드 |
| "이 회사는 적합한 대상인가?" | 핵심 필드, 점수, 소개 |
| "이 계정은 어떤 신호를 보이나?" | 점수, 요약 리서치, CRM 필드 |
| "상위 연락처는 누구야?" | 상위 연락처 |
| "RoomieAI는 뭐라고 말하나?" | 요약 리서치, 전체 리서치 |
| "이 계정의 엔지니어를 찾아줘" | Prospects(직함 필터 포함) |

## 4단계: 웹 검색(희소 데이터에만)

Common Room이 기본 데이터 소스입니다. CR이 풍부한 데이터를 반환하면 웹 검색을 하지 마세요.

CR 데이터가 희소할 때(패턴 3 - 반환된 필드가 적고, 활동과 점수가 없을 때)는 공백을 메우기 위해 표적 웹 검색을 실행하세요.
- `"[company name]" news` — scoped to the last 30 days
- Look for: funding rounds, acquisitions, product launches, executive changes, press coverage

사용자가 외부 컨텍스트나 최근 뉴스를 명시적으로 요청하면 데이터가 충분하더라도 웹 검색을 실행하세요.

## 5단계: 추론 적용(패턴 4)

사용자의 질문이 단순한 데이터 조회가 아니라 종합을 요구하면 분석을 더하세요.
- 계정 데이터를 세션 컨텍스트의 ICP 기준과 비교
- 적합 신호 식별(규모, 산업, 기술 스택, 채용 패턴)
- 타이밍 신호 메모(투자 유치, 체험판 상태, 최근 활동 급증)
- 인사이트는 추정이 아니라 데이터에서 명확히 도출된 것으로 표현

사용자의 회사 컨텍스트가 가능하면(`references/my-company-context.md` 참고) 결과를 사용자의 가치 제안과 ICP에 비춰 설명하세요.

## 6단계: 출력 생성

Common Room이 실제로 반환한 데이터가 있는 섹션만 포함하세요. 추측으로 섹션을 채우지 말고 아예 생략하세요.

**Full overview (when data is rich):**

```
## [Company Name] — Account Overview

**Snapshot**
[2–3 sentences: what they do, plan/stage, relationship status]

**Key Details**
[Employee count, industry, location, domain, funding — from key fields]

**CRM & Ownership** [If CRM fields returned]
[Owner, opp stage, ARR]

**Scores** [If scores returned]
[All available scores as raw values or percentiles]

**Signal Highlights** [If activity/signals exist]
[3–5 most important signals with dates]

**Top Contacts** [If contacts returned]
[Name | Title | Score — top 5 sorted by score desc]

**RoomieAI Research** [If summary research is non-null]
[Summary research output; list all available research topic names]

**Recommended Next Steps**
[2–3 specific, signal-backed actions]
```

**특정 질문:** 1~3문장의 직접 답변. 전체 브리핑은 불필요합니다.

**Sparse data (few fields returned, most sections would be empty):**

```
## [Company Name] — Account Overview (Limited Data)

**Data available:** [List exactly what Common Room returned]

[Present only the returned fields]

**Web Search**
[Findings from web search — or "No significant recent news found"]

**Note:** Common Room has limited data on this account. The account may need enrichment in Common Room.
```

## 품질 기준

- Scores는 항상 원시 값 또는 백분위여야 하며, 범주형 라벨을 사용하면 안 됩니다.
- 특정 질문에는 정확하게 답하고 과하게 늘어놓지 마세요.
- 데이터가 없거나 오래된 경우 명확히 밝히고, 추측하지 마세요.
- 전체 브리핑은 2~3분 안에 읽을 수 있게 유지하세요.
- **모든 사실은 도구 호출로 추적 가능해야 합니다** - Common Room이 반환하지 않은 데이터는 포함하지 마세요.

## 참고 파일

- **`references/signals-guide.md`** - 신호 유형 분류 및 해석 가이드
