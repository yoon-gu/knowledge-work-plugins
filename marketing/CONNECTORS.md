# 커넥터

## 도구 참조 방식

플러그인 파일은 `~~category`를 사용자가 해당 범주에서 연결한 도구를 가리키는 자리표시자로 사용합니다. 예를 들어 `~~marketing automation`은 HubSpot, Marketo 또는 MCP 서버가 있는 다른 마케팅 플랫폼을 뜻할 수 있습니다.

플러그인은 특정 제품이 아니라 범주(디자인, SEO, 이메일 마케팅 등)를 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 같은 범주의 다른 MCP 서버도 사용할 수 있습니다.

## 이 플러그인의 커넥터

| 카테고리 | 플레이스홀더 | 포함된 서버 | 기타 옵션 |
| ---------- | ------------- | ----------------- | --------------- |
| 채팅 | `~~chat` | Slack | Microsoft Teams |
| 디자인 | `~~design` | Canva, Figma | Adobe Creative Cloud |
| 마케팅 자동화 | `~~marketing automation` | HubSpot | Marketo, Pardot, Mailchimp |
| 제품 분석 | `~~product analytics` | Amplitude | Mixpanel, Google Analytics |
| 지식 베이스 | `~~knowledge base` | Notion | Confluence, Guru |
| SEO | `~~SEO` | Ahrefs, Similarweb | Semrush, Moz |
| 이메일 마케팅 | `~~email marketing` | Klaviyo | Mailchimp, Brevo, Customer.io |
| 마케팅 분석 | `~~marketing analytics` | Supermetrics | Google Analytics, Mailchimp, Semrush |
