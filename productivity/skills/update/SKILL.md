---
name: update
description: 현재 활동에서 작업을 동기화하고 기억을 새로 고칩니다. 프로젝트 추적기에서 새 할당을 TASKS.md로 가져올 때, 오래되었거나 기한이 지난 작업을 분류할 때, 모르는 사람이나 프로젝트에 대한 기억 공백을 채울 때, 채팅과 이메일에 묻힌 할 일을 잡기 위한 종합 스캔을 실행할 때 사용합니다.
argument-hint: "[--comprehensive]"
---

# 업데이트 명령

> 익숙하지 않은 자리표시자가 보이거나 어떤 도구가 연결되어 있는지 확인해야 한다면 [CONNECTORS.md](../../CONNECTORS.md)를 참고하세요.

작업 목록과 기억을 최신 상태로 유지합니다. 두 가지 모드가 있습니다.

- **기본:** 외부 도구에서 작업을 동기화하고, 오래된 항목을 분류하고, 기억의 누락을 확인합니다.
- **`--comprehensive`:** 채팅, 이메일, 캘린더, 문서를 깊게 스캔해 놓친 할 일을 표시하고 새 기억을 제안합니다.

## 사용법

```bash
/productivity:update
/productivity:update --comprehensive
```

## 기본 모드

### 1. 현재 상태 불러오기

`TASKS.md`와 `memory/` 디렉터리를 읽습니다. 없으면 먼저 `/productivity:start`를 제안합니다.

### 2. 외부 소스에서 작업 동기화

사용 가능한 작업 소스를 확인합니다.
- **Project tracker** (e.g. Asana, Linear, Jira) (if MCP available)
- **GitHub Issues** (if in a repo): `gh issue list --assignee=@me`

사용 가능한 소스가 없으면 3단계로 넘어갑니다.

**사용자에게 할당된 작업**(열림/진행 중)을 가져옵니다. TASKS.md와 비교합니다.

| 외부 작업 | TASKS.md 일치? | 조치 |
|---------------|-----------------|--------|
| 찾았지만 TASKS.md에는 없음 | 일치 없음 | 추가할지 제안 |
| 찾았고 이미 TASKS.md에 있음 | 제목으로 일치(유사 매칭) | 건너뜀 |
| TASKS.md에는 있는데 외부에는 없음 | 일치 없음 | 잠재적으로 오래된 항목으로 표시 |
| 외부에서 완료됨 | 진행 중 섹션에 있음 | 완료 표시를 제안 |

차이점을 제시하고 사용자가 추가/완료할지 결정하게 합니다.

### 3. 오래된 항목 분류

TASKS.md의 진행 중 작업을 검토하고 다음을 표시합니다.
- 기한이 지난 작업
- 30일 이상 진행 중인 작업
- 맥락이 없는 작업(사람이나 프로젝트 없음)

각 항목마다 분류를 제안합니다. 완료로 표시할까요? 일정 재조정할까요? 언젠가로 옮길까요?

### 4. 기억 공백을 위해 작업 해독

각 작업마다 모든 엔터티(사람, 프로젝트, 약어, 도구, 링크)를 해독하려 시도합니다.

```
작업: "Send PSR to Todd re: Phoenix blockers"

해독:
- PSR → ✓ Pipeline Status Report(용어집에 있음)
- Todd → ✓ Todd Martinez(people/에 있음)
- Phoenix → ? 기억에 없음
```

완전히 해독된 것과 공백이 있는 것을 구분해 추적합니다.

### 5. 공백 채우기

알 수 없는 용어를 묶어서 제시합니다.
```
작업에서 맥락이 없는 용어를 찾았습니다.

1. "Phoenix" (from: "Send PSR to Todd re: Phoenix blockers")
   → Phoenix가 무엇인가요?

2. "Maya" (from: "sync with Maya on API design")
   → Maya는 누구인가요?
```

답변을 적절한 기억 파일(people/, projects/, glossary.md)에 추가합니다.

### 6. 풍부한 맥락 수집

작업에는 기억보다 더 풍부한 맥락이 담겨 있는 경우가 많습니다. 다음을 추출하고 업데이트합니다.
- 작업의 **링크** → 프로젝트/사람 파일에 추가
- **상태 변경**("launch done") → 프로젝트 상태 업데이트, CLAUDE.md에서 내림
- **관계**("Todd's sign-off on Maya's proposal") → 사람 간 상호 참조
- **마감일** → 프로젝트 파일에 추가

### 7. 보고

```
업데이트 완료:
- 작업: 프로젝트 추적기(예: Asana)에서 +3개, 1개 완료, 2개 분류
- 기억: 공백 2개 채움, 프로젝트 1개 풍부화
- 모든 작업 해독 완료 ✓
```

## 종합 모드(`--comprehensive`)

기본 모드의 모든 내용에 더해 최근 활동을 깊게 스캔합니다.

### 추가 단계: 활동 소스 스캔

사용 가능한 MCP 소스에서 데이터를 수집합니다.
- **Chat:** Search recent messages, read active channels
- **Email:** Search sent messages
- **Documents:** List recently touched docs
- **Calendar:** List recent + upcoming events

### 추가 단계: 놓친 할 일 표시

활동을 TASKS.md와 비교합니다. 추적되지 않은 실행 항목을 표면화합니다.

```
## Possible Missing Tasks

From your activity, these look like todos you haven't captured:

1. From chat (Jan 18):
   "I'll send the updated mockups by Friday"
   → Add to TASKS.md?

2. From meeting "Phoenix Standup" (Jan 17):
   You have a recurring meeting but no Phoenix tasks active
   → Anything needed here?

3. From email (Jan 16):
   "I'll review the API spec this week"
   → Add to TASKS.md?
```

사용자가 무엇을 추가할지 선택하게 합니다.

### 추가 단계: 새 기억 제안

기억에 없는 새 엔터티를 표면화합니다.

```
## New People (not in memory)
| Name | Frequency | Context |
|------|-----------|---------|
| Maya Rodriguez | 12 mentions | design, UI reviews |
| Alex K | 8 mentions | DMs about API |

## New Projects/Topics
| Name | Frequency | Context |
|------|-----------|---------|
| Starlight | 15 mentions | planning docs, product |

## Suggested Cleanup
- **Horizon project** — No mentions in 30 days. Mark completed?
```

신뢰도별로 묶어 제시합니다. 신뢰도가 높은 항목은 직접 추가를 제안하고, 낮은 항목은 질문합니다.

## 참고

- 사용자 확인 없이 작업이나 기억을 자동 추가하지 않습니다.
- 가능하면 외부 소스 링크를 보존합니다.
- 작업 제목의 유사 매칭으로 사소한 표현 차이를 처리합니다.
- 자주 실행해도 안전합니다. 새로운 정보가 있을 때만 업데이트합니다.
- `--comprehensive`는 항상 대화식으로 실행합니다.
