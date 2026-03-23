---
name: prospect
description: "Common Room의 Prospector를 사용해 타깃 계정 또는 연락처 목록을 만듭니다. 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]' 또는 모든 목록 작성 요청에 반응합니다."
---

# 프로스펙팅

Common Room의 Prospector를 사용해 타깃 계정 및 연락처 목록을 만듭니다. 자연스러운 대화를 통한 반복적 세부 조정, 의도 기반 탐색, 새 계정 대상 프로스펙팅과 기존 계정 대상 신호 기반 쿼리를 모두 지원합니다.

## 중요한 구분: 두 가지 객체 유형

Common Room의 Prospector는 근본적으로 다른 두 객체 유형을 대상으로 동작합니다. 쿼리를 실행하기 전에 항상 어떤 유형인지 확인하세요.

**`ProspectorOrganization`** - Common Room에 아직 없는 회사
- Net-new companies that match specified criteria
- Available fields are firmographic only: name, domain, size, industry, capital raised, annual revenue, location
- Fewer filter options — no signal-based filters, no scores, no activity history
- Use when: building a brand-new target list, territory planning, top-of-funnel expansion

**`Organization`** (Common Room 내) - 이미 CR 워크스페이스에 있는 회사
- Full signal data available: product usage, community activity, CRM fields, scores, custom fields
- Much richer filter set — includes signal-based, score-based, segment-based, and firmographic filters
- Use when: finding warm accounts to prioritize, identifying expansion candidates, surfacing intent signals within existing pipeline

사용자 요청이 두 유형 모두에 적용될 수 있으면(예: "이번 달 AI 엔지니어를 채용 중인 회사를 보여줘") 다음처럼 확인하세요.
> "Are you looking for net-new companies not yet in Common Room, or filtering accounts already in your workspace?"

카탈로그는 이 차이를 명확히 드러내 LLM이 올바른 Prospector 엔드포인트를 선택할 수 있게 해야 합니다.

## 0단계: 사용자 컨텍스트( Me ) 불러오기

사용자의 세그먼트를 얻기 위해 `Me` 객체를 가져오세요. `Organization` 레코드(CR에 이미 있는 계정)를 대상으로 프로스펙팅할 때는 사용자가 더 넓은 검색을 요청하지 않는 한 기본적으로 "My Segments" 안에서 필터링하세요.

## 1단계: 타깃 기준 수집

기준이 이미 주어졌으면 진행하세요. 그렇지 않으면 다음처럼 묻습니다.

> "What kind of accounts or contacts are you looking for? For example: company size, industry, job titles, signals like recent product activity or community engagement, geographic region, or specific intent signals like recent funding or job postings."

Common Room 객체 카탈로그를 사용해 각 객체 유형에서 사용할 수 있는 필터를 확인하세요. 핵심 구분은 다음과 같습니다.
- **ProspectorOrganization** — firmographic and technographic filters only (industry, size, geography, funding, tech stack)
- **Organization** — all firmographic filters plus signal-based, score-based, segment-based, and CRM filters

**유사 회사 검색:** 사용자가 "find companies like [X]"라고 요청하면, 먼저 Common Room에서 기준 회사를 조회합니다(CR에 없으면 웹 검색 사용). 산업, 직원 규모, 기술 스택, 자금 조달 단계, 지역 같은 핵심 속성을 추출해 필터 기준으로 제안하세요. 유사 타깃팅은 어떤 속성이 중요한지 사용자가 조정할 수 있을 때 가장 효과적이므로, 검색 전에 도출된 기준을 사용자에게 보여 주고 확인을 받으세요.

## 2단계: 반복적 세부 조정 지원

프로스펙팅은 대화형입니다. 다중 턴 세부 조정을 자연스럽게 지원하세요.

1. Run initial query with provided criteria
2. If results are large (50+), summarize and offer: "I found [N] results. Want to narrow by [suggested filter]?"
3. If results are too few (< 5), suggest: "Only [N] results with those filters — I can broaden by relaxing [specific criterion]."
4. Apply each refinement as a follow-up query, not a new search from scratch

Example flow:
- Rep: "Find cybersecurity companies in California." → 500 results
- Rep: "Only show ones over 300 employees using AWS." → 47 results
- Rep: "Focus on the ones with recent hiring activity." → 12 results ✓

## 3단계: 쿼리 실행 및 결과 제시

확인된 기준으로 Prospector 쿼리를 실행하세요. 가능하면 알파벳순이 아니라 신호 강도 또는 적합도 점수로 정렬하세요.

**`ProspectorOrganization`(새 계정) 결과의 경우:**

| Company | Domain | Industry | Size | Capital Raised | Revenue | Location |
|---------|--------|----------|------|---------------|---------|----------|

**`Organization`(CR 내) 결과의 경우:**

| Company | Industry | Size | Top Signal | Signal Date | Score | CRM Stage |
|---------|----------|------|-----------|-------------|-------|-----------|

데이터가 얇거나 가장 최근 신호가 90일보다 오래된 결과는 표시하세요.

## 3.5단계: 새 결과를 웹 검색으로 보강

`ProspectorOrganization` 결과(CR에 없는 새 회사)에 대해서는 상위 3~5개 회사에 대해 간단한 웹 검색을 실행해 기업 정보 이상으로 맥락을 더하세요. 이 회사들에는 CR의 행동 신호가 없으므로 웹 검색이 공백을 메웁니다. 최근 투자 유치, 제품 출시, 리더십 변화, 보도 노출을 찾고, 각 회사 옆에 짧은 주석으로 결과를 포함하세요.

## 4단계: 다음 단계 제안

- "Want me to draft outreach for the top 3–5 prospects?"
- "Should I run a full account brief on any of these?"
- "Want to refine the criteria or add another filter?"
- "I can format this as a CSV if you'd like to export it."
- "For any net-new companies here, I can add them to Common Room for enrichment." *(future capability)*

## 품질 기준

- 쿼리를 실행하기 전에 항상 어떤 객체 유형(ProspectorOrg vs Organization)인지 확인하세요.
- 사용자가 달리 지정하지 않으면 Organization 레코드 조회 시 "My Segments"를 기본으로 사용하세요.
- 반복적 세부 조정을 지원하세요. 후속 요청은 새 검색이 아니라 필터 조정으로 다뤄야 합니다.
- ProspectorOrganization과 Organization의 결과 필드를 같은 목록에 섞지 마세요.
- 길지만 검증되지 않은 목록보다 고품질 결과가 적은 편이 낫습니다.
- **쿼리가 반환한 데이터만 보여 주세요** - 없는 필드는 비워 두거나 "—"로 두고 값을 만들어내지 마세요.

## 참고 파일

- **`references/prospect-guide.md`** - 필터 유형, 신호 기반 정렬, 객체 유형 구분, 목록 작성 전략
