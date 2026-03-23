# Connectors

## 도구 참조가 작동하는 방식

플러그인 파일은 사용자가 해당 카테고리에 연결하는 도구에 대한 플레이스홀더로 `~~category`를 사용합니다. 예를 들어, `~~chat`은 Slack, Microsoft Teams, 또는 MCP 서버가 있는 다른 채팅 도구를 의미할 수 있습니다.

플러그인은 **도구 독립적**입니다 — 특정 제품이 아닌 카테고리(채팅, 이메일, 클라우드 스토리지 등) 기준으로 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 어떤 MCP 서버도 작동합니다.

이 플러그인은 검색 결과의 소스 레이블로 `~~category` 참조를 광범위하게 사용합니다(예: `~~chat:`, `~~email:`). 이는 의도적인 것으로, 연결된 도구로 해석되는 동적 카테고리 마커를 나타냅니다.

## 이 플러그인의 Connectors

| 카테고리 | 플레이스홀더 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 채팅 | `~~chat` | Slack | Microsoft Teams, Discord |
| 이메일 | `~~email` | Microsoft 365 | — |
| 클라우드 스토리지 | `~~cloud storage` | Microsoft 365 | Dropbox |
| 지식 베이스 | `~~knowledge base` | Notion, Guru | Confluence, Slite |
| 프로젝트 트래커 | `~~project tracker` | Atlassian (Jira/Confluence), Asana | Linear, monday.com |
| CRM | `~~CRM` | *(사전 구성 안 됨)* | Salesforce, HubSpot |
| 오피스 스위트 | `~~office suite` | Microsoft 365 | Google Workspace |
