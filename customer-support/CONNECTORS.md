# Connectors

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~support platform`은 Intercom, Zendesk, 또는 MCP 서버를 갖춘 다른 지원 도구를 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품 대신 카테고리(지원 플랫폼, CRM, 채팅 등) 측면에서 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 사전 구성하지만, 해당 카테고리의 모든 MCP 서버를 사용할 수 있습니다.

## 이 플러그인의 Connectors

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 이메일 | `~~email` | Microsoft 365 | — |
| 클라우드 스토리지 | `~~cloud storage` | Microsoft 365 | — |
| 지원 플랫폼 | `~~support platform` | Intercom | Zendesk, Freshdesk, HubSpot Service Hub |
| CRM | `~~CRM` | HubSpot | Salesforce, Pipedrive |
| 지식 베이스 | `~~knowledge base` | Guru, Notion | Confluence, Help Scout |
| 프로젝트 트래커 | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
