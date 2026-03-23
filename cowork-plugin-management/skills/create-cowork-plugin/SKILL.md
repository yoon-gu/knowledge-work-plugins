---
name: create-cowork-plugin
description: >
  Cowork 세션에서 처음부터 새 플러그인을 만드는 과정을 사용자에게 안내합니다.
  사용자가 플러그인을 만들거나, 빌드하거나, 새 플러그인을 만들거나, 개발하거나, 스캐폴드하거나, 처음부터 시작하거나, 설계하고 싶을 때 사용합니다.
  이 스킬은 최종 .plugin 파일을 전달하기 위해 outputs 디렉토리에 접근할 수 있는 Cowork 모드가 필요합니다.
compatibility: 최종 .plugin 파일 전달을 위해 outputs 디렉토리에 접근할 수 있는 Cowork 데스크톱 앱 환경이 필요합니다.
---

# Cowork 플러그인 만들기

안내된 대화를 통해 처음부터 새 플러그인을 빌드합니다. 사용자를 발견, 계획, 설계, 구현 및 패키징 과정을 안내하며, 최종적으로 설치 준비가 된 `.plugin` 파일을 전달합니다.

## 개요

플러그인은 skills, agents, hooks 및 MCP 서버 통합으로 Claude의 기능을 확장하는 독립적인 디렉토리입니다. 이 스킬은 전체 플러그인 아키텍처와 대화형으로 플러그인을 만들기 위한 5단계 워크플로우를 인코딩합니다.

프로세스:

1. **발견** — 사용자가 무엇을 빌드하고 싶은지 이해
2. **컴포넌트 계획** — 어떤 컴포넌트 유형이 필요한지 결정
3. **설계 및 명확화 질문** — 각 컴포넌트를 상세하게 지정
4. **구현** — 모든 플러그인 파일 생성
5. **검토 및 패키징** — `.plugin` 파일 전달

> **비기술적 출력**: 모든 사용자 대면 대화를 평이한 언어로 유지합니다. 사용자가 요청하지 않는 한 파일 경로, 디렉토리 구조 또는 스키마 필드와 같은 구현 세부사항을 노출하지 마세요. 모든 것을 플러그인이 무엇을 할 것인지의 관점에서 설명하세요.

## 플러그인 아키텍처

### 디렉토리 구조

모든 플러그인은 다음 레이아웃을 따릅니다:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # 필수: 플러그인 매니페스트
├── skills/                   # 스킬 (SKILL.md가 있는 하위 디렉토리)
│   └── skill-name/
│       ├── SKILL.md
│       └── references/
├── agents/                   # 서브에이전트 정의 (.md 파일)
├── .mcp.json                 # MCP 서버 정의
└── README.md                 # 플러그인 문서
```

> **레거시 `commands/` 형식**: 이전 플러그인에는 단일 파일 `.md` 슬래시 명령이 있는 `commands/` 디렉토리가 포함될 수 있습니다. 이 형식은 여전히 작동하지만, 새 플러그인은 `skills/*/SKILL.md`를 사용해야 합니다 — Cowork UI는 둘 다 단일 "Skills" 개념으로 표시하며, skills 형식은 `references/`를 통한 점진적 공개를 지원합니다.

**규칙:**

- `.claude-plugin/plugin.json`은 항상 필수
- 컴포넌트 디렉토리(`skills/`, `agents/`)는 `.claude-plugin/` 내부가 아닌 플러그인 루트에 위치
- 플러그인이 실제로 사용하는 컴포넌트의 디렉토리만 생성
- 모든 디렉토리 및 파일 이름에 kebab-case 사용

### plugin.json 매니페스트

`.claude-plugin/plugin.json`에 위치합니다. 최소 필수 필드는 `name`입니다.

```json
{
  "name": "plugin-name",
  "version": "0.1.0",
  "description": "Brief explanation of plugin purpose",
  "author": {
    "name": "Author Name"
  }
}
```

**이름 규칙:** kebab-case, 소문자와 하이픈, 공백이나 특수 문자 불가.
**버전:** semver 형식 (MAJOR.MINOR.PATCH). `0.1.0`으로 시작.

선택적 필드: `homepage`, `repository`, `license`, `keywords`.

사용자 정의 컴포넌트 경로를 지정할 수 있습니다 (자동 검색을 대체하지 않고 보충):

```json
{
  "commands": "./custom-commands",
  "agents": ["./agents", "./specialized-agents"],
  "hooks": "./config/hooks.json",
  "mcpServers": "./.mcp.json"
}
```

### 컴포넌트 스키마

각 컴포넌트 유형에 대한 상세한 스키마는 `references/component-schemas.md`에 있습니다. 요약:

| 컴포넌트                          | 위치            | 형식                      |
| ---------------------------------- | ------------------- | --------------------------- |
| Skills                             | `skills/*/SKILL.md` | 마크다운 + YAML frontmatter |
| MCP 서버                        | `.mcp.json`         | JSON                        |
| Agents (Cowork에서 드물게 사용) | `agents/*.md`       | 마크다운 + YAML frontmatter |
| Hooks (Cowork에서 거의 사용 안 함)      | `hooks/hooks.json`  | JSON                        |
| Commands (레거시)                  | `commands/*.md`     | 마크다운 + YAML frontmatter |

이 스키마는 Claude Code의 플러그인 시스템과 공유되지만, 여기서는 지식 작업을 위한 데스크톱 앱인 Claude Cowork를 위한 플러그인을 만듭니다.
Cowork 사용자는 일반적으로 skills가 가장 유용합니다. **새 플러그인은 `skills/*/SKILL.md`로 스캐폴드하세요 — 사용자가 레거시 단일 파일 형식을 명시적으로 필요로 하지 않는 한 `commands/`를 만들지 마세요.**

### `~~` 플레이스홀더를 사용한 커스터마이징 가능한 플러그인

> **기본적으로 이 패턴을 사용하거나 물어보지 마세요.** 사용자가 조직 외부의 사람들이 플러그인을 사용하기를 원한다고 명시적으로 말하는 경우에만 `~~` 플레이스홀더를 도입하세요.
> 사용자가 플러그인을 외부에 배포하고 싶어하는 것 같으면 이것이 옵션임을 언급할 수 있지만, AskUserQuestion으로 이에 대해 선제적으로 질문하지 마세요.

플러그인이 회사 외부의 다른 사람들과 공유할 목적인 경우, 개별 사용자에게 맞게 조정해야 하는 부분이 있을 수 있습니다.
특정 제품이 아닌 카테고리별로 외부 도구를 참조해야 할 수 있습니다 (예: "Jira" 대신 "project tracker").
공유가 필요한 경우 범용적인 언어를 사용하고 `create an issue in ~~project tracker`와 같이 물결표 두 개로 커스터마이징이 필요한 부분을 표시합니다.
도구 카테고리를 사용한 경우, 플러그인 루트에 `CONNECTORS.md` 파일을 작성하여 설명합니다:

```markdown
# Connectors

## 도구 참조 방식

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. Plugins are tool-agnostic — they describe
workflows in terms of categories rather than specific products.

## 이 플러그인의 커넥터

| 카테고리        | 플레이스홀더         | 옵션                         |
| --------------- | ------------------- | ------------------------------- |
| Chat            | `~~chat`            | Slack, Microsoft Teams, Discord |
| Project tracker | `~~project tracker` | Linear, Asana, Jira             |
```

### ${CLAUDE_PLUGIN_ROOT} 변수

hooks와 MCP 설정에서 모든 플러그인 내부 경로 참조에 `${CLAUDE_PLUGIN_ROOT}`를 사용합니다. 절대 경로를 하드코딩하지 마세요.

## 안내 워크플로우

사용자에게 질문할 때는 AskUserQuestion을 사용합니다. "업계 표준" 기본값이 올바르다고 가정하지 마세요. 참고: AskUserQuestion에는 항상 건너뛰기 버튼과 자유 텍스트 입력 상자가 포함되므로, `None`이나 `Other`를 옵션으로 포함하지 마세요.

### Phase 1: 발견

**목표**: 사용자가 무엇을 빌드하고 싶은지, 그리고 왜인지 이해합니다.

질문합니다 (불분명한 것만 — 사용자의 초기 요청이 이미 답변한 질문은 건너뜁니다):

- 이 플러그인은 무엇을 해야 합니까? 어떤 문제를 해결합니까?
- 누가 어떤 맥락에서 사용합니까?
- 외부 도구나 서비스와 통합합니까?
- 참고할 유사한 플러그인이나 워크플로우가 있습니까?

이해한 내용을 요약하고 진행하기 전에 확인합니다.

**출력**: 플러그인 목적과 범위에 대한 명확한 설명.

### Phase 2: 컴포넌트 계획

**목표**: 플러그인에 어떤 컴포넌트 유형이 필요한지 결정합니다.

발견 답변을 기반으로 결정합니다:

- **Skills** — Claude가 필요에 따라 로드해야 하는 전문 지식이나 사용자 주도 작업이 필요합니까? (도메인 전문 지식, 참조 스키마, 워크플로우 가이드, 배포/구성/분석/검토 작업)
- **MCP 서버** — 외부 서비스 통합이 필요합니까? (데이터베이스, API, SaaS 도구)
- **Agents (드물게 사용)** — 자율적인 다단계 작업이 있습니까? (검증, 생성, 분석)
- **Hooks (거의 사용 안 함)** — 특정 이벤트에서 자동으로 발생해야 하는 것이 있습니까? (정책 시행, 컨텍스트 로드, 작업 검증)

만들지 않기로 결정한 컴포넌트 유형을 포함하여 컴포넌트 계획 표를 제시합니다:

```
| 컴포넌트 | 수량 | 목적 |
|-----------|-------|---------|
| Skills    | 3     | X에 대한 도메인 지식, /do-thing, /check-thing |
| Agents    | 0     | 필요 없음 |
| Hooks     | 1     | 쓰기 검증 |
| MCP       | 1     | 서비스 Y에 연결 |
```

진행하기 전에 사용자의 확인 또는 조정을 받습니다.

**출력**: 생성할 컴포넌트의 확인된 목록.

### Phase 3: 설계 및 명확화 질문

**목표**: 각 컴포넌트를 상세하게 지정합니다. 구현 전에 모든 모호성을 해결합니다.

계획의 각 컴포넌트 유형에 대해 타겟 설계 질문을 합니다. 컴포넌트 유형별로 질문을 그룹화하여 제시합니다. 답변을 기다린 후 진행합니다.

**Skills:**

- 어떤 사용자 쿼리가 이 스킬을 트리거해야 합니까?
- 어떤 지식 도메인을 다룹니까?
- 상세 콘텐츠를 위한 참조 파일을 포함해야 합니까?
- 스킬이 사용자 주도 작업을 나타내는 경우: 어떤 인수를 받고 어떤 도구가 필요합니까? (Read, Write, Bash, Grep 등)

**Agents:**

- 각 에이전트가 선제적으로 트리거되어야 합니까, 아니면 요청 시에만?
- 어떤 도구가 필요합니까?
- 출력 형식은 어떤 것이어야 합니까?

**Hooks:**

- 어떤 이벤트? (PreToolUse, PostToolUse, Stop, SessionStart 등)
- 어떤 동작 — 검증, 차단, 수정, 컨텍스트 추가?
- 프롬프트 기반 (LLM 구동) 또는 명령 기반 (결정론적 스크립트)?

**MCP 서버:**

- 어떤 서버 유형? (로컬은 stdio, OAuth가 있는 호스팅은 SSE, REST API는 HTTP)
- 어떤 인증 방법?
- 어떤 도구를 노출해야 합니까?

사용자가 "당신이 생각하는 최선으로"라고 말하면, 구체적인 권장 사항을 제공하고 명시적 확인을 받습니다.

**출력**: 모든 컴포넌트에 대한 상세 사양.

### Phase 4: 구현

**목표**: 모범 사례에 따라 모든 플러그인 파일을 생성합니다.

**작업 순서:**

1. 플러그인 디렉토리 구조 생성
2. `plugin.json` 매니페스트 생성
3. 각 컴포넌트 생성 (정확한 형식은 `references/component-schemas.md` 참조)
4. 플러그인을 문서화하는 `README.md` 생성

**구현 가이드라인:**

- **Skills**는 점진적 공개를 사용합니다: 간결한 SKILL.md 본문 (3,000단어 이하), 상세한 내용은 `references/`에. Frontmatter description은 구체적인 트리거 문구가 포함된 3인칭이어야 합니다. 스킬 본문은 Claude를 위한 지시사항이며 사용자를 위한 메시지가 아닙니다 — 무엇을 해야 하는지에 대한 지시형으로 작성하세요.
- **Agents**는 트리거 조건을 보여주는 `<example>` 블록이 있는 description과 마크다운 본문에 시스템 프롬프트가 필요합니다.
- **Hooks** 설정은 `hooks/hooks.json`에 들어갑니다. 스크립트 경로에 `${CLAUDE_PLUGIN_ROOT}`를 사용합니다. 복잡한 로직에는 프롬프트 기반 hooks를 선호합니다.
- **MCP 설정**은 플러그인 루트의 `.mcp.json`에 들어갑니다. 로컬 서버 경로에 `${CLAUDE_PLUGIN_ROOT}`를 사용합니다. README에 필요한 환경 변수를 문서화합니다.

### Phase 5: 검토 및 패키징

**목표**: 완성된 플러그인을 전달합니다.

1. 생성된 내용 요약 — 각 컴포넌트와 그 목적을 나열
2. 사용자에게 조정이 필요한지 질문
3. `claude plugin validate <path-to-plugin-json>`을 실행하여 플러그인 구조를 검사합니다. 이 명령을 사용할 수 없는 경우(예: Cowork 내부에서 실행 시), 수동으로 구조를 검증합니다:
   - `.claude-plugin/plugin.json`이 존재하고 최소한 `name` 필드가 있는 유효한 JSON을 포함
   - `name` 필드가 kebab-case (소문자, 숫자, 하이픈만)
   - 플러그인이 참조하는 모든 컴포넌트 디렉토리(`commands/`, `skills/`, `agents/`, `hooks/`)가 실제로 존재하고 예상 형식의 파일을 포함 — commands/skills/agents용 `.md`, hooks용 `.json`
   - 각 스킬 하위 디렉토리에 `SKILL.md`가 포함
   - CLI 검증기와 동일한 방식으로 통과/실패를 보고

   오류가 있으면 진행하기 전에 수정합니다.
4. `.plugin` 파일로 패키징:

```bash
cd /path/to/plugin-dir && zip -r /tmp/plugin-name.plugin . -x "*.DS_Store" && cp /tmp/plugin-name.plugin /path/to/outputs/plugin-name.plugin
```

> **중요**: 항상 `/tmp/`에서 먼저 zip을 생성한 다음 outputs 폴더에 복사합니다. outputs 폴더에 직접 쓰면 권한 문제로 실패할 수 있습니다.

> **이름 지정**: `.plugin` 파일에 `plugin.json`의 플러그인 이름을 사용합니다 (예: name이 `code-reviewer`이면, `code-reviewer.plugin`을 출력).

`.plugin` 파일은 채팅에서 리치 프리뷰로 표시되며, 사용자가 파일을 탐색하고 버튼을 눌러 플러그인을 수락할 수 있습니다.

## 모범 사례

- **작게 시작**: 최소한의 컴포넌트 세트로 시작합니다. 잘 만들어진 하나의 스킬이 있는 플러그인이 반쯤 완성된 다섯 개의 컴포넌트보다 더 유용합니다.
- **스킬의 점진적 공개**: 핵심 지식은 SKILL.md에, 상세한 참고 자료는 `references/`에, 작동하는 예시는 `examples/`에.
- **명확한 트리거 문구**: 스킬 description에는 사용자가 말할 구체적인 문구를 포함해야 합니다. 에이전트 description에는 `<example>` 블록을 포함해야 합니다.
- **스킬은 Claude를 위한 것**: 스킬 본문 내용은 Claude가 따라야 할 지시사항으로 작성하며, 사용자가 읽을 문서가 아닙니다.
- **명령형 작성 스타일**: 스킬에서 동사로 시작하는 지시를 사용합니다 ("Parse the config file," "You should parse the config file"가 아님).
- **이식성**: 플러그인 내부 경로에 항상 `${CLAUDE_PLUGIN_ROOT}`를 사용하며, 하드코딩된 경로는 절대 사용하지 않습니다.
- **보안**: 자격 증명에 환경 변수 사용, 원격 서버에 HTTPS, 최소 권한 도구 접근.

## 추가 리소스

- **`references/component-schemas.md`** — 모든 컴포넌트 유형(skills, agents, hooks, MCP, 레거시 commands, CONNECTORS.md)에 대한 상세 형식 명세
- **`references/example-plugins.md`** — 다양한 복잡도 수준의 세 가지 완전한 플러그인 구조 예시
