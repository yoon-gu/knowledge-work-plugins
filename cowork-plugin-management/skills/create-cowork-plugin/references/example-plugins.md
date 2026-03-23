# 플러그인 예시

다양한 복잡도 수준의 세 가지 완전한 플러그인 구조입니다. Phase 4에서 구현할 때 이를 템플릿으로 사용하세요.

## 최소 플러그인: 단일 스킬

하나의 스킬만 있고 다른 컴포넌트가 없는 간단한 플러그인입니다.

### 구조

```
meeting-notes/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── meeting-notes/
│       └── SKILL.md
└── README.md
```

### plugin.json

```json
{
  "name": "meeting-notes",
  "version": "0.1.0",
  "description": "Generate structured meeting notes from transcripts",
  "author": {
    "name": "User"
  }
}
```

### skills/meeting-notes/SKILL.md

```markdown
---
name: meeting-notes
description: >
  Generate structured meeting notes from a transcript. Use when the user asks
  to "summarize this meeting", "create meeting notes", "extract action items
  from this transcript", or provides a meeting transcript file.
---

Read the transcript file the user provided and generate structured meeting notes.

Include these sections:

1. **Attendees** — list all participants mentioned
2. **Summary** — 2-3 sentence overview of the meeting
3. **Key Decisions** — numbered list of decisions made
4. **Action Items** — table with columns: Owner, Task, Due Date
5. **Open Questions** — anything unresolved

Write the notes to a new file named after the transcript with `-notes` appended.
```

---

## 표준 플러그인: Skills + MCP

도메인 지식, 사용자 주도 작업 및 외부 서비스 통합을 결합한 플러그인입니다.

### 구조

```
code-quality/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── coding-standards/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── style-rules.md
│   ├── review-changes/
│   │   └── SKILL.md
│   └── fix-lint/
│       └── SKILL.md
├── .mcp.json
└── README.md
```

### plugin.json

```json
{
  "name": "code-quality",
  "version": "0.1.0",
  "description": "Enforce coding standards with reviews, linting, and style guidance",
  "author": {
    "name": "User"
  }
}
```

### skills/review-changes/SKILL.md

```markdown
---
name: review-changes
description: >
  Review code changes for style and quality issues. Use when the user asks to
  "review my changes", "check this diff", "review for style violations", or
  wants a code quality pass on uncommitted work.
---

Run `git diff --name-only` to get the list of changed files.

For each changed file:

1. Read the file
2. Check against the coding-standards skill for style violations
3. Identify potential bugs or anti-patterns
4. Flag any security concerns

Present a summary with:

- File path
- Issue severity (Error, Warning, Info)
- Description and suggested fix
```

### skills/fix-lint/SKILL.md

```markdown
---
name: fix-lint
description: >
  Auto-fix linting issues in changed files. Use when the user asks to
  "fix lint errors", "clean up linting", or "auto-fix my lint issues".
---

Run the linter: `npm run lint -- --format json 2>&1`

Parse the linter output and fix each issue:

- For auto-fixable issues, apply the fix directly
- For manual-fix issues, make the correction following project conventions
- Skip issues that require architectural changes

After all fixes, run the linter again to confirm clean output.
```

### skills/coding-standards/SKILL.md

```yaml
---
name: coding-standards
description: >
  This skill should be used when the user asks about "coding standards",
  "style guide", "naming conventions", "code formatting rules", or needs
  guidance on project-specific code quality expectations.
metadata:
  version: "0.1.0"
---
```

```markdown
# 코딩 표준

일관되고 고품질의 코드를 위한 프로젝트 코딩 표준 및 규칙입니다.

## 핵심 규칙

- 변수와 함수에는 camelCase 사용
- 클래스와 타입에는 PascalCase 사용
- let보다 const 선호; var 사용 금지
- 최대 줄 길이: 100자
- 모든 내보낸 함수에 명시적 반환 타입 사용

## Import 순서

1. 외부 패키지
2. 내부 패키지 (@/로 별칭)
3. 상대 import
4. 타입 전용 import은 마지막에

## 추가 리소스

- **`references/style-rules.md`** — 언어별 완전한 스타일 규칙
```

### .mcp.json

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

---

## 완전한 기능의 플러그인: 모든 컴포넌트 유형

skills, agents, hooks 및 도구 비의존적 커넥터가 포함된 MCP 통합을 사용하는 플러그인입니다.

### 구조

```
engineering-workflow/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── team-processes/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── workflow-guide.md
│   ├── standup-prep/
│   │   └── SKILL.md
│   └── create-ticket/
│       └── SKILL.md
├── agents/
│   └── ticket-analyzer.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── CONNECTORS.md
└── README.md
```

### plugin.json

```json
{
  "name": "engineering-workflow",
  "version": "0.1.0",
  "description": "Streamline engineering workflows: standup prep, ticket management, and code quality",
  "author": {
    "name": "User"
  },
  "keywords": ["engineering", "workflow", "tickets", "standup"]
}
```

### agents/ticket-analyzer.md

```markdown
---
name: ticket-analyzer
description: Use this agent when the user needs to analyze tickets, triage incoming issues, or prioritize a backlog.

<example>
Context: User is preparing for sprint planning
user: "Help me triage these new tickets"
assistant: "I'll use the ticket-analyzer agent to review and categorize the tickets."
<commentary>
Ticket triage requires systematic analysis across multiple dimensions, making the agent appropriate.
</commentary>
</example>

<example>
Context: User has a large backlog
user: "Prioritize my backlog for next sprint"
assistant: "Let me analyze the backlog using the ticket-analyzer agent to recommend priorities."
<commentary>
Backlog prioritization is a multi-step autonomous task well-suited for the agent.
</commentary>
</example>

model: inherit
color: cyan
tools: ["Read", "Grep"]
---

You are a ticket analysis specialist. Analyze tickets for priority, effort, and dependencies.

**Your Core Responsibilities:**

1. Categorize tickets by type (bug, feature, tech debt, improvement)
2. Estimate relative effort (S, M, L, XL)
3. Identify dependencies between tickets
4. Recommend priority ordering

**Analysis Process:**

1. Read all ticket descriptions
2. Categorize each by type
3. Estimate effort based on scope
4. Map dependencies
5. Rank by impact-to-effort ratio

**Output Format:**
| Ticket | Type | Effort | Dependencies | Priority |
|--------|------|--------|-------------|----------|
| ... | ... | ... | ... | ... |

Followed by a brief rationale for the top 5 priorities.
```

### hooks/hooks.json

```json
{
  "SessionStart": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "echo '## Team Context\n\nSprint cycle: 2 weeks. Standup: daily at 9:30 AM. Use ~~project tracker for ticket management.'",
          "timeout": 5
        }
      ]
    }
  ]
}
```

### CONNECTORS.md

```markdown
# Connectors

## 도구 참조 방식

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. Plugins are tool-agnostic.

## 이 플러그인의 커넥터

| 카테고리        | 플레이스홀더         | 포함된 서버 | 기타 옵션       |
| --------------- | ------------------- | ---------------- | ------------------- |
| Project tracker | `~~project tracker` | Linear           | Asana, Jira, Monday |
| Chat            | `~~chat`            | Slack            | Microsoft Teams     |
| Source control  | `~~source control`  | GitHub           | GitLab, Bitbucket   |
```

### .mcp.json

```json
{
  "mcpServers": {
    "linear": {
      "type": "sse",
      "url": "https://mcp.linear.app/sse"
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "slack": {
      "type": "http",
      "url": "https://slack.mcp.claude.com/mcp"
    }
  }
}
```
