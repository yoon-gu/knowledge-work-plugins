# Connectors

## 도구 참조 방식

플러그인 파일은 `~~category`를 사용자가 그 범주에서 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~project tracker`는 Linear, Asana, Jira 또는 MCP 서버가 있는 다른 추적 도구를 의미할 수 있습니다.

플러그인은 **도구 중립적**입니다. 특정 제품이 아니라 범주(project tracker, design, product analytics 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 범주에 속하기만 하면 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Chat | `~~chat` | Slack | Microsoft Teams |
| Competitive intelligence | `~~competitive intelligence` | Similarweb | Crayon, Klue |
| Design | `~~design` | Figma | Sketch, Adobe XD |
| Email | `~~email` | Gmail | Microsoft 365 |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Meeting transcription | `~~meeting transcription` | Fireflies | Gong, Dovetail, Otter.ai |
| Product analytics | `~~product analytics` | Amplitude, Pendo | Mixpanel, Heap, FullStory |
| Project tracker | `~~project tracker` | Linear, Asana, monday.com, ClickUp, Atlassian (Jira/Confluence) | Shortcut, Basecamp |
| User feedback | `~~user feedback` | Intercom | Productboard, Canny, UserVoice |
