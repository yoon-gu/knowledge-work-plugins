---
name: create-cowork-plugin
description: >
  공동 작업 세션에서 처음부터 새 플러그인을 만드는 과정을 사용자에게 안내합니다.
  사용자가 플러그인 생성, 플러그인 빌드, 새 플러그인 만들기, 플러그인 개발, 플러그인 스캐폴드, 플러그인 처음부터 시작 또는 플러그인 디자인을 원할 때 사용합니다.
  이 기술을 사용하려면 최종 .plugin 파일을 전달하기 위해 출력 디렉터리에 액세스할 수 있는 Cowork 모드가 필요합니다.
compatibility: Requires Cowork desktop app environment with access to the outputs directory for delivering .plugin files.
---

# Cowork 플러그인 만들기

안내된 대화를 통해 처음부터 새로운 플러그인을 구축하세요. 검색, 계획, 설계, 구현 및 패키징 과정을 사용자에게 안내하고 마지막에 바로 설치할 수 있는 `.plugin` 파일을 제공합니다.

## 개요

플러그인은 기술, 에이전트, 후크 및 MCP 서버 통합을 통해 Claude의 기능을 확장하는 독립형 디렉터리입니다. 이 기술은 전체 플러그인 아키텍처와 이를 대화식으로 생성하기 위한 5단계 워크플로를 인코딩합니다.

과정:

1. **발견** — 사용자가 구축하려는 것이 무엇인지 이해
2. **구성요소 계획** — 필요한 구성요소 유형 결정
3. **설계 및 명확화 질문** - 각 구성 요소를 자세히 지정합니다.
4. **구현** — 모든 플러그인 파일 생성
5. **검토 및 패키지** — `.plugin` 파일 전달

> **비기술적 출력**: 사용자가 접하는 모든 대화를 일반 언어로 유지합니다. 사용자가 요청하지 않는 한 파일 경로, 디렉터리 구조, 스키마 필드와 같은 구현 세부정보를 노출하지 마세요. 플러그인이 수행할 작업 측면에서 모든 것을 구성합니다.

## 플러그인 아키텍처

### 디렉토리 구조

모든 플러그인은 다음 레이아웃을 따릅니다.

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: plugin manifest
├── skills/                   # Skills (subdirectories with SKILL.md)
│   └── skill-name/
│       ├── SKILL.md
│       └── references/
├── agents/                   # Subagent definitions (.md files)
├── .mcp.json                 # MCP server definitions
└── README.md                 # Plugin documentation
```

> **레거시 `commands/` 형식**: 이전 플러그인에는 단일 파일 `.md` 슬래시 명령이 있는 `commands/` 디렉터리가 포함될 수 있습니다. 이 형식은 여전히 ​​작동하지만 새 플러그인은 대신 `skills/*/SKILL.md`을 사용해야 합니다. Cowork UI는 두 가지를 모두 단일 "Skills" 개념으로 표시하고 기술 형식은 `references/`를 통해 점진적인 공개를 지원합니다.

**규칙:**

- `.claude-plugin/plugin.json`은(는) 항상 필요합니다.
- 구성 요소 디렉터리(`skills/`, `agents/`)는 `.claude-plugin/` 내부가 아닌 플러그인 루트에 있습니다.
- 플러그인이 실제로 사용하는 구성요소에 대한 디렉토리만 생성
- 모든 디렉터리 및 파일 이름에 kebab-case를 사용하세요.

### 플러그인.json 매니페스트

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

**이름 규칙:** 케밥 대소문자, 하이픈 포함 소문자, 공백이나 특수 문자 없음. **버전:** semver 형식(MAJOR.MINOR.PATCH). `0.1.0`에서 시작하세요.

선택 필드: `homepage`, `repository`, `license`, `keywords`.

사용자 정의 구성요소 경로를 지정할 수 있습니다(보충, 대체하지 않음, 자동 검색).

```json
{
  "commands": "./custom-commands",
  "agents": ["./agents", "./specialized-agents"],
  "hooks": "./config/hooks.json",
  "mcpServers": "./.mcp.json"
}
```

### 구성요소 스키마

각 구성요소 유형에 대한 자세한 스키마는 `references/component-schemas.md`에 있습니다. 요약:

| 요소 | 위치 | 체재 |
| ---------------------------------- | ------ | -------------- |
| 기술 | `skills/*/SKILL.md` | 마크다운 + YAML 서문 |
| MCP 서버 | `.mcp.json` | JSON |
| 에이전트(Cowork에서는 자주 사용되지 않음) | `agents/*.md` | 마크다운 + YAML 서문 |
| Hooks (Cowork에서는 거의 사용되지 않음) | `hooks/hooks.json` | JSON |
| 명령(레거시) | `commands/*.md` | 마크다운 + YAML 서문 |

이 스키마는 지식 작업을 수행하기 위한 데스크톱 앱인 Claude Cowork용 플러그인을 만드는 Claude Code's plugin system, but you'와 공유됩니다. Cowork 사용자는 일반적으로 기술이 가장 유용하다고 생각합니다. **`skills/*/SKILL.md`을 사용한 스캐폴드 새 플러그인 — 사용자가 기존 단일 파일 형식을 명시적으로 필요로 하지 않는 한 `commands/`을 생성하지 마십시오.**

### `~~` 자리 표시자를 사용하여 사용자 정의 가능한 플러그인

> **기본적으로 이 패턴을 사용하거나 질문하지 마세요.** 사용자가 조직 외부의 사람들이 플러그인을 사용하기를 명시적으로 원하는 경우에만 `~~` 자리 표시자를 도입하세요.
> 사용자가 플러그인을 외부에 배포하고 싶어하는 것처럼 보이면 이것이 옵션이라고 언급할 수 있지만 AskUserQuestion을 통해 이에 대해 사전에 질문하지 마세요.

플러그인을 회사 외부의 다른 사람들과 공유하려는 경우 개별 사용자에게 맞게 조정해야 하는 부분이 있을 수 있습니다. 특정 제품이 아닌 카테고리별로 외부 도구를 참조해야 할 수도 있습니다(예: "Jira" 대신 "project tracker"). 공유가 필요한 경우 일반 언어를 사용하고 `create an issue in ~~project tracker`와 같은 두 개의 물결표 문자를 사용하여 사용자 정의가 필요하다고 표시하세요. 도구 카테고리를 사용한 경우 플러그인 루트에 `CONNECTORS.md` 파일을 작성하여 다음을 설명하세요.

```markdown
# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. Plugins are tool-agnostic — they describe
workflows in terms of categories rather than specific products.

## Connectors for this plugin

| Category        | Placeholder         | Options                         |
| --------------- | ------------------- | ------------------------------- |
| Chat            | `~~chat`            | Slack, Microsoft Teams, Discord |
| Project tracker | `~~project tracker` | Linear, Asana, Jira             |
```

### ${CLAUDE_PLUGIN_ROOT} 변수

후크 및 MCP 구성의 모든 플러그인 내 경로 참조에 `${CLAUDE_PLUGIN_ROOT}`을 사용하세요. 절대 경로를 하드코딩하지 마세요.

## 안내된 작업 흐름

사용자에게 무엇인가를 물어볼 때는 AskUserQuestion을 사용하세요. "industry standard" 기본값이 정확하다고 가정하지 마세요. 참고: AskUserQuestion에는 항상 건너뛰기 버튼과 맞춤 답변을 위한 자유 텍스트 입력 상자가 포함되어 있으므로 `None` 또는 `Other`를 옵션으로 포함하지 마세요.

### 1단계: 발견

**목표**: 사용자가 빌드하려는 항목과 이유를 이해합니다.

질문하세요(불분명한 것만 - 사용자의 초기 요청이 이미 답변한 경우 질문을 건너뛰세요):

- 이 플러그인은 무엇을 해야 합니까? 어떤 문제가 해결되나요?
- 누가, 어떤 맥락에서 사용할 것인가?
- 외부 도구나 서비스와 통합됩니까?
- 참조할 수 있는 유사한 플러그인이나 작업 흐름이 있나요?

계속 진행하기 전에 이해한 내용을 요약하고 확인하세요.

**출력**: 플러그인 목적과 범위에 대한 명확한 설명입니다.

### 2단계: 구성 요소 계획

**목표**: 플러그인에 필요한 구성 요소 유형을 결정합니다.

발견 답변을 바탕으로 다음을 결정합니다.

- **기술** — Claude가 온디맨드 또는 사용자 시작 작업을 로드해야 한다는 전문 지식이 필요합니까? (도메인 전문 지식, 참조 스키마, 워크플로 가이드, 배포/구성/분석/검토 작업)
- **MCP 서버** — 외부 서비스 통합이 필요합니까? (데이터베이스, API, SaaS 도구)
- **에이전트(흔하지 않음)** — 자율적인 다단계 작업이 있습니까? (검증, 생성, 분석)
- **후크(희귀)** — 특정 이벤트에서 자동으로 어떤 일이 발생해야 합니까? (정책 시행, 컨텍스트 로드, 작업 검증)

생성하지 않기로 결정한 구성 요소 유형을 포함하여 구성 요소 계획표를 제시합니다.

```
| Component | Count | Purpose |
|-----------|-------|---------|
| Skills    | 3     | Domain knowledge for X, /do-thing, /check-thing |
| Agents    | 0     | Not needed |
| Hooks     | 1     | Validate writes |
| MCP       | 1     | Connect to service Y |
```

계속하기 전에 사용자 확인이나 조정을 받으세요.

**출력**: 생성할 확인된 구성 요소 목록입니다.

### 3단계: 질문 설계 및 명확화

**목표**: 각 구성 요소를 자세히 지정합니다. 구현하기 전에 모든 모호성을 해결하십시오.

계획의 각 구성요소 유형에 대해 대상 설계 질문을 하십시오. 구성 요소 유형별로 그룹화된 질문을 제시합니다. 계속하기 전에 답변을 기다리십시오.

**기술:**

- 이 기술을 트리거해야 하는 사용자 쿼리는 무엇입니까?
- 어떤 지식 영역을 다루고 있나요?
- 자세한 내용에 대한 참조 파일을 포함해야 합니까?
- 스킬이 사용자 시작 작업을 나타내는 경우 어떤 인수를 허용하며 어떤 도구가 필요합니까? (읽기, 쓰기, Bash, Grep 등)

**자치령 대표:**

- 각 에이전트는 사전에 트리거해야 합니까, 아니면 요청된 경우에만 트리거해야 합니까?
- 어떤 도구가 필요합니까?
- 출력 형식은 무엇이어야 합니까?

**후크:**

- 어떤 이벤트인가요? (PreToolUse, PostToolUse, 중지, SessionStart 등)
- 어떤 행동 — 유효성 검사, 차단, 수정, 컨텍스트 추가?
- 프롬프트 기반(LLM 기반) 또는 명령 기반(결정적 스크립트)?

**MCP 서버:**

- 어떤 서버 유형인가요? (로컬의 경우 stdio, OAuth 호스팅의 경우 SSE, REST API의 경우 HTTP)
- 어떤 인증 방법이 있나요?
- 어떤 도구가 노출되어야 합니까?

사용자가 "whatever you think is best,"이라고 말하면 구체적인 권장사항을 제공하고 명시적인 확인을 받습니다.

**출력**: 모든 구성 요소에 대한 세부 사양입니다.

### 4단계: 구현

**목표**: 모범 사례에 따라 모든 플러그인 파일을 만듭니다.

**작업 순서:**

1. 플러그인 디렉토리 구조 생성
2. `plugin.json` 매니페스트 만들기
3. 각 구성 요소를 만듭니다(정확한 형식은 `references/component-schemas.md` 참조).
4. 플러그인을 문서화하는 `README.md` 생성

**구현 지침:**

- **스킬**은 점진적 공개를 사용합니다. 간결한 SKILL.md 본문(3,000단어 미만), 자세한 내용은 `references/`에 있습니다. 머리말 설명은 특정 트리거 문구가 포함된 3인칭이어야 합니다. 스킬 본문은 사용자에게 보내는 메시지가 아니라 Claude를 위한 지침입니다. 수행할 작업에 대한 지침으로 작성하세요.
- **에이전트**에는 트리거 조건을 보여주는 `<example>` 블록에 대한 설명과 마크다운 본문에 시스템 프롬프트가 필요합니다.
- **후크** 구성은 `hooks/hooks.json`에 들어갑니다. 스크립트 경로에는 `${CLAUDE_PLUGIN_ROOT}`을 사용하세요. 복잡한 논리에는 프롬프트 기반 후크를 선호합니다.
- **MCP 구성**은 플러그인 루트의 `.mcp.json`에 들어갑니다. 로컬 서버 경로에는 `${CLAUDE_PLUGIN_ROOT}`을 사용하세요. README에 필요한 환경 변수를 문서화하세요.

### 5단계: 검토 및 패키지

**목표**: 완성된 플러그인을 제공합니다.

1. 생성된 내용을 요약합니다. 각 구성 요소와 해당 목적을 나열합니다.
2. 사용자가 조정을 원하는지 묻습니다.
3. `claude plugin validate <path-to-plugin-json>`을 실행하여 플러그인 구조를 확인하세요. 이 명령을 사용할 수 없는 경우(예: Cowork 내부에서 실행하는 경우) 구조를 수동으로 확인하세요.
   - `.claude-plugin/plugin.json`이(가) 존재하며 최소한 `name` 필드가 있는 유효한 JSON을 포함합니다.
   - `name` 필드는 케밥 대소문자(소문자, 숫자, 하이픈만)입니다.
   - 플러그인에서 참조하는 모든 구성 요소 디렉터리(`commands/`, `skills/`, `agents/`, `hooks/`)는 실제로 존재하며 예상 형식(명령/스킬/에이전트의 경우 `.md`, 후크의 경우 `.json`)의 파일을 포함합니다.
   - 각 기술 하위 디렉터리에는 `SKILL.md`이 포함되어 있습니다.
   - CLI 유효성 검사기와 동일한 방식으로 통과한 것과 통과하지 못한 것을 보고합니다.

계속하기 전에 오류를 수정하세요.
4. `.plugin` 파일로 패키지:

```bash
cd /path/to/plugin-dir && zip -r /tmp/plugin-name.plugin . -x "*.DS_Store" && cp /tmp/plugin-name.plugin /path/to/outputs/plugin-name.plugin
```

> **중요**: 항상 `/tmp/`에 zip을 먼저 만든 다음 출력 폴더에 복사하세요. 권한으로 인해 출력 폴더에 직접 쓰지 못할 수 있습니다.

> **이름 지정**: `.plugin` 파일에 `plugin.json`의 플러그인 이름을 사용합니다(예: 이름이 `code-reviewer`인 경우 `code-reviewer.plugin`을 출력합니다).

`.plugin` 파일은 사용자가 버튼을 눌러 파일을 탐색하고 플러그인을 수락할 수 있는 풍부한 미리보기로 채팅에 표시됩니다.

## 모범 사례

- **작게 시작**: 실행 가능한 최소 구성 요소 세트로 시작합니다. 잘 만들어진 기술 하나가 포함된 플러그인은 5개의 절반만 구운 구성 요소가 포함된 플러그인보다 더 유용합니다.
- **기술에 대한 점진적 공개**: SKILL.md의 핵심 지식, `references/`의 자세한 참조 자료, `examples/`의 작업 예제.
- **명확한 트리거 문구**: 스킬 설명에는 사용자가 말할 특정 문구가 포함되어야 합니다. 에이전트 설명에는 `<example>` 블록이 포함되어야 합니다.
- **스킬은 클로드를 위한 것입니다**: 사용자가 읽을 문서가 아닌 클로드가 따라야 할 지침으로 스킬 본문 콘텐츠를 작성합니다.
- **명령형 글쓰기 스타일**: 기술에 동사 우선 지침을 사용하세요("Parse the config file," 아님 "You should parse the config file").
- **이식성**: 플러그인 내 경로에는 항상 `${CLAUDE_PLUGIN_ROOT}`을 사용하고 하드코딩된 경로는 사용하지 마세요.
- **보안**: 자격 증명에는 환경 변수를 사용하고 원격 서버에는 HTTPS를 사용하며 최소 권한 도구 액세스를 사용합니다.

## 추가 리소스

- **`references/component-schemas.md`** — 모든 구성 요소 유형(스킬, 에이전트, 후크, MCP, 레거시 명령, CONNECTORS.md)에 대한 자세한 형식 사양
- **`references/example-plugins.md`** — 서로 다른 복잡성 수준의 세 가지 완전한 예제 플러그인 구조
