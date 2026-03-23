---
name: design-handoff
description: Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.
argument-hint: "<Figma URL or design description>"
---

# /design-handoff

> 낯선 플레이스홀더가 보이거나 연결된 도구를 확인해야 할 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참고하세요.

디자인에서 개발자 핸드오프 문서를 포괄적으로 생성합니다.

## 사용법

```
/design-handoff $ARGUMENTS
```

다음에 대한 핸드오프 명세서를 생성합니다: @$1

Figma URL이 제공된 경우 Figma에서 디자인을 가져옵니다. 그렇지 않으면 제공된 설명이나 스크린샷을 기반으로 작업합니다.

## 포함해야 할 항목

### 시각적 명세

- 정확한 측정값 (padding, margins, widths)
- 디자인 토큰 참조 (색상, 타이포그래피, 간격)
- 반응형 중단점 및 동작 방식
- 컴포넌트 변형 및 상태

### 인터랙션 명세

- 클릭/탭 동작
- 호버 상태
- 전환 및 애니메이션 (지속 시간, easing)
- 제스처 지원 (swipe, pinch, long-press)

### 콘텐츠 명세

- 글자 수 제한
- 텍스트 잘림 동작
- 빈 상태
- 로딩 상태
- 오류 상태

### 엣지 케이스

- 최소/최대 콘텐츠
- 국제화 텍스트 (긴 문자열)
- 느린 연결
- 누락된 데이터

### 접근성

- 포커스 순서
- ARIA 레이블 및 역할
- 키보드 인터랙션
- 스크린 리더 알림

## 원칙

1. **추측하지 않기** — 명시되지 않으면 개발자가 임의로 처리합니다. 모든 것을 명세화하세요.
2. **값이 아닌 토큰 사용** — `16px`이 아닌 `spacing-md`를 참조하세요.
3. **모든 상태 표시** — Default, hover, active, disabled, loading, error, empty.
4. **이유 설명** — "사용자가 주로 한 손을 사용하기 때문에 모바일에서 접힙니다"는 설명은 개발자가 올바른 판단을 내리는 데 도움이 됩니다.

## 출력

```markdown
## Handoff Spec: [기능/화면 이름]

### 개요
[이 화면/기능이 하는 일, 사용자 컨텍스트]

### 레이아웃
[그리드 시스템, 중단점, 반응형 동작]

### 사용된 디자인 토큰
| 토큰 | 값 | 사용처 |
|-------|-------|-------|
| `color-primary` | #[hex] | CTA 버튼, 링크 |
| `spacing-md` | [X]px | 섹션 사이 |
| `font-heading-lg` | [size/weight/family] | 페이지 제목 |

### 컴포넌트
| 컴포넌트 | 변형 | Props | 노트 |
|-----------|---------|-------|-------|
| [컴포넌트] | [변형] | [Props] | [특수 동작] |

### 상태 및 인터랙션
| 요소 | 상태 | 동작 |
|---------|-------|----------|
| [CTA Button] | Hover | [배경 10% 어둡게] |
| [CTA Button] | Loading | [스피너, 비활성화] |
| [Form] | Error | [빨간 테두리, 아래 오류 메시지] |

### 반응형 동작
| 중단점 | 변경 사항 |
|------------|---------|
| Desktop (>1024px) | [기본 레이아웃] |
| Tablet (768-1024px) | [변경 사항] |
| Mobile (<768px) | [변경 사항] |

### 엣지 케이스
- **빈 상태**: [데이터가 없을 때 표시할 내용]
- **긴 텍스트**: [텍스트 잘림 규칙]
- **로딩**: [스켈레톤 또는 스피너]
- **오류**: [오류 상태 모양]

### 애니메이션 / 모션
| 요소 | 트리거 | 애니메이션 | 지속 시간 | Easing |
|---------|---------|-----------|----------|--------|
| [요소] | [트리거] | [설명] | [ms] | [easing] |

### 접근성 노트
- [포커스 순서]
- [필요한 ARIA 레이블]
- [키보드 인터랙션]
```

## 커넥터를 사용할 수 있는 경우

**~~design tool**이 연결된 경우:
- Figma에서 정확한 측정값, 토큰, 컴포넌트 명세 가져오기
- 에셋 내보내기 및 전체 명세서 생성

**~~project tracker**가 연결된 경우:
- 핸드오프를 구현 티켓에 연결
- 명세서의 각 섹션에 대한 하위 작업 생성

## 팁

1. **Figma 링크 공유** — 정확한 측정값, 토큰, 컴포넌트 정보를 가져올 수 있습니다.
2. **엣지 케이스 언급** — "100개 항목이 있으면 어떻게 되나요?"는 경계 조건 명세에 도움이 됩니다.
3. **기술 스택 명시** — "React + Tailwind를 사용합니다"는 관련 구현 노트 제공에 도움이 됩니다.
