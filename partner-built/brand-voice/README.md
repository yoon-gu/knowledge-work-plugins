# Brand Voice Plugin

[Tribe AI](https://tribe.ai)가 Claude Cowork를 위해 제작한 플러그인으로, Cowork 런치 파트너로 개발되었습니다.

회사를 알아볼 수 있게 만드는 브랜드 지식은 쓸모 있는 곳에 거의 존재하지 않습니다. 2022년에 만든 덱 어딘가에, 마지막 리브랜딩 이후 아무도 업데이트하지 않은 Confluence 페이지에, 그리고 충분히 오래 일해서 그냥 아는 몇몇 시니어 직원들의 직관 속에 흩어져 있습니다. 영업 담당자들이 AI로 아웃리치를 생성하고 신입사원들이 첫 주부터 콘텐츠를 작성할 때, 바로 그 지식이 사라집니다.

Brand Voice는 흩어진 브랜드 자료를 실행 가능한 AI 가이드라인으로 변환합니다. Confluence, Google Drive, Box, SharePoint, Slack, Gong, Granola를 검색해 회사가 실제로 어떻게 소통하는지 발굴하고, LLM에 바로 적용 가능한 브랜드 가이드라인을 생성하며, AI가 생성한 모든 콘텐츠를 그 기준에 맞게 검증합니다. Claude는 단순히 더 빠르게 작성하는 것이 아닙니다. 여러분처럼 작성합니다.

## 기능

### 1. 브랜드 발굴 (Brand Discovery)
브랜드 지식은 Notion, Confluence, Google Drive, Gong, Slack, 그리고 수년간의 영업 통화 및 회의 녹취록 전반에 묻혀 있습니다. Brand Voice는 이 모든 곳을 검색합니다 — 스타일 가이드, 피치 덱, 이메일 템플릿, 녹취록, 디자인 시스템 — 가장 강력한 브랜드 신호를 단 하나의 최신 정보 원천으로 정제합니다. 3년 전 스타일 가이드가 말하는 방식이 아니라, 여러분의 최고 인재들이 실제로 소통하는 방식에 근거합니다.

**슬래시 명령어:** `/brand-voice:discover-brand`

```
/brand-voice:discover-brand
/brand-voice:discover-brand Acme Corp
```

### 2. 가이드라인 생성 (Guideline Generation)
자료를 LLM에 바로 적용 가능한 가이드라인으로 합성합니다: 보이스 기둥(voice pillars), 톤 파라미터, Claude에게 명확한 운영 경계를 제시하는 "We Are / We Are Not" 프레임워크, 그리고 이상적인 카피가 아닌 실제 회사 언어를 반영하는 용어 기준. 베테랑 팀을 브랜드에 맞게 유지하는 동일한 가이드라인이 신입사원이 3개월이 아닌 첫 주부터 질 높은 콘텐츠를 생산하게 합니다.

**슬래시 명령어:** `/brand-voice:generate-guidelines`

```
/brand-voice:generate-guidelines
/brand-voice:generate-guidelines from the discovery report and these 3 PDFs
```

### 3. 브랜드 보이스 적용 (Brand Voice Enforcement)
AI가 생성하는 모든 콘텐츠 — 영업 이메일, 제안서, 마케팅 페이지, 보도자료 — 가 처음부터 가이드라인에 맞게 작성됩니다. 보이스는 일정하게 유지되면서 톤은 맥락에 따라 유연하게 조절됩니다: 격식 수준, 에너지, 기술적 깊이가 콜드 이메일, 엔터프라이즈 제안서, LinkedIn 게시물에 맞게 자동으로 적응합니다. 톤 드리프트와 포지셔닝 불일치는 잠재 고객이나 투자자에게 도달하기 전에 잡아냅니다.

**슬래시 명령어:** `/brand-voice:enforce-voice`

```
/brand-voice:enforce-voice Draft a cold email to a VP of Sales at a mid-market SaaS company
/brand-voice:enforce-voice Write a LinkedIn post announcing our new feature
```

### 열린 질문 (Open Questions)
플러그인이 해결할 수 없는 모호한 상황 — 상충하는 문서, 누락된 가이드라인, 명시된 브랜드와 실제 운용 브랜드의 차이 — 에 직면하면 팀 토론을 위한 열린 질문을 제시합니다. 모든 질문에는 에이전트 권고안이 포함되어 있어, 모호함을 막다른 길이 아닌 "확인 또는 재정의" 인터랙션으로 전환합니다.

## MCP 커넥터

| 커넥터 | URL | 목적 |
|-----------|-----|---------|
| **Notion** | `https://mcp.notion.com/mcp` | 발굴의 핵심 — 연결된 Google Drive, SharePoint, OneDrive, Slack, Jira를 통해 연합 검색. 결과 가이드라인도 저장. |
| **Atlassian** | `https://mcp.atlassian.com/v1/mcp` | Atlassian 중심 기업을 위한 심층 Confluence 검색 + Jira 컨텍스트 |
| **Box** | `https://mcp.box.com` | 클라우드 파일 스토리지 — 공식 브랜드 문서, 공유 덱, 스타일 가이드가 주로 여기에 있음 |
| **Microsoft 365** | `https://microsoft365.mcp.claude.com/mcp` | SharePoint, OneDrive, Outlook, Teams — 엔터프라이즈 문서 스토리지 및 이메일 템플릿 |
| **Figma** | `https://mcp.figma.com/mcp` | 브랜드 디자인 시스템 — 색상, 타이포그래피, 디자인 토큰이 보이스에 영향 |
| **Gong** | `https://mcp.gong.io/mcp` | 엔터프라이즈 대화 인텔리전스 — 영업 통화 녹취록 및 분석 |
| **Granola** | `https://mcp.granola.ai/mcp` | 미팅 인텔리전스 — 영업, 고객, 전략 회의 녹취록 및 노트 |

### 네이티브 통합

이 플랫폼들은 Claude 네이티브 통합으로, MCP 커넥터 설치가 필요 없습니다. 사용자가 Claude Desktop 또는 Cowork에서 연결하면 도구로 사용 가능합니다.

| 통합 | 목적 |
|-------------|---------|
| **Google Drive** | 공유 브랜드 문서, 스타일 가이드, 마케팅 자료, Google Docs 및 Slides |
| **Slack** | 브랜드 논의, 채널 검색, 고정된 브랜드 가이드라인, 비공식 보이스 패턴 |

## 빠른 시작

1. 플러그인을 설치하고 Claude Cowork를 엽니다
2. 최소 하나의 플랫폼을 연결합니다 (Notion 권장 — Google Drive, SharePoint, Slack, Jira에 걸쳐 연합 검색)
3. `/brand-voice:discover-brand` 실행 — Claude가 연결된 지식 베이스에서 브랜드 자료를 자동으로 검색
4. `/brand-voice:generate-guidelines` 실행 — 발굴 보고서로부터 지속 가능한 가이드라인 생성
5. 콘텐츠 작성 시 `/brand-voice:enforce-voice` 사용 — 영업 이메일, 제안서, LinkedIn 게시물 등 고객 대면 콘텐츠

특정 문서를 직접 지정하는 것도 가능합니다. 어느 방식이든 Claude가 프로세스를 안내합니다.

Brand Voice는 현재 개인 수준에서 작동합니다 — 팀 전체 적용은 곧 출시됩니다.

### 프로젝트별 설정

`settings/brand-voice.local.md.example`을 프로젝트의 `.claude/brand-voice.local.md`에 복사하고 회사명, 활성화된 플랫폼, 알려진 브랜드 자료 위치를 입력합니다.

## 파일 구조

```
├── .claude-plugin/
│   └── plugin.json                              # 플러그인 매니페스트
├── .mcp.json                                    # MCP 서버 연결 7개
├── README.md
├── agents/
│   ├── discover-brand.md                        # 자율 플랫폼 검색 에이전트
│   ├── content-generation.md                    # 브랜드 정렬 콘텐츠 생성
│   ├── conversation-analysis.md                 # 영업 통화 녹취록 분석
│   ├── document-analysis.md                     # 브랜드 문서 파싱
│   └── quality-assurance.md                     # 컴플라이언스 및 열린 질문 감사
├── commands/
│   ├── discover-brand.md                        # /brand-voice:discover-brand
│   ├── enforce-voice.md                         # /brand-voice:enforce-voice
│   └── generate-guidelines.md                   # /brand-voice:generate-guidelines
├── settings/
│   └── brand-voice.local.md.example             # 프로젝트별 설정 템플릿
└── skills/
    ├── discover-brand/
    │   ├── SKILL.md                             # 발굴 오케스트레이션
    │   └── references/
    │       ├── search-strategies.md             # 플랫폼별 쿼리 패턴
    │       └── source-ranking.md                # 랭킹 알고리즘 및 카테고리
    ├── brand-voice-enforcement/
    │   ├── SKILL.md                             # 적용 오케스트레이션
    │   └── references/
    │       ├── before-after-examples.md         # 콘텐츠 유형별 변환 예시
    │       └── voice-constant-tone-flexes.md    # "We Are / We Are Not" + 톤 매트릭스
    └── guideline-generation/
        ├── SKILL.md                             # 생성 오케스트레이션
        └── references/
            ├── confidence-scoring.md            # 신뢰도 점수 방법론
            └── guideline-template.md            # 전체 출력 템플릿
```

## 아키텍처

**Skills**는 도메인 지식을 제공하고 워크플로를 오케스트레이션합니다. 사용자 의도에 따라 자동으로 활성화됩니다.

**Agents**는 플랫폼 검색, 문서 분석, 녹취록 파싱, 콘텐츠 생성, 품질 검증 등 무거운 자율 작업을 처리합니다.

**Commands**는 스킬 워크플로를 트리거하는 명시적인 사용자 진입점입니다.

**핵심 설계 결정:**
- 보이스는 일정, 톤은 유연 — 적용을 위한 명확한 멘탈 모델
- 발굴 에이전트는 자율적이지만 책임감 있음 — 출처와 충돌 정보를 함께 제시
- 열린 질문은 실패가 아닌 기능 — 모든 모호함에 권고안 포함
- 점진적 공개 — frontmatter는 간결, SKILL.md는 집중, 세부 사항은 references/에 위치
- Notion AI Search를 연합 발굴 엔진으로 활용 — 하나의 API로 연결된 소스를 통해 8개 이상의 플랫폼 검색
- Google Drive와 Slack은 Claude 네이티브 통합 — MCP 커넥터 불필요
