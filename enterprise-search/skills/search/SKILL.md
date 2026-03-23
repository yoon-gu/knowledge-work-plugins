---
name: search
description: 연결된 모든 소스를 한 번의 쿼리로 검색합니다. "find that doc about...", "what did we decide on...", "where was the conversation about..." 같은 표현이 나오거나, chat, email, cloud storage, project tracker 어디에 있을지 모르는 결정, 문서, 대화를 찾을 때 트리거됩니다.
argument-hint: "<query>"
---

# 검색 명령

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

연결된 모든 MCP 소스를 한 번의 쿼리로 검색합니다. 사용자의 질문을 분해하고, 병렬 검색을 실행하고, 결과를 종합합니다.

## 지침

### 1. 사용 가능한 소스 확인

검색하기 전에 사용할 수 있는 MCP 소스를 확인합니다. 사용 가능한 도구 목록에서 연결된 도구를 식별하려고 시도합니다. 일반적인 소스:

- **~~chat** — 채팅 플랫폼 도구
- **~~email** — 이메일 도구
- **~~cloud storage** — 클라우드 저장소 도구
- **~~project tracker** — 프로젝트 추적 도구
- **~~CRM** — CRM 도구
- **~~knowledge base** — 지식 베이스 도구

MCP 소스가 하나도 연결되어 있지 않다면:
```
도구 전반을 검색하려면 최소 하나의 소스를 연결해야 합니다.
MCP 설정에서 ~~chat, ~~email, ~~cloud storage 또는 다른 도구를 추가하세요.

지원되는 소스: ~~chat, ~~email, ~~cloud storage, ~~project tracker, ~~CRM, ~~knowledge base,
그리고 MCP로 연결된 다른 모든 서비스.
```

### 2. 사용자 쿼리 파싱

검색 쿼리를 분석해 다음을 이해합니다:

- **의도**: 사용자가 무엇을 찾는가? (결정, 문서, 사람, 상태 업데이트, 대화)
- **엔터티**: 언급된 사람, 프로젝트, 팀, 도구
- **시간 제약**: 최신성 신호("이번 주", "지난달", 특정 날짜)
- **소스 힌트**: 특정 도구에 대한 참조("in ~~chat", "that email", "the doc")
- **필터**: 쿼리에서 명시적 필터를 추출
  - `from:` — 발신자/작성자로 필터
  - `in:` — 채널, 폴더, 위치로 필터
  - `after:` — 이 날짜 이후 결과만
  - `before:` — 이 날짜 이전 결과만
  - `type:` — 콘텐츠 타입으로 필터(message, email, doc, thread, file)

### 3. 하위 쿼리로 분해

사용 가능한 각 소스에 대해 그 소스의 네이티브 검색 문법을 사용한 타깃 하위 쿼리를 만듭니다:

**~~chat:**
- 채팅 플랫폼의 검색 및 읽기 도구 사용
- 필터를 변환: `from:`은 발신자, `in:`은 채널/방, 날짜는 시간 범위 필터
- 적절하면 자연어 쿼리를 의미 검색에 사용
- 정확한 일치를 위해 키워드 쿼리를 사용

**~~email:**
- 사용 가능한 이메일 검색 도구 사용
- 필터를 변환: `from:`은 발신자, 날짜는 시간 범위 필터
- `type:`은 첨부파일 필터나 제목 검색으로 매핑

**~~cloud storage:**
- 사용 가능한 파일 검색 도구 사용
- 파일 쿼리 문법으로 변환: 이름 포함, 전체 텍스트 포함, 수정 날짜, 파일 타입
- 파일 이름과 내용 모두 고려

**~~project tracker:**
- 사용 가능한 작업 검색 또는 typeahead 도구 사용
- 작업 텍스트 검색, 담당자 필터, 날짜 필터, 프로젝트 필터로 매핑

**~~CRM:**
- 사용 가능한 CRM 쿼리 도구 사용
- Account, Contact, Opportunity 및 기타 관련 객체를 검색

**~~knowledge base:**
- 개념적 질문에는 의미 검색을 사용
- 정확한 일치에는 키워드 검색을 사용

### 4. 병렬로 검색 실행

사용 가능한 소스 전반에서 모든 하위 쿼리를 동시에 실행합니다. 한 소스를 기다린 뒤 다음 소스를 검색하지 마세요.

각 소스에 대해:
- 변환된 쿼리 실행
- 메타데이터(타임스탬프, 작성자, 링크, 소스 유형)와 함께 결과 캡처
- 실패했거나 오류를 반환한 소스를 기록 - 한 소스의 실패가 다른 소스를 막지 않게 하기

### 5. 결과 순위화와 중복 제거

**중복 제거:**
- 같은 정보가 여러 소스에 나타나는 경우 식별하고 그룹화(예: ~~chat과 email 모두에 있는 결정)
- 중복을 그대로 보여 주지 말고 관련 결과를 함께 묶기
- 가장 권위 있거나 완전한 버전을 우선

**순위 요소:**
- **관련성**: 결과가 쿼리 의도와 얼마나 잘 맞는가?
- **최신성**: 상태/결정 질문에서는 더 최근 결과가 우선
- **권위**: 사실 질문에서는 공식 문서 > 위키 > chat; "무엇을 논의했나" 질문에서는 대화 > 문서
- **완전성**: 맥락이 더 많은 결과가 우선

### 6. 통합 결과 제시

원시 결과 목록이 아니라 종합된 답변으로 제시합니다:

**사실/결정 질문의 경우:**
```text
[Direct answer to the question]

Sources:
- [Source 1: brief description] (~~chat, #channel, date)
- [Source 2: brief description] (~~email, from person, date)
- [Source 3: brief description] (~~cloud storage, doc name, last modified)
```

**탐색적 질문("X에 대해 무엇을 알고 있나")의 경우:**
```text
[Synthesized summary combining information from all sources]

Found across:
- ~~chat: X relevant messages in Y channels
- ~~email: X relevant threads
- ~~cloud storage: X related documents
- [Other sources as applicable]

Key sources:
- [Most important source with link/reference]
- [Second most important source]
```

**"찾기" 질문(특정한 것을 찾는 경우)의 경우:**
```text
[The thing they're looking for, with direct reference]

Also found:
- [Related items from other sources]
```

### 7. 엣지 케이스 처리

**모호한 쿼리:**
쿼리가 여러 의미일 수 있으면, 검색하기 전에 한 번에 하나의 확인 질문을 합니다:
```text
"API redesign" could refer to a few things. Are you looking for:
1. The REST API v2 redesign (Project Aurora)
2. The internal SDK API changes
3. Something else?
```

**결과 없음:**
```text
I couldn't find anything matching "[query]" across [list of sources searched].

Try:
- Broader terms (e.g., "database" instead of "PostgreSQL migration")
- Different time range (currently searching [time range])
- Checking if the relevant source is connected (currently searching: [sources])
```

**부분 결과(일부 소스 실패):**
```text
[Results from successful sources]

Note: I couldn't reach [failed source(s)] during this search.
Results above are from [successful sources] only.
```

## 참고

- 항상 여러 소스를 병렬로 검색하세요 - 절대 순차적으로 하지 마세요
- 결과를 원시 목록이 아니라 답으로 종합하세요
- 사용자가 더 깊게 파고들 수 있도록 출처 표기를 포함하세요
- 사용자의 필터 문법을 존중하고 각 소스에 적절히 적용하세요
- 쿼리가 특정 인물을 언급하면, 모든 소스에서 그 사람의 메시지/문서/언급을 검색하세요
- 시간에 민감한 질문은 순위에서 최신성을 우선하세요
- 하나의 소스만 연결되어 있어도, 그 소스에서라도 유용한 결과를 제공하세요
