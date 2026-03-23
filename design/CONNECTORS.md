# 커넥터

## 도구 참조 방식

플러그인 파일은 `~~category`를 그 범주에 사용자가 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~design tool`은 MCP 서버가 있는 Figma, Sketch, 또는 다른 디자인 도구를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(design tool, project tracker, user feedback 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주의 어떤 MCP 서버라도 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 범주 | 플레이스홀더 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Design tool | `~~design tool` | Figma | Sketch, Adobe XD, Framer |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Project tracker | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Shortcut, ClickUp |
| User feedback | `~~user feedback` | Intercom | Productboard, Canny, UserVoice, Dovetail |
| Product analytics | `~~product analytics` | — | Amplitude, Mixpanel, Heap, FullStory |
