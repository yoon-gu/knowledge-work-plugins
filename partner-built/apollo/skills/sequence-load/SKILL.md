---
name: sequence-load
description: "Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow."
user-invocable: true
argument-hint: "[targeting criteria + sequence name]"
---

# 시퀀스 불러오기

아웃리치 시퀀스에 넣을 연락처를 찾고, 보강하고, 불러옵니다. 사용자는 `"$ARGUMENTS"`로 타게팅 기준과 시퀀스 이름을 제공합니다.

## Examples

- `/apollo:sequence-load add 20 VP Sales at SaaS companies to my "Q1 Outbound" sequence`
- `/apollo:sequence-load SDR managers at fintech startups → Cold Outreach v2`
- `/apollo:sequence-load list sequences` (shows all available sequences)
- `/apollo:sequence-load directors of engineering, 500+ employees, US → Demo Follow-up`
- `/apollo:sequence-load reload 15 more leads into "Enterprise Pipeline"`

## 1단계 - 입력 파싱

`"$ARGUMENTS"`에서 다음을 추출합니다.

**타게팅 기준:**
- 직함 → `person_titles`
- 시니어리티 수준 → `person_seniorities`
- 산업 키워드 → `q_organization_keyword_tags`
- 회사 규모 → `organization_num_employees_ranges`
- 위치 → `person_locations` 또는 `organization_locations`

**시퀀스 정보:**
- 시퀀스 이름("to", "into", "→" 뒤의 텍스트)
- 수량 - 추가할 연락처 수(지정되지 않으면 기본 10)

사용자가 그냥 "list sequences"라고 말하면 2단계로 건너뛰어 사용 가능한 시퀀스를 모두 보여줍니다.

## 2단계 - 시퀀스 찾기

Use `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_search` to find the target sequence:
- Set `q_name` to the sequence name from input

일치하는 항목이 없거나 여러 개면:
- 사용 가능한 모든 시퀀스를 표로 보여줍니다: | Name | ID | Status |
- 사용자가 하나를 고르게 합니다

## 3단계 - 이메일 계정 가져오기

Use `mcp__claude_ai_Apollo_MCP__apollo_email_accounts_index` to list linked email accounts.

- 계정이 1개면 자동으로 사용합니다
- 여러 개면 보여주고 어느 계정에서 보낼지 묻습니다

## 4단계 - 일치하는 사람 찾기

Use `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search` with the targeting criteria.
- Set `per_page` to the requested volume (or 10 by default)

후보를 미리보기 표로 제시합니다.

| # | Name | Title | Company | Location |
|---|---|---|---|---|

다음과 같이 묻습니다. **"[N]개의 연락처를 [시퀀스 이름]에 추가할까요? 보강에 Apollo 크레딧 [N]개가 소모됩니다."**

진행하기 전에 확인을 기다립니다.

## 5단계 - 연락처 보강 및 생성

For each approved lead:

1. **보강** - `mcp__claude_ai_Apollo_MCP__apollo_people_bulk_match`를 사용합니다(호출당 최대 10개 배치).
   - `first_name`, `last_name`, `domain` for each person
   - `reveal_personal_emails` set to `true`

2. **연락처 생성** - 보강된 각 사람에 대해 `mcp__claude_ai_Apollo_MCP__apollo_contacts_create`를 사용합니다.
   - `first_name`, `last_name`, `email`, `title`, `organization_name`
   - `direct_phone` or `mobile_phone` if available
   - `run_dedupe` set to `true`

생성된 모든 연락처 ID를 모읍니다.

## 6단계 - 시퀀스에 추가

Use `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_add_contact_ids` with:
- `id`: the sequence ID
- `emailer_campaign_id`: same sequence ID
- `contact_ids`: array of created contact IDs
- `send_email_from_email_account_id`: the chosen email account ID
- `sequence_active_in_other_campaigns`: `false` (safe default)

## 7단계 - 등록 확인

요약을 보여줍니다.

---

**시퀀스 불러오기 성공**

| Field | Value |
|---|---|
| 시퀀스 | [이름] |
| 추가된 연락처 | [개수] |
| 발신 계정 | [이메일 주소] |
| 사용한 크레딧 | [개수] |

**등록된 연락처:**

| Name | Title | Company | Email |
|---|---|---|---|

---

## 8단계 - 다음 행동 제안

사용자에게 다음을 묻습니다.

1. **더 불러오기** - 또 다른 리드 배치를 찾아 추가합니다
2. **시퀀스 검토** - 시퀀스 세부 정보와 등록된 모든 연락처를 보여줍니다
3. **연락처 제거** - 특정 연락처를 제거하기 위해 `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_remove_or_stop_contact_ids`를 사용합니다
4. **연락처 일시 중지** - `status: "paused"`와 `auto_unpause_at` 날짜를 사용해 다시 추가합니다
