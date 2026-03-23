---
name: architecture
description: 아키텍처 결정 기록(ADR)을 생성하거나 평가합니다. 기술 선택(예: Kafka vs SQS), 트레이드오프와 결과를 포함한 설계 결정 문서화, 시스템 설계 제안 검토, 요구 사항과 제약 조건으로부터 새 컴포넌트 설계 시 사용합니다.
argument-hint: "<결정 사항 또는 설계할 시스템>"
---

# /architecture

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

아키텍처 결정 기록(ADR)을 생성하거나 시스템 설계를 평가합니다.

## 사용법

```
/architecture $ARGUMENTS
```

## 모드

**ADR 생성**: "이벤트 버스에 Kafka를 사용할까요, SQS를 사용할까요?"
**설계 평가**: "이 마이크로서비스 제안을 검토해 주세요"
**시스템 설계**: "앱의 알림 시스템을 설계해 주세요"

요구 사항 수집, 확장성 분석, 트레이드오프 평가에 대한 자세한 프레임워크는 **system-design** skill을 참조하세요.

## 출력 — ADR 형식

```markdown
# ADR-[번호]: [제목]

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** [날짜]
**Deciders:** [승인이 필요한 담당자]

## Context
[상황은 무엇인가? 어떤 요소들이 작용하고 있는가?]

## Decision
[제안하는 변경 사항은 무엇인가?]

## Options Considered

### Option A: [이름]
| Dimension | Assessment |
|-----------|------------|
| Complexity | [Low/Med/High] |
| Cost | [평가] |
| Scalability | [평가] |
| Team familiarity | [평가] |

**Pros:** [목록]
**Cons:** [목록]

### Option B: [이름]
[동일한 형식]

## Trade-off Analysis
[명확한 근거를 포함한 옵션 간 주요 트레이드오프]

## Consequences
- [더 쉬워지는 것]
- [더 어려워지는 것]
- [다시 검토해야 할 것]

## Action Items
1. [ ] [구현 단계]
2. [ ] [후속 조치]
```

## 커넥터 사용 가능 시

**~~knowledge base**가 연결된 경우:
- 이전 ADR 및 설계 문서 검색
- 관련 기술 컨텍스트 찾기

**~~project tracker**가 연결된 경우:
- 관련 에픽 및 티켓에 연결
- 구현 작업 생성

## 팁

1. **제약 조건을 미리 명시하세요** — "2주 안에 출시해야 한다" 또는 "10K rps를 처리해야 한다"와 같은 조건이 답변의 방향을 결정합니다.
2. **옵션에 이름을 붙이세요** — 이미 한 방향으로 기울어져 있더라도, 명시적인 대안이 있을 때 더 균형 잡힌 분석이 가능합니다.
3. **비기능적 요구 사항을 포함하세요** — 지연 시간, 비용, 팀 전문성, 유지보수 부담은 기능만큼이나 중요합니다.
