# Connectors

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 플레이스홀더로 `~~category`를 사용합니다. 예를 들어, `~~design tool`은 Figma, Sketch, 또는 MCP 서버를 제공하는 다른 디자인 도구를 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품이 아닌 카테고리(디자인 도구, 프로젝트 트래커, 사용자 피드백 등) 기준으로 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 설정하지만, 해당 카테고리의 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 카테고리 | 플레이스홀더 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 디자인 도구 | `~~design tool` | Figma | Sketch, Adobe XD, Framer |
| 지식 베이스 | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| 프로젝트 트래커 | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Shortcut, ClickUp |
| 사용자 피드백 | `~~user feedback` | Intercom | Productboard, Canny, UserVoice, Dovetail |
| 제품 분석 | `~~product analytics` | — | Amplitude, Mixpanel, Heap, FullStory |
