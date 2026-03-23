---
name: design-handoff
description: 디자인으로부터 개발자 인수인계 명세를 생성합니다. 디자인이 엔지니어링 준비가 되었고 레이아웃, 디자인 토큰, 컴포넌트 props, 상호작용 상태, 반응형 브레이크포인트, 엣지 케이스, 애니메이션 세부 정보가 포함된 스펙 시트가 필요할 때 사용합니다.
argument-hint: "<Figma URL or design description>"
---

# /design-handoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

디자인으로부터 포괄적인 개발자 인수인계 문서를 생성합니다.

## 사용법

```
/design-handoff $ARGUMENTS
```

다음 디자인에 대한 인수인계 명세를 생성합니다: @$1

Figma URL이 제공되면 Figma에서 디자인을 불러옵니다. 그렇지 않으면 제공된 설명이나 스크린샷으로 작업합니다.

## 포함할 내용

### 시각 사양
- 정확한 측정값(패딩, 마진, 너비)
- 디자인 토큰 참조(색, 타이포그래피, 간격)
- 반응형 브레이크포인트와 동작
- 컴포넌트 변형과 상태

### 상호작용 사양
- 클릭/탭 동작
- 호버 상태
- 전환과 애니메이션(지속시간, easing)
- 제스처 지원(스와이프, 핀치, 롱프레스)

### 콘텐츠 사양
- 문자 제한
- 잘림 동작
- 빈 상태
- 로딩 상태
- 오류 상태

### 엣지 케이스
- 최소/최대 콘텐츠
- 국제화 텍스트(더 긴 문자열)
- 느린 연결
- 누락된 데이터

### 접근성
- 포커스 순서
- ARIA 레이블과 역할
- 키보드 상호작용
- 스크린 리더 알림

## 원칙

1. **추측하지 말기** - 명시되지 않으면 개발자가 추측하게 됩니다. 모든 것을 명시하세요.
2. **값이 아니라 토큰 사용** - `16px`보다 `spacing-md`를 참조하세요.
3. **모든 상태를 보여주기** - 기본, 호버, 활성, 비활성, 로딩, 오류, 빈 상태.
4. **이유 설명하기** - "이건 모바일에서 접히는데, 사용자가 주로 한 손으로 쓰기 때문입니다"는 개발자가 좋은 판단을 하게 돕습니다.

## 출력

```markdown
## Handoff Spec: [Feature/Screen Name]

### Overview
[이 화면/기능이 무엇을 하는지, 사용자 맥락]

### Layout
[그리드 시스템, 브레이크포인트, 반응형 동작]

### Design Tokens Used
| Token | Value | Usage |
|-------|-------|-------|
| `color-primary` | #[hex] | CTA 버튼, 링크 |
| `spacing-md` | [X]px | 섹션 사이 |
| `font-heading-lg` | [size/weight/family] | 페이지 제목 |

### Components
| Component | Variant | Props | Notes |
|-----------|---------|-------|-------|
| [Component] | [Variant] | [Props] | [Special behavior] |

### States and Interactions
| Element | State | Behavior |
|---------|-------|----------|
| [CTA Button] | Hover | [Background darken 10%] |
| [CTA Button] | Loading | [Spinner, disabled] |
| [Form] | Error | [Red border, error message below] |

### Responsive Behavior
| Breakpoint | Changes |
|------------|---------|
| Desktop (>1024px) | [Default layout] |
| Tablet (768-1024px) | [What changes] |
| Mobile (<768px) | [What changes] |

### Edge Cases
- **Empty state**: [데이터가 없을 때 보여줄 것]
- **Long text**: [잘림 규칙]
- **Loading**: [스켈레톤 또는 스피너]
- **Error**: [오류 상태 모양]

### Animation / Motion
| Element | Trigger | Animation | Duration | Easing |
|---------|---------|-----------|----------|--------|
| [Element] | [Trigger] | [Description] | [ms] | [easing] |

### Accessibility Notes
- [포커스 순서]
- [필요한 ARIA 레이블]
- [키보드 상호작용]
```

## 연결 도구가 있을 경우

**~~design tool**가 연결되어 있다면:
- Figma에서 정확한 측정값, 토큰, 컴포넌트 사양을 가져옵니다
- 자산을 내보내고 완전한 스펙 시트를 생성합니다

**~~project tracker**가 연결되어 있다면:
- 인수인계를 구현 티켓과 연결합니다
- 스펙의 각 섹션에 대한 하위 작업을 생성합니다

## 팁

1. **Figma 링크를 공유하세요** - 정확한 측정값, 토큰, 컴포넌트 정보를 가져올 수 있습니다.
2. **엣지 케이스를 언급하세요** - "100개 항목이면 어떻게 되나요?"가 경계 조건을 명세하는 데 도움이 됩니다.
3. **기술 스택을 알려 주세요** - "React + Tailwind를 사용합니다"라고 알려 주면 더 적절한 구현 노트를 드릴 수 있습니다.
