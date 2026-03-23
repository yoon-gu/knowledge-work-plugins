---
name: task-management
description: Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.
user-invocable: false
---

# 작업 관리

작업은 여러분과 사용자 모두가 편집할 수 있는 간단한 `TASKS.md` 파일에서 추적됩니다.

## 파일 위치

**항상 현재 작업 디렉터리의 `TASKS.md`를 사용합니다.**

- 존재하면 읽기/쓰기
- 존재하지 않으면 아래 템플릿으로 생성

## 대시보드 설정 (최초 실행)

작업 및 메모리 관리를 위한 시각적 대시보드를 사용할 수 있습니다. **작업과의 첫 번째 상호작용 시:**

1. 현재 작업 디렉터리에 `dashboard.html`이 있는지 확인
2. 없으면 `${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html`에서 현재 작업 디렉터리로 복사
3. 사용자에게 알립니다: "대시보드를 추가했습니다. `/productivity:start`를 실행하여 전체 시스템을 설정하세요."

작업 보드:
- 동일한 `TASKS.md` 파일을 읽고 씁니다
- 변경사항 자동 저장
- 외부 변경사항 감지 (CLI에서 편집 시 동기화)
- 작업 및 섹션의 드래그 앤 드롭 재정렬 지원

## 형식 및 템플릿

새 TASKS.md를 생성할 때 이 정확한 템플릿을 사용합니다 (예시 작업 없이):

```markdown
# Tasks

## Active

## Waiting On

## Someday

## Done
```

작업 형식:
- `- [ ] **작업 제목** - 컨텍스트, 담당자, 마감일`
- 추가 세부사항을 위한 하위 항목
- 완료: `- [x] ~~Task~~ (date)`

## 상호작용 방법

**사용자가 "what's on my plate" / "my tasks"라고 물을 때:**
- TASKS.md 읽기
- Active 및 Waiting On 섹션 요약
- 기한이 지났거나 긴급한 항목 강조

**사용자가 "add a task" / "remind me to"라고 말할 때:**
- `- [ ] **Task**` 형식으로 Active 섹션에 추가
- 제공된 경우 컨텍스트 포함 (담당자, 마감일)

**사용자가 "done with X" / "finished X"라고 말할 때:**
- 작업 찾기
- `[ ]`를 `[x]`로 변경
- 취소선 추가: `~~task~~`
- 완료 날짜 추가
- Done 섹션으로 이동

**사용자가 "what am I waiting on"이라고 물을 때:**
- Waiting On 섹션 읽기
- 각 항목이 얼마나 대기 중인지 메모

## 규칙

- 스캔 가능성을 위해 작업 제목을 **굵게** 표시
- 누군가에 대한 약속일 때 "for [person]" 포함
- 마감일을 위한 "due [date]" 포함
- 대기 항목을 위한 "since [date]" 포함
- 추가 컨텍스트를 위한 하위 항목
- Done 섹션은 ~1주일 보관 후 오래된 항목 삭제

## 작업 추출

회의나 대화를 요약할 때 추출된 작업 추가를 제안합니다:
- 사용자가 한 약속 ("I'll send that over")
- 사용자에게 배정된 실행 항목
- 언급된 후속 조치

추가하기 전에 확인을 구합니다 — 확인 없이 자동으로 추가하지 않습니다.
