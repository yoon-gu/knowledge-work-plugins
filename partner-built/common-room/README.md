# Common Room Plugin

Common Room으로 구동되는 GTM 워크플로우 — 계정 리서치, 컨택 리서치, 콜 준비, 개인화된 아웃리치, 프로스펙팅, 주간 브리핑.

## 개요

이 플러그인은 Claude를 Common Room의 MCP 서버에 연결하고, 가장 일반적인 담당자 워크플로우를 다루는 여섯 가지 skill을 제공합니다. 모든 결과물은 실제 Common Room 시그널 데이터, 즉 1st-party 제품 시그널, 2nd-party 커뮤니티 시그널, 3rd-party 인텐트 시그널, RoomieAI 및 Spark의 enrichment를 기반으로 합니다.

## 요구 사항

- **Common Room MCP** (`mcp.commonroom.io/mcp`)가 연결되고 인증되어야 합니다. 이것이 모든 플러그인 기능의 주요 데이터 소스입니다.
- **Calendar connector** (선택 사항) — `call-prep` 및 `weekly-prep-brief`에서 자동 회의 조회를 활성화합니다. 연결되지 않은 경우, 두 skill 모두 사용자에게 회의 세부 정보를 요청합니다.

## Skills

Skill은 대화 방식으로 트리거됩니다. 원하는 것을 설명하면 Claude가 자동으로 적절한 skill을 불러옵니다.

| Skill | 트리거 문구 |
|-------|----------------|
| `account-research` | "Research [company]", "tell me about [domain]", "what's going on with [account]", "is [company] showing buying signals" |
| `contact-research` | "Who is [name]", "look up [email]", "research [contact]", "is [name] a warm lead" |
| `call-prep` | "Prep me for my call with [company]", "prepare for a meeting with [company]", "what should I know before talking to [company]" |
| `compose-outreach` | "Draft outreach to [person]", "write an email to [name]", "compose a message for [contact]" |
| `prospect` | "Find companies that match [criteria]", "build a prospect list", "find contacts at [type of company]" |
| `weekly-prep-brief` | "Weekly prep brief", "prepare my week", "what calls do I have this week" |

## Commands

명시적 호출이 유용한 복잡한 워크플로우를 위한 두 가지 command:

| Command | 사용법 |
|---------|-------|
| `/generate-account-plan <company>` | 이해관계자 매핑, 인게이지먼트 분석, 기회, 리스크, 액션 아이템을 포함한 포괄적인 전략적 계정 계획 |
| `/weekly-brief [date range]` | 전체 주간 준비 브리핑 생성 (기본값: 향후 7일) |

## 각 Skill이 생성하는 결과물

**Account Research** — 네 가지 패턴을 처리: 전체 개요, 특정 필드 질문, 데이터 부족 시 솔직한 응답, MCP 데이터 + LLM 추론 결합. 최신 뉴스를 위한 웹 검색 포함. 자동으로 "My Segments"로 범위 한정.

**Contact Research** — 이메일, 이름+회사, 소셜 핸들로 조회. enriched identity, CRM 필드, 점수, 웹사이트 방문, 활동 이력, Spark 분석, 대화 시작 문구 반환.

**Call Prep** — 회사 스냅샷, 참석자별 프로필, 시그널 하이라이트, 맞춤 대화 포인트, 예상 이의 사항, 권장 콜 결과. Gong/콜 녹음 활동 우선 처리. 연결 시 캘린더 인식.

**Compose Outreach** — Common Room 시그널과 웹 검색 훅을 기반으로 한 세 가지 개인화된 형식 (이메일, 콜 스크립트, LinkedIn 메시지). 사용 가능한 경우 사용자의 회사 포지셔닝에 맞게 조정.

**Prospecting** — 신규 회사(ProspectorOrganization)와 기존 계정(Organization)을 구분. 반복적 정제 및 유사 검색("find companies like [X]") 지원. 웹 검색으로 신규 결과 보강.

**Weekly Prep Brief** — 향후 7일간의 모든 외부 콜을 다루는 전체 브리핑: 회사 스냅샷, 참석자 프로필, 시그널, 회의별 권장 목표.

## 설정

1. Cowork 설정에서 Common Room MCP 서버가 연결되고 인증되어 있는지 확인하십시오.
2. (선택 사항) 콜 준비 및 주간 브리핑에서 자동 회의 조회를 위해 캘린더 MCP 서버를 연결하십시오.
3. 이 플러그인을 설치하십시오. 모든 skill과 command를 즉시 사용할 수 있습니다.

## 사용자 컨텍스트

사용자의 담당 구역으로 범위를 한정하는 모든 skill은 Common Room에서 `Me` 객체를 자동으로 가져옵니다. 이를 통해 사용자의 프로필, 역할, "My Segments"를 제공하여 쿼리가 기본적으로 담당 구역으로 한정됩니다. 자세한 내용은 `references/me-context.md`를 참조하십시오.

회사 컨텍스트가 사용 가능한 경우, skill은 사용자의 제품 및 ICP에 맞게 권장 사항을 조정합니다. 자세한 내용은 `references/my-company-context.md`를 참조하십시오.

## 커스터마이징

캘린더 connector 및 도구 참조 작동 방식에 대한 자세한 내용은 `CONNECTORS.md`를 참조하십시오.
