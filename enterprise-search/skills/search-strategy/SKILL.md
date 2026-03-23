---
name: search-strategy
description: Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.
user-invocable: false
---

# Search Strategy

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

엔터프라이즈 검색의 핵심 인텔리전스입니다. 단일 자연어 질문을 소스별 병렬 검색으로 변환하고, 순위가 매겨진 중복 제거 결과를 생성합니다.

## 목표

다음을:
```
"API 마이그레이션 일정에 대해 어떤 결정을 내렸나요?"
```

연결된 모든 소스에 걸친 타겟 검색으로 변환합니다:
```
~~chat:  "API migration timeline decision" (semantic) + "API migration" in:#engineering after:2025-01-01
~~knowledge base: semantic search "API migration timeline decision"
~~project tracker:  text search "API migration" in relevant workspace
```

그런 다음 결과를 하나의 일관된 답변으로 종합합니다.

## 쿼리 분해

### Step 1: 쿼리 유형 파악

검색 전략을 결정하기 위해 사용자의 질문을 분류합니다:

| 쿼리 유형 | 예시 | 전략 |
|-----------|---------|----------|
| **결정** | "X에 대해 어떤 결정을 내렸나요?" | 대화(~~chat, 이메일)를 우선시하고, 결론 신호 탐색 |
| **상태** | "프로젝트 Y의 현재 상태는?" | 최근 활동, 태스크 트래커, 상태 업데이트 우선시 |
| **문서** | "Z의 사양서는 어디 있나요?" | Drive, 위키, 공유 문서 우선시 |
| **사람** | "X를 담당하는 사람이 누구인가요?" | 태스크 배정, 메시지 작성자, 문서 협업자 검색 |
| **사실** | "X에 대한 정책은?" | 위키, 공식 문서를 우선시하고, 확인용 대화 참조 |
| **시간** | "X는 언제 일어났나요?" | 넓은 날짜 범위로 검색, 타임스탬프 탐색 |
| **탐색** | "X에 대해 무엇을 알고 있나요?" | 모든 소스에서 광범위하게 검색하고 종합 |

### Step 2: 검색 구성 요소 추출

쿼리에서 다음을 추출합니다:

- **키워드**: 결과에 반드시 포함되어야 하는 핵심 용어
- **엔티티**: 사람, 프로젝트, 팀, 도구 (사용 가능한 경우 메모리 시스템 활용)
- **의도 신호**: 결정 단어, 상태 단어, 시간적 마커
- **제약 조건**: 시간 범위, 소스 힌트, 작성자 필터
- **부정**: 제외할 항목

### Step 3: 소스별 하위 쿼리 생성

사용 가능한 각 소스에 대해 하나 이상의 타겟 쿼리를 생성합니다:

**시맨틱 검색 선호** 상황:
- 개념적 질문 ("...에 대해 어떻게 생각하나요?")
- 정확한 키워드를 모르는 질문
- 탐색적 쿼리

**키워드 검색 선호** 상황:
- 알려진 용어, 프로젝트 이름, 약어
- 사용자가 인용한 정확한 구문
- 필터가 많은 쿼리 (from:, in:, after:)

**주제가 다른 이름으로 불릴 수 있는 경우 여러 쿼리 변형 생성:**
```
User: "Kubernetes setup"
Queries: "Kubernetes", "k8s", "cluster", "container orchestration"
```

## 소스별 쿼리 변환

### ~~chat

**시맨틱 검색** (자연어 질문):
```
query: "What is the status of project aurora?"
```

**키워드 검색:**
```
query: "project aurora status update"
query: "aurora in:#engineering after:2025-01-15"
query: "from:<@UserID> aurora"
```

**필터 매핑:**
| 엔터프라이즈 필터 | ~~chat 구문 |
|------------------|--------------|
| `from:sarah` | `from:sarah` or `from:<@USERID>` |
| `in:engineering` | `in:engineering` |
| `after:2025-01-01` | `after:2025-01-01` |
| `before:2025-02-01` | `before:2025-02-01` |
| `type:thread` | `is:thread` |
| `type:file` | `has:file` |

### ~~knowledge base (Wiki)

**시맨틱 검색** — 개념적 쿼리에 사용:
```
descriptive_query: "API migration timeline and decision rationale"
```

**키워드 검색** — 정확한 용어에 사용:
```
query: "API migration"
query: "\"API migration timeline\""  (exact phrase)
```

### ~~project tracker

**태스크 검색:**
```
text: "API migration"
workspace: [workspace_id]
completed: false  (상태 쿼리의 경우)
assignee_any: "me"  ("내 태스크" 쿼리의 경우)
```

**필터 매핑:**
| 엔터프라이즈 필터 | ~~project tracker 파라미터 |
|------------------|----------------|
| `from:sarah` | `assignee_any` or `created_by_any` |
| `after:2025-01-01` | `modified_on_after: "2025-01-01"` |
| `type:milestone` | `resource_subtype: "milestone"` |

## 결과 순위 지정

### 관련성 점수 산정

쿼리 유형에 따라 가중치를 부여하여 각 결과를 다음 요소로 점수화합니다:

| 요소 | 가중치 (결정) | 가중치 (상태) | 가중치 (문서) | 가중치 (사실) |
|--------|-------------------|------------------|--------------------|-------------------|
| 키워드 일치 | 0.3 | 0.2 | 0.4 | 0.3 |
| 최신성 | 0.3 | 0.4 | 0.2 | 0.1 |
| 권위도 | 0.2 | 0.1 | 0.3 | 0.4 |
| 완전성 | 0.2 | 0.3 | 0.1 | 0.2 |

### 권위 계층

쿼리 유형에 따라 달라집니다:

**사실/정책 질문의 경우:**
```
Wiki/Official docs > Shared documents > Email announcements > Chat messages
```

**"무슨 일이 있었나" / 결정 질문의 경우:**
```
Meeting notes > Thread conclusions > Email confirmations > Chat messages
```

**상태 질문의 경우:**
```
Task tracker > Recent chat > Status docs > Email updates
```

## 모호성 처리

쿼리가 모호할 때는 추측하기보다 한 가지 집중된 명확화 질문을 선호합니다:

```
모호한 쿼리: "마이그레이션 검색"
→ "몇 가지 마이그레이션 관련 항목을 찾았습니다. 다음 중 무엇을 찾고 계신가요:
   1. 데이터베이스 마이그레이션 (Project Phoenix)
   2. 클라우드 마이그레이션 (AWS → GCP)
   3. 이메일 마이그레이션 (Exchange → O365)"
```

명확화 질문은 다음 경우에만 요청합니다:
- 매우 다른 결과를 생성하는 명확히 구분되는 해석이 있는 경우
- 모호성이 검색할 소스에 크게 영향을 미치는 경우

다음 경우에는 명확화를 요청하지 않습니다:
- 쿼리가 유용한 결과를 생성하기에 충분히 명확한 경우
- 여러 해석의 결과를 반환함으로써 사소한 모호성을 해결할 수 있는 경우

## 폴백 전략

소스를 사용할 수 없거나 결과가 없을 때:

1. **소스 사용 불가**: 건너뛰고, 나머지 소스 검색 후 누락된 부분을 기록
2. **소스에서 결과 없음**: 더 넓은 쿼리 용어 시도, 날짜 필터 제거, 대체 키워드 시도
3. **모든 소스에서 결과 없음**: 사용자에게 쿼리 수정 제안
4. **속도 제한**: 제한 사항을 기록하고, 다른 소스에서 결과 반환 후 나중에 재시도 제안

### 쿼리 확장

초기 쿼리 결과가 너무 적을 경우:
```
원래: "PostgreSQL migration Q2 timeline decision"
확장:  "PostgreSQL migration"
더 확장:  "database migration"
최대 확장: "migration"
```

다음 순서로 제약을 제거합니다:
1. 날짜 필터 (전체 기간 검색)
2. 소스/위치 필터
3. 덜 중요한 키워드
4. 핵심 엔티티/주제 용어만 유지

## 병렬 실행

항상 소스 간 검색을 순차적이 아닌 병렬로 실행합니다. 총 검색 시간은 모든 소스의 합산이 아닌 가장 느린 단일 소스와 거의 같아야 합니다.

```
[사용자 쿼리]
     ↓ 분해
[~~chat query] [~~email query] [~~cloud storage query] [Wiki query] [~~project tracker query]
     ↓            ↓            ↓              ↓            ↓
  (병렬 실행)
     ↓
[병합 + 순위 지정 + 중복 제거]
     ↓
[종합된 답변]
```
