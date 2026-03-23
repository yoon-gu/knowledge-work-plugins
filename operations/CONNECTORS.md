# 커넥터

## 도구 참조 방식

플러그인 파일에서는 `~~category`를 사용자가 해당 범주에 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~ITSM`은 ServiceNow, Zendesk 또는 MCP 서버가 있는 다른 서비스 관리 도구를 뜻할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다**. 특정 제품이 아니라 범주(ITSM, project tracker, knowledge base 등)로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주에 속하기만 하면 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 범주 | 자리표시자 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Chat | `~~chat` | Slack | Microsoft Teams |
| Email | `~~email` | Gmail, Microsoft 365 | — |
| ITSM | `~~ITSM` | ServiceNow | Zendesk, Freshservice, Jira Service Management |
| Knowledge base | `~~knowledge base` | Notion, Atlassian (Confluence) | Guru, Coda |
| Project tracker | `~~project tracker` | Asana, Atlassian (Jira) | Linear, monday.com, ClickUp |
| Procurement | `~~procurement` | — | Coupa, SAP Ariba, Zip |
| Office suite | `~~office suite` | Microsoft 365 | Google Workspace |
