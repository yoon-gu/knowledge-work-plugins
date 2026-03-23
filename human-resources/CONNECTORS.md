# Connectors

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결한 도구의 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~HRIS`는 Workday, BambooHR, 또는 MCP 서버를 갖춘 다른 HRIS를 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품이 아닌 카테고리(HRIS, ATS, 이메일 등)를 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 설정하지만, 해당 카테고리의 어떤 MCP 서버도 사용할 수 있습니다.

## 이 플러그인의 Connectors

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| ATS | `~~ATS` | — | Greenhouse, Lever, Ashby, Workable |
| 캘린더 | `~~calendar` | Google Calendar | Microsoft 365 |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 이메일 | `~~email` | Gmail, Microsoft 365 | — |
| HRIS | `~~HRIS` | — | Workday, BambooHR, Rippling, Gusto |
| 지식 베이스 | `~~knowledge base` | Notion, Atlassian (Confluence) | Guru, Coda |
| 보상 데이터 | `~~compensation data` | — | Pave, Radford, Levels.fyi |
