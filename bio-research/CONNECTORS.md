# Connectors

## 도구 참조가 작동하는 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~literature`는 PubMed, bioRxiv 또는 MCP 서버가 있는 다른 문헌 소스를 의미할 수 있습니다.

플러그인은 **도구에 구애받지 않습니다** — 특정 제품보다는 카테고리(문헌, 임상 시험, 화학 데이터베이스 등)로 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 모든 MCP 서버가 작동합니다.

## 이 플러그인의 Connectors

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 문헌 | `~~literature` | PubMed, bioRxiv | Google Scholar, Semantic Scholar |
| 과학 일러스트레이션 | `~~scientific illustration` | BioRender | — |
| 임상 시험 | `~~clinical trials` | ClinicalTrials.gov | EU Clinical Trials Register |
| 화학 데이터베이스 | `~~chemical database` | ChEMBL | PubChem, DrugBank |
| 약물 표적 | `~~drug targets` | Open Targets | UniProt, STRING |
| 데이터 저장소 | `~~data repository` | Synapse | Zenodo, Dryad, Figshare |
| 저널 접근 | `~~journal access` | Wiley Scholar Gateway | Elsevier, Springer Nature |
| AI 연구 | `~~AI research` | Owkin | — |
| 실험실 플랫폼 | `~~lab platform` | Benchling\* | — |

\* 자리 표시자 — MCP URL 미구성
