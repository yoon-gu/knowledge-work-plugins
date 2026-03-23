# Connectors

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~cloud storage`는 Box, Egnyte, 또는 MCP 서버가 있는 다른 스토리지 제공업체를 의미할 수 있습니다.

플러그인은 **도구에 독립적**입니다 — 특정 제품이 아닌 카테고리(클라우드 스토리지, 채팅, 오피스 제품군 등) 측면에서 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 모든 MCP 서버에서 작동합니다.

## 이 플러그인의 Connectors

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Chat | `~~chat` | Slack | Microsoft Teams |
| Cloud storage | `~~cloud storage` | Box, Egnyte | Dropbox, SharePoint, Google Drive |
| CLM | `~~CLM` | — | Ironclad, Agiloft |
| CRM | `~~CRM` | — | Salesforce, HubSpot |
| Email | `~~email` | Gmail | Microsoft 365 |
| E-signature | `~~e-signature` | DocuSign | Adobe Sign |
| Office suite | `~~office suite` | Microsoft 365 | Google Workspace |
| Project tracker | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
