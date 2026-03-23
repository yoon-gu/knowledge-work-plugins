---
name: customer-escalation
description: 전체 맥락을 고려하여 엔지니어링, 제품 또는 리더십에 대한 에스컬레이션을 패키지화하세요. 버그에 일반 지원 이상의 엔지니어링 주의가 필요한 경우, 여러 고객이 동일한 문제를 보고하는 경우, 고객이 이탈하겠다고 위협하는 경우, 문제가 SLA를 넘어 해결되지 않은 경우에 사용하세요.
argument-hint: "<issue summary> [customer name]"
---

# /customer-escalation

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

엔지니어링, 제품 또는 리더십에 대한 구조화된 에스컬레이션 개요에 지원 문제를 패키지화합니다. 상황을 수집하고, 재현 단계를 구성하고, 비즈니스 영향을 평가하고, 올바른 에스컬레이션 대상을 식별합니다.

## 용법

```
/customer-escalation <issue description> [customer name or account]
```

예:
- `/customer-escalation API returning 500 errors intermittently for Acme Corp`
- `/customer-escalation Data export is missing rows — 3 customers reported this week`
- `/customer-escalation SSO login loop affecting all Enterprise customers`
- `/customer-escalation Customer threatening to churn over missing audit log feature`

## 작업흐름

### 1. 문제 이해

입력을 구문 분석하고 다음을 결정합니다.

- **부족하거나 필요한 것**: 핵심 기술 또는 제품 문제
- **영향을 받는 사람**: 특정 고객, 세그먼트 또는 모든 사용자
- **얼마 동안**: 언제 시작되었나요? 고객이 얼마나 오랫동안 기다렸나요?
- **시도한 방법**: 시도한 모든 문제 해결 또는 해결 방법
- **지금 에스컬레이션해야 하는 이유**: 일반적인 지원 이상의 주의가 필요한 이유

아래 "When to Escalate vs. Handle in Support" 기준을 사용하여 영장 에스컬레이션을 확인하세요.

### 2. 맥락 수집

사용 가능한 소스에서 관련 정보를 수집합니다.

- **~~지원 플랫폼**: 관련 티켓, 커뮤니케이션 타임라인, 이전 문제 해결
- **~~CRM**(연결된 경우): 계정 세부정보, 주요 연락처, 이전 에스컬레이션
- **~~채팅**: 이 문제에 대한 내부 논의, 다른 고객의 유사한 보고서
- **~~프로젝트 트래커**(연결된 경우): 관련 버그 보고서 또는 기능 요청, 엔지니어링 상태
- **~~지식 기반**: 알려진 문제 또는 해결 방법, 관련 문서

### 3. 비즈니스 영향 평가

아래의 영향 차원을 사용하여 수량화합니다.

- **폭**: 얼마나 많은 고객/사용자가 영향을 받나요? 성장하고 있나요?
- **심도**: 막혔나요 아니면 불편했나요?
- **기간**: 이 일이 얼마나 오랫동안 지속되었나요?
- **수익**: ARR이 위험합니까? 보류 중인 거래가 영향을 받나요?
- **시간 압박**: 마감 기한이 빡빡합니까?

### 4. 에스컬레이션 대상 결정

아래 에스컬레이션 계층을 사용하여 L2 지원, 엔지니어링, 제품, 보안 또는 리더십과 같은 올바른 대상을 식별하십시오.

### 5. 구조 재현 단계(버그용)

문제가 버그인 경우 아래의 재현 단계 모범 사례에 따라 환경 세부 정보 및 증거와 함께 명확한 재현 단계를 문서화하세요.

### 6. 에스컬레이션 개요 생성

```
## ESCALATION: [One-line summary]

**Severity:** [Critical / High / Medium]
**Target team:** [Engineering / Product / Security / Leadership]
**Reported by:** [Your name/team]
**Date:** [Today's date]

### Impact
- **Customers affected:** [Who and how many]
- **Workflow impact:** [What they can't do]
- **Revenue at risk:** [If applicable]
- **Time in queue:** [How long this has been an issue]

### Issue Description
[Clear, concise description of the problem — 3-5 sentences]

### What's Been Tried
1. [Troubleshooting step and result]
2. [Troubleshooting step and result]
3. [Troubleshooting step and result]

### Reproduction Steps
[If applicable — follow the format below]
1. [Step]
2. [Step]
3. [Step]
Expected: [X]
Actual: [Y]
Environment: [Details]

### Customer Communication
- **Last update to customer:** [Date and what was communicated]
- **Customer expectation:** [What they're expecting and by when]
- **Escalation risk:** [Will they escalate further if not resolved by X?]

### What's Needed
- [Specific ask — "investigate root cause", "prioritize fix",
  "make product decision on X", "approve exception for Y"]
- **Deadline:** [When this needs resolution or an update]

### Supporting Context
- [Related tickets or links]
- [Internal discussion threads]
- [Documentation or logs]
```

### 7. 다음 단계 제안

에스컬레이션을 생성한 후:
- "Want me to post this in a ~~chat channel for the target team?"
- "Should I update the customer with an interim response?"
- "Want me to set a follow-up reminder to check on this?"
- "Should I draft a customer-facing update with the current status?"

---

## 에스컬레이션해야 하는 경우와 지원 처리 시기

### 다음과 같은 경우 지원 처리:
- 문제에 문서화된 솔루션 또는 알려진 해결 방법이 있습니다.
- 해결할 수 있는 구성 또는 설정 문제입니다.
- 고객에게 문제 해결이 아닌 지침이나 교육이 필요함
- 문제는 문서화된 대안의 알려진 제한 사항입니다.
- 이전의 유사한 티켓이 지원 수준에서 해결되었습니다.

### 에스컬레이션 시기:
- **기술**: 버그가 확인되었으며 코드 수정이 필요함, 인프라 조사 필요, 데이터 손상 또는 손실
- **복잡성**: 지원 범위를 벗어나는 문제's ability to diagnose, requires access support doesn'없음, 맞춤 구현 포함
- **영향**: 여러 고객이 영향을 받음, 생산 시스템 다운, 데이터 무결성 위험, 보안 문제
- **비즈니스**: 위험에 처한 고가치 고객, SLA 위반이 임박했거나 발생함, 고객이 경영진의 개입을 요청함
- **시간**: 문제가 SLA 이후에 공개되었으며, 고객이 비합리적으로 오랫동안 기다려 왔으며, 일반적인 지원 채널이 진행되지 않고 있습니다.
- **패턴**: 3명 이상의 고객이 보고한 동일한 문제, 수정된 것으로 추정되는 반복되는 문제, 시간이 지남에 따라 심각도가 증가함

## 에스컬레이션 계층

### L1 → L2(지원 에스컬레이션)
**발신:** 일선 지원 **수신:** 고위 지원/기술 지원 전문가 **시기:** 문제에 대한 심층적인 조사, 전문적인 제품 지식 또는 고급 문제 해결이 필요함 **포함 내용:** 티켓 요약, 이미 시도한 단계, 고객 상황

### L2 → 엔지니어링
**발신:** 고위 지원 **수신:** 엔지니어링 팀(관련 제품 영역) **시기:** 버그 확인, 인프라 문제, 코드 변경 필요, 시스템 수준 조사 필요 **포함 내용:** 전체 재현 단계, 환경 세부 정보, 로그 또는 오류 메시지, 비즈니스 영향, 고객 타임라인

### L2 → 제품
**시작:** 고위 지원 **수행:** 제품 관리 **시기:** 고객의 고통을 유발하는 기능 격차, 설계 결정 필요, 워크플로가 고객 기대와 일치하지 않음, 경쟁 고객 요구에 우선순위 지정 필요 **포함 내용:** 고객 사용 사례, 비즈니스 영향, 요청 빈도, 경쟁 압력(알려진 경우)

### 모두 → 보안
**발신:** 모든 지원 계층 **받는 사람:** 보안 팀 **시기:** 잠재적인 데이터 노출, 무단 액세스, 취약성 보고, 규정 준수 문제 **포함 내용:** 관찰된 내용, 잠재적으로 영향을 받은 대상, 즉각적인 격리 조치 수행, 긴급 평가 **참고:** 보안 에스컬레이션은 일반적인 계층 진행을 우회합니다. 레벨에 관계없이 즉시 에스컬레이션합니다.

### 모두 → 리더십
**발신:** 모든 계층(일반적으로 L2 또는 관리자) **수신:** 지원 리더십, 경영진 **시기:** 고수익 고객 위협, 중요한 계정에 대한 SLA 위반, 부서 간 결정 필요, 정책 예외 필요, PR 또는 법적 위험 **포함 내용:** 전체 비즈니스 상황, 위험에 처한 수익, 시도한 내용, 필요한 특정 결정 또는 조치, 기한

## 비즈니스 영향 평가

에스컬레이션할 때 가능한 경우 영향을 정량화합니다.

### 충격 크기

| 차원 | 대답할 질문 |
|-----------|-------------------|
| **폭** | 얼마나 많은 고객/사용자가 영향을 받습니까? 성장하고 있나요? |
| **깊이** | 얼마나 심각한 영향을 받나요? 막혔나요 vs 불편했나요? |
| **지속** | 이런 일이 얼마나 오랫동안 계속됐나요? 심각한 문제가 발생할 때까지 얼마나 걸리나요? |
| **수익** | 위험에 처한 ARR은 무엇입니까? 보류 중인 거래가 영향을 받나요? |
| **평판** | 이거 공개될 수도 있나요? 참고고객인가요? |
| **계약** | SLA가 위반되고 있나요? 계약상 의무가 있나요? |

### 심각도 약어

- **중요**: 생산 중단, 데이터 위험, 보안 침해 또는 다수의 고가치 고객이 영향을 받음. 즉각적인 주의가 필요합니다.
- **높음**: 주요 기능 손상, 주요 고객 차단, SLA 위험. 당일 주의가 필요합니다.
- **중간**: 해결 방법이 있는 심각한 문제, 중요하지만 긴급하지는 않은 비즈니스 영향. 이번 주에는 주의가 필요합니다.

## 재생산 단계 작성

좋은 재현 단계는 버그 에스컬레이션에서 가장 중요한 것입니다. 다음 관행을 따르십시오.

1. **깨끗한 상태에서 시작**: 시작점 설명(계정 유형, 구성, 권한)
2. **구체적으로 설명하세요**: "try to export"이 아닌 "Click the Export button in the top-right of the Dashboard page"
3. **정확한 값 포함**: "enter some data"이 아닌 특정 입력, 날짜, ID를 사용하세요.
4. **환경 참고**: 브라우저, OS, 계정 유형, 기능 플래그, 계획 수준
5. **빈도 포착**: 항상 재현 가능합니까? 간헐적으로? 특정 조건에서만?
6. **증거 포함**: 스크린샷, 오류 메시지(정확한 텍스트), 네트워크 로그, 콘솔 출력
7. **제외한 사항에 유의하세요**: "Tested in Chrome and Firefox — same behavior" "Not account-specific — reproduced on test account"

## 에스컬레이션 후 후속 조치 주기

확대하고 잊지 마십시오. 고객 관계에 대한 소유권을 유지합니다.

| 심각성 | 내부 후속 조치 | 고객 업데이트 |
|----------|-------------------|-----------------|
| **비판적인** | 2시간마다 | 2~4시간마다(또는 SLA에 따라) |
| **높은** | 4시간마다 | 4~8시간마다 |
| **중간** | 일일 | 영업일 기준 1~2일마다 |

### 후속 조치
- 진행 상황은 수신 팀에 문의하세요.
- 아직 조사 중이더라도's no new information ("We'고객에게 업데이트하세요. 지금까지 우리가 알고 있는 정보는 다음과 같습니다.")
- 상황이 바뀌면(좋든 나쁘든) 심각도를 조정하세요.
- 감사 추적을 위해 티켓의 모든 업데이트를 문서화하세요.
- 해결 시 루프 종료: 고객에게 확인, 내부 추적 업데이트, 학습 내용 캡처

## 단계적 축소

모든 에스컬레이션이 에스컬레이션된 상태로 유지되는 것은 아닙니다. 다음과 같은 경우 에스컬레이션을 축소하세요.
- 근본 원인을 찾았으며 지원을 통해 해결할 수 있는 문제입니다.
- 고객 차단을 해제하는 해결 방법이 발견되었습니다.
- 문제는 저절로 해결됩니다(그러나 여전히 근본 원인을 문서화함).
- 새로운 정보로 인해 심각도 평가가 변경됩니다.

단계적 축소 시:
- 에스컬레이션한 팀에 알림
- 해결 방법으로 티켓을 업데이트하세요.
- 고객에게 해결 방법을 알립니다.
- 나중에 참고할 수 있도록 학습한 내용을 문서화하세요.

## 에스컬레이션 모범 사례

1. 항상 영향을 정량화하세요. 모호한 에스컬레이션은 우선순위가 낮습니다.
2. 버그 재현 단계를 포함합니다. 이것이 엔지니어링에 가장 필요한 것입니다.
3. 필요한 것이 무엇인지 명확히 하세요. "investigate", "fix", "decide"는 서로 다른 질문입니다.
4. 마감일 설정 및 전달 - 마감일이 없는 긴급성은 모호합니다.
5. 기술 문제를 에스컬레이션한 후에도 고객 관계에 대한 소유권을 유지합니다.
6. 적극적으로 후속 조치를 취하십시오. 수신 팀이 귀하에게 올 때까지 기다리지 마십시오.
7. 모든 것을 문서화합니다. 에스컬레이션 추적은 패턴 감지 및 프로세스 개선에 유용합니다.
