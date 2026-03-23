# 커넥터

## 도구 참조 방식

플러그인 파일은 `~~category`를 사용자가 해당 범주에서 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~data warehouse`는 MCP 서버가 있는 Snowflake, BigQuery 또는 다른 웨어하우스를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(data warehouse, chat, project tracker 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주의 어떤 MCP 서버라도 사용할 수 있습니다.

## 이 플러그인의 커넥터

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Data warehouse | `~~data warehouse` | Snowflake\*, Databricks\*, BigQuery | Redshift, PostgreSQL |
| Email | `~~email` | Microsoft 365 | — |
| Office suite | `~~office suite` | Microsoft 365 | — |
| Chat | `~~chat` | Slack | Microsoft Teams |
| ERP / Accounting | `~~erp` | — (아직 지원되는 MCP 서버 없음) | NetSuite, SAP, QuickBooks, Xero |
| Analytics / BI | `~~analytics` | — (아직 지원되는 MCP 서버 없음) | Tableau, Looker, Power BI |

\* 자리표시자 - MCP URL이 아직 구성되지 않았습니다
