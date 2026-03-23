# 커넥터

## 도구 참조 방식

플러그인 파일은 사용자가 해당 범주에 연결한 도구를 나타내는 플레이스홀더로 `~~category`를 사용합니다. 예를 들어 `~~source control`은 GitHub, GitLab, 또는 MCP 서버가 있는 다른 VCS를 의미할 수 있습니다.

플러그인은 **도구 비종속적**입니다. 특정 제품이 아니라 범주(소스 제어, CI/CD, 모니터링 등) 기준으로 워크플로를 설명합니다. `.mcp.json`은 특정 MCP 서버를 미리 설정하지만, 같은 범주라면 어떤 MCP 서버든 사용할 수 있습니다.

## 이 플러그인의 커넥터

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Source control | `~~source control` | GitHub | GitLab, Bitbucket |
| Project tracker | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Shortcut, ClickUp |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Monitoring | `~~monitoring` | Datadog | New Relic, Grafana, Splunk |
| Incident management | `~~incident management` | PagerDuty | Opsgenie, Incident.io, FireHydrant |
| CI/CD | `~~CI/CD` | — | CircleCI, GitHub Actions, Jenkins, BuildKite |
