# 커넥터

## 도구 참조 방식

플러그인 파일은 `~~category`를 해당 범주에서 사용자가 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~chat`은 MCP 서버가 있는 Slack, Microsoft Teams, 또는 다른 채팅 도구를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(chat, email, cloud storage 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주의 어떤 MCP 서버라도 사용할 수 있습니다.

이 플러그인은 검색 결과의 소스 라벨로 `~~category` 참조를 광범위하게 사용합니다(예: `~~chat:`, `~~email:`). 이는 의도된 것으로, 연결된 도구에 맞게 해석되는 동적 범주 표시자입니다.

## 이 플러그인의 커넥터

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Microsoft 365 | — |
| Cloud storage | `~~cloud storage` | Microsoft 365 | Dropbox |
| Knowledge base | `~~knowledge base` | Notion, Guru | Confluence, Slite |
| Project tracker | `~~project tracker` | Atlassian (Jira/Confluence), Asana | Linear, monday.com |
| CRM | `~~CRM` | *(not pre-configured)* | Salesforce, HubSpot |
| Office suite | `~~office suite` | Microsoft 365 | Google Workspace |
