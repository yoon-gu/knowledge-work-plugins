---
name: design-critique
description: 사용성, 계층, 일관성에 대한 구조화된 디자인 피드백을 받습니다. "review this design", "critique this mockup", "what do you think of this screen?" 같은 표현이 나오거나, 탐색 단계부터 최종 다듬기까지 Figma 링크나 스크린샷을 공유해 피드백을 요청할 때 트리거됩니다.
argument-hint: "<Figma URL, screenshot, or description>"
---

# /design-critique

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

여러 차원에서 구조화된 디자인 피드백을 받습니다.

## 사용법

```
/design-critique $ARGUMENTS
```

디자인을 검토합니다: @$1

Figma URL이 제공되면 Figma에서 디자인을 불러옵니다. 파일이 참조되면 읽습니다. 그렇지 않으면 사용자가 디자인을 설명하거나 공유하도록 요청합니다.

## 필요한 것

- **디자인**: Figma URL, 스크린샷, 또는 자세한 설명
- **맥락**: 이게 무엇인가요? 누구를 위한 건가요? 어떤 단계인가요(탐색, 다듬기, 최종)?
- **집중 포인트**(선택): "모바일에 집중해 주세요" 또는 "온보딩 흐름에 집중해 주세요"

## 비평 프레임워크

### 1. 첫인상(2초)
- 가장 먼저 눈에 들어오는 것은 무엇인가요? 그게 맞나요?
- 감정적 반응은 어떤가요?
- 목적이 즉시 분명한가요?

### 2. 사용성
- 사용자가 목표를 달성할 수 있나요?
- 내비게이션은 직관적인가요?
- 상호작용 요소는 분명한가요?
- 불필요한 단계가 있나요?

### 3. 시각적 계층
- 명확한 읽기 순서가 있나요?
- 올바른 요소가 강조되나요?
- 여백이 효과적으로 사용되나요?
- 타이포그래피가 올바른 계층을 만들고 있나요?

### 4. 일관성
- 디자인 시스템을 따르나요?
- 간격, 색, 타이포그래피가 일관되나요?
- 유사한 요소가 유사하게 동작하나요?

### 5. 접근성
- 색 대비 비율
- 터치 타깃 크기
- 텍스트 가독성
- 이미지의 대체 텍스트

## 피드백 방법

- **구체적으로 말하기**: "레이아웃이 혼란스럽다"보다 "CTA가 내비게이션과 경쟁한다"가 좋습니다
- **이유 설명하기**: 피드백을 디자인 원칙이나 사용자 필요와 연결하세요
- **대안 제안하기**: 문제를 찾는 데서 멈추지 말고 해결책을 제안하세요
- **잘된 점 인정하기**: 좋은 피드백에는 긍정적 관찰도 포함됩니다
- **단계에 맞추기**: 초기 탐색과 최종 다듬기는 서로 다른 피드백이 필요합니다

## 출력

```markdown
## Design Critique: [Design Name]

### Overall Impression
[1-2문장 첫 반응 - 무엇이 잘 작동하는지, 가장 큰 기회는 무엇인지]

### Usability
| Finding | Severity | Recommendation |
|---------|----------|----------------|
| [Issue] | 🔴 Critical / 🟡 Moderate / 🟢 Minor | [Fix] |

### Visual Hierarchy
- **What draws the eye first**: [Element] — [이게 맞나요?]
- **Reading flow**: [시선이 레이아웃을 어떻게 이동하나요?]
- **Emphasis**: [올바른 것이 강조되고 있나요?]

### Consistency
| Element | Issue | Recommendation |
|---------|-------|----------------|
| [Typography/spacing/color] | [Inconsistency] | [Fix] |

### Accessibility
- **Color contrast**: [핵심 텍스트가 통과/실패하는지]
- **Touch targets**: [충분한 크기인가요?]
- **Text readability**: [폰트 크기, 줄 높이]

### What Works Well
- [긍정적 관찰 1]
- [긍정적 관찰 2]

### Priority Recommendations
1. **[가장 영향력 있는 변화]** — [이유와 방법]
2. **[두 번째 우선순위]** — [이유와 방법]
3. **[세 번째 우선순위]** — [이유와 방법]
```

## 연결 도구가 있을 경우

**~~design tool**가 연결되어 있다면:
- Figma에서 디자인을 직접 불러와 컴포넌트, 토큰, 레이어를 검사
- 기존 디자인 시스템과 일관성 비교

**~~user feedback**가 연결되어 있다면:
- 최근 사용자 피드백과 지원 티켓을 디자인 결정과 대조

## 팁

1. **맥락을 공유하세요** - "이건 B2B SaaS의 결제 흐름입니다"라고 알려 주면 더 관련성 높은 피드백을 드릴 수 있습니다.
2. **단계를 알려 주세요** - 초기 탐색과 최종 다듬기는 서로 다른 피드백이 필요합니다.
3. **집중할 부분을 지정하세요** - "내비게이션만 봐 주세요"라고 하면 한 영역을 더 깊게 볼 수 있습니다.
