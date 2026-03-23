---
name: prospect
description: "Full ICP-to-leads pipeline. Describe your ideal customer in plain English and get a ranked table of enriched decision-maker leads with emails and phone numbers."
user-invocable: true
argument-hint: "[describe your ideal customer]"
---

# 잠재고객 발굴

ICP 설명에서 순위가 매겨진 보강 리드 목록까지 한 번에 만듭니다. 사용자는 `"$ARGUMENTS"`로 이상적인 고객을 설명합니다.

## 예시

- `/apollo:prospect VP of Engineering at Series B+ SaaS companies in the US, 200-1000 employees`
- `/apollo:prospect heads of marketing at e-commerce companies in Europe`
- `/apollo:prospect CTOs at fintech startups, 50-500 employees, New York`
- `/apollo:prospect procurement managers at manufacturing companies with 1000+ employees`
- `/apollo:prospect SDR leaders at companies using Salesforce and Outreach`

## 1단계 - ICP 파싱

`"$ARGUMENTS"`의 자연어 설명에서 구조화된 필터를 추출합니다.

**회사 필터:**
- 산업/세로 키워드 → `q_organization_keyword_tags`
- 직원 수 범위 → `organization_num_employees_ranges`
- 회사 위치 → `organization_locations`
- 특정 도메인 → `q_organization_domains_list`

**사람 필터:**
- 직함 → `person_titles`
- 시니어리티 수준 → `person_seniorities`
- 사람 위치 → `person_locations`

ICP가 모호하면 진행 전에 1-2개의 확인 질문을 합니다. 최소한 직함/역할과 산업 또는 회사 규모가 필요합니다.

## 2단계 - 회사 검색

Use `mcp__claude_ai_Apollo_MCP__apollo_mixed_companies_search` with the company filters:
- `q_organization_keyword_tags` for industry/vertical
- `organization_num_employees_ranges` for size
- `organization_locations` for geography
- Set `per_page` to 25

## 3단계 - 상위 회사 보강

Use `mcp__claude_ai_Apollo_MCP__apollo_organizations_bulk_enrich` with the domains from the top 10 results. This reveals revenue, funding, headcount, and firmographic data to help rank companies.

## 4단계 - 의사결정자 찾기

Use `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search` with:
- `person_titles` and `person_seniorities` from the ICP
- `q_organization_domains_list` scoped to the enriched company domains
- `per_page` set to 25

## 5단계 - 상위 리드 보강

> **크레딧 경고**: 진행 전에 정확히 몇 크레딧이 소모되는지 사용자에게 알려줍니다.

Use `mcp__claude_ai_Apollo_MCP__apollo_people_bulk_match` to enrich up to 10 leads per call with:
- `first_name`, `last_name`, `domain` for each person
- `reveal_personal_emails` set to `true`

리드가 10개를 넘으면 여러 호출로 나눕니다.

## 6단계 - 리드 표 제시

결과를 순위형 표로 보여줍니다.

### 일치하는 리드: [ICP 요약]

| # | Name | Title | Company | Employees | Revenue | Email | Phone | ICP Fit |
|---|---|---|---|---|---|---|---|---|

**ICP 적합도** 점수:
- **Strong** - 직함, 시니어리티, 회사 규모, 산업이 모두 일치
- **Good** - 4개 기준 중 3개가 일치
- **Partial** - 4개 기준 중 2개가 일치

**요약**: Y개 회사에서 X개의 리드를 찾았습니다. Z크레딧을 사용했습니다.

## 7단계 - 다음 행동 제안

사용자에게 다음을 묻습니다.

1. **모두 Apollo에 저장** - 각 리드에 대해 `run_dedupe: true`를 사용해 `mcp__claude_ai_Apollo_MCP__apollo_contacts_create`로 연락처를 일괄 생성합니다
2. **시퀀스에 불러오기** - 어느 시퀀스인지 묻고 이 연락처들에 대해 sequence-load 흐름을 실행합니다
3. **회사 심층 분석** - 목록의 어떤 회사든 `/apollo:company-intel`을 실행합니다
4. **검색 정교화** - 필터를 조정하고 다시 실행합니다
5. **내보내기** - 쉽게 복사할 수 있도록 CSV 형식 표로 정리합니다
