---
name: digest
description: 연결된 모든 소스의 활동을 일간 또는 주간 다이제스트로 생성합니다. 자리를 비운 뒤 따라잡을 때, 하루를 시작하며 언급과 액션 아이템 요약을 원할 때, 또는 프로젝트별로 묶인 한 주의 결정과 문서 업데이트를 검토할 때 사용합니다.
argument-hint: "[--daily | --weekly | --since <date>]"
---

# 다이제스트 명령

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

연결된 모든 소스의 최근 활동을 훑어, 중요한 내용을 강조한 구조화된 다이제스트를 생성합니다.

## 지침

### 1. 플래그 해석

사용자 입력에서 시간 범위를 결정합니다:

- `--daily` - 최근 24시간(플래그가 없으면 기본값)
- `--weekly` - 최근 7일

사용자는 커스텀 범위도 지정할 수 있습니다:
- `--since yesterday`
- `--since Monday`
- `--since 2025-01-20`

### 2. 사용 가능한 소스 확인

연결된 MCP 소스를 식별합니다(검색 명령과 같은 방식):

- **~~chat** - 채널, DM, 멘션
- **~~email** - 받은편지함, 보낸편지함, 스레드
- **~~cloud storage** - 최근 수정되었거나 사용자와 공유된 문서
- **~~project tracker** - 사용자에게 할당되었거나, 완료되었거나, 댓글이 달린 작업
- **~~CRM** - 기회 상태 변경, 계정 활동
- **~~knowledge base** - 최근 업데이트된 위키 페이지

연결된 소스가 없다면 사용자에게 안내합니다:
```
다이제스트를 생성하려면 최소 하나의 소스가 연결되어 있어야 합니다.
MCP 설정에서 ~~chat, ~~email, ~~cloud storage 또는 다른 도구를 추가하세요.
```

### 3. 각 소스에서 활동 수집

**~~chat:**
- 사용자에게 언급된 메시지 검색(`to:me`)
- 사용자가 속한 채널의 최근 활동 확인
- 사용자가 참여한 스레드 찾기
- 핵심 채널의 새 메시지 식별

**~~email:**
- 최근 받은편지함 메시지 검색
- 새 답장이 달린 스레드 식별
- 사용자에게 직접 질문이 오거나 액션 아이템이 있는 이메일 표시

**~~cloud storage:**
- 최근 수정되었거나 사용자와 공유된 문서 찾기
- 사용자가 소유하거나 협업 중인 문서의 새 댓글 확인

**~~project tracker:**
- 사용자에게 할당된 작업(새 작업 또는 업데이트된 작업)
- 사용자가 팔로우하는 다른 사람의 완료 작업
- 사용자가 관여한 작업의 댓글

**~~CRM:**
- 기회 단계 변경
- 사용자가 소유한 계정에 기록된 새 활동
- 업데이트된 연락처 또는 계정

**~~knowledge base:**
- 관련 컬렉션의 최근 업데이트 문서
- 감시 중인 영역에서 새로 생성된 문서

### 4. 핵심 항목 식별

수집한 모든 활동에서 다음을 추출하고 분류합니다:

**액션 아이템:**
- 사용자에게 직접 요청된 사항("Can you...", "Please...", "@user")
- 할당되었거나 곧 마감되는 작업
- 사용자의 응답을 기다리는 질문
- 검토 요청

**결정 사항:**
- 스레드나 이메일에서 도달한 결론
- 승인 또는 거절
- 정책 또는 방향 변경

**언급:**
- 사용자가 언급되거나 참조된 사례
- 사용자의 프로젝트나 영역에 대한 논의

**업데이트:**
- 사용자가 팔로우하는 프로젝트의 상태 변경
- 사용자의 영역에 대한 문서 업데이트
- 사용자가 기다리던 완료 항목

### 5. 주제별 그룹화

소스별이 아니라 주제, 프로젝트, 테마별로 다이제스트를 정리합니다. 관련 활동은 소스 전반에서 합칩니다:

```
## Project Aurora
- ~~chat: Design review thread concluded — team chose Option B (#design, Tuesday)
- ~~email: Sarah sent updated spec incorporating feedback (Wednesday)
- ~~cloud storage: "Aurora API Spec v3" updated by Sarah (Wednesday)
- ~~project tracker: 3 tasks moved to In Progress, 2 completed

## Budget Planning
- ~~email: Finance team requesting Q2 projections by Friday
- ~~chat: Todd shared template in #finance (Monday)
- ~~cloud storage: "Q2 Budget Template" shared with you (Monday)
```

### 6. 다이제스트 형식화

출력을 명확하게 구조화합니다:

```
# [Daily/Weekly] Digest — [Date or Date Range]

Sources scanned: ~~chat, ~~email, ~~cloud storage, [others]

## Action Items (X items)
- [ ] [Action item 1] — from [person], [source] ([date])
- [ ] [Action item 2] — from [person], [source] ([date])

## Decisions Made
- [Decision 1] — [context] ([source], [date])
- [Decision 2] — [context] ([source], [date])

## [Topic/Project Group 1]
[Activity summary with source attribution]

## [Topic/Project Group 2]
[Activity summary with source attribution]

## Mentions
- [Mention context] — [source] ([date])

## Documents Updated
- [Doc name] — [who modified, what changed] ([date])
```

### 7. 사용 불가 소스 처리

소스가 실패하거나 접근할 수 없다면:
```
Note: Could not reach [source name] for this digest.
The following sources were included: [list of successful sources].
```

한 소스가 실패했다고 해서 다이제스트 생성이 중단되면 안 됩니다. 사용 가능한 소스로 최선의 다이제스트를 만드세요.

### 8. 요약 통계

끝에 간단한 요약을 남깁니다:
```
---
[X] action items · [Y] decisions · [Z] mentions · [W] doc updates
Across [N] sources · Covering [time range]
```

## 참고

- 플래그가 없으면 기본적으로 `--daily`를 사용합니다
- 소스가 아니라 주제/프로젝트로 그룹화하세요. 사용자는 어디가 아니라 무슨 일이 있었는지에 관심이 있습니다
- 액션 아이템은 항상 먼저 나열해야 합니다. 다이제스트에서 가장 실행 가능하기 때문입니다
- 소스 간 중복 활동은 중복 제거하세요(같은 결정이 ~~chat과 email에 있으면 하나만)
- 주간 다이제스트는 완전성보다 중요도를 우선하세요. 중요한 것만 보여 주고 잡음은 줄입니다
- 사용자가 메모리 시스템(CLAUDE.md)을 가지고 있다면, 사람 이름과 프로젝트 참조를 해석하는 데 활용하세요
- 클릭하지 않고도 사용자가 더 파고들지 판단할 수 있도록 각 항목에 충분한 맥락을 넣으세요
