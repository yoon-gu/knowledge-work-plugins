# Connectors

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~data warehouse`는 Snowflake, BigQuery, 또는 MCP 서버가 있는 다른 데이터 웨어하우스를 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품이 아닌 카테고리(data warehouse, chat, project tracker 등) 기준으로 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| Data warehouse | `~~data warehouse` | Snowflake\*, Databricks\*, BigQuery | Redshift, PostgreSQL |
| Email | `~~email` | Microsoft 365 | — |
| Office suite | `~~office suite` | Microsoft 365 | — |
| Chat | `~~chat` | Slack | Microsoft Teams |
| ERP / Accounting | `~~erp` | — (아직 지원되는 MCP 서버 없음) | NetSuite, SAP, QuickBooks, Xero |
| Analytics / BI | `~~analytics` | — (아직 지원되는 MCP 서버 없음) | Tableau, Looker, Power BI |

\* 자리 표시자 — MCP URL 미구성
