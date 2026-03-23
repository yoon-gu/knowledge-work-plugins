---
name: start
description: Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.
---

# Start 명령어

> 낯선 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

작업 및 메모리 시스템을 초기화한 다음 통합 대시보드를 엽니다.

## 지침

### 1. 기존 항목 확인

작업 디렉터리에서 다음을 확인합니다:
- `TASKS.md` — 작업 목록
- `CLAUDE.md` — 작업 메모리
- `memory/` — 심층 메모리 디렉터리
- `dashboard.html` — 시각적 UI

### 2. 없는 항목 생성

**`TASKS.md`가 없으면:** 표준 템플릿으로 생성합니다 (task-management 스킬 참조). 현재 작업 디렉터리에 배치합니다.

**`dashboard.html`이 없으면:** `${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html`에서 현재 작업 디렉터리로 복사합니다.

**`CLAUDE.md`와 `memory/`가 없으면:** 최초 설정입니다 — 대시보드를 열고 나서 메모리 부트스트랩 워크플로우를 시작합니다 (아래 참조). 현재 작업 디렉터리에 배치합니다.

### 3. 대시보드 열기

`open` 또는 `xdg-open`을 사용하지 마세요 — Cowork에서는 에이전트가 VM에서 실행되므로 셸 open 명령어가 사용자의 브라우저에 도달하지 않습니다. 대신 사용자에게 알려주세요: "대시보드가 `dashboard.html`에 준비되었습니다. 파일 브라우저에서 열어 시작하세요."

### 4. 사용자 안내

모든 것이 이미 초기화된 경우:
```
대시보드가 열렸습니다. 작업과 메모리가 모두 로드되었습니다.
- /productivity:update 로 작업을 동기화하고 메모리를 확인하세요
- /productivity:update --comprehensive 로 모든 활동을 심층 스캔합니다
```

메모리가 아직 부트스트랩되지 않은 경우, 5단계로 계속합니다.

### 5. 메모리 부트스트랩 (최초 실행만)

`CLAUDE.md`와 `memory/`가 아직 없을 때만 수행합니다.

직장 언어의 가장 좋은 출처는 사용자의 실제 작업 목록입니다. 실제 작업 = 실제 약어.

**사용자에게 질문합니다:**
```
할 일이나 작업 목록을 어디에 보관하시나요? 다음이 될 수 있습니다:
- 로컬 파일 (예: TASKS.md, todo.txt)
- 앱 (예: Asana, Linear, Jira, Notion, Todoist)
- 메모 파일

작업을 사용하여 직장 약어를 학습하겠습니다.
```

**작업 목록에 접근하면:**

각 작업 항목에서 잠재적 약어를 분석합니다:
- 별명일 수 있는 이름
- 약어 또는 축약어
- 프로젝트 참조 또는 코드명
- 내부 용어 또는 전문용어

**각 항목을 대화형으로 해독합니다:**

```
작업: "Send PSR to Todd re: Phoenix blockers"

이해하고 싶은 몇 가지 용어가 있습니다:

1. **PSR** - 이것은 무엇의 약자인가요?
2. **Todd** - Todd는 누구인가요? (전체 이름, 역할)
3. **Phoenix** - 프로젝트 코드명인가요? 어떤 내용인가요?
```

이미 해독한 용어는 다시 묻지 않고 각 작업을 계속 진행합니다.

### 6. 선택적 종합 스캔

작업 목록 해독 후 제안합니다:
```
메시지, 이메일, 문서를 종합적으로 스캔하시겠습니까?
시간이 더 걸리지만 업무의 사람, 프로젝트, 용어에 대해 훨씬 풍부한 컨텍스트를 구축합니다.

또는 현재 내용으로 유지하고 나중에 컨텍스트를 추가할 수 있습니다.
```

**종합 스캔을 선택하면:**

사용 가능한 MCP 소스에서 데이터를 수집합니다:
- **채팅:** 최근 메시지, 채널, DM
- **이메일:** 발송 메시지, 수신자
- **문서:** 최근 문서, 협업자
- **캘린더:** 회의, 참석자

발견된 사람, 프로젝트, 용어를 정리합니다. 신뢰도별로 그룹화하여 결과를 제시합니다:
- **추가 준비 완료** (높은 신뢰도) — 직접 추가 제안
- **명확화 필요** — 사용자에게 질문
- **낮은 빈도 / 불명확** — 나중을 위해 메모

### 7. 메모리 파일 작성

수집한 모든 것을 바탕으로 생성합니다:

**CLAUDE.md** (작업 메모리, ~50-80줄):
```markdown
# Memory

## Me
[Name], [Role] on [Team].

## People
| Who | Role |
|-----|------|
| **[Nickname]** | [Full Name], [role] |

## Terms
| Term | Meaning |
|------|---------|
| [acronym] | [expansion] |

## Projects
| Name | What |
|------|------|
| **[Codename]** | [description] |

## Preferences
- [preferences discovered]
```

**memory/** 디렉터리:
- `memory/glossary.md` — 전체 해독 목록 (약어, 용어, 별명, 코드명)
- `memory/people/{name}.md` — 개인 프로필
- `memory/projects/{name}.md` — 프로젝트 세부사항
- `memory/context/company.md` — 팀, 도구, 프로세스

### 8. 결과 보고

```
생산성 시스템 준비 완료:
- 작업: TASKS.md (X개 항목)
- 메모리: X명, X개 용어, X개 프로젝트
- 대시보드: 브라우저에서 열기

/productivity:update 로 최신 상태 유지 (심층 스캔은 --comprehensive 추가).
```

## 참고사항

- 메모리가 이미 초기화된 경우, 대시보드만 엽니다
- 별명이 중요합니다 — 항상 사람들이 실제로 어떻게 지칭되는지 캡처합니다
- 소스를 사용할 수 없으면 건너뛰고 차이를 메모합니다
- 부트스트랩 후 자연스러운 대화를 통해 메모리가 유기적으로 성장합니다
