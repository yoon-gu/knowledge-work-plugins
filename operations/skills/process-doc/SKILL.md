---
name: process-doc
description: Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.
argument-hint: "<process name or description>"
---

# /process-doc

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

비즈니스 프로세스를 완전한 표준 운영 절차(SOP)로 문서화합니다.

## 사용법

```
/process-doc $ARGUMENTS
```

## 동작 방식

프로세스를 안내해 주세요. 설명하거나 기존 문서를 붙여넣거나, 이름만 알려주셔도 제가 적절한 질문을 던집니다. 완전한 SOP를 만들어 드립니다.

## 출력

```markdown
## 프로세스 문서: [프로세스 이름]
**담당자:** [사람/팀] | **마지막 업데이트:** [날짜] | **검토 주기:** [분기별/연간]

### 목적
[이 프로세스가 존재하는 이유와 달성하는 것]

### 범위
[포함되는 것과 제외되는 것]

### RACI 매트릭스
| 단계 | Responsible | Accountable | Consulted | Informed |
|------|------------|-------------|-----------|----------|
| [단계] | [누가 수행하는지] | [누가 책임지는지] | [누구와 상의하는지] | [누구에게 알리는지] |

### 프로세스 흐름
[ASCII 플로우차트 또는 단계별 설명]

### 세부 단계

#### 단계 1: [이름]
- **누가**: [역할]
- **언제**: [트리거 또는 시점]
- **어떻게**: [세부 지침]
- **출력**: [이 단계가 만들어내는 것]

#### 단계 2: [이름]
[같은 형식]

### 예외와 경계 사례
| 시나리오 | 대응 방법 |
|----------|-----------|
| [예외] | [어떻게 처리할지] |

### 지표
| 지표 | 목표 | 측정 방법 |
|--------|--------|----------------|
| [지표] | [목표] | [방법] |

### 관련 문서
- [관련 프로세스 또는 정책 링크]
```

## 연결 도구가 있을 경우

If **~~knowledge base** is connected:
- 기존 프로세스 문서를 검색해 중복 생성 대신 업데이트합니다.
- 완성된 SOP를 위키에 게시합니다.

If **~~project tracker** is connected:
- 프로세스를 관련 프로젝트와 워크플로에 연결합니다.
- 프로세스 개선 실행 항목용 작업을 만듭니다.

## 팁

1. **일단 거칠게 시작하세요** - 완벽한 설명은 필요 없습니다. 현재 어떻게 돌아가는지만 말해 주면 구조화하겠습니다.
2. **예외를 포함하세요** - "보통은 X를 하지만, 가끔 Y를 한다"가 가장 가치 있는 문서화 대상입니다.
3. **사람 이름을 적으세요** - 역할은 바뀌어도 오늘 누가 무엇을 하는지 알면 프로세스를 정확히 잡는 데 도움이 됩니다.
