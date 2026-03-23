# 커넥터

## 도구 참조 방식

플러그인 파일에서는 `~~category`를 사용자가 해당 범주에서 연결한 도구를 가리키는 플레이스홀더로 사용합니다. 예를 들어 `~~HRIS`는 MCP 서버가 있는 Workday, BambooHR, 또는 다른 HRIS를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(HRIS, ATS, 이메일 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주의 어떤 MCP 서버라도 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 범주 | 플레이스홀더 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| ATS | `~~ATS` | — | Greenhouse, Lever, Ashby, Workable |
| 캘린더 | `~~calendar` | Google Calendar | Microsoft 365 |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| Email | `~~email` | Gmail, Microsoft 365 | — |
| HRIS | `~~HRIS` | — | Workday, BambooHR, Rippling, Gusto |
| 지식 베이스 | `~~knowledge base` | Notion, Atlassian (Confluence) | Guru, Coda |
| 보상 데이터 | `~~compensation data` | — | Pave, Radford, Levels.fyi |
