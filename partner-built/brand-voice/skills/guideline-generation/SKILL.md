---
name: guideline-generation
description: >
  이 스킬은 원천 자료로부터 브랜드 보이스 가이드를 생성, 작성, 구축합니다.
  사용자가 "brand guidelines 생성", "style guide 만들기", "brand voice 추출",
  "통화에서 가이드 만들기", "brand materials 통합", "세일즈 통화를 분석해 brand voice 파악",
  "문서로 brand playbook 만들기", "voice and tone guide 종합"을 요청하거나,
  브랜드 분석을 위해 브랜드 문서, 전사 기록, 회의 녹음을 업로드할 때 사용합니다.
  탐색 보고서를 받아 실행 가능한 가이드라인으로 바꾸고 싶을 때도 트리거됩니다.
---

# 가이드라인 생성

브랜드 문서, 세일즈 통화 전사, 탐색 보고서, 직접 입력 등 어떤 조합이든 활용해
LLM 친화적인 포괄적 브랜드 보이스 가이드라인을 생성합니다. 원재료를 구조화되고
실행 가능한 가이드라인으로 바꾸며, 신뢰도 점수와 열린 질문을 포함합니다.

## 입력

다음 조합을 자유롭게 받습니다.
- **Discovery report** from the discover-brand skill (structured, pre-triaged)
- **Brand documents** uploaded or from connected platforms (PDF, PPTX, DOCX, MD, TXT)
- **Conversation transcripts** from Gong, Granola, manual uploads, or Notion meeting notes
- **Direct user input** about their brand voice and values

탐색 보고서가 제공되면 그것을 주요 입력으로 사용합니다. 출처는 이미 선별되고 순위화되어 있습니다. 필요하면 추가 분석으로 보완합니다.

## 생성 워크플로

### 1. 출처 식별 및 분류

사용자가 무엇을 제공했는지 판단합니다. 출처가 없다면:
- Check if a discovery report exists from a previous `/brand-voice:discover-brand` run
- Check `.claude/brand-voice.local.md` for known brand material locations
- Suggest running discovery first: `/brand-voice:discover-brand`

### 2. 출처 처리

**문서의 경우:** 무거운 파싱은 document-analysis 에이전트에 위임합니다. 보이스 속성, 메시지 주제, 용어, 톤 가이드, 예시를 추출합니다.

**전사의 경우:** 패턴 인식은 conversation-analysis 에이전트에 위임합니다. 암묵적 보이스 속성, 성공적인 언어 패턴, 맥락별 톤, 안티 패턴을 추출합니다.

**탐색 보고서의 경우:** 이미 선별된 출처, 충돌, 공백을 추출합니다. 순위화된 출처를 그대로 사용합니다.

### 3. 가이드라인으로 종합

모든 결과를 `references/guideline-template.md`의 템플릿에 따라 하나의 가이드 문서로 통합합니다. 핵심 섹션은 다음과 같습니다.

**"We Are / We Are Not" 표** — 브랜드 정체성의 핵심 기준점입니다.

| We Are | We Are Not |
|--------|------------|
| [Attribute — e.g., "Confident"] | [Counter — e.g., "Arrogant"] |
| [Attribute — e.g., "Approachable"] | [Counter — e.g., "Casual or sloppy"] |

Derive attributes from the most consistent patterns across sources. Each row should have supporting evidence.

**Voice Constants vs. Tone Flexes** — 무엇이 고정되고 무엇이 조정되는지 명확히 합니다.
- **Voice** = 성격, 가치, "We Are / We Are Not" — 모든 콘텐츠에서 고정
- **Tone** = 격식, 에너지, 기술적 깊이 — 맥락에 따라 유연하게 조정

**맥락별 톤 매트릭스:**

| Context | Formality | Energy | Technical Depth | Example |
|---------|-----------|--------|-----------------|---------|
| Cold outreach | Medium | High | Low | "[example phrase]" |
| Enterprise proposal | High | Medium | High | "[example phrase]" |
| Social media | Low | High | Low | "[example phrase]" |

### 4. 신뢰도 점수 부여

`references/confidence-scoring.md`의 방법론을 사용해 각 섹션에 점수를 부여합니다.
- **High confidence**: 3+ corroborating sources, explicit guidance found
- **Medium confidence**: 1-2 sources, or inferred from patterns
- **Low confidence**: Single source, inferred, or conflicting data

### 5. 열린 질문 표시

해결할 수 없는 모호성에 대해서는 열린 질문을 생성합니다.

```markdown
## Open Questions for Team Discussion

### High Priority (blocks guideline completion)
1. **[Question Title]**
   - What was found: [conflicting or incomplete info]
   - Agent recommendation: [suggested resolution with reasoning]
   - Need from you: [specific decision or confirmation needed]
```

모든 열린 질문에는 반드시 에이전트 권고가 들어가야 합니다. 모호함을 "확인하거나 변경"할 수 있는 형태로 바꾸고, 막다른 길로 두지 마세요.

### 6. 품질 점검

보여 주기 전에 `agents/quality-assurance.md`에 정의된 quality-assurance 에이전트로 검증합니다.
- All major sections populated (including Brand Personality and Content Examples if sources support them)
- At least 3 voice attributes with evidence
- "We Are / We Are Not" table has 4+ rows
- Tone matrix covers at least 3 contexts
- Confidence scores assigned per section
- Source attribution for all extracted elements
- No PII exposed
- Open questions include recommendations

### 7. 제시 및 다음 단계 제안

핵심 발견을 요약합니다.
- Total sections generated with confidence breakdown
- Strongest voice attribute and most effective message
- Number of open questions (if any)

### 8. 이후 세션을 위한 저장

기본 저장 위치는 사용자의 작업 폴더 안 `.claude/brand-voice-guidelines.md`입니다.

**중요:** 에이전트의 작업 디렉터리는 사용자의 프로젝트 루트가 아닐 수 있습니다(특히 Cowork에서는 플러그인이 캐시 디렉터리에서 실행됩니다). 현재 작업 디렉터리가 아니라 사용자의 작업 폴더를 기준으로 경로를 해석하세요. 작업 폴더가 설정되지 않았다면 파일 저장을 건너뛰고, 가이드는 이 대화에서만 사용할 수 있다고 알려 주세요.

1. **저장 경로를 확인합니다.** 파일은 반드시 사용자의 작업 폴더 안 `.claude/brand-voice-guidelines.md`에 저장해야 합니다. 쓰기 전에 작업 폴더 경로를 확인하세요.
2. **해당 경로에 기존 가이드가 있는지 확인합니다**
3. **있다면 이전 버전을 보관합니다.** 같은 디렉터리에서 기존 파일 이름을 `brand-voice-guidelines-YYYY-MM-DD.md`로 바꿉니다(오늘 날짜 사용)
4. **새 가이드를 저장합니다** 작업 폴더의 `.claude/brand-voice-guidelines.md`에 저장합니다
5. **사용자에게 확인합니다** 전체 절대 경로와 함께: "Guidelines saved to `<full-path>`. `/brand-voice:enforce-voice` will find them automatically in future sessions."

The guidelines are also present in this conversation, so `/brand-voice:enforce-voice` can use them immediately without loading from file.

After saving, offer:
1. Walk through the guidelines section by section
2. Start creating content with `/brand-voice:enforce-voice`
3. Resolve open questions

## 개인정보 및 보안

이 개인정보 제약은 출력 시점뿐 아니라 전체 생성 워크플로 내내 적용합니다.
- Redact customer names and contact information from all examples
- Anonymize company names in transcript excerpts if requested
- Flag any sensitive information detected during processing

## 참고 파일

- **`references/guideline-template.md`** — 모든 섹션, 필드 정의, 서식 안내가 포함된 완전한 출력 템플릿
- **`references/confidence-scoring.md`** — 신뢰도 점수 방법론, 기준점, 예시
