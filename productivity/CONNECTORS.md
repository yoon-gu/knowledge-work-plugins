# 커넥터

## 도구 참조 방식

플러그인 파일은 사용자가 해당 카테고리에 연결한 도구를 나타내는 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~project tracker`는 Asana, Linear, Jira, 또는 MCP 서버가 있는 다른 프로젝트 트래커를 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품이 아닌 카테고리(채팅, 프로젝트 트래커, 지식 베이스 등) 기준으로 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 어떤 MCP 서버도 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 채팅 | `~~chat` | Slack | Microsoft Teams, Discord |
| 이메일 | `~~email` | Microsoft 365 | — |
| 캘린더 | `~~calendar` | Microsoft 365 | — |
| 지식 베이스 | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| 프로젝트 트래커 | `~~project tracker` | Asana, Linear, Atlassian (Jira/Confluence), monday.com, ClickUp | Shortcut, Basecamp, Wrike |
| 오피스 제품군 | `~~office suite` | Microsoft 365 | — |
