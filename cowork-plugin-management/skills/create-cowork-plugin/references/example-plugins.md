# 예제 플러그인

서로 다른 복잡성 수준의 세 가지 완전한 플러그인 구조. 4단계에서 구현할 때 이를 템플릿으로 사용하세요.

## 최소 플러그인: 단일 스킬

하나의 기술만 있고 다른 구성 요소는 없는 간단한 플러그인입니다.

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

### 플러그인.json

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

### Skills/meeting-notes/SKILL.md

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

도메인 지식, 사용자가 시작한 작업 및 외부 서비스 통합을 결합한 플러그인입니다.

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

### 플러그인.json

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

### 기술/검토-변경 사항/SKILL.md

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

### Skills/fix-lint/SKILL.md

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

### 기술/코딩 표준/SKILL.md

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
# Coding Standards

Project coding standards and conventions for consistent, high-quality code.

## Core Rules

- Use camelCase for variables and functions
- Use PascalCase for classes and types
- Prefer const over let; avoid var
- Maximum line length: 100 characters
- Use explicit return types on all exported functions

## Import Order

1. External packages
2. Internal packages (aliased with @/)
3. Relative imports
4. Type-only imports last

## Additional Resources

- **`references/style-rules.md`** — complete style rules by language
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

## 모든 기능을 갖춘 플러그인: 모든 구성요소 유형

도구에 구애받지 않는 커넥터와 기술, 에이전트, 후크 및 MCP 통합을 사용하는 플러그인입니다.

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

### 플러그인.json

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

### 에이전트/티켓 분석기.md

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

### 후크/hooks.json

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

### 커넥터.md

```markdown
# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. Plugins are tool-agnostic.

## Connectors for this plugin

| Category        | Placeholder         | Included servers | Other options       |
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
