---
name: knowledge-synthesis
description: 여러 소스의 검색 결과를 출처가 표시된 일관되고 중복이 제거된 답변으로 결합합니다. 최신성과 권위에 기반한 신뢰도 점수를 다루고, 큰 결과 집합을 효과적으로 요약합니다.
user-invocable: false
---

# 지식 종합

엔터프라이즈 검색의 마지막 단계입니다. 여러 소스의 원시 결과를 받아 신뢰할 수 있고 일관된 답변으로 만듭니다.

## 목표

이렇게 된 결과를:
```
~~chat result: "Sarah said in #eng: 'let's go with REST, GraphQL is overkill for our use case'"
~~email result: "Subject: API Decision — Sarah's email confirming REST approach with rationale"
~~cloud storage result: "API Design Doc v3 — updated section 2 to reflect REST decision"
~~project tracker result: "Task: Finalize API approach — marked complete by Sarah"
```

이렇게 바꿉니다:
```
The team decided to go with REST over GraphQL for the API redesign. Sarah made the
call, noting that GraphQL was overkill for the current use case. This was discussed
in #engineering on Tuesday, confirmed via email Wednesday, and the design doc has
been updated to reflect the decision. The related ~~project tracker task is marked complete.

Sources:
- ~~chat: #engineering thread (Jan 14)
- ~~email: "API Decision" from Sarah (Jan 15)
- ~~cloud storage: "API Design Doc v3" (updated Jan 15)
- ~~project tracker: "Finalize API approach" (completed Jan 15)
```

## 중복 제거

### 소스 간 중복 제거

같은 정보가 여러 곳에 나타나는 경우가 많습니다. 중복을 식별하고 합치세요:

**같은 결과라고 볼 수 있는 신호:**
- 내용이 같거나 매우 비슷함
- 같은 작성자/발신자
- 타임스탬프가 짧은 간격(같은 날 또는 인접한 날)
- 같은 엔터티를 참조(프로젝트 이름, 문서, 결정)
- 한 소스가 다른 소스를 참조("as discussed in ~~chat", "per the email", "see the doc")

**합치는 방법:**
- 하나의 서술 항목으로 결합
- 나타난 모든 소스를 인용
- 가장 완전한 버전을 주 텍스트로 사용
- 각 소스의 고유한 세부 사항을 추가

### 중복 제거 우선순위

같은 정보가 여러 소스에 있다면 다음을 우선하세요:
```
1. 가장 완전한 버전(맥락이 가장 풍부한 것)
2. 가장 권위 있는 소스(공식 문서 > chat)
3. 가장 최근 버전(변하는 정보는 최신 값)
```

### 중복 제거하면 안 되는 경우

다음은 별도 항목으로 유지하세요:
- 같은 주제지만 결론이 다른 경우
- 서로 다른 사람이 서로 다른 관점을 표현한 경우
- 정보가 의미 있게 진화한 경우(v1 vs v2의 결정)
- 서로 다른 시간대가 표현된 경우

## 출처 인용과 표기

종합된 답변의 모든 주장은 출처에 연결되어야 합니다.

### 표기 형식

직접 참조는 인라인으로:
```
Sarah confirmed the REST approach in her email on Wednesday.
The design doc was updated to reflect this (~~cloud storage: "API Design Doc v3").
```

완전성을 위한 출처 목록:
```
Sources:
- ~~chat: #engineering discussion (Jan 14) — initial decision thread
- ~~email: "API Decision" from Sarah Chen (Jan 15) — formal confirmation
- ~~cloud storage: "API Design Doc v3" last modified Jan 15 — updated specification
```

### 인용 규칙

- 항상 소스 유형을 명시합니다(`~~chat`, `~~email`, `~~cloud storage` 등)
- 구체적인 위치를 포함합니다(채널, 폴더, 스레드)
- 날짜나 상대 시간을 포함합니다
- 관련이 있으면 작성자를 포함합니다
- 가능하면 문서/스레드 제목을 포함합니다
- ~~chat에는 채널 이름을 적습니다
- ~~email에는 제목과 발신자를 적습니다
- ~~cloud storage에는 문서 제목을 적습니다

## 신뢰도 수준

모든 결과가 같은 신뢰도를 가지지는 않습니다. 최신성과 권위를 기준으로 평가하세요:

### 최신성

| Recency | Confidence impact |
|---------|------------------|
| 오늘 / 어제 | 현재 상태에 대한 신뢰도 높음 |
| 이번 주 | 좋은 신뢰도 |
| 이번 달 | 보통 - 바뀌었을 수 있음 |
| 한 달 이상 전 | 신뢰도 낮음 - 오래되었을 수 있음 표시 |

상태 질문에서는 최신성을 매우 중요하게 봅니다. 정책/사실 질문에서는 최신성이 덜 중요할 수 있습니다.

### 권위

| Source type | Authority level |
|-------------|----------------|
| 공식 위키 / 지식 베이스 | 최고 - 큐레이션되고 유지됨 |
| 공유 문서(최종본) | 높음 - 의도적으로 게시됨 |
| 이메일 공지 | 높음 - 공식 커뮤니케이션 |
| 회의 노트 | 중간-높음 - 불완전할 수 있음 |
| chat 메시지(스레드 결론) | 중간 - 비공식적이지만 실시간 |
| chat 메시지(스레드 중간) | 낮음 - 최종 입장을 반영하지 않을 수 있음 |
| 초안 문서 | 낮음 - 최종본 아님 |
| 작업 댓글 | 문맥적 - 작성자에 따라 다름 |

### 신뢰도 표현

신뢰도가 높을 때(여러 개의 최신, 권위 있는 소스가 일치):
```
The team decided to use REST for the API redesign. [direct statement]
```

신뢰도가 보통일 때(단일 소스 또는 다소 오래됨):
```
Based on the discussion in #engineering last month, the team was leaning
toward REST for the API redesign. This may have evolved since then.
```

신뢰도가 낮을 때(오래된 데이터, 비공식 소스, 또는 충돌 신호):
```
I found a reference to an API migration discussion from three months ago
in ~~chat, but I couldn't find a formal decision document. The information
may be outdated. You might want to check with the team for current status.
```

### 충돌 정보

소스가 서로 다를 때:
```
I found conflicting information about the API approach:
- The ~~chat discussion on Jan 10 suggested GraphQL
- But Sarah's email on Jan 15 confirmed REST
- The design doc (updated Jan 15) reflects REST

The most recent sources indicate REST was the final decision,
but the earlier ~~chat discussion explored GraphQL first.
```

충돌은 묵살하지 말고 드러내세요.

## 요약 전략

### 작은 결과 집합(1-5개)

각 결과를 맥락과 함께 제시하세요. 요약은 필요 없습니다. 모두 보여 주세요:
```
[Direct answer synthesized from results]

[Detail from source 1]
[Detail from source 2]

Sources: [full attribution]
```

### 중간 결과 집합(5-15개)

주제별로 그룹화하고 각 그룹을 요약하세요:
```
[Overall answer]

Theme 1: [summary of related results]
Theme 2: [summary of related results]

Key sources: [top 3-5 most relevant sources]
Full results: [count] items found across [sources]
```

### 큰 결과 집합(15개 이상)

상세 탐색 옵션과 함께 높은 수준의 종합을 제공합니다:
```
[Overall answer based on most relevant results]

Summary:
- [Key finding 1] (supported by N sources)
- [Key finding 2] (supported by N sources)
- [Key finding 3] (supported by N sources)

Top sources:
- [Most authoritative/relevant source]
- [Second most relevant]
- [Third most relevant]

Found [total count] results across [source list].
Want me to dig deeper into any specific aspect?
```

### 요약 규칙

- 답부터 시작하고 검색 과정을 먼저 말하지 마세요
- 원시 결과를 나열하지 말고 종합하세요
- 서로 다른 소스의 관련 항목을 함께 묶으세요
- 중요한 뉘앙스와 주의점을 유지하세요
- 충분히 큰 결과 집합이라면 더 자세히 볼 수 있다고 제안하세요
