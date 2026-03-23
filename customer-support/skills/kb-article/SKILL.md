---
name: kb-article
description: 해결된 문제나 일반적인 질문을 바탕으로 기술 자료 문서 초안을 작성합니다. 셀프 서비스를 위해 티켓 해결을 문서화할 가치가 있거나, 동일한 질문이 계속 나오거나, 해결 방법을 게시해야 하거나, 알려진 문제를 고객에게 전달해야 하는 경우에 사용하세요.
argument-hint: "<resolved issue or ticket>"
---

# /kb-article

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

해결된 지원 문제, 일반적인 질문 또는 문서화된 해결 방법을 바탕으로 즉시 게시 가능한 기술 자료 문서의 초안을 작성하세요. 검색 가능성과 셀프 서비스를 위해 콘텐츠를 구성합니다.

## 용법

```
/kb-article <resolved issue, ticket reference, or topic description>
```

예:
- `/kb-article How to configure SSO with Okta — resolved this for 3 customers last month`
- `/kb-article Ticket #4521 — customer couldn't export data over 10k rows`
- `/kb-article Common question: how to set up webhook notifications`
- `/kb-article Known issue: dashboard charts not loading on Safari 16`

## 작업흐름

### 1. 원본 자료 이해

입력을 구문 분석하여 다음을 식별합니다.

- **문제가 무엇이었습니까?** 원래 문제, 질문 또는 오류
- **해결책은 무엇이었습니까?** 해결 방법, 해결 방법 또는 답변
- **이것은 누구에게 영향을 미치나요?** 사용자 유형, 계획 수준 또는 구성
- **이 현상은 얼마나 흔한가요?** 일회성 또는 반복되는 문제
- **가장 적합한 문서 유형은 무엇입니까?** 방법, 문제 해결, FAQ, 알려진 문제 또는 참조(아래 문서 유형 참조)

티켓 참조가 제공되면 전체 컨텍스트를 찾아보세요.

- ****지원 플랫폼**: 티켓 스레드, 해결 방법, 내부 메모 가져오기
- **~~지식 기반**: 유사한 기사가 이미 존재하는지 확인합니다(업데이트 및 새로 만들기).
- **~~프로젝트 트래커**: 관련 버그나 기능 요청이 있는지 확인하세요.

### 2. 기사 초안 작성

아래의 기사 구조, 형식 지정 표준 및 검색 가능성 모범 사례를 사용하세요.

- 선택한 기사 유형(방법, 문제 해결, FAQ, 알려진 문제 또는 참조)에 대한 템플릿을 따릅니다.
- 검색 가능성 모범 사례 적용: 고객 언어 제목, 일반 언어 시작 문장, 정확한 오류 메시지, 공통 동의어
- 스캔 가능하게 유지: 헤더, 번호가 매겨진 단계, 짧은 단락

### 3. 기사 생성

메타데이터와 함께 초안을 제시합니다.

```
## KB Article Draft

**Title:** [Article title]
**Type:** [How-to / Troubleshooting / FAQ / Known Issue / Reference]
**Category:** [Product area or topic]
**Tags:** [Searchable tags]
**Audience:** [All users / Admins / Developers / Specific plan]

---

[Full article content — using the appropriate template below]

---

### Publishing Notes
- **Source:** [Ticket #, customer conversation, or internal discussion]
- **Existing articles to update:** [If this overlaps with existing content]
- **Review needed from:** [SME or team if technical accuracy needs verification]
- **Suggested review date:** [When to revisit for accuracy]
```

### 4. 다음 단계 제안

기사를 생성한 후:
- "Want me to check if a similar article already exists in your ~~knowledge base?"
- "Should I adjust the technical depth for a different audience?"
- "Want me to draft a companion article (e.g., a how-to to go with this troubleshooting guide)?"
- "Should I create an internal-only version with additional technical detail?"

---

## 기사 구조 및 형식 표준

### 범용 기사 요소

모든 KB 문서에는 다음이 포함되어야 합니다.

1. **제목**: 명확하고 검색 가능하며 결과 또는 문제를 설명합니다(내부 전문 용어 아님).
2. **개요**: 이 기사에서 다루는 내용과 대상을 설명하는 1~2개의 문장
3. **본문**: 기사 유형에 적합한 구조화된 콘텐츠
4. **관련 기사**: 관련 컴패니언 콘텐츠 링크
5. **메타데이터**: 카테고리, 태그, 잠재고객, 마지막 업데이트 날짜

### 서식 규칙

- **헤더(H2, H3)를 사용**하여 콘텐츠를 스캔 가능한 섹션으로 나눕니다.
- **순차적인 단계에는 번호가 매겨진 목록 사용**
- 비순차적 항목에는 **글머리 기호 목록 사용**
- UI 요소 이름, 주요 용어 및 강조점에는 **굵게 표시**를 사용하세요.
- 명령, API 호출, 오류 메시지 및 구성 값에 **코드 블록 사용**
- 비교, 옵션 또는 참조 데이터를 보려면 **표를 사용**하세요.
- **콜아웃/메모**를 사용하여 경고, 팁, 중요한 주의 사항을 확인하세요.
- **문단을 짧게 유지하세요** — 최대 2~4문장
- **섹션당 하나의 아이디어** — 섹션이 두 가지 주제를 다루는 경우 분할하세요.

## 검색 가능성을 위한 글쓰기

고객이 기사를 찾을 수 없으면 기사는 쓸모가 없습니다. 검색을 위해 모든 기사를 최적화합니다.

### 제목 모범 사례

| 좋은 제목 | 잘못된 제목 | 왜 |
|------------|-----------|-----|
| "How to configure SSO with Okta" | "SSO Setup" | 구체적이며 고객이 검색하는 도구 이름이 포함됩니다. |
| "Fix: Dashboard shows blank page" | "Dashboard Issue" | 고객이 경험하는 증상을 포함합니다. |
| "API rate limits and quotas" | "API Information" | 고객이 검색하는 특정 용어를 포함합니다. |
| "Error: 'Connection refused' when importing data" | "Import Problems" | 정확한 오류 메시지를 포함합니다. |

### 키워드 최적화

- **정확한 오류 메시지 포함** - 고객이 오류 텍스트를 복사하여 검색에 붙여넣습니다.
- **내부 용어가 아닌 고객 언어를 사용** — "authentication failure"이 아닌 "can't log in"
- **공통 동의어 포함** — "delete/remove", "dashboard/home page", "export/download"
- **대체 문구 추가** - 개요의 다른 각도에서 동일한 문제를 해결합니다.
- **제품 영역으로 태그 지정** - 카테고리와 태그가 고객이 제품에 대해 생각하는 방식과 일치하는지 확인하세요.

### 여는 문장 공식

문제나 작업을 일반 언어로 다시 설명하는 문장으로 모든 기사를 시작하세요.

- **방법**: "This guide shows you how to [accomplish X]."
- **문제 해결**: "If you're seeing [symptom], this article explains how to fix it."
- **FAQ**: "[Question in the customer's words]? Here's the answer."
- **알려진 문제**: "Some users are experiencing [symptom]. Here's what we know and how to work around it."

## 기사 유형 템플릿

### 방법 기사

**목적**: 작업 수행을 위한 단계별 지침입니다.

**구조**:
```
# How to [accomplish task]

[Overview — what this guide covers and when you'd use it]

## Prerequisites
- [What's needed before starting]

## Steps
### 1. [Action]
[Instruction with specific details]

### 2. [Action]
[Instruction]

## Verify It Worked
[How to confirm success]

## Common Issues
- [Issue]: [Fix]

## Related Articles
- [Links]
```

**모범 사례**:
- 각 단계를 동사로 시작하세요
- 특정 경로 포함: "Go to Settings > Integrations > API Keys"
- 각 단계 후에 사용자가 봐야 할 내용을 언급하세요("You should see a green confirmation banner").
- 단계를 직접 테스트하거나 최근 티켓 해결을 통해 확인하세요.

### 문제 해결 기사

**목적**: 특정 문제를 진단하고 해결합니다.

**구조**:
```
# [Problem description — what the user sees]

## Symptoms
- [What the user observes]

## Cause
[Why this happens — brief, non-jargon explanation]

## Solution
### Option 1: [Primary fix]
[Steps]

### Option 2: [Alternative if Option 1 doesn't work]
[Steps]

## Prevention
[How to avoid this in the future]

## Still Having Issues?
[How to get help]
```

**모범 사례**:
- 원인이 아닌 증상을 먼저 살펴보세요. 고객은 눈에 보이는 것을 검색합니다.
- 가능하면 여러 가지 솔루션을 제공하세요(대부분 먼저 해결)
- 지원을 가리키는 "Still having issues?" 섹션을 포함하세요.
- 근본 원인이 복잡한 경우 고객에게 설명하는 내용을 단순하게 유지하세요.

### FAQ 기사

**목적**: 일반적인 질문에 대한 빠른 답변입니다.

**구조**:
```
# [Question — in the customer's words]

[Direct answer — 1-3 sentences]

## Details
[Additional context, nuance, or explanation if needed]

## Related Questions
- [Link to related FAQ]
- [Link to related FAQ]
```

**모범 사례**:
- 첫 번째 문장의 질문에 대답하세요.
- 간결하게 유지하세요. 답변에 연습이 필요한 경우 FAQ가 아닌 방법을 설명하는 것입니다.
- 그룹 관련 FAQ 및 FAQ 간의 링크

### 알려진 문제 기사

**목적**: 해결 방법과 함께 알려진 버그나 제한 사항을 문서화합니다.

**구조**:
```
# [Known Issue]: [Brief description]

**Status:** [Investigating / Workaround Available / Fix In Progress / Resolved]
**Affected:** [Who/what is affected]
**Last updated:** [Date]

## Symptoms
[What users experience]

## Workaround
[Steps to work around the issue, or "No workaround available"]

## Fix Timeline
[Expected fix date or current status]

## Updates
- [Date]: [Update]
```

**모범 사례**:
- 상태를 최신 상태로 유지하세요. 오래된 알려진 문제 기사보다 더 빠르게 신뢰를 약화시키는 것은 없습니다.
- 수정 사항이 배송되면 문서를 업데이트하고 해결된 것으로 표시하세요.
- 해결된 경우 고객이 여전히 이전 증상을 검색할 수 있도록 30일 동안 기사를 게시하세요.

## 검토 및 유지 관리 주기

유지 관리가 없으면 지식 기반이 손상됩니다. 다음 일정을 따르세요.

| 활동 | 빈도 | WHO |
|----------|-----------|-----|
| **신규 기사 리뷰** | 출판하기 전에 | 기술 콘텐츠에 대한 동료 검토 + SME |
| **정확성 감사** | 계간지 | 지원팀은 트래픽이 가장 많은 기사를 검토합니다. |
| **오래된 콘텐츠 확인** | 월간 간행물 | 6개월 이상 업데이트되지 않은 기사 신고 |
| **알려진 문제 업데이트** | 주간 | 알려진 모든 문제에 대한 상태 업데이트 |
| **분석 검토** | 월간 간행물 | 유용성 평점이 낮거나 반송률이 높은 기사를 확인하세요. |
| **갭 분석** | 계간지 | KB 기사 없이 주요 티켓 주제 식별 |

### 기사 수명주기

1. **초안**: 작성, 검토 필요
2. **게시됨**: 실시간으로 고객에게 제공됩니다.
3. **업데이트 필요**: 개정 플래그가 지정됨(제품 변경, 피드백 또는 연식)
4. **보관됨**: 더 이상 관련이 없지만 참조용으로 보존됩니다.
5. **폐기**: 기술 자료에서 제거되었습니다.

### 업데이트 시기와 새로 작성 시기

**기존 업데이트**:
- 제품이 변경되었으며 단계를 새로 고쳐야 합니다.
- 기사는 대부분 맞지만 세부정보가 누락되었습니다.
- 피드백을 통해 고객이 특정 섹션에 대해 혼란스러워하고 있음을 나타냅니다.
- 더 나은 해결 방법이나 솔루션을 찾았습니다.

**새로 만들기** 다음과 같은 경우:
- 새로운 기능이나 제품 영역에는 문서가 필요합니다.
- 해결된 티켓에는 공백이 드러납니다. 이 주제에 대한 기사가 없습니다.
- 기존 문서가 너무 많은 주제를 다루므로 분할해야 합니다.
- 서로 다른 청중은 동일한 정보를 다르게 설명해야 합니다.

## 연결 및 분류 분류

### 카테고리 구조

고객이 생각하는 방식과 일치하는 계층 구조로 기사를 구성합니다.

```
Getting Started
├── Account setup
├── First-time configuration
└── Quick start guides

Features & How-tos
├── [Feature area 1]
├── [Feature area 2]
└── [Feature area 3]

Integrations
├── [Integration 1]
├── [Integration 2]
└── API reference

Troubleshooting
├── Common errors
├── Performance issues
└── Known issues

Billing & Account
├── Plans and pricing
├── Billing questions
└── Account management
```

### 모범 사례 연결

- **문제 해결에서 방법까지의 링크**: "For setup instructions, see [How to configure X]"
- **방법 및 문제 해결 링크**: "If you encounter errors, see [Troubleshooting X]"
- **FAQ에서 자세한 기사 링크**: "For a full walkthrough, see [Guide to X]"
- **알려진 문제에서 해결 방법으로 연결**: 문제에서 해결 방법으로의 연결을 짧게 유지합니다.
- KB 내에서 **상대 링크 사용** - 절대 URL보다 재구성이 더 잘 유지됩니다.
- **순환 링크를 피하세요** — A가 B에 연결되면 B는 둘 다 실제로 유용한 진입점이 아닌 이상 A에 다시 연결되어서는 안 됩니다.

## KB 작성 모범 사례

1. 좌절감을 느끼고 답을 찾고 있는 고객을 위해 명확하고 직접적이며 도움이 되는 내용을 작성하십시오.
2. 모든 기사는 고객이 입력하는 단어를 사용한 검색을 통해 찾을 수 있어야 합니다.
3. 기사를 테스트하세요. 직접 단계를 따르거나 주제에 익숙하지 않은 사람이 따라하도록 하세요.
4. 기사의 초점을 유지하세요. 하나의 문제, 하나의 솔루션입니다. 기사가 너무 길어지는 경우 분할
5. 적극적으로 유지하십시오. 잘못된 기사는 기사가 없는 것보다 더 나쁩니다.
6. 누락된 내용 추적 - KB 기사일 수도 있었던 모든 티켓은 콘텐츠 공백입니다.
7. 영향 측정 - 티켓을 줄이지 않는 기사는 개선되거나 폐기되어야 합니다.
