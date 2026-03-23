# 마케팅 플러그인

주로 Anthropic의 에이전트 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 마케팅 플러그인으로, Claude Code에서도 작동합니다. 콘텐츠 제작, 캠페인 기획, 브랜드 보이스 관리, 경쟁사 분석, 성과 보고 기능을 제공합니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/marketing
```

## 명령어

| 명령어 | 설명 |
|---|---|
| `/draft-content` | 블로그 포스트, 소셜 미디어, 이메일 뉴스레터, 랜딩 페이지, 보도자료, 케이스 스터디 초안 작성 |
| `/campaign-plan` | 목표, 채널, 콘텐츠 캘린더, 성공 지표를 포함한 전체 캠페인 브리프 생성 |
| `/brand-review` | 브랜드 보이스, 스타일 가이드, 메시지 기둥에 맞춰 콘텐츠 검토 |
| `/competitive-brief` | 경쟁사 조사 및 포지셔닝·메시지 비교 분석 생성 |
| `/performance-report` | 핵심 지표, 트렌드, 최적화 권고사항이 포함된 마케팅 성과 보고서 작성 |
| `/seo-audit` | 종합 SEO 감사 실행 — 키워드 조사, 온페이지 분석, 콘텐츠 갭, 기술 점검, 경쟁사 비교 |
| `/email-sequence` | 육성 플로우, 온보딩, 드립 캠페인 등을 위한 멀티 이메일 시퀀스 설계 및 초안 작성 |

## 스킬

| 스킬 | 설명 |
|---|---|
| `content-creation` | 콘텐츠 유형 템플릿, 채널별 작성 모범 사례, SEO 기초, 헤드라인 공식, CTA 가이드 |
| `campaign-planning` | 캠페인 프레임워크, 채널 선택, 콘텐츠 캘린더 작성, 예산 배분, 성공 지표 |
| `brand-voice` | 브랜드 보이스 문서화, 보이스 속성, 톤 적용, 스타일 가이드 적용, 용어 관리 |
| `competitive-analysis` | 경쟁 조사 방법론, 메시지 비교, 콘텐츠 갭 분석, 포지셔닝, 배틀카드 작성 |
| `performance-analytics` | 채널별 핵심 지표, 보고서 템플릿, 트렌드 분석, 어트리뷰션 모델링, 최적화 프레임워크 |

## 워크플로우 예시

### 블로그 포스트 초안 작성

```
> /draft-content
Type: blog post
Topic: How AI is transforming B2B marketing
Audience: Marketing directors at mid-market SaaS companies
Key messages: AI saves time on repetitive tasks, improves personalization, requires human oversight
Tone: Authoritative but approachable
Length: 1200 words
```

Claude는 흥미로운 헤드라인, 훅이 있는 도입부, 체계적인 섹션, SEO 최적화된 소제목, 명확한 행동 유도 문구를 갖춘 구조화된 블로그 포스트 초안을 생성합니다.

### 캠페인 기획

```
> /campaign-plan
Goal: Drive 500 signups for our new product launch
Audience: Technical decision-makers at enterprise companies
Timeline: 6 weeks
Budget range: $20,000-$30,000
```

Claude는 목표, 오디언스 세분화, 핵심 메시지, 채널 전략, 주차별 콘텐츠 캘린더, 추적할 KPI를 담은 캠페인 브리프를 작성합니다.

### 브랜드 가이드라인에 맞춘 콘텐츠 검토

```
> /brand-review
[paste your draft content]
```

로컬 설정에 브랜드 스타일 가이드가 구성되어 있으면 Claude가 보이스, 톤, 용어, 메시지 기둥에 맞춰 콘텐츠를 검토합니다. 구성되지 않은 경우 가이드라인을 요청하거나 명확성, 일관성, 전문성에 대한 일반 검토를 제공합니다.

## 설정

맞춤형 결과물을 위해 로컬 설정 파일에 브랜드 보이스, 스타일 가이드, 타겟 페르소나를 구성하세요. 이를 통해 `/draft-content`, `/brand-review` 같은 명령어가 매번 묻지 않고 자동으로 브랜드 기준을 적용할 수 있습니다.

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

이 플러그인은 다음 MCP 서버와 함께 작동합니다:

- **Slack** — 초안, 보고서, 브리프를 팀과 공유
- **Canva** — 디자인 에셋 생성 및 편집
- **Figma** — 디자인 파일 및 브랜드 에셋 접근
- **HubSpot** — 캠페인 데이터 조회, 연락처 관리, 마케팅 자동화 추적
- **Amplitude** — 제품 분석 및 사용자 행동 데이터 조회
- **Notion** — 브리프, 스타일 가이드, 캠페인 문서 접근
- **Ahrefs** — SEO 키워드 조사, 백링크 분석, 사이트 감사
- **Similarweb** — 경쟁사 트래픽 분석 및 시장 벤치마킹
- **Klaviyo** — 이메일 마케팅 시퀀스 및 캠페인 초안 작성·검토
- **Supermetrics** — 분석 및 보고를 위해 여러 플랫폼의 마케팅 데이터 수집
