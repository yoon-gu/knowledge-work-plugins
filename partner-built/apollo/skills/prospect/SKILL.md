---
name: prospect
description: "ICP에서 리드까지의 전체 파이프라인. 이상적인 고객을 평문으로 설명하면 이메일과 전화번호가 포함된 보강된 의사결정권자 리드의 순위표를 받습니다."
user-invocable: true
argument-hint: "[이상적인 고객 설명]"
---

# Prospect

ICP 설명에서 순위가 매겨진 보강된 리드 목록을 한 번에 생성합니다. 사용자는 "$ARGUMENTS"를 통해 이상적인 고객을 설명합니다.

## 예시

- `/apollo:prospect VP of Engineering at Series B+ SaaS companies in the US, 200-1000 employees`
- `/apollo:prospect heads of marketing at e-commerce companies in Europe`
- `/apollo:prospect CTOs at fintech startups, 50-500 employees, New York`
- `/apollo:prospect procurement managers at manufacturing companies with 1000+ employees`
- `/apollo:prospect SDR leaders at companies using Salesforce and Outreach`

## 1단계 — ICP 파싱

"$ARGUMENTS"의 자연어 설명에서 구조화된 필터를 추출합니다:

**회사 필터:**
- 업종/수직 키워드 → `q_organization_keyword_tags`
- 직원 수 범위 → `organization_num_employees_ranges`
- 회사 위치 → `organization_locations`
- 특정 도메인 → `q_organization_domains_list`

**인물 필터:**
- 직함 → `person_titles`
- 직급 → `person_seniorities`
- 인물 위치 → `person_locations`

ICP가 모호하면 진행 전에 1-2개의 명확화 질문을 합니다. 최소한 직함/역할과 업종 또는 회사 규모가 필요합니다.

## 2단계 — 회사 검색

회사 필터를 사용하여 `mcp__claude_ai_Apollo_MCP__apollo_mixed_companies_search`를 실행합니다:
- 업종/수직에는 `q_organization_keyword_tags`
- 규모에는 `organization_num_employees_ranges`
- 지역에는 `organization_locations`
- `per_page`를 25로 설정

## 3단계 — 상위 회사 보강

상위 10개 결과의 도메인으로 `mcp__claude_ai_Apollo_MCP__apollo_organizations_bulk_enrich`를 사용합니다. 이를 통해 매출, 펀딩, 직원 수, 기업 데이터를 확인하여 회사 순위를 매기는 데 도움이 됩니다.

## 4단계 — 의사결정권자 찾기

다음을 사용하여 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`를 실행합니다:
- ICP의 `person_titles`와 `person_seniorities`
- 보강된 회사 도메인으로 범위를 좁힌 `q_organization_domains_list`
- `per_page`를 25로 설정

## 5단계 — 상위 리드 보강

> **크레딧 경고**: 진행 전에 소비될 크레딧 수를 사용자에게 정확히 알려주세요.

다음을 사용하여 `mcp__claude_ai_Apollo_MCP__apollo_people_bulk_match`로 호출당 최대 10명의 리드를 보강합니다:
- 각 인물의 `first_name`, `last_name`, `domain`
- `reveal_personal_emails`를 `true`로 설정

10명 이상의 리드가 있을 경우, 여러 번의 호출로 나눕니다.

## 6단계 — 리드 테이블 제시

결과를 순위 테이블로 표시합니다:

### 일치하는 리드: [ICP 요약]

| # | 이름 | 직함 | 회사 | 직원 수 | 매출 | 이메일 | 전화번호 | ICP 적합도 |
|---|---|---|---|---|---|---|---|---|

**ICP 적합도** 점수:
- **Strong** — 직함, 직급, 회사 규모, 업종 모두 일치
- **Good** — 4가지 기준 중 3개 일치
- **Partial** — 4가지 기준 중 2개 일치

**요약**: Y개 회사에서 X명의 리드 발견. Z 크레딧 소비.

## 7단계 — 다음 행동 제안

사용자에게 다음을 제안합니다:

1. **전체 Apollo에 저장** — 각 리드에 대해 `run_dedupe: true`로 `mcp__claude_ai_Apollo_MCP__apollo_contacts_create`를 통해 연락처 일괄 생성
2. **시퀀스에 로딩** — 어떤 시퀀스인지 묻고 이 연락처들에 대해 sequence-load 플로우 실행
3. **회사 심층 분석** — 목록의 회사에 대해 `/apollo:company-intel` 실행
4. **검색 조정** — 필터를 조정하고 재실행
5. **내보내기** — 쉬운 복사-붙여넣기를 위해 리드를 CSV 형식 테이블로 포맷
