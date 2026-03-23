# 생산성 플러그인

[Cowork](https://claude.com/product/cowork)를 위해 주로 설계된 생산성 플러그인입니다. Anthropic의 에이전트형 데스크톱 애플리케이션이지만 Claude Code에서도 작동합니다. 작업 관리, 업무 기억, 시각적 대시보드를 제공하며, Claude가 사람, 프로젝트, 용어를 학습해 챗봇이 아니라 동료처럼 행동할 수 있게 합니다.

## 설치

```
claude plugins add knowledge-work-plugins/productivity
```

## 하는 일

이 플러그인은 Claude에게 업무에 대한 지속적인 이해를 제공합니다.

- **작업 관리** - Claude가 읽고, 쓰고, 실행하는 마크다운 작업 목록(`TASKS.md`). 자연스럽게 작업을 추가하면, Claude가 상태를 추적하고, 오래된 항목을 분류하고, 외부 도구와 동기화합니다.
- **업무 기억** - Claude에게 약어, 사람, 프로젝트, 용어를 가르치는 2단계 기억 시스템. "ask todd to do the PSR for oracle"라고 말하면 Claude는 누가, 무엇을, 어떤 거래에 대해 말하는지 정확히 압니다.
- **시각적 대시보드** - 작업의 보드 뷰와 Claude가 업무에 대해 알고 있는 내용을 실시간으로 보여 주는 로컬 HTML 파일. 보드나 파일에서 수정해도 서로 동기화됩니다.

## 명령

| 명령 | 하는 일 |
|---------|--------------|
| `/start` | 작업 + 기억을 초기화하고 대시보드를 엽니다 |
| `/update` | 오래된 항목을 분류하고, 기억의 누락을 확인하고, 해당 시 외부 도구와 동기화합니다 |
| `/update --comprehensive` | 이메일, 캘린더, 채팅을 깊게 스캔해 놓친 할 일을 표시하고 새로운 기억을 제안합니다 |

## 스킬

| 스킬 | 설명 |
|-------|-------------|
| `memory-management` | 2단계 기억 시스템 - 작업 기억용 CLAUDE.md, 심층 저장용 memory/ 디렉터리 |
| `task-management` | 공유 TASKS.md 파일을 사용하는 마크다운 기반 작업 추적 |

## 예시 워크플로

### 시작하기

```
당신: /start

Claude: [TASKS.md, CLAUDE.md, memory/ 디렉터리, dashboard.html을 만듭니다]
        [브라우저에서 대시보드를 엽니다]
        [기억을 채우기 위해 역할, 팀, 현재 우선순위를 묻습니다]
```

### 작업을 자연스럽게 추가하기

```
당신: 금요일까지 Sarah의 예산 제안을 검토해야 하고,
     Greg와 동기화한 뒤 Q2 로드맵 초안을 작성해야 하며, Platform 팀의
     API 사양도 후속 조치해야 해

Claude: [세 작업 모두를 맥락과 함께 TASKS.md에 추가합니다]
        [대시보드가 자동으로 업데이트됩니다]
```

### 아침 동기화

```
당신: /update --comprehensive

Claude: [이메일, 캘린더, 채팅을 스캔해 새 실행 항목을 찾습니다]
        [표시: "예산 제안 검토가 내일 마감입니다 - 아직 열려 있음"]
        [제안: "3개 스레드에서 새 인물이 언급됨: Jamie Park,
         Design Lead - 기억에 추가할까요?"]
        [오래된 작업을 업데이트하고 기억의 빈틈을 채웁니다]
```

### 업무 약어 해석

기억이 채워지면 Claude가 약어를 즉시 해독합니다.

```
당신: ask todd to do the PSR for oracle

Claude: "Todd Martinez(Finance lead)에게 Oracle Systems 거래($2.3M, Q2 마감)의
         Pipeline Status Report를 준비해 달라고 요청하세요"
```

추가 확인 질문도, 왕복도 없습니다.

## 데이터 소스

> 익숙하지 않은 자리표시자가 보이거나 어떤 도구가 연결되어 있는지 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

최상의 경험을 위해 커뮤니케이션 및 프로젝트 관리 도구를 연결하세요. 연결하지 않아도 작업과 기억은 수동으로 관리할 수 있습니다.

**포함된 MCP 연결:**
- 팀 맥락과 메시지 스캔을 위한 채팅(Slack)
- 실행 항목 탐지를 위한 이메일과 캘린더(Microsoft 365)
- 참고 문서를 위한 지식 베이스(Notion)
- 작업 동기화를 위한 프로젝트 추적기(Asana, Linear, Atlassian, monday.com, ClickUp)
- 문서를 위한 오피스 제품군(Microsoft 365)

**추가 옵션:**
- 각 범주의 대체 도구는 [CONNECTORS.md](CONNECTORS.md)를 참고하세요
