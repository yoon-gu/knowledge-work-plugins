---
name: accessibility-review
description: 디자인이나 페이지에 대해 WCAG 2.1 AA 접근성 감사를 수행합니다. "audit accessibility", "check a11y", "is this accessible?" 같은 표현이 나오거나, 인수인계 전 색 대비, 키보드 내비게이션, 터치 타깃 크기, 스크린 리더 동작을 검토할 때 트리거됩니다.
argument-hint: "<Figma URL, URL, or description>"
---

# /accessibility-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

디자인이나 페이지의 WCAG 2.1 AA 접근성 준수 여부를 감사합니다.

## 사용법

```
/accessibility-review $ARGUMENTS
```

접근성을 감사합니다: @$1

## WCAG 2.1 AA 빠른 참조

### Perceivable
- **1.1.1** 비텍스트 콘텐츠에는 대체 텍스트가 있어야 함
- **1.3.1** 정보와 구조는 의미적으로 전달되어야 함
- **1.4.3** 대비 비율 >= 4.5:1(일반 텍스트), >= 3:1(큰 텍스트)
- **1.4.11** 비텍스트 대비 >= 3:1(UI 구성요소, 그래픽)

### Operable
- **2.1.1** 모든 기능이 키보드로 사용 가능해야 함
- **2.4.3** 논리적인 포커스 순서
- **2.4.7** 보이는 포커스 표시
- **2.5.5** 터치 타깃 >= 44x44 CSS 픽셀

### Understandable
- **3.2.1** 포커스 시 예측 가능해야 함(예상치 못한 변경 없음)
- **3.3.1** 오류 식별(오류를 설명)
- **3.3.2** 입력에 대한 레이블 또는 지침

### Robust
- **4.1.2** 모든 UI 구성요소에 이름, 역할, 값

## 흔한 문제

1. 대비가 부족한 색 사용
2. 폼 레이블 누락
3. 상호작용 요소의 키보드 접근 불가
4. 의미 있는 이미지에 대체 텍스트 누락
5. 모달의 포커스 트랩
6. ARIA 랜드마크 누락
7. 제어 없이 자동 재생되는 미디어
8. 연장 옵션 없는 시간 제한

## 테스트 접근법

1. 자동 스캔(문제의 약 30% 탐지)
2. 키보드만으로 탐색
3. 스크린 리더 테스트(VoiceOver, NVDA)
4. 색 대비 검증
5. 200% 확대 - 레이아웃이 깨지는가?

## 출력

```markdown
## Accessibility Audit: [Design/Page Name]
**Standard:** WCAG 2.1 AA | **Date:** [Date]

### Summary
**Issues found:** [X] | **Critical:** [X] | **Major:** [X] | **Minor:** [X]

### Findings

#### Perceivable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [1.4.3 Contrast] | 🔴 Critical | [Fix] |

#### Operable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [2.1.1 Keyboard] | 🟡 Major | [Fix] |

#### Understandable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [3.3.2 Labels] | 🟢 Minor | [Fix] |

#### Robust
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [4.1.2 Name, Role, Value] | 🟡 Major | [Fix] |

### Color Contrast Check
| Element | Foreground | Background | Ratio | Required | Pass? |
|---------|-----------|------------|-------|----------|-------|
| [Body text] | [color] | [color] | [X]:1 | 4.5:1 | ✅/❌ |

### Keyboard Navigation
| Element | Tab Order | Enter/Space | Escape | Arrow Keys |
|---------|-----------|-------------|--------|------------|
| [Element] | [Order] | [Behavior] | [Behavior] | [Behavior] |

### Screen Reader
| Element | Announced As | Issue |
|---------|-------------|-------|
| [Element] | [What SR says] | [Problem if any] |

### Priority Fixes
1. **[Critical fix]** — [누구에게 어떤 영향을 주고 무엇을 막는지]
2. **[Major fix]** — [누구에게 무엇을 개선하는지]
3. **[Minor fix]** — 있으면 좋은 개선
```

## 연결 도구가 있을 경우

**~~design tool**가 연결되어 있다면:
- Figma에서 색상 값, 폰트 크기, 터치 타깃을 직접 검사
- 디자인 스펙에서 컴포넌트 ARIA 역할과 키보드 동작을 확인

**~~project tracker**가 연결되어 있다면:
- 각 접근성 이슈에 심각도와 WCAG 기준을 포함한 티켓 생성
- 발견 사항을 기존 접근성 개선 에픽과 연결

## 팁

1. **대비와 키보드부터 시작** - 가장 흔하고 영향 큰 문제를 잡습니다.
2. **실제 보조 기술로 테스트** - 이 감사는 좋은 출발점이지만, VoiceOver/NVDA로 수동 테스트하면 제가 못 보는 문제를 찾을 수 있습니다.
3. **영향으로 우선순위를 정하기** - 먼저 사용자를 막는 문제를 고치고, 다듬기는 나중에 하세요.
