# 연결 도구

## 도구 참조 방식

플러그인 파일은 `~~category`를 해당 카테고리에 사용자가 연결한 도구의 자리표시자로 사용합니다. 예를 들어 `~~project tracker`는 Asana, Linear, Jira 또는 MCP 서버가 있는 다른 프로젝트 트래커를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 카테고리(chat, project tracker, knowledge base 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 MCP 서버라면 무엇이든 사용할 수 있습니다.

## 이 플러그인의 연결 도구

| 카테고리 | 자리표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Microsoft 365 | — |
| Calendar | `~~calendar` | Microsoft 365 | — |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Project tracker | `~~project tracker` | Asana, Linear, Atlassian(Jira/Confluence), monday.com, ClickUp | Shortcut, Basecamp, Wrike |
| Office suite | `~~office suite` | Microsoft 365 | — |
