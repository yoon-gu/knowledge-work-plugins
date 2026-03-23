# 커넥터

## 도구 참조 방식

플러그인 파일에서는 `~~category`를 사용자가 그 범주에 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~CRM`은 MCP 서버가 있는 Salesforce, HubSpot 또는 다른 CRM을 뜻할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(CRM, 채팅, 이메일 등)로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주의 어떤 MCP 서버라도 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 범주 | 자리표시자 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| 캘린더 | `~~calendar` | Google Calendar, Microsoft 365 | — |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 경쟁 인텔리전스 | `~~competitive intelligence` | Similarweb | Crayon, Klue |
| CRM | `~~CRM` | HubSpot, Close | Salesforce, Pipedrive, Copper |
| 데이터 보강 | `~~data enrichment` | Clay, ZoomInfo, Apollo | Clearbit, Lusha |
| 이메일 | `~~email` | Gmail, Microsoft 365 | — |
| 지식 베이스 | `~~knowledge base` | Notion | Confluence, Guru |
| 회의 전사 | `~~conversation intelligence` | Fireflies | Gong, Chorus, Otter.ai |
| 프로젝트 추적기 | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
| 세일즈 참여 | `~~sales engagement` | Outreach | Salesloft, Apollo |
