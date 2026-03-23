---
name: design-system
description: 디자인 시스템을 감사, 문서화, 확장합니다. 컴포넌트 전반의 명명 불일치나 하드코딩 값 점검, 컴포넌트의 변형·상태·접근성 노트 문서화, 또는 기존 시스템에 맞는 새 패턴 설계할 때 사용합니다.
argument-hint: "[audit | document | extend] <component or system>"
---

# /design-system

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

디자인 시스템을 관리합니다. 일관성을 감사하고, 컴포넌트를 문서화하고, 새 패턴을 설계합니다.

## 사용법

```
/design-system audit                    # 전체 시스템 감사
/design-system document [component]     # 컴포넌트 문서화
/design-system extend [pattern]         # 새 컴포넌트나 패턴 설계
```

## 디자인 시스템의 구성 요소

### 디자인 토큰
시각 언어를 정의하는 원자적 값:
- 색상(브랜드, 의미, 중립)
- 타이포그래피(스케일, 굵기, 줄 높이)
- 간격(스케일, 컴포넌트 패딩)
- 경계선(반경, 두께)
- 그림자(고도 수준)
- 모션(지속시간, easing)

### 컴포넌트
정의된 다음 요소를 가진 재사용 가능한 UI 요소:
- 변형(primary, secondary, ghost)
- 상태(default, hover, active, disabled, loading, error)
- 크기(sm, md, lg)
- 동작(interactions, animations)
- 접근성(ARIA, keyboard)

### 패턴
컴포넌트를 조합한 일반적인 UI 솔루션:
- 폼(input groups, validation, submission)
- 내비게이션(sidebar, tabs, breadcrumbs)
- 데이터 표시(tables, cards, lists)
- 피드백(toasts, modals, inline messages)

## 원칙

1. **창의성보다 일관성** - 시스템은 팀이 바퀴를 다시 만들지 않게 하려고 존재합니다
2. **제약 안의 유연성** - 컴포넌트는 경직되지 않고 조합 가능해야 합니다
3. **모든 것을 문서화** - 문서에 없으면 존재하지 않는 것입니다
4. **버전과 마이그레이션** - 파괴적 변경에는 마이그레이션 경로가 필요합니다

## 출력 - 감사

```markdown
## Design System Audit

### Summary
**Components reviewed:** [X] | **Issues found:** [X] | **Score:** [X/100]

### Naming Consistency
| Issue | Components | Recommendation |
|-------|------------|----------------|
| [Inconsistent naming] | [List] | [Standard to adopt] |

### Token Coverage
| Category | Defined | Hardcoded Values Found |
|----------|---------|----------------------|
| Colors | [X] | [X] instances of hardcoded hex |
| Spacing | [X] | [X] instances of arbitrary values |
| Typography | [X] | [X] instances of custom fonts/sizes |

### Component Completeness
| Component | States | Variants | Docs | Score |
|-----------|--------|----------|------|-------|
| Button | ✅ | ✅ | ⚠️ | 8/10 |
| Input | ✅ | ⚠️ | ❌ | 5/10 |

### Priority Actions
1. [가장 영향력 있는 개선]
2. [두 번째 우선순위]
3. [세 번째 우선순위]
```

## 출력 - 문서화

```markdown
## Component: [Name]

### Description
[이 컴포넌트가 무엇이며 언제 사용하는지]

### Variants
| Variant | Use When |
|---------|----------|
| [Primary] | [Main actions] |
| [Secondary] | [Supporting actions] |

### Props / Properties
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| [prop] | [type] | [default] | [description] |

### States
| State | Visual | Behavior |
|-------|--------|----------|
| Default | [description] | — |
| Hover | [description] | [interaction] |
| Active | [description] | [interaction] |
| Disabled | [description] | Non-interactive |
| Loading | [description] | [animation] |

### Accessibility
- **Role**: [ARIA role]
- **Keyboard**: [Tab, Enter, Escape behavior]
- **Screen reader**: [Announced as...]

### Do's and Don'ts
| ✅ Do | ❌ Don't |
|------|---------|
| [Best practice] | [Anti-pattern] |

### Code Example
[Framework-appropriate code snippet]
```

## 출력 - 확장

```markdown
## New Component: [Name]

### Problem
[이 컴포넌트가 해결하는 사용자 필요나 빈틈]

### Existing Patterns
| Related Component | Similarity | Why It's Not Enough |
|-------------------|-----------|---------------------|
| [Component] | [What's shared] | [What's missing] |

### Proposed Design

#### API / Props
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| [prop] | [type] | [default] | [description] |

#### Variants
| Variant | Use When | Visual |
|---------|----------|--------|
| [Variant] | [Scenario] | [Description] |

#### States
| State | Behavior | Notes |
|-------|----------|-------|
| Default | [Description] | — |
| Hover | [Description] | [Interaction] |
| Disabled | [Description] | Non-interactive |
| Loading | [Description] | [Animation] |

#### Tokens Used
- Colors: [어떤 토큰인지]
- Spacing: [어떤 토큰인지]
- Typography: [어떤 토큰인지]

### Accessibility
- **Role**: [ARIA role]
- **Keyboard**: [예상 상호작용]
- **Screen reader**: [Announced as...]

### Open Questions
- [디자인 검토가 필요한 결정]
- [해결해야 할 엣지 케이스]
```

## 연결 도구가 있을 경우

**~~design tool**가 연결되어 있다면:
- Figma에서 직접 컴포넌트를 감사하고 명명, 변형, 토큰 사용을 확인
- 컴포넌트 속성과 레이어 구조를 가져와 문서화

**~~knowledge base**가 연결되어 있다면:
- 기존 컴포넌트 문서와 사용 지침을 검색
- 업데이트된 문서를 위키에 게시

## 팁

1. **감사부터 시작** - 어디에 있는지 알아야 어디로 갈지 정할 수 있습니다.
2. **빌드하면서 문서화** - 컴포넌트를 설계하는 동안 문서화하는 편이 쉽습니다.
3. **완벽함보다 범위 우선** - 컴포넌트 10개를 100% 문서화하는 것보다 80%의 컴포넌트를 문서화하는 편이 낫습니다.
