# 커넥터

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 플레이스홀더로 `~~category`를 사용합니다. 예를 들어 `~~CRM`은 Salesforce, HubSpot, 또는 MCP 서버를 지원하는 다른 CRM을 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품이 아닌 카테고리(CRM, 채팅, 이메일 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 사전 구성하지만, 해당 카테고리의 모든 MCP 서버가 동작합니다.

## 이 플러그인의 커넥터

| 카테고리 | 플레이스홀더 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 캘린더 | `~~calendar` | Google Calendar, Microsoft 365 | — |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 경쟁 인텔리전스 | `~~competitive intelligence` | Similarweb | Crayon, Klue |
| CRM | `~~CRM` | HubSpot, Close | Salesforce, Pipedrive, Copper |
| 데이터 보강 | `~~data enrichment` | Clay, ZoomInfo, Apollo | Clearbit, Lusha |
| 이메일 | `~~email` | Gmail, Microsoft 365 | — |
| 지식 베이스 | `~~knowledge base` | Notion | Confluence, Guru |
| 미팅 전사 | `~~conversation intelligence` | Fireflies | Gong, Chorus, Otter.ai |
| 프로젝트 트래커 | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
| 영업 참여 | `~~sales engagement` | Outreach | Salesloft, Apollo |
