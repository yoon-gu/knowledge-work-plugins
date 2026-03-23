---
name: sequence-load
description: "기준에 맞는 리드를 찾아 Apollo 아웃리치 시퀀스에 일괄 추가합니다. 보강, 연락처 생성, 중복 제거 및 등록을 하나의 플로우로 처리합니다."
user-invocable: true
argument-hint: "[타겟팅 기준 + 시퀀스 이름]"
---

# Sequence Load

아웃리치 시퀀스에 연락처를 찾고, 보강하고, 로딩합니다 — 전 과정을 처리합니다. 사용자는 "$ARGUMENTS"를 통해 타겟팅 기준과 시퀀스 이름을 제공합니다.

## 예시

- `/apollo:sequence-load add 20 VP Sales at SaaS companies to my "Q1 Outbound" sequence`
- `/apollo:sequence-load SDR managers at fintech startups → Cold Outreach v2`
- `/apollo:sequence-load list sequences` (사용 가능한 모든 시퀀스 표시)
- `/apollo:sequence-load directors of engineering, 500+ employees, US → Demo Follow-up`
- `/apollo:sequence-load reload 15 more leads into "Enterprise Pipeline"`

## 1단계 — 입력 파싱

"$ARGUMENTS"에서 다음을 추출합니다:

**타겟팅 기준:**
- 직함 → `person_titles`
- 직급 → `person_seniorities`
- 업종 키워드 → `q_organization_keyword_tags`
- 회사 규모 → `organization_num_employees_ranges`
- 위치 → `person_locations` 또는 `organization_locations`

**시퀀스 정보:**
- 시퀀스 이름 ("to", "into", 또는 "→" 뒤의 텍스트)
- 추가할 연락처 수 (지정하지 않은 경우 기본값: 10)

사용자가 "list sequences"라고만 하면 2단계로 건너뛰고 사용 가능한 모든 시퀀스를 표시합니다.

## 2단계 — 시퀀스 찾기

대상 시퀀스를 찾기 위해 `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_search`를 사용합니다:
- `q_name`을 입력의 시퀀스 이름으로 설정

일치하지 않거나 여러 개가 일치하는 경우:
- 모든 사용 가능한 시퀀스를 테이블로 표시: | 이름 | ID | 상태 |
- 사용자에게 하나를 선택하도록 요청

## 3단계 — 이메일 계정 가져오기

연결된 이메일 계정 목록을 보기 위해 `mcp__claude_ai_Apollo_MCP__apollo_email_accounts_index`를 사용합니다.

- 계정이 하나이면 → 자동으로 사용
- 여러 개이면 → 목록을 표시하고 어느 것으로 발송할지 묻습니다

## 4단계 — 일치하는 인물 찾기

타겟팅 기준으로 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`를 사용합니다.
- `per_page`를 요청한 수량(또는 기본값 10)으로 설정

후보를 미리보기 테이블로 제시합니다:

| # | 이름 | 직함 | 회사 | 위치 |
|---|---|---|---|---|

묻습니다: **"이 [N]명의 연락처를 [시퀀스 이름]에 추가하겠습니까? 보강에 [N] Apollo 크레딧이 소비됩니다."**

진행 전에 확인을 기다립니다.

## 5단계 — 보강 및 연락처 생성

승인된 각 리드에 대해:

1. **보강** — `mcp__claude_ai_Apollo_MCP__apollo_people_bulk_match` 사용 (호출당 최대 10명 일괄 처리):
   - 각 인물의 `first_name`, `last_name`, `domain`
   - `reveal_personal_emails`를 `true`로 설정

2. **연락처 생성** — 각 보강된 인물에 대해 `mcp__claude_ai_Apollo_MCP__apollo_contacts_create` 사용:
   - `first_name`, `last_name`, `email`, `title`, `organization_name`
   - 사용 가능한 경우 `direct_phone` 또는 `mobile_phone`
   - `run_dedupe`를 `true`로 설정

생성된 모든 연락처 ID를 수집합니다.

## 6단계 — 시퀀스에 추가

다음을 사용하여 `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_add_contact_ids`를 실행합니다:
- `id`: 시퀀스 ID
- `emailer_campaign_id`: 동일한 시퀀스 ID
- `contact_ids`: 생성된 연락처 ID 배열
- `send_email_from_email_account_id`: 선택된 이메일 계정 ID
- `sequence_active_in_other_campaigns`: `false` (안전한 기본값)

## 7단계 — 등록 확인

요약을 표시합니다:

---

**시퀀스 로딩 완료**

| 항목 | 값 |
|---|---|
| 시퀀스 | [이름] |
| 추가된 연락처 | [수] |
| 발송 계정 | [이메일 주소] |
| 사용된 크레딧 | [수] |

**등록된 연락처:**

| 이름 | 직함 | 회사 | 이메일 |
|---|---|---|---|

---

## 8단계 — 다음 행동 제안

사용자에게 다음을 제안합니다:

1. **더 로딩** — 다른 배치의 리드를 찾아 추가
2. **시퀀스 검토** — 시퀀스 세부 정보와 등록된 모든 연락처 표시
3. **연락처 제거** — `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_remove_or_stop_contact_ids`를 사용하여 특정 연락처 제거
4. **연락처 일시 중지** — `status: "paused"`와 `auto_unpause_at` 날짜로 재추가
