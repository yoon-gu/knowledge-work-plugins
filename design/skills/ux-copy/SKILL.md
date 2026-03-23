---
name: ux-copy
description: Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this error message", or when naming a CTA, wording a confirmation dialog, filling an empty state, or writing onboarding text.
argument-hint: "<context or copy to review>"
---

# /ux-copy

> 낯선 플레이스홀더가 보이거나 연결된 도구를 확인해야 할 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참고하세요.

모든 인터페이스 컨텍스트에 맞는 UX 카피를 작성하거나 검토합니다.

## 사용법

```
/ux-copy $ARGUMENTS
```

## 필요한 정보

- **컨텍스트**: 어떤 화면, 플로우, 또는 기능인가요?
- **사용자 상태**: 사용자가 무엇을 하려고 하나요? 어떤 감정 상태인가요?
- **톤**: 격식적, 친근한, 유쾌한, 안심시키는?
- **제약 조건**: 글자 수 제한, 플랫폼 가이드라인?

## 원칙

1. **명확하게**: 정확히 말하고자 하는 바를 표현합니다. 전문 용어나 모호함이 없어야 합니다.
2. **간결하게**: 완전한 의미를 전달하는 최소한의 단어를 사용합니다.
3. **일관되게**: 같은 것에는 항상 같은 용어를 사용합니다.
4. **유용하게**: 모든 단어가 사용자의 목표 달성을 도와야 합니다.
5. **인간적으로**: 로봇이 아닌 도움이 되는 사람처럼 씁니다.

## 카피 패턴

### CTAs
- 동사로 시작: "Start free trial", "Save changes", "Download report"
- 구체적으로: "Submit"이 아닌 "Create account"
- 레이블과 결과를 일치시키기

### 오류 메시지
구조: 무슨 일이 있었는지 + 이유 + 해결 방법
- "Payment declined. Your card was declined by your bank. Try a different card or contact your bank."

### 빈 상태
구조: 이것이 무엇인지 + 왜 비어 있는지 + 어떻게 시작하는지
- "No projects yet. Create your first project to start collaborating with your team."

### 확인 대화상자
- 행동을 명확하게: "Are you sure?"가 아닌 "Delete 3 files?"
- 결과를 설명: "This can't be undone"
- 버튼에 동작 명시: "OK" / "Cancel"이 아닌 "Delete files" / "Keep files"

### 툴팁
- 간결하고, 도움이 되며, 명백한 것을 반복하지 않음

### 로딩 상태
- 기대치 설정, 불안감 감소

### 온보딩
- 점진적 공개, 한 번에 하나의 개념

## 보이스와 톤

컨텍스트에 맞게 톤 조정:
- **성공**: 축하하되 과하지 않게
- **오류**: 공감적이고 도움이 되게
- **경고**: 명확하고 실행 가능하게
- **중립**: 정보 제공적이고 간결하게

## 출력

```markdown
## UX Copy: [컨텍스트]

### 권장 카피
**[요소]**: [카피]

### 대안
| 옵션 | 카피 | 톤 | 최적 사용 시기 |
|--------|------|------|----------|
| A | [카피] | [톤] | [사용 시기] |
| B | [카피] | [톤] | [사용 시기] |
| C | [카피] | [톤] | [사용 시기] |

### 근거
[이 카피가 효과적인 이유 — 사용자 컨텍스트, 명확성, 행동 지향성]

### 현지화 노트
[번역자가 알아야 할 사항 — 피해야 할 관용구, 글자 수 확장, 문화적 맥락]
```

## 커넥터를 사용할 수 있는 경우

**~~knowledge base**가 연결된 경우:
- 브랜드 보이스 가이드라인 및 콘텐츠 스타일 가이드 가져오기
- 기존 카피 패턴 및 용어 표준 확인

**~~design tool**이 연결된 경우:
- Figma에서 전체 사용자 플로우 맥락의 화면 확인
- 디자인에서 글자 수 제한 및 레이아웃 제약 조건 확인

## 팁

1. **컨텍스트를 구체적으로 설명하세요** — "오류 메시지"보다 "결제 실패 시 오류 메시지"가 더 좋습니다.
2. **브랜드 보이스를 공유하세요** — "우리는 전문적이지만 따뜻합니다"라는 정보가 톤을 맞추는 데 도움이 됩니다.
3. **사용자의 감정 상태를 고려하세요** — 오류 메시지에는 공감이 필요합니다. 성공 메시지는 축하할 수 있습니다.
