# 커넥터

## 도구 참조가 작동하는 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구를 나타내는 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~project tracker`는 Linear, Asana, Jira, 또는 MCP 서버가 있는 다른 트래커를 의미할 수 있습니다.

플러그인은 **도구에 구애받지 않습니다** — 특정 제품이 아니라 카테고리(프로젝트 트래커, 디자인, 제품 분석 등)로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 사전 구성하지만, 해당 카테고리의 모든 MCP 서버에서 작동합니다.

## 이 플러그인의 커넥터

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| 캘린더 | `~~calendar` | Google Calendar | Microsoft 365 |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 경쟁 인텔리전스 | `~~competitive intelligence` | Similarweb | Crayon, Klue |
| 디자인 | `~~design` | Figma | Sketch, Adobe XD |
| 이메일 | `~~email` | Gmail | Microsoft 365 |
| 지식 베이스 | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| 미팅 전사 | `~~meeting transcription` | Fireflies | Gong, Dovetail, Otter.ai |
| 제품 분석 | `~~product analytics` | Amplitude, Pendo | Mixpanel, Heap, FullStory |
| 프로젝트 트래커 | `~~project tracker` | Linear, Asana, monday.com, ClickUp, Atlassian (Jira/Confluence) | Shortcut, Basecamp |
| 사용자 피드백 | `~~user feedback` | Intercom | Productboard, Canny, UserVoice |
