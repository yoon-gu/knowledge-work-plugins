# 구성요소 스키마

모든 플러그인 구성 요소 유형에 대한 자세한 형식 사양입니다. 4단계에서 구성 요소를 구현할 때 이를 참조하세요.

## 기술

**위치**: `skills/skill-name/SKILL.md` **형식**: YAML 머리말을 사용한 마크다운

### 머리말 필드

| 필드 | 필수의 | 유형 | 설명 |
| ------------- | -------- | ------ | ------------------------------------------ |
| `name` | 예 | 끈 | 스킬 식별자(소문자, 하이픈, 디렉터리 이름과 일치) |
| `description` | 예 | 끈 | 트리거 문구가 포함된 3인칭 설명 |
| `metadata` | 아니요 | 지도 | 임의의 키-값 쌍(예: `version`, `author`) |

### 예시 스킬

```yaml
---
name: api-design
description: >
  This skill should be used when the user asks to "design an API",
  "create API endpoints", "review API structure", or needs guidance
  on REST API best practices, endpoint naming, or request/response design.
metadata:
  version: "0.1.0"
---
```

### 글쓰기 스타일 규칙

- **본문 설명**: 3인칭("This skill should be used when..."), 특정 트리거 문구가 따옴표로 묶여 있습니다.
- **본문**: 명령형/부정사 형식("You should parse the config file"이 아닌 "Parse the config file,").
- **길이**: SKILL.md 본문을 3,000단어(이상적으로는 1,500-2,000) 미만으로 유지하세요. 자세한 내용을 `references/`로 이동하세요.

### 스킬 디렉토리 구조

```
skill-name/
├── SKILL.md              # Core knowledge (required)
├── references/           # Detailed docs loaded on demand
│   ├── patterns.md
│   └── advanced.md
├── examples/             # Working code examples
│   └── sample-config.json
└── scripts/              # Utility scripts
    └── validate.sh
```

### 점진적 공개 수준

1. **메타데이터**(항상 맥락에 있음): 이름 + 설명(최대 100단어)
2. **SKILL.md 본문**(스킬 발동 시): 핵심 지식(<5,000단어)
3. **번들 리소스**(필요에 따라): 참조, 예시, 스크립트(무제한)

## 자치령 대표

**위치**: `agents/agent-name.md` **형식**: YAML 머리말을 사용한 마크다운

### 머리말 필드

| 필드 | 필수의 | 유형 | 설명 |
| ------------- | -------- | ------ | -------------------------------------- |
| `name` | 예 | 끈 | 소문자, 하이픈, 3~50자 |
| `description` | 예 | 끈 | `<example>` 블록을 사용한 트리거 조건 |
| `model` | 예 | 끈 | `inherit`, `sonnet`, `opus` 또는 `haiku` |
| `color` | 예 | 끈 | `blue`, `cyan`, `green`, `yellow`, `magenta`, `red` |
| `tools` | 아니요 | 정렬 | 특정 도구로 제한 |

### 예시 에이전트

```markdown
---
name: code-reviewer
description: Use this agent when the user asks for a thorough code review or wants detailed analysis of code quality, security, and best practices.

<example>
Context: User has just written a new module
user: "Can you do a deep review of this code?"
assistant: "I'll use the code-reviewer agent to provide a thorough analysis."
<commentary>
User explicitly requested a detailed review, which matches this agent's specialty.
</commentary>
</example>

<example>
Context: User is about to merge a PR
user: "Review this before I merge"
assistant: "Let me run a comprehensive review using the code-reviewer agent."
<commentary>
Pre-merge review benefits from the agent's structured analysis process.
</commentary>
</example>

model: inherit
color: blue
tools: ["Read", "Grep", "Glob"]
---

You are a code review specialist focused on identifying issues across security, performance, maintainability, and correctness.

**Your Core Responsibilities:**

1. Analyze code structure and organization
2. Identify security vulnerabilities
3. Flag performance concerns
4. Check adherence to best practices

**Analysis Process:**

1. Read all files in scope
2. Identify patterns and anti-patterns
3. Categorize findings by severity
4. Provide specific remediation suggestions

**Output Format:**
Present findings grouped by severity (Critical, Warning, Info) with:

- File path and line number
- Description of the issue
- Suggested fix
```

### 에이전트 명명 규칙

- 3~50자
- 소문자, 숫자, 하이픈만 가능
- 영숫자로 시작하고 끝나야 합니다.
- 밑줄, 공백 또는 특수 문자가 없습니다.

### 색상 지침

- 파란색/청록색: 분석, 검토
- 녹색: 성공 지향적 작업
- 노란색: 주의, 검증
- 빨간색: 위험, 보안
- 마젠타: 크리에이티브, 세대

## 후크

**위치**: `hooks/hooks.json` **형식**: JSON

### 이용 가능한 이벤트

| 이벤트 | 불이 붙을 때 |
| ------------------ | ------------------ |
| `PreToolUse` | 도구 호출이 실행되기 전 |
| `PostToolUse` | 도구 호출이 완료된 후 |
| `Stop` | 클로드가 응답을 마치면 |
| `SubagentStop` | 하위 에이전트가 완료되면 |
| `SessionStart` | 세션이 시작되면 |
| `SessionEnd` | 세션이 종료되면 |
| `UserPromptSubmit` | 사용자가 메시지를 보낼 때 |
| `PreCompact` | 컨텍스트 압축 전 |
| `Notification` | 알림이 실행될 때 |

### 후크 유형

**프롬프트 기반**(복잡한 로직에 권장):

```json
{
  "type": "prompt",
  "prompt": "Evaluate whether this file write follows project conventions: $TOOL_INPUT",
  "timeout": 30
}
```

지원되는 이벤트: Stop, SubagentStop, UserPromptSubmit, PreToolUse.

**명령 기반**(결정적 검사):

```json
{
  "type": "command",
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/validate.sh",
  "timeout": 60
}
```

### 예시 Hooks.json

```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Check that this file write follows project coding standards. If it violates standards, explain why and block.",
          "timeout": 30
        }
      ]
    }
  ],
  "SessionStart": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "cat ${CLAUDE_PLUGIN_ROOT}/context/project-context.md",
          "timeout": 10
        }
      ]
    }
  ]
}
```

### 후크 출력 형식(명령 후크)

명령 후크는 JSON을 stdout으로 반환합니다.

```json
{
  "decision": "block",
  "reason": "File write violates naming convention"
}
```

결정: `approve`, `block`, `ask_user`(확인 요청).

## MCP 서버

**위치**: 플러그인 루트의 `.mcp.json` **형식**: JSON

### 서버 유형

**stdio** (로컬 프로세스):

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/server.js"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

**SSE**(원격 서버, 서버에서 보낸 이벤트 전송):

```json
{
  "mcpServers": {
    "asana": {
      "type": "sse",
      "url": "https://mcp.asana.com/sse"
    }
  }
}
```

**HTTP**(원격 서버, 스트리밍 가능한 HTTP 전송):

```json
{
  "mcpServers": {
    "api-service": {
      "type": "http",
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${API_TOKEN}"
      }
    }
  }
}
```

### 환경변수 확장

모든 MCP 구성은 `${VAR_NAME}` 대체를 지원합니다.

- `${CLAUDE_PLUGIN_ROOT}` — 플러그인 디렉터리(항상 이식성을 위해 사용)
- `${ANY_ENV_VAR}` — 사용자 환경 변수

플러그인 README에 필요한 모든 환경 변수를 문서화하세요.

### URL이 없는 디렉토리 서버

엔드포인트가 동적이기 때문에 일부 MCP 디렉터리 항목에는 `url`이 없습니다. 플러그인은 대신 **이름**으로 이러한 서버를 참조할 수 있습니다. 플러그인의 MCP 구성에 있는 서버 이름이 디렉터리 항목 이름과 일치하면 URL 일치와 동일하게 처리됩니다.

## 명령(레거시)

> **새 플러그인에는 `skills/*/SKILL.md`을(를) 선호하세요.** 이제 Cowork UI는 명령과 기술을 단일 "Skills" 개념으로 표시합니다. `commands/` 형식은 여전히 ​​작동하지만 `$ARGUMENTS`/`$1` 대체 및 인라인 bash 실행이 포함된 단일 파일 형식이 특별히 필요한 경우에만 사용하십시오.

**위치**: `commands/command-name.md` **형식**: 선택적 YAML 머리말이 포함된 마크다운

### 머리말 필드

| 필드 | 필수의 | 유형 | 설명 |
| --------------- | -------- | --------------- | -------------------------------------- |
| `description` | 아니요 | 끈 | `/help`에 표시된 간략한 설명(60자 미만) |
| `allowed-tools` | 아니요 | 문자열 또는 배열 | 명령이 사용할 수 있는 도구 |
| `model` | 아니요 | 끈 | 모델 재정의: `sonnet`, `opus`, `haiku` |
| `argument-hint` | 아니요 | 끈 | 자동 완성에 대한 예상 인수를 문서화합니다. |

### 예제 명령

```markdown
---
description: Review code for security issues
allowed-tools: Read, Grep, Bash(git:*)
argument-hint: [file-path]
---

Review @$1 for security vulnerabilities including:

- SQL injection
- XSS attacks
- Authentication bypass
- Insecure data handling

Provide specific line numbers, severity ratings, and remediation suggestions.
```

### 주요 규칙

- 명령은 사용자를 위한 메시지가 아니라 Claude를 위한 지침입니다. 지시어로 작성하세요.
- `$ARGUMENTS`은 모든 인수를 단일 문자열로 캡처합니다. `$1`, `$2`, `$3` 위치 인수를 캡처합니다.
- `@path` 구문에는 명령 컨텍스트의 파일 내용이 포함됩니다.
- `!` 백틱 구문은 동적 컨텍스트에 대해 bash 인라인을 실행합니다(예: `` !`git diff --name-only` ``).
- 플러그인 파일을 이식적으로 참조하려면 `${CLAUDE_PLUGIN_ROOT}`을(를) 사용하세요.

### 허용된 도구 패턴

```yaml
# Specific tools
allowed-tools: Read, Write, Edit, Bash(git:*)

# Bash with specific commands only
allowed-tools: Bash(npm:*), Read

# MCP tools (specific)
allowed-tools: ["mcp__plugin_name_server__tool_name"]
```

## 커넥터.md

**위치**: 플러그인 루트 **생성 시기**: 플러그인이 특정 제품이 아닌 카테고리별로 외부 도구를 참조하는 경우

### 체재

```markdown
# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. For example, `~~project tracker` might mean
Asana, Linear, Jira, or any other project tracker with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories
rather than specific products.

## Connectors for this plugin

| Category        | Placeholder         | Included servers | Other options            |
| --------------- | ------------------- | ---------------- | ------------------------ |
| Chat            | `~~chat`            | Slack            | Microsoft Teams, Discord |
| Project tracker | `~~project tracker` | Linear           | Asana, Jira, Monday      |
```

### ~~ 자리 표시자 사용

플러그인 파일(스킬, 에이전트)에서 참조 도구는 일반적으로 다음과 같습니다.

```markdown
Check ~~project tracker for open tickets assigned to the user.
Post a summary to ~~chat in the team channel.
```

cowork-plugin-customizer 기술을 통해 사용자 정의하는 동안 특정 도구 이름으로 대체됩니다.

## 읽어보기.md

모든 플러그인에는 다음과 같은 README가 포함되어야 합니다.

1. **개요** — 플러그인의 기능
2. **구성 요소** — 스킬, 에이전트, 후크, MCP 서버 목록
3. **설정** — 필요한 환경 변수 또는 구성
4. **사용법** — 각 스킬을 발동하는 방법
5. **사용자 정의** — CONNECTORS.md가 존재하는 경우 이를 언급하세요.
