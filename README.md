# 지식 업무 플러그인

플러그인은 Claude를 여러분의 역할, 팀, 회사에 맞는 전문가로 만들어줍니다. [Claude Cowork](https://claude.com/product/cowork)를 위해 제작되었으며, [Claude Code](https://claude.com/product/claude-code)와도 호환됩니다.

## 왜 플러그인인가

Cowork에서는 목표를 설정하면 Claude가 완성도 높은 전문적인 결과물을 제공합니다. 플러그인을 사용하면 더 나아갈 수 있습니다: Claude에게 업무 처리 방식, 사용할 도구와 데이터, 중요 워크플로우 처리 방법, 노출할 슬래시 명령어를 알려주어 팀이 더 좋고 일관된 결과를 얻을 수 있습니다.

각 플러그인은 특정 직무에 필요한 스킬, 커넥터, 슬래시 명령어, 서브 에이전트를 하나로 묶어줍니다. 기본 상태에서도 해당 역할의 누구에게나 도움이 되는 강력한 출발점을 제공합니다. 진정한 힘은 여러분의 회사에 맞게 커스터마이징할 때 발휘됩니다 — 여러분의 도구, 용어, 프로세스를 반영하면 Claude가 마치 여러분의 팀을 위해 만들어진 것처럼 작동합니다.

## 플러그인 마켓플레이스

우리는 자체 업무에서 영감을 받아 제작한 11개의 플러그인을 오픈소스로 공개합니다:

| 플러그인 | 도움이 되는 방법 | 커넥터 |
|--------|-------------|------------|
| **[productivity](./productivity)** | 작업, 캘린더, 일일 워크플로우, 개인 컨텍스트를 관리하여 반복적인 일에 드는 시간을 줄입니다. | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **[sales](./sales)** | 잠재 고객을 조사하고, 통화를 준비하며, 파이프라인을 검토하고, 아웃리치를 작성하며, 경쟁 배틀카드를 만듭니다. | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| **[customer-support](./customer-support)** | 티켓을 분류하고, 응답을 작성하며, 에스컬레이션을 패키징하고, 고객 컨텍스트를 조사하며, 해결된 이슈를 지식 기반 문서로 전환합니다. | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| **[product-management](./product-management)** | 스펙을 작성하고, 로드맵을 계획하며, 사용자 리서치를 종합하고, 이해관계자에게 업데이트하며, 경쟁 환경을 추적합니다. | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| **[marketing](./marketing)** | 콘텐츠를 작성하고, 캠페인을 계획하며, 브랜드 보이스를 유지하고, 경쟁사를 브리핑하며, 채널별 성과를 보고합니다. | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| **[legal](./legal)** | 계약을 검토하고, NDA를 분류하며, 컴플라이언스를 탐색하고, 리스크를 평가하며, 미팅을 준비하고, 템플릿 응답을 작성합니다. | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **[finance](./finance)** | 분개 전표를 준비하고, 계정을 조정하며, 재무제표를 생성하고, 차이를 분석하며, 결산을 관리하고, 감사를 지원합니다. | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **[data](./data)** | 데이터셋을 조회, 시각화, 해석합니다 — SQL을 작성하고, 통계 분석을 수행하며, 대시보드를 구축하고, 공유 전 작업을 검증합니다. | Snowflake, Databricks, BigQuery, Definite, Hex, Amplitude, Jira |
| **[enterprise-search](./enterprise-search)** | 이메일, 채팅, 문서, 위키를 아우르는 통합 검색 — 회사의 모든 도구를 하나의 쿼리로 검색합니다. | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **[bio-research](./bio-research)** | 전임상 연구 도구 및 데이터베이스(문헌 검색, 유전체 분석, 타겟 우선순위 지정)에 연결하여 초기 단계 생명과학 R&D를 가속화합니다. | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Synapse, Wiley, Owkin, Open Targets, Benchling |
| **[cowork-plugin-management](./cowork-plugin-management)** | 조직의 특정 도구와 워크플로우에 맞는 새 플러그인을 만들거나 기존 플러그인을 커스터마이징합니다. | — |

Cowork에서 직접 설치하거나, GitHub에서 전체 컬렉션을 둘러보거나, 직접 만들 수 있습니다.

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

설치 후 플러그인은 자동으로 활성화됩니다. 스킬은 관련 상황에서 자동으로 실행되며, 슬래시 명령어는 세션에서 사용할 수 있습니다 (예: `/sales:call-prep`, `/data:write-query`).

## 플러그인 작동 방식

모든 플러그인은 동일한 구조를 따릅니다:

```
plugin-name/
├── .claude-plugin/plugin.json   # 매니페스트
├── .mcp.json                    # 도구 연결
├── commands/                    # 명시적으로 호출하는 슬래시 명령어
└── skills/                      # Claude가 자동으로 활용하는 도메인 지식
```

- **스킬**은 Claude가 유용한 도움을 제공하는 데 필요한 도메인 전문 지식, 모범 사례, 단계별 워크플로우를 인코딩합니다. Claude는 관련 상황에서 자동으로 이를 활용합니다.
- **명령어**는 명시적으로 트리거하는 작업입니다 (예: `/finance:reconciliation`, `/product-management:write-spec`).
- **커넥터**는 Claude를 여러분의 역할에 필요한 외부 도구(CRM, 프로젝트 트래커, 데이터 웨어하우스, 디자인 도구 등)에 [MCP 서버](https://modelcontextprotocol.io/)를 통해 연결합니다.

모든 구성 요소는 파일 기반입니다 — 마크다운과 JSON만 사용하며, 코드도, 인프라도, 빌드 단계도 필요 없습니다.

## 나만의 플러그인 만들기

이 플러그인들은 범용적인 출발점입니다. 여러분의 회사가 실제로 일하는 방식에 맞게 커스터마이징하면 훨씬 더 유용해집니다:

- **커넥터 교체** — `.mcp.json`을 편집하여 여러분의 특정 도구 스택을 지정하세요.
- **회사 컨텍스트 추가** — 스킬 파일에 여러분의 용어, 조직 구조, 프로세스를 추가하여 Claude가 여러분의 세계를 이해하도록 하세요.
- **워크플로우 조정** — 스킬 지침을 팀이 실제로 일하는 방식에 맞게 수정하세요. 교과서가 아닌 현실에 맞추세요.
- **새 플러그인 만들기** — `cowork-plugin-management` 플러그인을 사용하거나 위의 구조를 따라 아직 다루지 않은 역할과 워크플로우를 위한 플러그인을 만드세요.

팀이 플러그인을 만들고 공유함에 따라 Claude는 부서를 아우르는 전문가가 됩니다. 여러분이 정의한 컨텍스트는 모든 관련 상호작용에 반영되므로, 리더와 관리자는 프로세스를 강제하는 데 시간을 덜 쓰고 개선하는 데 더 많은 시간을 쓸 수 있습니다.

## 기여하기

플러그인은 마크다운 파일일 뿐입니다. 저장소를 포크하고, 변경하고, PR을 제출하세요.
