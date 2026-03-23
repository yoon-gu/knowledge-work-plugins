# Design 플러그인

[Cowork](https://claude.com/product/cowork)을 위해 주로 설계된 디자인 생산성 플러그인입니다. Anthropic의 에이전틱 데스크톱 앱이지만 Claude Code에서도 작동합니다. 디자인 비평, 시스템 관리, UX 작성, 접근성, 리서치 종합, 개발자 인수인계를 돕습니다. 어떤 디자인 팀에도 잘 맞고, 입력만 있으면 독립적으로 동작하며, Figma와 다른 도구를 연결하면 더 강력해집니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/design
```

## 명령

슬래시 명령으로 호출하는 명시적 워크플로입니다:

| Command | Description |
|---|---|
| `/critique` | 사용성, 시각적 계층, 접근성, 일관성에 대한 구조화된 디자인 피드백 받기 |
| `/design-system` | 컴포넌트, 토큰, 패턴을 감사, 문서화, 확장하기 |
| `/handoff` | 측정값, 토큰, 상태, 상호작용, 엣지 케이스를 포함한 개발자 인수인계 명세 생성 |
| `/ux-copy` | 마이크로카피, 오류 메시지, 빈 상태, 온보딩 흐름 등 UX 카피 작성 또는 검토 |
| `/accessibility` | WCAG 준수, 색 대비, 스크린 리더, 키보드 내비게이션에 대한 접근성 감사 실행 |
| `/research-synthesis` | 인터뷰, 설문, 사용성 테스트를 실행 가능한 인사이트로 종합 |

모든 명령은 **독립 실행**(디자인을 설명하거나 스크린샷을 붙여넣기)할 수 있고, MCP 커넥터를 연결하면 **더 강력해집니다**.

## 스킬

Claude가 관련 있을 때 자동으로 사용하는 도메인 지식입니다:

| Skill | Description |
|---|---|
| `design-critique` | 사용성, 시각적 계층, 일관성, 디자인 원칙 준수 여부를 평가 |
| `design-system-management` | 디자인 토큰, 컴포넌트 라이브러리, 패턴 문서를 관리 |
| `ux-writing` | 명확하고 간결하며 일관되고 브랜드에 맞는 마이크로카피 작성 |
| `accessibility-review` | 디자인과 코드의 WCAG 2.1 AA 준수 여부를 감사 |
| `user-research` | 인터뷰, 설문, 사용성 테스트를 계획하고 수행하고 종합 |
| `design-handoff` | 디자인으로부터 포괄적인 개발자 인수인계 문서를 작성 |

## 예시 워크플로

### 디자인 피드백 받기

```
/critique
```

Figma 링크, 스크린샷, 또는 디자인 설명을 공유하세요. 사용성, 시각적 계층, 일관성, 접근성에 대한 구조화된 피드백을 받습니다.

### 디자인 시스템 감사하기

```
/design-system audit
```

컴포넌트 라이브러리의 일관성, 완성도, 명명 규칙을 검토합니다. 구체적인 개선 권고가 포함된 보고서를 받습니다.

### UX 카피 작성하기

```
/ux-copy error messages for payment flow
```

상황에 맞는 카피와 톤 가이드, 대안, 지역화 노트를 받습니다.

### 개발자 인수인계

```
/handoff
```

Figma 링크를 공유하면 측정값, 디자인 토큰, 컴포넌트 상태, 상호작용 노트, 엣지 케이스를 포함한 완전한 명세를 받습니다.

### 접근성 점검

```
/accessibility
```

디자인이나 URL을 공유하세요. 구체적인 문제, 심각도, 수정 단계가 포함된 WCAG 2.1 AA 준수 보고서를 받습니다.

### 리서치 종합

```
/research-synthesis
```

인터뷰 전사, 설문 결과, 사용성 테스트 노트를 업로드하세요. 주제, 인사이트, 우선순위가 매겨진 권고안을 받습니다.

## 독립 실행 + 더 강력한 모드

모든 명령과 스킬은 어떤 통합도 없이 작동합니다:

| What You Can Do | Standalone | Supercharged With |
|-----------------|------------|-------------------|
| Design critique | Describe or screenshot | Figma MCP (pull designs directly) |
| Design system | Describe your system | Figma MCP (audit component library) |
| Handoff specs | Describe or screenshot | Figma MCP (exact measurements, tokens) |
| UX copy | Describe the context | Knowledge base (brand voice guidelines) |
| Accessibility | Describe or screenshot | Figma MCP, analytics for real usage data |
| Research synthesis | Paste transcripts | User feedback tools (pull raw data) |

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 어떤 도구가 연결되어 있는지 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

더 풍부한 경험을 위해 도구를 연결하세요:

| Category | Examples | What It Enables |
|---|---|---|
| **Design tool** | Figma | 디자인을 불러오고, 컴포넌트를 살펴보고, 디자인 토큰에 접근 |
| **User feedback** | Intercom, Productboard | 원시 피드백, 기능 요청, NPS 데이터 |
| **Project tracker** | Linear, Asana, Jira | 디자인과 티켓을 연결하고 구현 추적 |
| **Knowledge base** | Notion | 브랜드 가이드라인, 디자인 원칙, 리서치 저장소 |
| **Product analytics** | Amplitude, Mixpanel | 리서치 종합과 디자인 결정을 위한 사용 데이터 |

지원되는 전체 통합 목록은 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.
