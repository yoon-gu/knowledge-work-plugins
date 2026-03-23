# 컴포넌트 스키마

모든 플러그인 컴포넌트 유형에 대한 상세한 형식 명세입니다. Phase 4에서 컴포넌트를 구현할 때 이를 참조하세요.

## Skills

**위치**: `skills/skill-name/SKILL.md`
**형식**: YAML frontmatter가 포함된 마크다운

### Frontmatter 필드

| 필드         | 필수 | 타입   | 설명                                             |
| ------------- | -------- | ------ | ------------------------------------------------------- |
| `name`        | 예      | String | 스킬 식별자 (소문자, 하이픈; 디렉토리 이름과 일치) |
| `description` | 예      | String | 트리거 문구가 포함된 3인칭 설명           |
| `metadata`    | 아니오       | Map    | 임의의 키-값 쌍 (예: `version`, `author`)   |

### 스킬 예시

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

### 작성 스타일 규칙

- **Frontmatter description**: 3인칭 ("This skill should be used when..."), 구체적인 트리거 문구를 따옴표로 표시.
- **본문**: 명령형/부정사형 ("Parse the config file," "You should parse the config file"가 아님).
- **길이**: SKILL.md 본문을 3,000단어 이하로 유지 (이상적으로 1,500-2,000). 상세한 내용은 `references/`로 이동.

### 스킬 디렉토리 구조

```
skill-name/
├── SKILL.md              # 핵심 지식 (필수)
├── references/           # 필요시 로드되는 상세 문서
│   ├── patterns.md
│   └── advanced.md
├── examples/             # 작동하는 코드 예시
│   └── sample-config.json
└── scripts/              # 유틸리티 스크립트
    └── validate.sh
```

### 점진적 공개 수준

1. **메타데이터** (항상 컨텍스트에 포함): name + description (~100단어)
2. **SKILL.md 본문** (스킬이 트리거될 때): 핵심 지식 (<5,000단어)
3. **번들 리소스** (필요시): references, examples, scripts (무제한)

## Agents

**위치**: `agents/agent-name.md`
**형식**: YAML frontmatter가 포함된 마크다운

### Frontmatter 필드

| 필드         | 필수 | 타입   | 설명                                         |
| ------------- | -------- | ------ | --------------------------------------------------- |
| `name`        | 예      | String | 소문자, 하이픈, 3-50자                      |
| `description` | 예      | String | `<example>` 블록이 포함된 트리거 조건       |
| `model`       | 예      | String | `inherit`, `sonnet`, `opus`, 또는 `haiku`             |
| `color`       | 예      | String | `blue`, `cyan`, `green`, `yellow`, `magenta`, `red` |
| `tools`       | 아니오       | Array  | 특정 도구로 제한                          |

### 에이전트 예시

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

### 에이전트 이름 규칙

- 3-50자
- 소문자, 숫자, 하이픈만 사용
- 영숫자로 시작하고 끝나야 함
- 밑줄, 공백 또는 특수 문자 불가

### 색상 가이드라인

- Blue/Cyan: 분석, 검토
- Green: 성공 지향 작업
- Yellow: 주의, 검증
- Red: 중요, 보안
- Magenta: 창의적, 생성

## Hooks

**위치**: `hooks/hooks.json`
**형식**: JSON

### 사용 가능한 이벤트

| 이벤트              | 발생 시기                   |
| ------------------ | ------------------------------- |
| `PreToolUse`       | 도구 호출 실행 전     |
| `PostToolUse`      | 도구 호출 완료 후     |
| `Stop`             | Claude가 응답을 완료할 때 |
| `SubagentStop`     | 서브에이전트가 완료할 때        |
| `SessionStart`     | 세션이 시작될 때           |
| `SessionEnd`       | 세션이 종료될 때             |
| `UserPromptSubmit` | 사용자가 메시지를 보낼 때   |
| `PreCompact`       | 컨텍스트 압축 전       |
| `Notification`     | 알림이 발생할 때       |

### Hook 유형

**프롬프트 기반** (복잡한 로직에 권장):

```json
{
  "type": "prompt",
  "prompt": "Evaluate whether this file write follows project conventions: $TOOL_INPUT",
  "timeout": 30
}
```

지원되는 이벤트: Stop, SubagentStop, UserPromptSubmit, PreToolUse.

**명령 기반** (결정론적 검사):

```json
{
  "type": "command",
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/validate.sh",
  "timeout": 60
}
```

### hooks.json 예시

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

### Hook 출력 형식 (명령 Hook)

명령 Hook은 stdout으로 JSON을 반환합니다:

```json
{
  "decision": "block",
  "reason": "File write violates naming convention"
}
```

결정: `approve`, `block`, `ask_user` (확인 요청).

## MCP 서버

**위치**: 플러그인 루트의 `.mcp.json`
**형식**: JSON

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

**SSE** (원격 서버, server-sent events 전송):

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

**HTTP** (원격 서버, streamable HTTP 전송):

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

### 환경 변수 확장

모든 MCP 설정은 `${VAR_NAME}` 치환을 지원합니다:

- `${CLAUDE_PLUGIN_ROOT}` — 플러그인 디렉토리 (이식성을 위해 항상 사용)
- `${ANY_ENV_VAR}` — 사용자 환경 변수

플러그인 README에 필요한 모든 환경 변수를 문서화하세요.

### URL이 없는 디렉토리 서버

일부 MCP 디렉토리 항목은 엔드포인트가 동적이기 때문에 `url`이 없습니다. 플러그인은 URL 대신 **이름**으로 이러한 서버를 참조할 수 있습니다 — 플러그인의 MCP 설정에서 서버 이름이 디렉토리 항목 이름과 일치하면 URL 일치와 동일하게 처리됩니다.

## Commands (레거시)

> **새 플러그인에는 `skills/*/SKILL.md`를 사용하세요.** Cowork UI는 이제 commands와 skills를 하나의 "Skills" 개념으로 표시합니다. `commands/` 형식은 여전히 작동하지만, `$ARGUMENTS`/`$1` 치환과 인라인 bash 실행이 포함된 단일 파일 형식이 특별히 필요한 경우에만 사용하세요.

**위치**: `commands/command-name.md`
**형식**: 선택적 YAML frontmatter가 포함된 마크다운

### Frontmatter 필드

| 필드           | 필수 | 타입            | 설명                                         |
| --------------- | -------- | --------------- | --------------------------------------------------- |
| `description`   | 아니오       | String          | `/help`에 표시되는 간략한 설명 (60자 미만) |
| `allowed-tools` | 아니오       | String 또는 Array | 명령이 사용할 수 있는 도구                           |
| `model`         | 아니오       | String          | 모델 재정의: `sonnet`, `opus`, `haiku`           |
| `argument-hint` | 아니오       | String          | 자동완성을 위한 예상 인수 문서화       |

### 명령 예시

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

### 핵심 규칙

- Commands는 Claude를 위한 지시사항이지, 사용자를 위한 메시지가 아닙니다. 지시형으로 작성하세요.
- `$ARGUMENTS`는 모든 인수를 단일 문자열로 캡처합니다; `$1`, `$2`, `$3`는 위치 인수를 캡처합니다.
- `@path` 구문은 명령 컨텍스트에 파일 내용을 포함합니다.
- `!` 백틱 구문은 동적 컨텍스트를 위해 bash를 인라인으로 실행합니다 (예: `` !`git diff --name-only` ``).
- 플러그인 파일을 이식 가능하게 참조하려면 `${CLAUDE_PLUGIN_ROOT}`를 사용하세요.

### allowed-tools 패턴

```yaml
# 특정 도구
allowed-tools: Read, Write, Edit, Bash(git:*)

# 특정 명령만 허용하는 Bash
allowed-tools: Bash(npm:*), Read

# MCP 도구 (특정)
allowed-tools: ["mcp__plugin_name_server__tool_name"]
```

## CONNECTORS.md

**위치**: 플러그인 루트
**생성 시기**: 플러그인이 특정 제품이 아닌 카테고리별로 외부 도구를 참조할 때

### 형식

```markdown
# Connectors

## 도구 참조 방식

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. For example, `~~project tracker` might mean
Asana, Linear, Jira, or any other project tracker with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories
rather than specific products.

## 이 플러그인의 커넥터

| 카테고리        | 플레이스홀더         | 포함된 서버 | 기타 옵션            |
| --------------- | ------------------- | ---------------- | ------------------------ |
| Chat            | `~~chat`            | Slack            | Microsoft Teams, Discord |
| Project tracker | `~~project tracker` | Linear           | Asana, Jira, Monday      |
```

### ~~ 플레이스홀더 사용

플러그인 파일(skills, agents)에서 도구를 범용적으로 참조합니다:

```markdown
Check ~~project tracker for open tickets assigned to the user.
Post a summary to ~~chat in the team channel.
```

커스터마이징(cowork-plugin-customizer 스킬을 통해) 시 이러한 항목이 특정 도구 이름으로 대체됩니다.

## README.md

모든 플러그인에는 다음이 포함된 README가 있어야 합니다:

1. **개요** — 플러그인이 하는 일
2. **컴포넌트** — skills, agents, hooks, MCP 서버 목록
3. **설정** — 필요한 환경 변수 또는 구성
4. **사용법** — 각 스킬을 트리거하는 방법
5. **커스터마이징** — CONNECTORS.md가 있는 경우 이를 언급
