---
name: synthesize-research
description: 인터뷰, 설문, 피드백에서 나온 사용자 리서치를 구조화된 인사이트로 종합합니다. 인터뷰 메모, 설문 응답, 지원 티켓 더미를 정리해야 할 때, 주제를 추출해 빈도와 영향으로 발견 사항을 순위화해야 할 때, 원시 피드백을 로드맵 권장 사항으로 바꿔야 할 때 사용합니다.
argument-hint: "<research topic or question>"
---

# 리서치 종합

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

여러 출처의 사용자 리서치를 구조화된 인사이트와 권장 사항으로 종합합니다.

## 사용법

```
/synthesize-research $ARGUMENTS
```

## 워크플로

### 1. 리서치 입력 수집

Accept research from any combination of:
- **Pasted text**: Interview notes, transcripts, survey responses, feedback
- **Uploaded files**: Research documents, spreadsheets, recordings summaries
- **~~knowledge base** (if connected): Search for research documents, interview notes, survey results
- **~~user feedback** (if connected): Pull recent support tickets, feature requests, bug reports
- **~~product analytics** (if connected): Pull usage data, funnel metrics, behavioral data
- **~~meeting transcription** (if connected): Pull interview recordings, meeting summaries, and discussion notes

Ask the user what they have:
- What type of research? (interviews, surveys, usability tests, analytics, support tickets, sales call notes)
- How many sources / participants?
- Is there a specific question or hypothesis they are investigating?
- What decisions will this research inform?

### 2. 리서치 처리

For each source, extract:
- **Key observations**: What did users say, do, or experience?
- **Quotes**: Verbatim quotes that illustrate important points
- **Behaviors**: What users actually did (vs what they said they do)
- **Pain points**: Frustrations, workarounds, and unmet needs
- **Positive signals**: What works well, moments of delight
- **Context**: User segment, use case, experience level

### 3. 주제와 패턴 식별

Apply thematic analysis — see **Research Synthesis Methodology** below for detailed guidance on thematic analysis, affinity mapping, and triangulation techniques.

Group observations into themes, count frequency across participants, and assess impact severity. Note contradictions and surprises.

Create a priority matrix:
- **High frequency + High impact**: Top priority findings
- **Low frequency + High impact**: Important for specific segments
- **High frequency + Low impact**: Quality-of-life improvements
- **Low frequency + Low impact**: Note but deprioritize

### 4. 종합본 생성

Produce a structured research synthesis:

#### 리서치 개요
- Methodology: what types of research, how many participants/sources
- Research question(s): what we set out to learn
- Timeframe: when the research was conducted

#### 핵심 발견
For each major finding (aim for 5-8):
- **Finding statement**: One clear sentence describing the insight
- **Evidence**: Supporting quotes, data points, or observations (with source attribution)
- **Frequency**: How many participants/sources support this finding
- **Impact**: How significantly this affects the user experience or business
- **Confidence level**: High (strong evidence), Medium (suggestive), Low (early signal)

Order findings by priority (frequency x impact).

#### 사용자 세그먼트 / 페르소나
If the research reveals distinct user segments:
- Segment name and description
- Key characteristics and behaviors
- Unique needs and pain points
- Size estimate if data is available

#### 기회 영역
Based on the findings, identify opportunity areas:
- What user needs are unmet or underserved
- Where do current solutions fall short
- What new capabilities would unlock value
- Prioritized by potential impact

#### 권장 사항
Specific, actionable recommendations:
- What to build, change, or investigate further
- Tied back to specific findings
- Prioritized by impact and feasibility

#### 열린 질문
What the research did not answer:
- Gaps in understanding
- Areas needing further investigation
- Suggested follow-up research methods

### 5. 검토 및 확장

After generating the synthesis:
- Ask if any findings need more detail or different framing
- Offer to generate specific artifacts: persona documents, opportunity maps, research presentations
- Offer to create follow-up research plans for open questions
- Offer to draft product implications (how findings should influence the roadmap)

## 리서치 종합 방법론

### 주제 분석
The core method for synthesizing qualitative research:

1. **Familiarization**: Read through all the data. Get a feel for the overall landscape before coding anything.
2. **Initial coding**: Go through the data systematically. Tag each observation, quote, or data point with descriptive codes. Be generous with codes — it is easier to merge than to split later.
3. **Theme development**: Group related codes into candidate themes. A theme captures something important about the data in relation to the research question.
4. **Theme review**: Check themes against the data. Does each theme have sufficient evidence? Are themes distinct from each other? Do they tell a coherent story?
5. **Theme refinement**: Define and name each theme clearly. Write a 1-2 sentence description of what each theme captures.
6. **Report**: Write up the themes as findings with supporting evidence.

### 애피니티 맵핑
A collaborative method for grouping observations:

1. **Capture observations**: Write each distinct observation, quote, or data point as a separate note
2. **Cluster**: Group related notes together based on similarity. Do not pre-define categories — let them emerge from the data.
3. **Label clusters**: Give each cluster a descriptive name that captures the common thread
4. **Organize clusters**: Arrange clusters into higher-level groups if patterns emerge
5. **Identify themes**: The clusters and their relationships reveal the key themes

**Tips for affinity mapping**:
- One observation per note. Do not combine multiple insights.
- Move notes between clusters freely. The first grouping is rarely the best.
- If a cluster gets too large, it probably contains multiple themes. Split it.
- Outliers are interesting. Do not force every observation into a cluster.
- The process of grouping is as valuable as the output. It builds shared understanding.

### 삼각 검증
Strengthen findings by combining multiple data sources:

- **Methodological triangulation**: Same question, different methods (interviews + survey + analytics)
- **Source triangulation**: Same method, different participants or segments
- **Temporal triangulation**: Same observation at different points in time

A finding supported by multiple sources and methods is much stronger than one supported by a single source. When sources disagree, that is interesting — it may reveal different user segments or contexts.

## 인터뷰 노트 분석

### 인터뷰 노트에서 인사이트 추출
For each interview, identify:

**Observations**: What did the participant describe doing, experiencing, or feeling?
- Distinguish between behaviors (what they do) and attitudes (what they think/feel)
- Note context: when, where, with whom, how often
- Flag workarounds — these are unmet needs in disguise

**Direct quotes**: Verbatim statements that powerfully illustrate a point
- Good quotes are specific and vivid, not generic
- Attribute to participant type, not name: "Enterprise admin, 200-person team" not "Sarah"
- A quote is evidence, not a finding. The finding is your interpretation of what the quote means.

**Behaviors vs stated preferences**: What people DO often differs from what they SAY they want
- Behavioral observations are stronger evidence than stated preferences
- If a participant says "I want feature X" but their workflow shows they never use similar features, note the contradiction
- Look for revealed preferences through actual behavior

**Signals of intensity**: How much does this matter to the participant?
- Emotional language: frustration, excitement, resignation
- Frequency: how often do they encounter this issue
- Workarounds: how much effort do they expend working around the problem
- Impact: what is the consequence when things go wrong

### 인터뷰 간 분석
After processing individual interviews:
- Look for patterns: which observations appear across multiple participants?
- Note frequency: how many participants mentioned each theme?
- Identify segments: do different types of users have different patterns?
- Surface contradictions: where do participants disagree? This often reveals meaningful segments.
- Find surprises: what challenged your prior assumptions?

## 설문 데이터 해석

### 정량 설문 분석
- **Response rate**: How representative is the sample? Low response rates may introduce bias.
- **Distribution**: Look at the shape of responses, not just averages. A bimodal distribution (lots of 1s and 5s) tells a different story than a normal distribution (lots of 3s).
- **Segmentation**: Break down responses by user segment. Aggregates can mask important differences.
- **Statistical significance**: For small samples, be cautious about drawing conclusions from small differences.
- **Benchmark comparison**: How do scores compare to industry benchmarks or previous surveys?

### 서술형 응답 분석
- Treat open-ended responses like mini interview notes
- Code each response with themes
- Count frequency of themes across responses
- Pull representative quotes for each theme
- Look for themes that appear in open-ended responses but not in structured questions — these are things you did not think to ask about

### 흔한 설문 분석 실수
- Reporting averages without distributions. A 3.5 average could mean everyone is lukewarm or half love it and half hate it.
- Ignoring non-response bias. The people who did not respond may be systematically different.
- Over-interpreting small differences. A 0.1 point change in NPS is noise, not signal.
- Treating Likert scales as interval data. The difference between "Strongly Agree" and "Agree" is not necessarily the same as between "Agree" and "Neutral."
- Confusing correlation with causation in cross-tabulations.

## 정성 및 정량 인사이트 결합

### 정성-정량 피드백 루프
- **Qualitative first**: Interviews and observation reveal WHAT is happening and WHY. They generate hypotheses.
- **Quantitative validation**: Surveys and analytics reveal HOW MUCH and HOW MANY. They test hypotheses at scale.
- **Qualitative deep-dive**: Return to qualitative methods to understand unexpected quantitative findings.

### 통합 전략
- Use quantitative data to prioritize qualitative findings. A theme from interviews is more important if usage data shows it affects many users.
- Use qualitative data to explain quantitative anomalies. A drop in retention is a number; interviews reveal it is because of a confusing onboarding change.
- Present combined evidence: "47% of surveyed users report difficulty with X (survey), and interviews reveal this is because Y (qualitative finding)."

### 출처가 서로 다를 때
- Quantitative and qualitative sources may tell different stories. This is signal, not error.
- Check if the disagreement is due to different populations being measured
- Check if stated preferences (survey) differ from actual behavior (analytics)
- Check if the quantitative question captured what you think it captured
- Report the disagreement honestly and investigate further rather than choosing one source

## 리서치 기반 페르소나 개발

### 근거 기반 페르소나 만들기
Personas should emerge from research data, not imagination:

1. **Identify behavioral patterns**: Look for clusters of similar behaviors, goals, and contexts across participants
2. **Define distinguishing variables**: What dimensions differentiate one cluster from another? (e.g., company size, technical skill, usage frequency, primary use case)
3. **Create persona profiles**: For each behavioral cluster:
   - Name and brief description
   - Key behaviors and goals
   - Pain points and needs
   - Context (role, company, tools used)
   - Representative quotes
4. **Validate with data**: Can you size each persona segment using quantitative data?

### 페르소나 템플릿
```
[Persona Name] — [One-line description]

Who they are:
- Role, company type/size, experience level
- How they found/started using the product

What they are trying to accomplish:
- Primary goals and jobs to be done
- How they measure success

How they use the product:
- Frequency and depth of usage
- Key workflows and features used
- Tools they use alongside this product

Key pain points:
- Top 3 frustrations or unmet needs
- Workarounds they have developed

What they value:
- What matters most in a solution
- What would make them switch or churn

Representative quotes:
- 2-3 verbatim quotes that capture this persona's perspective
```

### 흔한 페르소나 실수
- Demographic personas: defining by age/gender/location instead of behavior. Behavior predicts product needs better than demographics.
- Too many personas: 3-5 is the sweet spot. More than that and they are not actionable.
- Fictional personas: made up based on assumptions rather than research data.
- Static personas: never updated as the product and market evolve.
- Personas without implications: a persona that does not change any product decisions is not useful.

## 기회 규모 추정

### 기회 규모 추정
For each research finding or opportunity area, estimate:

- **Addressable users**: How many users could benefit from addressing this? Use product analytics, survey data, or market data to estimate.
- **Frequency**: How often do affected users encounter this issue? (Daily, weekly, monthly, one-time)
- **Severity**: How much does this issue impact users when it occurs? (Blocker, significant friction, minor annoyance)
- **Willingness to pay**: Would addressing this drive upgrades, retention, or new customer acquisition?

### 기회 점수화
Score opportunities on a simple matrix:

- **Impact**: (Users affected) x (Frequency) x (Severity) = impact score
- **Evidence strength**: How confident are we in the finding? (Multiple sources > single source, behavioral data > stated preferences)
- **Strategic alignment**: Does this opportunity align with company strategy and product vision?
- **Feasibility**: Can we realistically address this? (Technical feasibility, resource availability, time to impact)

### 기회 규모 제시
- Be transparent about assumptions and confidence levels
- Show the math: "Based on support ticket volume, approximately 2,000 users per month encounter this issue. Interview data suggests 60% of them consider it a significant blocker."
- Use ranges rather than false precision: "This affects 1,500-2,500 users monthly" not "This affects 2,137 users monthly"
- Compare opportunities against each other to create a relative ranking, not just absolute scores

## 출력 형식

Use clear headers and structured formatting. Each finding should stand on its own — a reader should be able to read any single finding and understand it without reading the rest.

## 팁

- Let the data speak. Do not force findings into a predetermined narrative.
- Distinguish between what users say and what they do. Behavioral data is stronger than stated preferences.
- Quotes are powerful evidence. Include them generously, with attribution to participant type (not name).
- Be explicit about confidence levels. A finding from 2 interviews is a hypothesis, not a conclusion.
- Contradictions in the data are interesting, not inconvenient. They often reveal distinct user segments.
- Recommendations should be specific enough to act on. "Improve onboarding" is not actionable. "Add a progress indicator to the setup flow" is.
- Resist the temptation to synthesize too many themes. 5-8 strong findings are better than 20 weak ones.
