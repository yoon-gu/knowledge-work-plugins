---
name: enrich-lead
description: "즉시 리드 보강. 이름, 회사, LinkedIn URL, 또는 이메일을 입력하면 이메일, 전화번호, 직함, 회사 정보, 다음 행동이 포함된 완전한 연락처 카드를 받습니다."
user-invocable: true
argument-hint: "[이름, 회사, LinkedIn URL, 또는 이메일]"
---

# 리드 보강

식별자를 완전한 연락처 정보로 변환합니다. 사용자가 "$ARGUMENTS"를 통해 식별 정보를 제공합니다.

## 예시

- `/apollo:enrich-lead Tim Zheng at Apollo`
- `/apollo:enrich-lead https://www.linkedin.com/in/timzheng`
- `/apollo:enrich-lead sarah@stripe.com`
- `/apollo:enrich-lead Jane Smith, VP Engineering, Notion`
- `/apollo:enrich-lead CEO of Figma`

## 1단계 — 입력 파싱

"$ARGUMENTS"에서 사용 가능한 모든 식별자를 추출합니다:
- 이름, 성
- 회사명 또는 도메인
- LinkedIn URL
- 이메일 주소
- 직함 (매칭 힌트로 사용)

입력이 모호한 경우(예: "Figma의 CEO"), 먼저 관련 직함 및 도메인 필터로 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`를 사용하여 인물을 확인한 후 보강을 진행합니다.

## 2단계 — 인물 보강

> **크레딧 경고**: 보강 호출 전에 사용자에게 1 Apollo 크레딧이 소비됨을 알려주세요.

사용 가능한 모든 식별자와 함께 `mcp__claude_ai_Apollo_MCP__apollo_people_match`를 사용합니다:
- 이름이 알려진 경우 `first_name`, `last_name`
- 회사가 알려진 경우 `domain` 또는 `organization_name`
- LinkedIn이 제공된 경우 `linkedin_url`
- 이메일이 제공된 경우 `email`
- `reveal_personal_emails`를 `true`로 설정

매칭이 실패하면 느슨한 필터로 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`를 시도하고 상위 3명의 후보를 제시합니다. 사용자가 한 명을 선택하면 다시 보강합니다.

## 3단계 — 소속 회사 보강

해당 인물의 회사 도메인으로 `mcp__claude_ai_Apollo_MCP__apollo_organizations_enrich`를 사용하여 기업 데이터를 가져옵니다.

## 4단계 — 연락처 카드 제시

출력을 정확히 다음 형식으로 포맷합니다:

---

**[전체 이름]** | [직함]
[회사명] · [업종] · [직원 수] 명

| 항목 | 세부 정보 |
|---|---|
| 이메일 (업무) | ... |
| 이메일 (개인) | ... (공개된 경우) |
| 전화번호 (직통) | ... |
| 전화번호 (모바일) | ... |
| 전화번호 (회사) | ... |
| 위치 | 도시, 주, 국가 |
| LinkedIn | URL |
| 회사 도메인 | ... |
| 회사 매출 | 범위 |
| 회사 펀딩 | 총 조달액 |
| 회사 본사 | 위치 |

---

## 5단계 — 다음 행동 제안

사용자에게 다음 중 어떤 행동을 취할지 묻습니다:

1. **Apollo에 저장** — `run_dedupe: true`로 `mcp__claude_ai_Apollo_MCP__apollo_contacts_create`를 통해 이 인물을 연락처로 생성
2. **시퀀스에 추가** — 어떤 시퀀스인지 묻고 sequence-load 플로우 실행
3. **동료 찾기** — 이 회사의 `q_organization_domains_list`를 설정하여 `mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search`로 동일 회사의 더 많은 사람 검색
4. **유사한 사람 찾기** — 다른 회사에서 동일한 직함/직급의 사람 검색
