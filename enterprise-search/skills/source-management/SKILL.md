---
name: source-management
description: 엔터프라이즈 검색용 연결된 MCP 소스를 관리합니다. 사용 가능한 소스를 감지하고, 새 소스 연결을 안내하고, 소스 우선순위 순서를 다루고, 속도 제한 인식을 관리합니다.
user-invocable: false
---

# 소스 관리

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

어떤 소스를 사용할 수 있는지 알고, 새 소스를 연결하도록 돕고, 소스가 어떻게 조회되는지 관리합니다.

## 사용 가능한 소스 확인

사용 가능한 도구를 확인해 연결된 MCP 소스를 판별합니다. 각 소스는 MCP 도구 집합에 대응합니다:

| Source | Key capabilities |
|--------|-----------------|
| **~~chat** | 메시지 검색, 채널과 스레드 읽기 |
| **~~email** | 메시지 검색, 개별 이메일 읽기 |
| **~~cloud storage** | 파일 검색, 문서 내용 가져오기 |
| **~~project tracker** | 작업 검색, typeahead 검색 |
| **~~CRM** | 레코드 쿼리(accounts, contacts, opportunities) |
| **~~knowledge base** | 의미 검색, 키워드 검색 |

도구 접두사가 보이면 해당 소스가 연결되어 있고 검색 가능합니다.

## 사용자가 소스 연결하도록 안내하기

사용자가 검색하지만 연결된 소스가 거의 없거나 없을 때:

```text
You currently have [N] source(s) connected: [list].

To expand your search, you can connect additional sources in your MCP settings:
- ~~chat — messages, threads, channels
- ~~email — emails, conversations, attachments
- ~~cloud storage — docs, sheets, slides
- ~~project tracker — tasks, projects, milestones
- ~~CRM — accounts, contacts, opportunities
- ~~knowledge base — wiki pages, knowledge base articles

The more sources you connect, the more complete your search results.
```

사용자가 아직 연결되지 않은 특정 도구를 묻는 경우:

```text
[Tool name] isn't currently connected. To add it:
1. Open your MCP settings
2. Add the [tool] MCP server configuration
3. Authenticate when prompted

Once connected, it will be automatically included in future searches.
```

## 소스 우선순위 순서

질문 유형에 따라 먼저 검색하면 좋은 소스가 다릅니다. 이 우선순위는 결과의 가중치를 정하는 데 쓰고, 소스를 건너뛰는 데 쓰지 않습니다:

### 질문 유형별

**결정 질문**("What did we decide..."):
```text
1. ~~chat (conversations where decisions happen)
2. ~~email (decision confirmations, announcements)
3. ~~cloud storage (meeting notes, decision logs)
4. Wiki (if decisions are documented)
5. Task tracker (if decisions are captured in tasks)
```

**상태 질문**("What's the status of..."):
```text
1. Task tracker (~~project tracker — authoritative status)
2. ~~chat (real-time discussion)
3. ~~cloud storage (status docs, reports)
4. ~~email (status update emails)
5. Wiki (project pages)
```

**문서 질문**("Where's the doc for..."):
```text
1. ~~cloud storage (primary doc storage)
2. Wiki / ~~knowledge base (knowledge base)
3. ~~email (docs shared via email)
4. ~~chat (docs shared in channels)
5. Task tracker (docs linked to tasks)
```

**사람 질문**("Who works on..." / "Who knows about..."):
```text
1. ~~chat (message authors, channel members)
2. Task tracker (task assignees)
3. ~~cloud storage (doc authors, collaborators)
4. ~~CRM (account owners, contacts)
5. ~~email (email participants)
```

**사실/정책 질문**("What's our policy on..."):
```text
1. Wiki / ~~knowledge base (official documentation)
2. ~~cloud storage (policy docs, handbooks)
3. ~~email (policy announcements)
4. ~~chat (policy discussions)
```

### 기본 우선순위(일반 질문)

질문 유형이 불명확할 때:
```text
1. ~~chat (highest volume, most real-time)
2. ~~email (formal communications)
3. ~~cloud storage (documents and files)
4. Wiki / ~~knowledge base (structured knowledge)
5. Task tracker (work items)
6. CRM (customer data)
```

## 속도 제한 인식

MCP 소스는 속도 제한이 있을 수 있습니다. 우아하게 처리하세요:

### 감지

속도 제한 응답은 보통 다음처럼 나타납니다:
- HTTP 429 응답
- "rate limit", "too many requests", "quota exceeded"를 언급하는 오류 메시지
- 지연되거나 throttled된 응답

### 처리

소스가 속도 제한되면:

1. **즉시 재시도하지 않기** - 제한을 존중하세요
2. **다른 소스를 계속 사용** - 전체 검색을 막지 마세요
3. **사용자에게 알리기**:
```text
Note: [Source] is temporarily rate limited. Results below are from
[other sources]. You can retry in a few minutes to include [source].
```
4. **다이제스트의 경우** - 중간에 제한되면, 제한에 걸리기 전에 어떤 시간 범위가 덮였는지 알리기

### 예방

- 불필요한 API 호출을 피하세요 - 쿼리하기 전에 해당 소스에 결과가 있을 가능성이 높은지 확인
- 가능하면 광범위한 스캔보다 타깃팅된 쿼리 사용
- 다이제스트는 API가 지원한다면 요청을 배치로 묶기
- 캐시 인식: 방금 같은 검색을 했다면 즉시 다시 실행하지 않기

## 소스 상태

세션 동안 소스 가용성을 추적합니다:

```text
Source Status:
  ~~chat:        ✓ Available
  ~~email:        ✓ Available
  ~~cloud storage:  ✓ Available
  ~~project tracker:        ✗ Not connected
  ~~CRM:   ✗ Not connected
  ~~knowledge base:      ⚠ Rate limited (retry in 2 min)
```

검색 결과를 보고할 때는 어떤 소스를 검색했는지 포함해 답변의 범위를 사용자가 알 수 있게 하세요.

## 커스텀 소스 추가

엔터프라이즈 검색 플러그인은 MCP로 연결된 어떤 소스와도 작동합니다. 새로운 MCP 서버가 생기면 `.mcp.json` 구성에 추가할 수 있습니다. 검색과 다이제스트 명령은 사용 가능한 도구를 기준으로 새 소스를 자동 감지하고 포함합니다.

새 소스를 추가하려면:
1. `.mcp.json`에 MCP 서버 구성을 추가
2. 필요한 경우 인증
3. 이후 검색에 자동으로 포함됨
