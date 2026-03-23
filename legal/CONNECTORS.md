# Connectors

## 도구 참조 방식

플러그인 파일은 `~~category`를 사용자가 해당 범주에서 연결한 도구를 가리키는 플레이스홀더로 사용합니다. 예를 들어 `~~cloud storage`는 Box, Egnyte 또는 MCP 서버가 있는 다른 저장소 공급자를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(cloud storage, chat, office suite 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주의 어떤 MCP 서버라도 사용할 수 있습니다.

## 이 플러그인의 연결 도구

| 범주 | 플레이스홀더 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| 캘린더 | `~~calendar` | Google Calendar | Microsoft 365 |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 클라우드 저장소 | `~~cloud storage` | Box, Egnyte | Dropbox, SharePoint, Google Drive |
| CLM | `~~CLM` | — | Ironclad, Agiloft |
| CRM | `~~CRM` | — | Salesforce, HubSpot |
| 이메일 | `~~email` | Gmail | Microsoft 365 |
| 전자서명 | `~~e-signature` | DocuSign | Adobe Sign |
| 오피스 제품군 | `~~office suite` | Microsoft 365 | Google Workspace |
| 프로젝트 추적기 | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
