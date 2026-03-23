# 커넥터

## 도구 참조 방식

플러그인 파일에서는 `~~category`를 그 범주에 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~literature`는 MCP 서버가 있는 PubMed, bioRxiv, 또는 다른 문헌 소스를 뜻할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다**. 특정 제품이 아니라 범주(문헌, 임상시험, 화학 데이터베이스 등)로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주에 속하기만 하면 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 범주 | 자리표시자 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| 문헌 | `~~literature` | PubMed, bioRxiv | Google Scholar, Semantic Scholar |
| 과학 일러스트레이션 | `~~scientific illustration` | BioRender | — |
| 임상시험 | `~~clinical trials` | ClinicalTrials.gov | EU Clinical Trials Register |
| 화학 데이터베이스 | `~~chemical database` | ChEMBL | PubChem, DrugBank |
| 약물 타깃 | `~~drug targets` | Open Targets | UniProt, STRING |
| 데이터 저장소 | `~~data repository` | Synapse | Zenodo, Dryad, Figshare |
| 저널 접근 | `~~journal access` | Wiley Scholar Gateway | Elsevier, Springer Nature |
| AI 연구 | `~~AI research` | Owkin | — |
| 실험실 플랫폼 | `~~lab platform` | Benchling\* | — |

\* 자리표시자 - MCP URL이 아직 구성되지 않았습니다
