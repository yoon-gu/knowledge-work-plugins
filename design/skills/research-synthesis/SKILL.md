---
name: research-synthesis
description: 사용자 리서치를 주제, 인사이트, 추천 사항으로 종합합니다. 인터뷰 녹취록, 설문 결과, 사용성 테스트 노트, 지원 티켓, NPS 응답을 패턴, 사용자 세그먼트, 우선순위가 정해진 다음 단계로 정리해야 할 때 사용하세요.
argument-hint: "<리서치 데이터, 녹취록, 또는 설문 결과>"
---

# /research-synthesis

> 낯선 플레이스홀더가 보이거나 연결된 도구를 확인해야 한다면 [CONNECTORS.md](../../CONNECTORS.md)를 참고하세요.

사용자 리서치 데이터를 실행 가능한 인사이트로 종합합니다. 리서치 방법, 인터뷰 가이드, 분석 프레임워크는 **user-research** 스킬을 참고하세요.

## Usage

```
/research-synthesis $ARGUMENTS
```

## 입력 가능 항목

- 인터뷰 녹취록 또는 노트
- 설문 결과(CSV, 붙여넣은 데이터)
- 사용성 테스트 녹화본 또는 노트
- 지원 티켓 또는 피드백
- NPS/CSAT 응답
- 앱 스토어 리뷰

## Output

```markdown
## Research Synthesis: [Study Name]
**Method:** [Interviews / Survey / Usability Test] | **Participants:** [X]
**Date:** [Date range] | **Researcher:** [Name]

### 핵심 요약
[핵심 발견에 대한 3-4문장 개요]

### Key Themes

#### Theme 1: [Name]
**빈도:** [전체 참가자 Y명 중 X명]
**요약:** [이 주제가 무엇을 의미하는지]
**근거:**
- "[Quote]" — P[X]
- "[Quote]" — P[X]
**시사점:** [이것이 제품에 의미하는 바]

#### Theme 2: [Name]
[동일한 형식]

### Insights → Opportunities

| Insight | Opportunity | Impact | Effort |
|---------|-------------|--------|--------|
| [우리가 배운 점] | [우리가 할 수 있는 일] | 높음/중간/낮음 | 높음/중간/낮음 |

### User Segments Identified
| Segment | Characteristics | Needs | Size |
|---------|----------------|-------|------|
| [이름] | [설명] | [핵심 니즈] | [대략적인 %] |

### Recommendations
1. **[높은 우선순위]** — [어떤 발견을 근거로 하는지, 왜 필요한지]
2. **[중간 우선순위]** — [이유]
3. **[낮은 우선순위]** — [이유]

### Questions for Further Research
- [아직 알지 못하는 것]

### Methodology Notes
[리서치를 어떻게 수행했는지, 적어둘 제한점이나 편향]
```

## 연결 도구가 있는 경우

**~~user feedback**가 연결되어 있으면:
- 지원 티켓, 기능 요청, NPS 응답을 가져와 리서치 데이터를 보완합니다
- 실제 사용자 불만과 요청을 주제별로 교차 검증합니다

**~~product analytics**가 연결되어 있으면:
- 사용 데이터와 행동 지표로 정성적 발견을 검증합니다
- 확인된 문제의 영향을 수치화합니다

**~~knowledge base**가 연결되어 있으면:
- 기존 리서치와 발견 사항을 찾아 비교합니다
- 종합 결과를 리서치 저장소에 게시합니다

## 팁

1. **원문 인용을 포함하세요** — 참가자 직접 인용은 인사이트를 더 신뢰할 수 있고 기억에 남게 만듭니다.
2. **관찰과 해석을 분리하세요** — "8명 중 5명이 잘못된 버튼을 클릭했다"는 관찰입니다. "버튼 배치가 혼란스럽다"는 해석입니다.
3. **가능하면 수치화하세요** — "대부분의 사용자"는 모호합니다. "10명 중 7명"은 구체적입니다.
