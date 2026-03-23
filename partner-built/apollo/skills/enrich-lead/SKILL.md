---
name: enrich-lead
description: "Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next actions."
user-invocable: true
argument-hint: "[name, company, LinkedIn URL, or email]"
---

# 리드 보강

어떤 식별자든 완전한 연락처 파일로 바꿉니다. 사용자는 `"$ARGUMENTS"`로 식별 정보를 제공합니다.

## 예시

- `/apollo:enrich-lead Tim Zheng at Apollo`
- `/apollo:enrich-lead https://www.linkedin.com/in/timzheng`
- `/apollo:enrich-lead sarah@stripe.com`
- `/apollo:enrich-lead Jane Smith, VP Engineering, Notion`
- `/apollo:enrich-lead CEO of Figma`

## 1단계 - 입력 파싱

`"$ARGUMENTS"`에서 사용할 수 있는 모든 식별자를 추출합니다.
- 이름, 성
- 회사 이름 또는 도메인
- LinkedIn URL
- 이메일 주소
- 직함(매칭 힌트로 사용)

입력이 모호하다면(예: "Figma의 CEO"만 있는 경우) 먼저 관련 직함과 도메인 필터를 사용해 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`로 사람을 식별한 뒤 보강을 진행합니다.

## 2단계 - 사람 보강

> **크레딧 경고**: 호출 전에 보강에 Apollo 크레딧 1개가 소모된다고 사용자에게 알립니다.

Use `mcp__claude_ai_Apollo_MCP__apollo_people_match` with all available identifiers:
- `first_name`, `last_name` if name is known
- `domain` or `organization_name` if company is known
- `linkedin_url` if LinkedIn is provided
- `email` if email is provided
- Set `reveal_personal_emails` to `true`

매칭이 실패하면 더 느슨한 필터로 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`를 시도하고 상위 3개 후보를 보여줍니다. 사용자에게 하나를 고르게 한 뒤 다시 보강합니다.

## 3단계 - 회사 보강

Use `mcp__claude_ai_Apollo_MCP__apollo_organizations_enrich` with the person's company domain to pull firmographic context.

## 4단계 - 연락처 카드 제시

출력을 정확히 다음 형식으로 만듭니다.

---

**[전체 이름]** | [직함]
[회사 이름] · [산업] · [직원 수]명

| Field | Detail |
|---|---|
| 이메일(업무) | ... |
| 이메일(개인) | ... (공개된 경우) |
| 전화(직통) | ... |
| 전화(모바일) | ... |
| 전화(회사) | ... |
| 위치 | 도시, 주, 국가 |
| LinkedIn | URL |
| 회사 도메인 | ... |
| 회사 매출 | 범위 |
| 회사 펀딩 | 총 조달 금액 |
| 회사 본사 | 위치 |

---

## 5단계 - 다음 행동 제안

사용자에게 어떤 행동을 할지 묻습니다.

1. **Apollo에 저장** - `run_dedupe: true`를 사용해 `mcp__claude_ai_Apollo_MCP__apollo_contacts_create`로 이 사람을 연락처로 만듭니다
2. **시퀀스에 추가** - 어느 시퀀스인지 묻고 sequence-load 흐름을 실행합니다
3. **동료 찾기** - `q_organization_domains_list`를 이 회사로 설정한 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`로 같은 회사의 다른 사람을 찾습니다
4. **비슷한 사람 찾기** - 다른 회사에서 같은 직함/시니어리티의 사람을 검색합니다
