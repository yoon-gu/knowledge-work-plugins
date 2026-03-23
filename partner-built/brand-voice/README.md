# Brand Voice 플러그인

[Tribe AI](https://tribe.ai)의 Claude Cowork용 플러그인입니다. Cowork 출시 파트너로 제작되었습니다.

회사를 알아볼 수 있게 만드는 브랜드 지식은 거의 언제나 쓸모 있는 곳에 있지 않습니다. 2022년의 덱, 마지막 리브랜딩 이후 아무도 업데이트하지 않은 Confluence 페이지, 그리고 오래 일한 몇몇 시니어의 감각 속에 흩어져 있습니다. 영업 담당자가 AI로 아웃리치를 만들고 신입이 첫 주부터 콘텐츠를 만든다면, 바로 그 지식이 사라집니다.

Brand Voice는 흩어진 브랜드 자료를 실행 가능한 AI 가드레일로 바꿉니다. Confluence, Google Drive, Box, SharePoint, Slack, Gong, Granola를 검색해 회사가 실제로 어떻게 소통하는지 찾아낸 뒤, LLM에 바로 쓸 수 있는 브랜드 가이드라인을 만들고 AI 생성 콘텐츠 하나하나를 그 기준으로 검증합니다. Claude는 단지 더 빨리 쓰는 것이 아니라, 여러분답게 씁니다.

## 기능

### 1. 브랜드 발견
브랜드 지식은 Notion, Confluence, Google Drive, Gong, Slack, 그리고 수년간의 영업 통화와 회의 녹취에 걸쳐 묻혀 있습니다. Brand Voice는 스타일 가이드, 피치 덱, 이메일 템플릿, 녹취, 디자인 시스템 전부를 검색해 가장 강력한 브랜드 신호를 하나의 최신 진실로 압축합니다. 3년 전 스타일 가이드가 말하는 방식이 아니라, 실제로 가장 잘하는 사람들이 어떻게 소통하는지에 기반합니다.

**슬래시 명령:** `/brand-voice:discover-brand`

```
/brand-voice:discover-brand
/brand-voice:discover-brand Acme Corp
```

### 2. 가이드라인 생성
자료를 LLM용 가이드라인으로 종합합니다. Voice 기둥, 톤 파라미터, Claude에게 명확한 운영 경계를 주는 "We Are / We Are Not" 프레임워크, 그리고 바람직한 문구가 아니라 실제 회사 언어를 반영한 용어 기준이 포함됩니다. 베테랑 팀의 브랜드 일관성을 지키는 것과 같은 가드레일이 신입에게도 첫 주부터 품질 높은 콘텐츠를 만들게 합니다.

**슬래시 명령:** `/brand-voice:generate-guidelines`

```
/brand-voice:generate-guidelines
/brand-voice:generate-guidelines from the discovery report and these 3 PDFs
```

### 3. 브랜드 보이스 집행
AI가 생성하는 모든 콘텐츠, 즉 영업 이메일, 제안서, 마케팅 페이지, 보도자료는 처음부터 가이드라인에 맞춰 작성됩니다. Voice는 일정하게 유지되고 tone은 맥락에 따라 유연하게 바뀝니다. 격식, 에너지, 기술 깊이는 콜드 이메일, 엔터프라이즈 제안서, LinkedIn 게시물에 맞게 자동으로 조정됩니다. 톤 드리프트와 포지셔닝 격차는 고객이나 투자자에게 도달하기 전에 잡아냅니다.

**슬래시 명령:** `/brand-voice:enforce-voice`

```
/brand-voice:enforce-voice Draft a cold email to a VP of Sales at a mid-market SaaS company
/brand-voice:enforce-voice Write a LinkedIn post announcing our new feature
```

### 열린 질문
플러그인이 충돌하는 문서, 빠진 가이드라인, 말과 실제가 다른 브랜드 차이처럼 스스로 해결할 수 없는 모호함을 만나면 팀 토론용 열린 질문을 띄웁니다. 모든 질문에는 에이전트 권고가 포함되어, 모호함을 막다른 길이 아니라 "확인 또는 재정의" 상호작용으로 바꿉니다.

## MCP 커넥터

| 커넥터 | URL | 용도 |
|-----------|-----|---------|
| **Notion** | `https://mcp.notion.com/mcp` | 발견의 중심축 - 연결된 Google Drive, SharePoint, OneDrive, Slack, Jira를 연합 검색합니다. 출력 가이드라인도 저장합니다. |
| **Atlassian** | `https://mcp.atlassian.com/v1/mcp` | Atlassian 비중이 높은 조직을 위한 심층 Confluence 검색 + Jira 맥락 |
| **Box** | `https://mcp.box.com` | 클라우드 파일 저장소 - 공식 브랜드 문서, 공유 덱, 스타일 가이드가 여기에 있는 경우가 많습니다 |
| **Microsoft 365** | `https://microsoft365.mcp.claude.com/mcp` | SharePoint, OneDrive, Outlook, Teams - 엔터프라이즈 문서 저장소와 이메일 템플릿 |
| **Figma** | `https://mcp.figma.com/mcp` | 브랜드 디자인 시스템 - 색상, 타이포그래피, 디자인 토큰이 voice에 반영됩니다 |
| **Gong** | `https://mcp.gong.io/mcp` | 엔터프라이즈 대화 인텔리전스 - 영업 통화 녹취와 분석 |
| **Granola** | `https://mcp.granola.ai/mcp` | 회의 인텔리전스 - 영업, 고객, 전략 회의의 녹취와 메모 |

### 네이티브 통합

이 플랫폼들은 네이티브 Claude 통합입니다. MCP 커넥터 설치는 필요 없고, 사용자가 Claude Desktop이나 Cowork에서 연결하면 도구로 사용할 수 있습니다.

| 통합 | 용도 |
|-------------|---------|
| **Google Drive** | 공유 브랜드 문서, 스타일 가이드, 마케팅 자료, Google Docs와 Slides |
| **Slack** | 브랜드 토론, 채널 검색, 고정된 브랜드 가이드라인, 비공식적 voice 패턴 |

## 빠른 시작

1. 플러그인을 설치하고 Claude Cowork를 엽니다
2. 최소 한 개의 플랫폼을 연결합니다(Notion 권장 - Google Drive, SharePoint, Slack, Jira를 연합 검색합니다)
3. `/brand-voice:discover-brand`를 실행합니다 - Claude가 연결된 지식 베이스에서 브랜드 자료를 자동으로 검색합니다
4. `/brand-voice:generate-guidelines`를 실행해 발견 보고서에서 지속 가능한 가이드라인 세트를 만듭니다
5. 콘텐츠를 만들 때는 `/brand-voice:enforce-voice`를 사용합니다 - 영업 이메일, 제안서, LinkedIn 게시물, 고객 대상 콘텐츠 모두 해당됩니다

원한다면 Claude가 특정 문서를 직접 보도록 할 수도 있습니다. 어느 방식이든 과정을 안내합니다.

Brand Voice는 현재 개인 단위로 동작하며, 팀 전체 집행은 곧 제공될 예정입니다.

### 프로젝트별 설정

`settings/brand-voice.local.md.example`를 프로젝트의 `.claude/brand-voice.local.md`로 복사하고 회사 이름, 활성화할 플랫폼, 알고 있는 브랜드 자료 위치를 채우세요.

## 파일 구조

```
├── .claude-plugin/
│   └── plugin.json                              # 플러그인 매니페스트
├── .mcp.json                                    # 7개의 MCP 서버 연결
├── README.md
├── agents/
│   ├── discover-brand.md                        # 자율 플랫폼 검색 에이전트
│   ├── content-generation.md                    # 브랜드 일치 콘텐츠 생성
│   ├── conversation-analysis.md                 # 영업 통화 녹취 분석
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
    │   ├── SKILL.md                             # 발견 오케스트레이션
    │   └── references/
    │       ├── search-strategies.md             # 플랫폼별 쿼리 패턴
    │       └── source-ranking.md                # 순위 알고리즘과 범주
    ├── brand-voice-enforcement/
    │   ├── SKILL.md                             # 집행 오케스트레이션
    │   └── references/
    │       ├── before-after-examples.md         # 콘텐츠 유형 변환 예시
    │       └── voice-constant-tone-flexes.md    # "We Are / We Are Not" + 톤 매트릭스
    └── guideline-generation/
        ├── SKILL.md                             # 생성 오케스트레이션
        └── references/
            ├── confidence-scoring.md            # 점수화 방법론
            └── guideline-template.md            # 전체 출력 템플릿
```

## 아키텍처

**Skills**는 도메인 지식을 제공하고 워크플로를 조율합니다. 사용자 의도에 따라 자동으로 활성화됩니다.

**Agents**는 플랫폼 검색, 문서 분석, 녹취 파싱, 콘텐츠 생성, 품질 검증 같은 무거운 자율 작업을 처리합니다.

**Commands**는 스킬 워크플로를 트리거하는 명시적 사용자 진입점입니다.

**핵심 설계 결정:**
- Voice는 일정하고 tone은 유연하게 바뀝니다 - 집행을 위한 명확한 정신 모델
- 발견 에이전트는 자율적이지만 책임이 있습니다 - 출처와 충돌을 드러내며 작업을 보여줍니다
- 열린 질문은 실패가 아니라 기능입니다 - 모든 모호함에는 권고가 포함됩니다
- 점진적 공개 - frontmatter는 간결하고, SKILL.md는 집중되어 있으며, 세부 내용은 references/에 있습니다
- Notion AI Search를 연합 발견 엔진으로 사용합니다 - 하나의 API가 연결된 소스를 통해 8개 이상의 플랫폼을 검색합니다
- Google Drive와 Slack은 네이티브 Claude 통합입니다 - 별도 MCP 커넥터가 필요 없습니다
