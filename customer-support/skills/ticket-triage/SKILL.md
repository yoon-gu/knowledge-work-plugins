---
name: ticket-triage
description: 지원 티켓 또는 고객 문제를 분류하고 우선순위를 지정합니다. 새 티켓이 들어와 분류가 필요할 때, P1~P4 우선순위를 할당하거나, 어떤 팀이 이를 처리해야 할지 결정하거나, 라우팅하기 전에 중복되거나 알려진 문제인지 확인하는 데 사용하세요.
argument-hint: "<ticket or issue description>"
---

# /ticket-triage

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

들어오는 지원 티켓이나 고객 문제를 분류하고 우선순위를 지정하고 라우팅합니다. 제안된 초기 대응을 통해 구조화된 분류 평가를 생성합니다.

## 용법

```
/ticket-triage <ticket text, customer message, or issue description>
```

예:
- `/ticket-triage Customer says their dashboard has been showing a blank page since this morning`
- `/ticket-triage "I was charged twice for my subscription this month"`
- `/ticket-triage User can't connect their SSO — getting a 403 error on the callback URL`
- `/ticket-triage Feature request: they want to export reports as PDF`

## 작업흐름

### 1. 문제 분석

입력을 읽고 추출합니다.

- **핵심 문제**: 고객이 실제로 겪고 있는 상황은 무엇입니까?
- **증상**: 어떤 구체적인 동작이나 오류가 표시됩니까?
- **고객 상황**: 누구인가요? 사용 가능한 계정 세부정보, 계획 수준 또는 내역이 있나요?
- **긴급 신호**: 차단되었나요? 이게 생산인가요? 영향을 받은 사용자는 몇 명입니까?
- **감정 상태**: 좌절감, 혼란스러움, 사실 문제, 고조되고 있습니까?

### 2. 분류 및 우선순위 지정

아래의 카테고리 분류 및 우선순위 프레임워크를 사용하세요.

- **기본 카테고리**(버그, 방법, 기능 요청, 청구, 계정, 통합, 보안, 데이터, 성능) 및 선택적 보조 카테고리를 할당합니다.
- 영향과 긴급성을 기준으로 **우선순위**(P1~P4)를 할당합니다.
- 문제가 해당되는 **제품 영역**을 식별하세요.

### 3. 중복 및 알려진 문제 확인

라우팅하기 전에 사용 가능한 소스를 확인하세요.

- ****지원 플랫폼**: 유사한 진행 중인 티켓 또는 최근 해결된 티켓 검색
- **~~지식 기반**: 알려진 문제 또는 기존 문서를 확인하세요.
- **~~프로젝트 트래커**: 기존 버그 보고서나 기능 요청이 있는지 확인하세요.

아래의 중복 감지 프로세스를 적용하세요.

### 4. 라우팅 결정

아래 라우팅 규칙을 사용하여 카테고리와 복잡성에 따라 어떤 팀이나 대기열을 처리해야 하는지 추천하세요.

### 5. 분류 출력 생성

```
## Triage: [One-line issue summary]

**Category:** [Primary] / [Secondary if applicable]
**Priority:** [P1-P4] — [Brief justification]
**Product area:** [Area/team]

### Issue Summary
[2-3 sentence summary of what the customer is experiencing]

### Key Details
- **Customer:** [Name/account if known]
- **Impact:** [Who and what is affected]
- **Workaround:** [Available / Not available / Unknown]
- **Related tickets:** [Links to similar issues if found]
- **Known issue:** [Yes — link / No / Checking]

### Routing Recommendation
**Route to:** [Team or queue]
**Why:** [Brief reasoning]

### Suggested Initial Response
[Draft first response to the customer — acknowledge the issue,
set expectations, provide workaround if available.
Use the auto-response templates below as a starting point.]

### Internal Notes
- [Any additional context for the agent picking this up]
- [Reproduction hints if it's a bug]
- [Escalation triggers to watch for]
```

### 6. 다음 단계 제안

분류를 제시한 후:
- "Want me to draft a full response to the customer?"
- "Should I search for more context on this issue?"
- "Want me to check if this is a known bug in the tracker?"
- "Should I escalate this? I can package it with /customer-escalation."

---

## 카테고리 분류

모든 티켓에 **기본 카테고리**를 할당하고 선택적으로 **보조 카테고리**를 할당하세요.

| 범주 | 설명 | 신호어 |
|----------|-------------|-------------|
| **벌레** | 제품이 올바르지 않거나 예기치 않게 작동합니다. | 오류, 파손, 충돌, 작동하지 않음, 예상치 못한, 잘못됨, 실패 |
| **방법** | 고객이 제품 사용에 대한 안내를 필요로 합니다. | 어떻게, 어떻게 할 수 있습니까, 어디에 있습니까? 설정, 구성, 도움 |
| **기능 요청** | 고객이 존재하지 않는 기능을 원함 | 내가 할 수 있으면 좋겠고, 어떤 계획도 요청한다면 좋을 것입니다. |
| **결제** | 결제, 구독, 송장 또는 가격 문제 | 청구, 송장, 결제, 구독, 환불, 업그레이드, 다운그레이드 |
| **계정** | 계정 액세스, 권한, 설정 또는 사용자 관리 | 로그인, 비밀번호, 액세스, 권한, SSO, 잠김, 로그인할 수 없음 |
| **완성** | 타사 도구 또는 API 연결 문제 | API, 웹훅, 통합, 연결, OAuth, 동기화, 타사 |
| **보안** | 보안 문제, 데이터 액세스 또는 규정 준수 관련 질문 | 데이터 침해, 무단, 규정 준수, GDPR, SOC 2, 취약성 |
| **데이터** | 데이터 품질, 마이그레이션, 가져오기/내보내기 문제 | 데이터 누락, 내보내기, 가져오기, 마이그레이션, 잘못된 데이터, 중복 |
| **성능** | 속도, 안정성 또는 가용성 문제 | 느림, 시간 초과, 대기 시간, 작동 중지, 사용할 수 없음, 저하됨 |

### 카테고리 결정 팁

- 고객이 버그와 기능 요청 **모두**를 신고하는 경우 해당 버그가 주요 버그입니다.
- 버그로 인해 로그인할 수 없는 경우 카테고리는 **버그**(계정 아님)입니다. 근본 원인이 카테고리를 결정합니다.
- "It used to work and now it doesn't" = **버그**
- "I want it to work differently" = **기능 요청**
- "How do I make it work?" = **방법**
- 의심스러운 경우 **버그**에 의지하세요. 무시하는 것보다 조사하는 것이 좋습니다.

## 우선순위 프레임워크

### P1 — 위험
**기준:** 프로덕션 시스템 다운, 데이터 손실 또는 손상, 보안 위반, 전체 또는 대부분의 사용자가 영향을 받습니다.

- 고객이 제품을 전혀 사용할 수 없습니다.
- 데이터가 손실, 손상 또는 노출되고 있습니다.
- 보안 사고가 진행 중입니다.
- 문제가 악화되거나 범위가 확대됨

**SLA 기대치:** 1시간 이내에 응답합니다. 해결되거나 완화될 때까지 지속적인 작업입니다. 1~2시간마다 업데이트됩니다.

### P2 - 높음
**기준:** 주요 기능이 손상되고, 중요한 워크플로가 차단되고, 많은 사용자가 영향을 받으며, 해결 방법이 없습니다.

- 핵심 워크플로가 중단되었지만 제품을 부분적으로 사용할 수 있습니다.
- 여러 사용자가 영향을 받거나 주요 계정이 영향을 받음
- 문제는 시간에 민감한 작업을 차단하는 것입니다.
- 합리적인 해결 방법이 없습니다.

**SLA 기대치:** 4시간 이내에 응답합니다. 당일 적극적인 조사. 4시간마다 업데이트됩니다.

### P3 — 중간
**기준:** 기능이 부분적으로 손상됨, 해결 방법 사용 가능, 단일 사용자 또는 소규모 팀이 영향을 받음.

- 기능이 제대로 작동하지 않지만 해결 방법이 있습니다.
- 문제가 불편하지만 중요한 작업을 방해하지는 않습니다.
- 단일 사용자 또는 소규모 팀이 영향을 받음
- 고객이 긴급하게 에스컬레이션하지 않고 있습니다.

**SLA 기대치:** 영업일 기준 1일 이내에 응답합니다. 영업일 기준 3일 이내에 문제를 해결하거나 업데이트하세요.

### P4 - 낮음
**기준:** 사소한 불편, 외관 문제, 일반적인 질문, 기능 요청.

- 기능에 영향을 주지 않는 외관 또는 UI 문제
- 기능 요청 및 개선 아이디어
- 일반적인 질문이나 이용방법 문의
- 간단하고 문서화된 솔루션 관련 문제

**SLA 기대치:** 영업일 기준 2일 이내에 응답하세요. 정상적인 속도로 해결합니다.

### 우선순위 에스컬레이션 트리거

다음과 같은 경우 자동으로 우선순위를 높입니다.
- 고객이 SLA에서 허용하는 것보다 오래 기다리고 있습니다.
- 여러 고객이 동일한 문제를 보고함(패턴 감지)
- 고객이 경영진의 개입을 명시적으로 에스컬레이션하거나 언급합니다.
- 기존에 있던 해결 방법이 작동을 멈춥니다.
- 문제의 범위가 확장됩니다(더 많은 사용자, 더 많은 데이터, 새로운 증상).

## 라우팅 규칙

카테고리 및 복잡성을 기준으로 티켓 라우팅:

| 라우팅 대상 | 언제 |
|----------|------|
| **계층 1(일선 지원)** | 방법 질문, 문서화된 솔루션에 대한 알려진 문제, 청구 문의, 비밀번호 재설정 |
| **계층 2(고위 지원)** | 조사가 필요한 버그, 복잡한 구성, 통합 문제 해결, 계정 문제 |
| **공학** | 코드 수정, 인프라 문제, 성능 저하가 필요한 버그 확인 |
| **제품** | 상당한 수요, 디자인 결정, 워크플로우 격차가 있는 기능 요청 |
| **보안** | 데이터 액세스 문제, 취약성 보고서, 규정 준수 질문 |
| **결제/재무** | 환불 요청, 계약 분쟁, 복잡한 결제 조정 |

## 중복 감지

새 티켓이나 라우팅을 만들기 전에 중복이 있는지 확인하세요.

1. **증상별 검색**: 유사한 오류 메시지나 설명이 있는 티켓을 찾습니다.
2. **고객별 검색**: 이 고객이 동일한 문제에 대한 티켓을 보유하고 있는지 확인하세요.
3. **상품 영역별 검색**: 동일 기능 영역의 최근 티켓을 찾아보세요.
4. **알려진 문제 확인**: 문서화된 알려진 문제와 비교

**중복이 발견된 경우:**
- 새 티켓을 기존 티켓에 연결
- 고객에게 이것이 알려진 문제이며 추적 중임을 알립니다.
- 새 보고서의 새 정보를 기존 티켓에 추가하세요.
- 새 보고서에 긴급성이 추가되면 우선순위를 높입니다(더 많은 고객이 영향을 받는 등).

## 카테고리별 자동 응답 템플릿

### 버그 — 초기 대응
```
Thank you for reporting this. I can see how [specific impact]
would be disruptive for your work.

I've logged this as a [priority] issue and our team is
investigating. [If workaround exists: "In the meantime, you
can [workaround]."]

I'll update you within [SLA timeframe] with what we find.
```

### 방법 — 초기 대응
```
Great question! [Direct answer or link to documentation]

[If more complex: "Let me walk you through the steps:"]
[Steps or guidance]

Let me know if that helps, or if you have any follow-up
questions.
```

### 기능 요청 - 초기 응답
```
Thank you for this suggestion — I can see why [capability]
would be valuable for your workflow.

I've documented this and shared it with our product team.
While I can't commit to a specific timeline, your feedback
directly informs our roadmap priorities.

[If alternative exists: "In the meantime, you might find
[alternative] helpful for achieving something similar."]
```

### 청구 — 초기 응답
```
I understand billing issues need prompt attention. Let me
look into this for you.

[If straightforward: resolution details]
[If complex: "I'm reviewing your account now and will have
an answer for you within [timeframe]."]
```

### 보안 - 초기 대응
```
Thank you for flagging this — we take security concerns
seriously and are reviewing this immediately.

I've escalated this to our security team for investigation.
We'll follow up with you within [timeframe] with our findings.

[If action is needed: "In the meantime, we recommend
[protective action]."]
```

## 선별 모범 사례

1. 분류하기 전에 전체 티켓을 읽으십시오. 이후 메시지의 맥락에 따라 평가가 변경되는 경우가 많습니다.
2. 설명된 증상뿐만 아니라 **근본 원인**을 기준으로 분류하세요.
3. 우선순위가 의심스러우면 더 높은 쪽을 선택하세요. 놓친 SLA를 복구하는 것보다 에스컬레이션을 줄이는 것이 더 쉽습니다.
4. 라우팅하기 전에 항상 중복 및 알려진 문제를 확인하세요.
5. 다음 사람이 상황을 빠르게 파악하는 데 도움이 되는 내부 메모를 작성하세요.
6. 중복 조사를 피하기 위해 이미 확인했거나 배제한 내용을 포함하세요.
7. 패턴 신고 — 동일한 문제가 반복적으로 발생하는 경우 개별 티켓의 우선순위가 낮더라도 패턴을 에스컬레이션하세요.
