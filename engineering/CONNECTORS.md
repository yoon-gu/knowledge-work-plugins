# Connectors

## 도구 참조 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 자리 표시자로 `~~category`를 사용합니다. 예를 들어, `~~source control`은 GitHub, GitLab, 또는 MCP 서버가 있는 다른 VCS를 의미할 수 있습니다.

플러그인은 **도구에 종속되지 않습니다** — 특정 제품이 아닌 카테고리(source control, CI/CD, monitoring 등)로 워크플로우를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 구성하지만, 해당 카테고리의 모든 MCP 서버가 동작합니다.

## 이 플러그인의 Connectors

| 카테고리 | 자리 표시자 | 포함된 서버 | 다른 옵션 |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Source control | `~~source control` | GitHub | GitLab, Bitbucket |
| Project tracker | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Shortcut, ClickUp |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Monitoring | `~~monitoring` | Datadog | New Relic, Grafana, Splunk |
| Incident management | `~~incident management` | PagerDuty | Opsgenie, Incident.io, FireHydrant |
| CI/CD | `~~CI/CD` | — | CircleCI, GitHub Actions, Jenkins, BuildKite |
