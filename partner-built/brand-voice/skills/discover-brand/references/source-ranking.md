# 출처 순위 알고리즘

발견된 브랜드 출처를 분류, 순위화, 우선순위화하는 방법입니다.

## 출처 범주

### AUTHORITATIVE
공식 승인된 브랜드 문서입니다. 신뢰도가 가장 높습니다.

**신호:**
- Published style guides or brand books
- C-suite or marketing leadership authored/approved
- Lives in an official "Brand" folder or Confluence space
- Has version numbers or approval dates
- Referenced by other documents as "the brand guide"

**예시:**
- "Acme Corp Brand Guidelines v3.2.pdf"
- "Official Style Guide" page in Confluence Marketing space
- Brand book in Google Drive with company-wide sharing
- Brand book in Box with company-wide sharing
- Official Style Guide in SharePoint Marketing site

**신뢰 가중치:** 1.0(기준값)

### OPERATIONAL
브랜드가 실제로 어떻게 적용되는지 보여 줍니다. 가이드라인이 실제 콘텐츠에서 어떻게 나타나는지 확인할 수 있습니다.

**신호:**
- Templates actively used by teams
- Sales playbooks with messaging guidance
- Email sequences with established tone
- Presentation templates with brand messaging

**예시:**
- "Cold Email Templates Q4 2024"
- "Enterprise Sales Playbook"
- "Customer Success Response Templates"
- Pitch deck templates in Google Slides
- Email templates in Outlook
- Sales playbook on SharePoint

**신뢰 가중치:** 0.8

### CONVERSATIONAL
실제 커뮤니케이션에서 드러나는 암묵적 브랜드 보이스입니다.

**신호:**
- Sales call transcripts (especially successful ones)
- Meeting notes with customer-facing language
- Internal discussions about positioning
- Slack threads discussing brand decisions

**예시:**
- Gong recordings of top performer calls
- Meeting notes from brand strategy sessions
- Customer success call transcripts
- Slack #brand channel discussions about tone

**신뢰 가중치:** 0.6(패턴 파악에는 유용하지만 규범적이지는 않음)

### CONTEXTUAL
브랜드를 이해하는 데 참고가 되지만 직접 정의하지는 않는 배경 정보입니다.

**신호:**
- Design files without explicit brand guidelines
- Competitor analysis documents
- Industry reports
- Product documentation

**예시:**
- Figma component library (visual only)
- "Competitive Landscape Q3 2024"
- Product feature specifications

**신뢰 가중치:** 0.3

### STALE
더 새로운 버전에 의해 대체된 오래된 콘텐츠입니다.

**신호:**
- Older version when a newer version exists
- Pre-rebrand materials after a rebrand
- Documents explicitly marked as deprecated
- Content more than 2 years old without updates

**예시:**
- "Brand Guidelines v1.0" when v3.2 exists
- "2022 Style Guide" when "2024 Brand Update" exists
- Documents in an "Archive" or "Deprecated" folder

**신뢰 가중치:** 0.1(검토 표시만 하고 의존하지 않음)

## 순위 알고리즘

Apply these five ranking factors in order of priority:

### 1. Recency (Weight: 30%)

More recent sources are more likely to reflect current brand voice.

- **Score 1.0**: Updated within last 6 months
- **Score 0.7**: Updated within last year
- **Score 0.4**: Updated within last 2 years
- **Score 0.1**: Older than 2 years

When two sources conflict, the more recent one wins unless the older source is explicitly marked as the "official" guide.

Always prefer the most recent version of any document. When multiple sources cover the same topic, weight the newest one heavily. Flag any non-AUTHORITATIVE source older than 12 months in the discovery report.

### Recency Cutoffs

In addition to soft recency scoring, apply hard cutoffs to prevent stale content from polluting discovery:

**AUTHORITATIVE sources**: No hard cutoff. Official brand guides remain valid regardless of age unless explicitly superseded by a newer version.

**OPERATIONAL, CONVERSATIONAL, CONTEXTUAL sources**: Exclude from deep fetch if older than 12 months, with one exception: if zero sources in a category fall within the 12-month window, include the single most recent source from that category and flag it as potentially stale.

**STALE sources**: Exclude entirely from deep fetch. Include in the discovery report for reference only.

These cutoffs apply at the deep-fetch stage (Phase 3). All sources are still collected during broad discovery (Phase 1) and triage (Phase 2) — the cutoffs filter what gets fully retrieved and analyzed.

### 2. Explicitness (Weight: 25%)

Sources that explicitly define brand voice outrank those that merely demonstrate it.

- **Score 1.0**: Explicit brand instructions ("Our voice is...")
- **Score 0.7**: Documented tone guidelines ("Emails should be...")
- **Score 0.4**: Implicit patterns in templates or examples
- **Score 0.2**: Inferred from conversational patterns

### 3. Authority (Weight: 20%)

Higher organizational authority indicates more trustworthy brand definitions.

- **Score 1.0**: Official brand team or C-suite authored
- **Score 0.7**: Marketing leadership authored
- **Score 0.4**: Team leads or senior ICs
- **Score 0.2**: Individual contributor or unknown author

### 4. Specificity (Weight: 15%)

Detailed, actionable guidance outranks vague principles.

- **Score 1.0**: Specific rules with examples ("Use 'platform' not 'tool'")
- **Score 0.7**: Detailed guidelines ("Tone should be warm but professional")
- **Score 0.4**: General principles ("Be authentic")
- **Score 0.2**: Abstract values only ("We believe in innovation")

### 5. 출처 간 일관성(가중치: 10%)

여러 출처에서 확인되는 요소가 더 높은 순위를 얻습니다.

- **Score 1.0**: Appears in 3+ independent sources
- **Score 0.7**: Appears in 2 independent sources
- **Score 0.4**: Appears in 1 source only
- **Score 0.1**: Contradicted by another source

## 종합 점수 계산

```
final_score = (recency × 0.30) + (explicitness × 0.25) + (authority × 0.20)
            + (specificity × 0.15) + (consistency × 0.10)
```

범주 신뢰 가중치를 곱합니다.
```
ranked_score = final_score × category_trust_weight
```

### 점수 예시

**Source: "Brand Voice Guidelines v3.2" (Confluence, updated 3 months ago)**
- Recency: 1.0 (3 months old)
- Explicitness: 1.0 (explicit brand instructions)
- Authority: 1.0 (marketing VP authored)
- Specificity: 0.7 (good guidelines, some gaps)
- Consistency: 0.7 (corroborated by email templates)
- Category: AUTHORITATIVE (1.0)
- **Final: (1.0×0.30 + 1.0×0.25 + 1.0×0.20 + 0.7×0.15 + 0.7×0.10) × 1.0 = 0.925**

**Source: "Top Performer Call — Enterprise Close" (Gong, 2 months ago)**
- Recency: 1.0
- Explicitness: 0.2 (implicit patterns only)
- Authority: 0.4 (senior AE)
- Specificity: 0.7 (specific phrases used)
- Consistency: 0.4 (single source)
- Category: CONVERSATIONAL (0.6)
- **Final: (1.0×0.30 + 0.2×0.25 + 0.4×0.20 + 0.7×0.15 + 0.4×0.10) × 0.6 = 0.345**

## 적응형 점수: AUTHORITATIVE 출처가 없을 때

탐색에서 **AUTHORITATIVE 출처가 0개**라면, 대화형 및 운영성 출처가 주요 브랜드 근거라는 점을 반영하도록 점수 알고리즘을 조정합니다.

### 조정된 신뢰 가중치(AUTHORITATIVE 없음)

| Category | Default Weight | Adapted Weight | Rationale |
|----------|---------------|----------------|-----------|
| AUTHORITATIVE | 1.0 | 1.0 | (n/a — none found) |
| OPERATIONAL | 0.8 | 0.9 | 템플릿이 주요 명시적 근거가 됩니다 |
| CONVERSATIONAL | 0.6 | 0.85 | 전사 기록은 브랜드가 실제로 어떻게 말하는지 보여 주는 가장 좋은 신호입니다 |
| CONTEXTUAL | 0.3 | 0.4 | 정식 문서가 없을 때는 디자인과 경쟁 맥락이 더 중요합니다 |
| STALE | 0.1 | 0.2 | 현재 자료가 없을 때는 오래된 문서도 더 의미가 있습니다 |

### 조정된 명시성 점수(AUTHORITATIVE 없음)

권위 있는 출처가 없을 때는 대화 패턴이 더 규범적 가중치를 가집니다.

- **Score 0.2 → 0.5**: "Inferred from conversational patterns" — these ARE the brand evidence now
- **Score 0.4 → 0.6**: "Implicit patterns in templates or examples"
- Other explicitness scores unchanged

### 예시: 조정된 전사 기록 점수화

**Source: "Top Performer Call — Enterprise Close" (Gong, 2 months ago)**
- Recency: 1.0
- Explicitness: 0.5 (adapted from 0.2 — patterns are primary evidence)
- Authority: 0.4 (senior AE)
- Specificity: 0.7 (specific phrases used)
- Consistency: 0.4 (single source)
- Category: CONVERSATIONAL (0.85 adapted)
- **Adapted score: (1.0×0.30 + 0.5×0.25 + 0.4×0.20 + 0.7×0.15 + 0.4×0.10) × 0.85 = 0.552**

이렇게 하면 전사 기록이 0.5 심층 조회 기준을 충분히 넘어서, 대화형 출처가 가이드라인 생성에 의미 있게 기여하게 됩니다.

### 적용 시점

적응형 점수는 다음 경우에 적용합니다.
- Phase 2 triage produces zero AUTHORITATIVE sources
- 탐색 보고서에 다음 문구를 표시합니다: "No formal brand guidelines found — scoring adapted to weight conversational and operational sources higher"

## 선별 의사결정 기준

### 심층 조회에 포함(상위 5-15개 출처)
- Ranked score > 0.5
- All AUTHORITATIVE sources regardless of score
- At least one source per category if available (this overrides the score threshold)
- At least one source per platform if available

### 검토 표시
- Sources with conflicting information
- STALE sources that may still be referenced by teams
- Sources with high specificity but low authority

### 제외
- Ranked score < 0.1
- Clearly irrelevant results (e.g., "brand" used in product name, not brand guidelines)
- Duplicate content already captured from another platform
