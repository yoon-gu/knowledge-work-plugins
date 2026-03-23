# MCP 검색 및 연결

플러그인 맞춤 설정 과정에서 MCP를 찾고 연결하는 방법입니다.

## 사용 가능한 도구

### `search_mcp_registry`
사용 가능한 커넥터를 확인하려면 MCP 디렉터리를 검색하세요.

**입력:** `{ "keywords": ["array", "of", "search", "terms"] }`

**출력:** 최대 10개 결과, 각 결과에는 다음이 포함됩니다.
- `name`: MCP 표시 이름
- `description`: 한 줄 설명
- `tools`: MCP가 제공하는 도구 이름 목록
- `url`: `.mcp.json`에서 사용할 MCP 엔드포인트 URL
- `directoryUuid`: `suggest_connectors`와 함께 사용하기 위한 UUID
- `connected`: 사용자가 이 MCP에 연결했는지 여부를 나타내는 불리언 값

### `suggest_connectors`
사용자가 MCP를 설치하거나 연결할 수 있도록 연결 버튼을 표시합니다.

**입력:** `{ "directoryUuids": ["uuid1", "uuid2"] }`

**출력:** 각 MCP에 대한 연결 버튼이 포함된 UI를 렌더링합니다.

## 카테고리-키워드 매핑

| 카테고리 | 키워드 검색 |
|----------|-----------------|
| `project-management` | `["asana", "jira", "linear", "monday", "tasks"]` |
| `software-coding` | `["github", "gitlab", "bitbucket", "code"]` |
| `chat` | `["slack", "teams", "discord"]` |
| `documents` | `["google docs", "notion", "confluence"]` |
| `calendar` | `["google calendar", "calendar"]` |
| `email` | `["gmail", "outlook", "email"]` |
| `design-graphics` | `["figma", "sketch", "design"]` |
| `analytics-bi` | `["datadog", "grafana", "analytics"]` |
| `crm` | `["salesforce", "hubspot", "crm"]` |
| `wiki-knowledge-base` | `["notion", "confluence", "outline", "wiki"]` |
| `data-warehouse` | `["bigquery", "snowflake", "redshift"]` |
| `conversation-intelligence` | `["gong", "chorus", "call recording"]` |

## 작업 흐름

1. **맞춤 설정 지점 찾기**: `~~` 접두사가 붙은 값(예: `~~Jira`)을 찾습니다.
2. **이전 단계 결과 확인**: 이미 어떤 도구를 사용하는지 알아냈나요?
   - **예**: 해당 도구를 검색해 `url`을 가져온 뒤 5단계로 건너뜁니다.
   - **아니요**: 3단계로 진행합니다.
3. **검색**: 매핑된 키워드로 `search_mcp_registry`를 호출합니다.
4. **후보 제시 및 질문**: 검색 결과를 모두 보여 주고 무엇을 사용할지 묻습니다.
5. **필요한 경우 연결**: 아직 연결되어 있지 않다면 `suggest_connectors`를 호출합니다.
6. **MCP 구성 업데이트**: 검색 결과의 `url`을 사용해 구성을 추가합니다.

## 플러그인 MCP 구성 업데이트

### 구성 파일 찾기

1. **`plugin.json`의 `mcpServers` 필드**를 확인합니다.
```json
{
  "name": "내 플러그인",
  "mcpServers": "./config/servers.json"
}
```
해당 필드가 있으면 지정된 경로의 파일을 수정합니다.

2. **`mcpServers` 필드가 없으면** 플러그인 루트의 `.mcp.json`을 기본값으로 사용합니다.

3. **`mcpServers`가 `.mcpb` 파일만 가리키는 경우**(번들 서버) 플러그인 루트에 새 `.mcp.json`을 만듭니다.

### 구성 파일 형식

중첩된 형식과 평면 형식이 모두 지원됩니다.

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

`search_mcp_registry` 결과의 `url` 필드를 사용하세요.

### URL이 없는 디렉터리 항목

엔드포인트가 동적으로 생성되므로 일부 디렉터리 항목에는 `url`이 없습니다. 관리자가 해당 서버를 연결할 때 이 값을 제공합니다. 이런 서버는 플러그인의 MCP 구성에서 **이름**으로 계속 참조할 수 있습니다. 구성의 MCP 서버 이름이 디렉터리 항목 이름과 같으면 URL이 일치하는 것과 동일하게 처리됩니다.
