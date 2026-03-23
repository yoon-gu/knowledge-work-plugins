# Common Room 플러그인

Common Room으로 구동되는 GTM 워크플로입니다. 계정 조사, 연락처 조사, 통화 준비, 개인화 아웃리치, 프로스펙팅, 주간 브리핑을 지원합니다.

## 개요

이 플러그인은 Claude를 Common Room의 MCP 서버에 연결하고, 담당자가 가장 자주 사용하는 여섯 가지 워크플로를 다루는 스킬을 제공합니다. 모든 출력은 실제 Common Room 신호 데이터에 기반합니다. 여기에는 1차 제품 신호, 2차 커뮤니티 신호, 3차 의도 신호, 그리고 RoomieAI와 Spark의 보강 정보가 포함됩니다.

## 요구사항

- **Common Room MCP**(`mcp.commonroom.io/mcp`)는 반드시 연결 및 인증되어 있어야 합니다. 이것이 플러그인 기능 전반의 기본 데이터 소스입니다.
- **캘린더 커넥터**(선택 사항)는 `call-prep`와 `weekly-prep-brief`에서 미팅을 자동으로 조회할 수 있게 해줍니다. 연결되어 있지 않으면 두 스킬 모두 사용자의 미팅 세부 정보를 직접 요청합니다.

## 스킬

스킬은 대화 중 자연스럽게 활성화됩니다. 원하는 내용을 말하면 Claude가 자동으로 맞는 스킬을 불러옵니다.

| 스킬 | 트리거 문구 |
|-------|----------------|
| `account-research` | "Research [company]", "tell me about [domain]", "what's going on with [account]", "is [company] showing buying signals" |
| `contact-research` | "Who is [name]", "look up [email]", "research [contact]", "is [name] a warm lead" |
| `call-prep` | "Prep me for my call with [company]", "prepare for a meeting with [company]", "what should I know before talking to [company]" |
| `compose-outreach` | "Draft outreach to [person]", "write an email to [name]", "compose a message for [contact]" |
| `prospect` | "Find companies that match [criteria]", "build a prospect list", "find contacts at [type of company]" |
| `weekly-prep-brief` | "Weekly prep brief", "prepare my week", "what calls do I have this week" |

## 명령어

명시적으로 호출할 때 특히 유용한 복잡한 워크플로용 명령어 두 개가 있습니다.

| 명령어 | 용도 |
|---------|-------|
| `/generate-account-plan <company>` | 이해관계자 매핑, 참여도 분석, 기회, 위험, 실행 항목을 포함한 포괄적인 전략 계정 계획 생성 |
| `/weekly-brief [date range]` | 전체 주간 준비 브리핑 생성(기본값은 앞으로 7일) |

## 각 스킬의 결과물

**Account Research** - 전체 개요, 특정 필드 질문, 솔직한 희소 데이터 응답, MCP 데이터 + LLM 추론 결합이라는 네 가지 패턴을 처리합니다. 최근 뉴스에 대한 웹 검색도 포함합니다. 기본적으로 "My Segments"에 자동 범위를 맞춥니다.

**Contact Research** - 이메일, 이름+회사, 또는 소셜 핸들로 조회합니다. 보강된 신원 정보, CRM 필드, 점수, 웹사이트 방문, 활동 이력, Spark 분석, 대화 시작점을 반환합니다.

**Call Prep** - 회사 스냅샷, 참석자별 프로필, 신호 하이라이트, 맞춤형 대화 포인트, 예상 반론, 권장 통화 결과를 제공합니다. Gong/통화 녹음 활동을 우선시합니다. 연결되어 있으면 캘린더를 인식합니다.

**Compose Outreach** - Common Room 신호와 웹 검색 단서를 기반으로 한 세 가지 개인화 형식(이메일, 통화 스크립트, LinkedIn 메시지)을 생성합니다. 가능하면 사용자의 회사 포지셔닝에 맞춰 조정합니다.

**Prospecting** - 새 회사(ProspectorOrganization)와 기존 계정(Organization)을 구분합니다. 반복적인 세부 조정과 유사 회사 검색("find companies like [X]")을 지원합니다. 웹 검색은 새로 찾은 결과를 보강합니다.

**Weekly Prep Brief** - 앞으로 7일 동안의 모든 외부 통화를 포괄하는 전체 브리핑을 제공합니다. 회사 스냅샷, 참석자 프로필, 신호, 각 미팅별 권장 목표를 포함합니다.

## 설정

1. Cowork 설정에서 Common Room MCP 서버가 연결되고 인증되어 있는지 확인하세요.
2. 선택 사항으로, 통화 준비와 주간 브리핑용 자동 미팅 조회를 위해 캘린더 MCP 서버를 연결하세요.
3. 이 플러그인을 설치하세요. 모든 스킬과 명령어는 즉시 사용할 수 있습니다.

## 사용자 컨텍스트

사용자의 담당 구역으로 범위를 정하는 모든 스킬은 Common Room에서 자동으로 `Me` 객체를 가져옵니다. 이를 통해 사용자의 프로필, 역할, "My Segments"를 확인하고 쿼리가 기본적으로 담당 구역에 맞춰지도록 합니다. 자세한 내용은 `references/me-context.md`를 참고하세요.

회사 컨텍스트가 उपलब्ध하면 스킬은 사용자의 제품과 ICP에 맞춰 추천을 조정합니다. 자세한 내용은 `references/my-company-context.md`를 참고하세요.

## 사용자화

캘린더 커넥터와 도구 참조 방식에 대한 자세한 내용은 `CONNECTORS.md`를 참고하세요.
