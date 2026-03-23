---
name: search-strategy
description: 쿼리 분해와 다중 소스 검색 오케스트레이션을 담당합니다. 자연어 질문을 소스별 타깃 검색으로 나누고, 쿼리를 소스별 문법으로 번역하고, 관련도 순으로 결과를 정렬하고, 모호성과 대체 전략을 처리합니다.
user-invocable: false
---

# 검색 전략

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

엔터프라이즈 검색 뒤의 핵심 지능입니다. 하나의 자연어 질문을 병렬의 소스별 검색으로 바꾸고, 순위가 매겨진 중복 제거 결과를 만듭니다.

## 목표

이렇게:
```text
"What did we decide about the API migration timeline?"
```

연결된 각 소스에 대한 타깃 검색으로 바꿉니다:
```text
~~chat:  "API migration timeline decision" (semantic) + "API migration" in:#engineering after:2025-01-01
~~knowledge base: semantic search "API migration timeline decision"
~~project tracker:  text search "API migration" in relevant workspace
```

그런 다음 결과를 하나의 일관된 답변으로 종합합니다.

## 쿼리 분해

### 1단계: 쿼리 유형 식별

사용자 질문을 분류해 검색 전략을 정합니다:

| Query Type | Example | Strategy |
|-----------|---------|----------|
| **Decision** | "What did we decide about X?" | 대화(~~chat, email)를 우선하고, 결론 신호를 찾기 |
| **Status** | "What's the status of Project Y?" | 최근 활동, 작업 추적기, 상태 업데이트 우선 |
| **Document** | "Where's the spec for Z?" | Drive, 위키, 공유 문서 우선 |
| **Person** | "Who's working on X?" | 작업 할당, 메시지 작성자, 문서 협업자 검색 |
| **Factual** | "What's our policy on X?" | 위키, 공식 문서, 그다음 확인용 대화 우선 |
| **Temporal** | "When did X happen?" | 넓은 날짜 범위로 검색하고 타임스탬프 찾기 |
| **Exploratory** | "What do we know about X?" | 모든 소스를 넓게 검색하고 종합 |

### 2단계: 검색 구성요소 추출

질문에서 다음을 추출합니다:

- **키워드**: 결과에 반드시 들어가야 하는 핵심 용어
- **엔터티**: 사람, 프로젝트, 팀, 도구(가능하면 메모리 시스템 사용)
- **의도 신호**: 결정 단어, 상태 단어, 시간 표현
- **제약**: 시간 범위, 소스 힌트, 작성자 필터
- **부정**: 제외할 것

### 3단계: 소스별 하위 쿼리 생성

사용 가능한 각 소스에 대해 한 개 이상 타깃 쿼리를 만듭니다:

**의미 검색을 선호하는 경우:**
- 개념적 질문("What do we think about...")
- 정확한 키워드를 모를 때
- 탐색적 질의

**키워드 검색을 선호하는 경우:**
- 이미 아는 용어, 프로젝트 이름, 약어
- 사용자가 인용한 정확한 문구
- 필터 중심 쿼리(from:, in:, after:)

**여러 쿼리 변형을 생성하는 경우:**
```text
User: "Kubernetes setup"
Queries: "Kubernetes", "k8s", "cluster", "container orchestration"
```

## 소스별 쿼리 변환

### ~~chat

**의미 검색**(자연어 질문):
```text
query: "What is the status of project aurora?"
```

**키워드 검색:**
```text
query: "project aurora status update"
query: "aurora in:#engineering after:2025-01-15"
query: "from:<@UserID> aurora"
```

**필터 매핑:**
| Enterprise filter | ~~chat syntax |
|------------------|--------------|
| `from:sarah` | `from:sarah` or `from:<@USERID>` |
| `in:engineering` | `in:engineering` |
| `after:2025-01-01` | `after:2025-01-01` |
| `before:2025-02-01` | `before:2025-02-01` |
| `type:thread` | `is:thread` |
| `type:file` | `has:file` |

### ~~knowledge base (Wiki)

**의미 검색** - 개념적 질문에 사용:
```text
descriptive_query: "API migration timeline and decision rationale"
```

**키워드 검색** - 정확한 용어에 사용:
```text
query: "API migration"
query: "\"API migration timeline\""  (exact phrase)
```

### ~~project tracker

**작업 검색:**
```text
text: "API migration"
workspace: [workspace_id]
completed: false  (for status queries)
assignee_any: "me"  (for "my tasks" queries)
```

**필터 매핑:**
| Enterprise filter | ~~project tracker parameter |
|------------------|----------------|
| `from:sarah` | `assignee_any` or `created_by_any` |
| `after:2025-01-01` | `modified_on_after: "2025-01-01"` |
| `type:milestone` | `resource_subtype: "milestone"` |

## 결과 순위화

### 관련도 점수

쿼리 유형에 따라 다음 요소를 가중해 각 결과를 점수화합니다:

| Factor | Weight (Decision) | Weight (Status) | Weight (Document) | Weight (Factual) |
|--------|-------------------|------------------|--------------------|-------------------|
| Keyword match | 0.3 | 0.2 | 0.4 | 0.3 |
| Freshness | 0.3 | 0.4 | 0.2 | 0.1 |
| Authority | 0.2 | 0.1 | 0.3 | 0.4 |
| Completeness | 0.2 | 0.3 | 0.1 | 0.2 |

### 권위 계층

질문 유형에 따라 다릅니다:

**사실/정책 질문의 경우:**
```text
Wiki/Official docs > Shared documents > Email announcements > Chat messages
```

**"무슨 일이 있었나" / 결정 질문의 경우:**
```text
Meeting notes > Thread conclusions > Email confirmations > Chat messages
```

**상태 질문의 경우:**
```text
Task tracker > Recent chat > Status docs > Email updates
```

## 모호성 처리

쿼리가 모호하다면, 추측하기보다 한 번에 하나의 초점이 있는 확인 질문을 던집니다:

```text
Ambiguous: "search for the migration"
→ "I found references to a few migrations. Are you looking for:
   1. The database migration (Project Phoenix)
   2. The cloud migration (AWS → GCP)
   3. The email migration (Exchange → O365)"
```

다음 경우에만 확인 질문을 합니다:
- 매우 다른 결과를 낳는 정말로 다른 해석이 있을 때
- 모호성이 어떤 소스를 검색할지에 크게 영향을 줄 때

다음 경우에는 묻지 않습니다:
- 유용한 결과를 낼 만큼 질문이 충분히 명확할 때
- 약간의 모호성은 여러 해석의 결과를 돌려주면 해결될 때

## 대체 전략

소스가 없거나 결과가 없을 때:

1. **소스를 사용할 수 없음**: 건너뛰고 나머지를 검색하며, 누락을 알려 줍니다
2. **소스에서 결과 없음**: 더 넓은 용어로 다시 시도하고, 날짜 필터를 제거하고, 대체 키워드를 사용합니다
3. **모든 소스에서 결과 없음**: 사용자에게 쿼리 수정을 제안합니다
4. **속도 제한**: 제한을 알리고 다른 소스의 결과를 반환하며, 나중에 다시 시도하라고 안내합니다

### 쿼리 확장

초기 쿼리가 너무 적은 결과를 반환하면:
```text
Original: "PostgreSQL migration Q2 timeline decision"
Broader:  "PostgreSQL migration"
Broader:  "database migration"
Broadest: "migration"
```

제약은 다음 순서로 제거합니다:
1. 날짜 필터(전체 기간 검색)
2. 소스/위치 필터
3. 덜 중요한 키워드
4. 핵심 엔터티/토픽만 유지

## 병렬 실행

항상 소스 전반에서 검색을 병렬로 실행하고, 순차적으로 하지 않습니다. 총 검색 시간은 모든 소스의 합이 아니라 가장 느린 단일 소스 정도가 되어야 합니다.

```text
[User query]
     ↓ decompose
[~~chat query] [~~email query] [~~cloud storage query] [Wiki query] [~~project tracker query]
     ↓            ↓            ↓              ↓            ↓
  (parallel execution)
     ↓
[Merge + Rank + Deduplicate]
     ↓
```
