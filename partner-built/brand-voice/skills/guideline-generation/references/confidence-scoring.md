# 신뢰도 점수 방법론

생성된 브랜드 가이드라인에 신뢰도 점수를 부여하고 해석하는 방법입니다.

## 점수 수준

### High Confidence
가이드라인 섹션이 충분한 근거를 갖고 있고 실행 가능합니다.

**기준(최소 3개 충족):**
- 3개 이상의 상호 검증 출처
- AUTHORITATIVE 출처 1개 이상에서 명시적 가이드 발견
- 문서 분석과 대화 분석 모두에서 일관됨
- 구체적이고 실행 가능한 지침(모호한 원칙만 있는 것이 아님)
- 해결되지 않은 충돌 없음

**예시:** 보이스 속성 "Confident but not arrogant"가 공식 스타일 가이드에 나오고, 이메일 템플릿에서 확인되며, 상위 성과자 통화 패턴과도 일치합니다.

### Medium Confidence
섹션은 타당하지만, 더 많은 데이터나 팀 확인이 있으면 좋습니다.

**기준(최소 2개 충족):**
- 1-2개의 상호 검증 출처
- 명시적 지침이 아니라 패턴에서 추론됨
- 최신성이나 권위로 해결된 작은 불일치
- 실행 가능하지만 해석이 조금 필요함
- 해결되지 않은 충돌이 1개 있을 수 있음

**예시:** 소셜 미디어 톤이 이메일 템플릿과 Slack 스레드 하나에서 추론되지만, 공식 소셜 미디어 가이드는 없습니다.

### Low Confidence
섹션은 최선의 추정입니다. 팀 검토를 강하게 권장합니다.

**기준(최소 2개 충족):**
- 단일 출처만 존재
- 간접 증거에서 주로 추론됨
- 상당한 해석이 필요함
- 출처 간 해결되지 않은 충돌
- 구체성 제한

**예시:** 경쟁 포지셔닝이 경쟁사가 언급된 단일 세일즈 통화에서만 도출되었고, 이를 뒷받침하는 문서가 없습니다.

## 섹션별 점수 가이드

### Voice Attributes
- **High**: 속성이 공식 브랜드 가이드에 있고 템플릿이나 통화에서도 확인됩니다
- **Medium**: 속성이 한 가지 문서 유형에서만 보이거나, 여러 대화에서 추론됩니다
- **Low**: 단일 출처 또는 간접 증거에서 추론됩니다

### Messaging Framework
- **High**: 가치 제안이 공식 자료에 문서화되어 있고 세일즈 대화에서도 일관되게 사용됩니다
- **Medium**: 문서화되어 있지만 실무에서는 보이지 않거나, 반대로 실무에서는 보이지만 문서화되지 않았습니다
- **Low**: 단일 피치 덱이나 단일 통화에서만 추출되었습니다

### Tone Matrix
- **High**: 해당 맥락에 대한 명시적 톤 가이드가 있고 관찰된 행동과도 맞습니다
- **Medium**: 해당 맥락의 콘텐츠 예시 3개 이상에서 톤이 추론됩니다
- **Low**: 1-2개 예시에서 추론되거나, 비슷한 맥락에서 외삽되었습니다

### Terminology
- **High**: 스타일 가이드나 용어집에 명시적으로 나와 있습니다
- **Medium**: 템플릿과 통화에서 일관되게 쓰입니다(패턴 기반)
- **Low**: 단일 문서에서 관찰되거나 브랜드 성격에서 추론됩니다

### Language Patterns (from transcripts)
- **High**: 여러 화자의 5회 이상 통화에서 패턴이 관찰됩니다
- **Medium**: 3-4회 통화에서, 또는 단일 상위 성과자에게서 패턴이 관찰됩니다
- **Low**: 1-2회 통화에서만 패턴이 관찰됩니다

### Transcript-Primary Scenarios

가이드라인이 주로 대화형 출처에서 생성되었고(AUTHORITATIVE 문서가 없는 경우):
- 5개 이상의 전사에서 도출된 Voice Attributes = **Medium**(Low 아님)
- 5회 이상 통화에서 일관된 패턴으로 도출된 Messaging Framework = **Medium**
- Language Patterns 가중치는 종합 계산에서 10%에서 20%로 증가합니다(Voice Attributes에서 10%를 뺍니다)

이를 가이드라인 메타데이터에 다음과 같이 적습니다: "Guidelines generated primarily from conversational sources — team review recommended to formalize."

## 종합 신뢰도

전체 가이드라인 신뢰도는 섹션 점수의 가중 평균으로 계산합니다.

| Section | Weight |
|---------|--------|
| Voice Attributes | 30% |
| Messaging Framework | 25% |
| Tone Matrix | 20% |
| Terminology | 15% |
| Language Patterns | 10% |

점수 변환: High = 1.0, Medium = 0.6, Low = 0.3

**예시:**
- Voice Attributes: High (1.0 x 0.30 = 0.30)
- Messaging: Medium (0.6 x 0.25 = 0.15)
- Tone: Medium (0.6 x 0.20 = 0.12)
- Terminology: High (1.0 x 0.15 = 0.15)
- Language: Low (0.3 x 0.10 = 0.03)
- **전체: 0.75 = Medium-High confidence**

**종합 점수 기준:**
- 0.85–1.0 = High
- 0.60–0.84 = Medium
- 0.60 미만 = Low

## 표시 방식

각 섹션 헤더 옆에 신뢰도를 표시합니다.

```markdown
## Voice Attributes (Confidence: High)
[content]

## Tone Matrix (Confidence: Medium)
[content — note: no official social media guidelines found, tone inferred from email patterns]
```

Medium과 Low 섹션에는 신뢰도가 제한적인 이유와 무엇이 신뢰도를 높일지 간단히 적습니다.

## 열린 질문과의 관계

Low confidence 섹션은 대응하는 열린 질문을 만들어야 합니다.

- **Low confidence + conflict** = High Priority 열린 질문
- **Low confidence + gap** = Medium Priority 열린 질문
- **Medium confidence + minor inconsistency** = Low Priority 열린 질문

모든 열린 질문에는 권고가 포함되어야 하며, 그 권고가 확인되면 해당 섹션의 신뢰도 점수가 올라가야 합니다.
