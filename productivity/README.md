# 생산성 플러그인

Anthropic의 에이전트형 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 주로 설계된 생산성 플러그인으로, Claude Code에서도 동작합니다. 작업 관리, 직장 메모리, 시각적 대시보드를 제공하며 — Claude가 여러분의 사람들, 프로젝트, 용어를 학습하여 챗봇이 아닌 동료처럼 행동할 수 있게 합니다.

## 설치

```
claude plugins add knowledge-work-plugins/productivity
```

## 기능

이 플러그인은 Claude에게 여러분의 업무에 대한 지속적인 이해를 제공합니다:

- **작업 관리** — Claude가 읽고, 쓰고, 실행하는 마크다운 작업 목록(`TASKS.md`). 자연스럽게 작업을 추가하면 Claude가 상태를 추적하고, 오래된 항목을 분류하고, 외부 도구와 동기화합니다.
- **직장 메모리** — Claude에게 여러분의 약어, 사람들, 프로젝트, 용어를 가르치는 이중 계층 메모리 시스템. "ask todd to do the PSR for oracle"이라고 말하면 Claude는 누구인지, 무엇인지, 어떤 거래인지 정확히 알고 있습니다.
- **시각적 대시보드** — 작업의 보드 뷰와 Claude가 알고 있는 직장 정보의 실시간 뷰를 제공하는 로컬 HTML 파일. 보드나 파일에서 편집해도 항상 동기화가 유지됩니다.

## 명령어

| 명령어 | 기능 |
|---------|--------------|
| `/start` | 작업 및 메모리 초기화, 대시보드 열기 |
| `/update` | 오래된 항목 분류, 메모리 갭 확인, 외부 도구와 동기화 |
| `/update --comprehensive` | 이메일, 캘린더, 채팅 심층 스캔 — 놓친 할 일 플래그 지정 및 새 메모리 제안 |

## 스킬

| 스킬 | 설명 |
|-------|-------------|
| `memory-management` | 이중 계층 메모리 시스템 — 작업 메모리를 위한 CLAUDE.md, 심층 저장소를 위한 memory/ 디렉터리 |
| `task-management` | 공유 TASKS.md 파일을 사용한 마크다운 기반 작업 추적 |

## 예시 워크플로우

### 시작하기

```
사용자: /start

Claude: [TASKS.md, CLAUDE.md, memory/ 디렉터리, dashboard.html 생성]
        [브라우저에서 대시보드 열기]
        [메모리 초기화를 위해 역할, 팀, 현재 우선순위 질문]
```

### 자연스럽게 작업 추가하기

```
사용자: 금요일까지 Sarah의 예산안을 검토하고,
        Greg과 싱크 후 Q2 로드맵을 작성하고,
        Platform 팀의 API 스펙에 대한 후속 조치를 해야 해

Claude: [세 가지 작업을 모두 컨텍스트와 함께 TASKS.md에 추가]
        [대시보드 자동 업데이트]
```

### 아침 싱크

```
사용자: /update --comprehensive

Claude: [새 액션 아이템을 위해 이메일, 캘린더, 채팅 스캔]
        [플래그: "예산안 검토가 내일 마감 — 아직 진행 중"]
        [제안: "3개 스레드에서 새로운 사람 언급됨: Jamie Park,
         Design Lead — 메모리에 추가할까요?"]
        [오래된 작업 업데이트 및 메모리 갭 채우기]
```

### 직장 약어 해독

메모리가 구성되면 Claude가 여러분의 약어를 즉시 해독합니다:

```
사용자: ask todd to do the PSR for oracle

Claude: "Todd Martinez(재무 팀장)에게 Oracle Systems 거래($2.3M, Q2 마감)에 대한
         Pipeline Status Report 작성을 요청하세요"
```

추가 질문 없음. 불필요한 왕복 없음.

## 데이터 소스

> 낯선 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

최상의 경험을 위해 커뮤니케이션 및 프로젝트 관리 도구를 연결하세요. 연결하지 않으면 작업과 메모리를 수동으로 관리합니다.

**포함된 MCP 연결:**
- 팀 컨텍스트 및 메시지 스캔을 위한 채팅(Slack)
- 액션 아이템 발견을 위한 이메일 및 캘린더(Microsoft 365)
- 참조 문서를 위한 지식 베이스(Notion)
- 작업 동기화를 위한 프로젝트 트래커(Asana, Linear, Atlassian, monday.com, ClickUp)
- 문서를 위한 오피스 제품군(Microsoft 365)

**추가 옵션:**
- 각 카테고리의 대체 도구는 [CONNECTORS.md](CONNECTORS.md)를 참조하세요
