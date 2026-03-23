---
name: brand-voice-enforcement
description: >
  이 스킬은 브랜드 가이드라인을 콘텐츠 제작에 적용합니다. 사용자가 "이메일 작성",
  "제안서 초안", "피치 덱 만들기", "LinkedIn 글쓰기", "발표자료 초안",
  "Slack 메시지 작성", "세일즈 콘텐츠 초안"처럼 브랜드 보이스를 적용해야 하는
  콘텐츠 제작 요청을 할 때 사용합니다. "on-brand", "brand voice", "enforce voice",
  "apply brand guidelines", "brand-aligned content", "write in our voice",
  "use our brand tone", "make this sound like us", "rewrite this in our tone",
  "this doesn't sound on-brand" 같은 표현에서도 트리거됩니다. 가이드를 처음부터
  만드는 용도는 아닙니다(`guideline-generation` 사용). 브랜드 자료를 찾는 용도도 아닙니다
  (`discover-brand` 사용).
---

# 브랜드 보이스 적용

기존 브랜드 가이드라인을 모든 세일즈 및 마케팅 콘텐츠 생성에 적용합니다.
사용자의 브랜드 가이드를 불러오고, 요청에 보이스 상수와 톤 유연성을 적용하고,
출력을 검증한 뒤 브랜드 선택을 설명합니다.

## 브랜드 가이드 로드

다음 순서로 사용자의 브랜드 가이드를 찾습니다. 찾는 즉시 중단합니다.

1. **세션 컨텍스트** — 이 세션에서 이미 브랜드 가이드라인이 생성되었는지(`/brand-voice:generate-guidelines`를 통해) 확인합니다. 있다면 대화에 이미 포함된 것이므로 그대로 사용합니다. 세션에서 생성된 가이드는 가장 최신이고 사용자의 최근 의도를 반영합니다.

2. **로컬 가이드 파일** — 사용자의 작업 폴더 안에 `.claude/brand-voice-guidelines.md`가 있는지 확인합니다. 에이전트의 현재 작업 디렉터리를 기준으로 한 상대 경로는 사용하지 마세요. Cowork에서는 에이전트가 사용자 프로젝트가 아닌 플러그인 캐시 디렉터리에서 실행됩니다. 경로는 사용자의 작업 폴더를 기준으로 해석하세요. 작업 폴더가 설정되지 않았다면 이 단계는 건너뜁니다.

3. **사용자에게 묻기** — 위 단계에서 가이드를 찾지 못하면 사용자에게 다음과 같이 말합니다.
   "I couldn't find your brand guidelines. You can:
   - Run `/brand-voice:discover-brand` to find brand materials across your platforms
   - Run `/brand-voice:generate-guidelines` to create guidelines from documents or transcripts
   - Paste guidelines directly into this chat or point me to a file"

   사용자가 가이드를 제공할 때까지 기다립니다.

또한 시행 설정을 위해 `.claude/brand-voice.local.md`도 읽습니다(가이드가 다른 출처에서 왔더라도).
- `strictness`: strict | balanced | flexible
- `always-explain`: whether to always explain brand choices

## 적용 워크플로

### 1. 콘텐츠 요청 분석

Before writing, identify:
- **Content type**: email, presentation, proposal, social post, message, etc.
- **Target audience**: role, seniority, industry, company stage
- **Key messages needed**: which message pillars apply
- **Specific requirements**: length, format, tone overrides

### 2. 보이스 상수 적용

Voice is the brand's personality — it stays constant across all content:
- 가이드라인의 "We Are / We Are Not" 속성을 적용합니다
- 브랜드 성격을 일관되게 사용합니다
- 승인된 용어를 반영하고 금지 용어는 배제합니다
- 메시지 프레임워크와 가치 제안을 따릅니다

`references/voice-constant-tone-flexes.md`의 "보이스는 고정, 톤은 유연" 모델을 참고하세요.

### 3. 맥락에 맞게 톤 조정

톤은 콘텐츠 유형과 대상에 따라 달라집니다. 가이드라인의 맥락별 톤 매트릭스를 사용해 다음을 정합니다.
- **Formality**: How formal or casual should this be?
- **Energy**: How much urgency or enthusiasm?
- **Technical depth**: How detailed or accessible?

### 4. 콘텐츠 생성

Create content that:
- 전체적으로 브랜드 보이스 속성과 일치합니다
- 해당 콘텐츠 유형의 톤 가이드라인을 따릅니다
- 핵심 메시지를 자연스럽게 녹입니다
- 선호 용어를 사용합니다
- 가이드라인 예시의 품질과 스타일을 반영합니다

복잡하거나 장문의 콘텐츠는 `agents/content-generation.md`에 정의된 content-generation 에이전트에 위임합니다.
중요도가 높은 콘텐츠는 `agents/quality-assurance.md`에 정의된 quality-assurance 에이전트에 검증을 맡깁니다.

### 5. 검증 및 설명

콘텐츠를 생성한 뒤에는 다음을 수행합니다.
- 어떤 브랜드 가이드라인을 적용했는지 간단히 짚습니다
- 핵심 보이스와 톤 결정 사항을 설명합니다
- 맥락에 맞게 가이드라인을 조정한 부분이 있으면 밝힙니다
- 피드백에 따라 다듬을 수 있다고 제안합니다

설정에서 `always-explain`이 true이면, 모든 응답에 브랜드 적용 노트를 포함합니다.

## 충돌 처리

사용자 요청이 브랜드 가이드라인과 충돌하면 다음 순서로 처리합니다.
1. Explain the conflict clearly
2. Provide a recommendation
3. Offer options: follow guidelines strictly, adapt for context, or override

기본값은 가이드라인을 맥락에 맞게 조정하되, 트레이드오프를 설명하는 것입니다.

## 열린 질문 인식

열린 질문은 가이드라인 생성 중에 표시된, 아직 해결되지 않은 브랜드 포지셔닝 결정입니다. 이는 가이드라인의 "Open Questions" 섹션에 저장됩니다. 콘텐츠를 생성할 때 브랜드 가이드라인에 열린 질문이 있는지 확인합니다.
- If content touches an unresolved open question, note it
- Apply the agent's recommendation from the open question unless the user specifies otherwise
- Suggest resolving the question if it significantly impacts the content

## 참고 파일

- **`references/voice-constant-tone-flexes.md`** — "보이스는 고정, 톤은 유연" 사고모델, "We Are / We Are Not" 표 구조, 맥락별 톤 매트릭스 설명
- **`references/before-after-examples.md`** — 콘텐츠 유형별 before/after 예시로, 적용이 실제로 어떻게 작동하는지 보여 줍니다
