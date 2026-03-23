# Knowledge Work Plugins

Claude를 여러분의 역할, 팀, 회사에 맞는 전문가로 바꿔 주는 플러그인입니다. [Claude Cowork](https://claude.com/product/cowork)을 위해 만들어졌으며, [Claude Code](https://claude.com/product/claude-code)와도 호환됩니다.

## 왜 플러그인인가

Cowork는 목표를 정하면 Claude가 완성도 높은 결과물을 내놓게 해 줍니다. 플러그인은 여기서 더 나아가, 작업을 어떤 방식으로 진행할지, 어떤 도구와 데이터를 가져올지, 중요한 워크플로를 어떻게 처리할지, 어떤 슬래시 명령을 노출할지까지 Claude에 알려 줄 수 있게 해 줍니다. 그래서 팀은 더 일관되고 더 나은 결과를 얻습니다.

각 플러그인은 특정 직무에 필요한 스킬, 커넥터, 슬래시 명령, 서브 에이전트를 묶어 둡니다. 기본 상태만으로도 Claude가 해당 역할을 돕는 데 훌륭한 출발점을 제공합니다. 진짜 힘은 회사의 도구, 용어, 프로세스에 맞게 커스터마이즈할 때 나옵니다. 그러면 Claude가 마치 여러분 팀을 위해 처음부터 만들어진 것처럼 동작합니다.

## 플러그인 마켓플레이스

우리는 우리 자신의 업무에서 만들고 영감을 얻은 11개의 플러그인을 오픈소스로 공개합니다.

| 플러그인 | 도움 되는 방식 | 커넥터 |
|--------|-------------|------------|
| **[productivity](./productivity)** | 작업, 일정, 일상 워크플로, 개인 컨텍스트를 관리해 같은 말을 반복하는 시간을 줄여 줍니다. | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **[sales](./sales)** | 잠재 고객을 조사하고, 통화 준비를 하고, 파이프라인을 검토하고, 아웃리치를 초안 작성하고, 경쟁 배틀카드를 만듭니다. | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| **[customer-support](./customer-support)** | 티켓을 분류하고, 응답을 초안 작성하고, 에스컬레이션을 정리하고, 고객 맥락을 조사하고, 해결된 이슈를 지식 베이스 문서로 바꿉니다. | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| **[product-management](./product-management)** | 명세서를 쓰고, 로드맵을 계획하고, 사용자 리서치를 종합하고, 이해관계자에게 업데이트를 제공하고, 경쟁 지형을 추적합니다. | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| **[marketing](./marketing)** | 콘텐츠 초안 작성, 캠페인 기획, 브랜드 보이스 준수, 경쟁사 브리핑, 채널별 성과 보고를 지원합니다. | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| **[legal](./legal)** | 계약서 검토, NDA 분류, 컴플라이언스 대응, 리스크 평가, 회의 준비, 템플릿 응답 초안 작성을 돕습니다. | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **[finance](./finance)** | 분개를 준비하고, 계정을 조정하고, 재무제표를 생성하고, 차이를 분석하고, 결산을 관리하고, 감사 지원을 합니다. | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **[data](./data)** | 데이터셋을 조회, 시각화, 해석합니다. SQL을 작성하고, 통계 분석을 수행하고, 대시보드를 만들고, 공유 전에 검증합니다. | Snowflake, Databricks, BigQuery, Definite, Hex, Amplitude, Jira |
| **[enterprise-search](./enterprise-search)** | 이메일, 채팅, 문서, 위키 전반에서 무엇이든 찾습니다. 회사 도구 전체를 한 번의 쿼리로 검색합니다. | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **[bio-research](./bio-research)** | 전임상 연구 도구와 데이터베이스에 연결해 문헌 검색, 유전체 분석, 타깃 우선순위화를 수행하고 초기 생명과학 R&D를 가속합니다. | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Synapse, Wiley, Owkin, Open Targets, Benchling |
| **[cowork-plugin-management](./cowork-plugin-management)** | 조직의 고유한 도구와 워크플로에 맞는 새 플러그인을 만들거나 기존 플러그인을 커스터마이즈합니다. | — |

이 플러그인들은 Cowork에서 바로 설치할 수도 있고, GitHub에서 전체 컬렉션을 둘러볼 수도 있고, 직접 새로 만들 수도 있습니다.

## 시작하기

### Cowork

[claude.com/plugins](https://claude.com/plugins/)에서 플러그인을 설치하세요.

### Claude Code

```bash
# 먼저 마켓플레이스를 추가합니다
claude plugin marketplace add anthropics/knowledge-work-plugins

# 그런 다음 특정 플러그인을 설치합니다
claude plugin install sales@knowledge-work-plugins
```

설치가 끝나면 플러그인은 자동으로 활성화됩니다. 관련성이 있을 때 스킬이 실행되고, 세션에서 슬래시 명령을 사용할 수 있습니다. 예: `/sales:call-prep`, `/data:write-query`.

## 플러그인이 작동하는 방식

모든 플러그인은 같은 구조를 따릅니다.

```
plugin-name/
├── .claude-plugin/plugin.json   # 매니페스트
├── .mcp.json                    # 도구 연결
├── commands/                    # 직접 호출하는 슬래시 명령
└── skills/                      # Claude가 자동으로 활용하는 도메인 지식
```

- **스킬**은 Claude가 유용한 도움을 주는 데 필요한 도메인 전문성, 모범 사례, 단계별 워크플로를 담고 있습니다. 관련성이 있을 때 Claude가 자동으로 활용합니다.
- **명령**은 여러분이 직접 트리거하는 명시적 작업입니다. 예: `/finance:reconciliation`, `/product-management:write-spec`
- **커넥터**는 여러분의 역할이 의존하는 외부 도구, 예를 들어 CRM, 프로젝트 추적 도구, 데이터 웨어하우스, 디자인 도구 등을 [MCP 서버](https://modelcontextprotocol.io/)를 통해 Claude와 연결합니다.

모든 구성 요소는 파일 기반이며, 마크다운과 JSON으로만 이뤄집니다. 코드도, 인프라도, 빌드 단계도 없습니다.

## 여러분의 것으로 만들기

이 플러그인들은 범용적인 출발점입니다. 회사가 실제로 일하는 방식에 맞게 바꾸면 훨씬 더 유용해집니다.

- **커넥터 교체** - `.mcp.json`을 수정해 여러분의 실제 도구 스택을 가리키게 하세요.
- **회사 컨텍스트 추가** - 용어, 조직 구조, 프로세스를 스킬 파일에 넣어 Claude가 여러분의 세계를 이해하게 하세요.
- **워크플로 조정** - 교과서식이 아니라 팀이 실제로 일하는 방식에 맞게 스킬 지침을 수정하세요.
- **새 플러그인 만들기** - `cowork-plugin-management` 플러그인을 사용하거나 위 구조를 따라 아직 다루지 않은 역할과 워크플로용 플러그인을 만드세요.

팀이 플러그인을 만들고 공유할수록 Claude는 더 폭넓은 분야를 아우르는 전문가가 됩니다. 여러분이 정의한 컨텍스트는 관련된 모든 상호작용에 스며들어, 리더와 관리자는 프로세스를 강제하는 데 쓰는 시간을 줄이고 개선하는 데 더 많은 시간을 쓸 수 있습니다.

## 기여

플러그인은 결국 마크다운 파일입니다. 저장소를 포크하고, 변경을 만든 뒤, PR을 제출하세요.
