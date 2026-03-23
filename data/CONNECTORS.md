# 커넥터

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구에 대한 플레이스홀더로 `~~category`를 사용합니다. 예를 들어, `~~data warehouse`는 Snowflake, BigQuery, 또는 MCP 서버가 있는 다른 웨어하우스를 의미할 수 있습니다.

플러그인은 **특정 도구에 종속되지 않습니다** — 특정 제품 대신 카테고리(data warehouse, notebook, product analytics 등) 단위로 워크플로우를 기술합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 카테고리 | 플레이스홀더 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| Data warehouse | `~~data warehouse` | Snowflake\*, Databricks\*, BigQuery, Definite | Redshift, PostgreSQL, MySQL |
| Notebook | `~~notebook` | Hex | Jupyter, Deepnote, Observable |
| Product analytics | `~~product analytics` | Amplitude | Mixpanel, Heap |
| Project tracker | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |

\* 플레이스홀더 — MCP URL이 아직 구성되지 않음
