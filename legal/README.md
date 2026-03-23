# Legal Productivity Plugin

사내 법무팀을 위한 AI 기반 생산성 플러그인으로, Anthropic의 에이전틱 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 주로 설계되었으나 Claude Code에서도 작동합니다. 계약 검토, NDA 분류, 컴플라이언스 워크플로, 법률 브리핑, 템플릿 기반 응답 등을 자동화하며, 조직의 구체적인 플레이북과 위험 허용 범위에 맞게 모두 구성할 수 있습니다.

> **면책 조항:** 이 플러그인은 법률 워크플로를 지원하지만 법률 조언을 제공하지는 않습니다. 항상 자격을 갖춘 법률 전문가와 결론을 검토하십시오. AI가 생성한 분석은 법적 결정에 의존하기 전에 면허를 보유한 변호사가 검토해야 합니다. 이 플러그인의 기본 플레이북 예시는 미국 법률 입장 및 관할권(델라웨어, 뉴욕, 캘리포니아)을 반영합니다. 다른 법률 시스템(EU, UK, 네덜란드, 호주 등)에서 운영하는 경우, 플러그인의 분석에 의존하기 전에 .claude/legal.local.md의 플레이북을 해당 관할권의 특정 법적 요건, 표준 계약 조건 및 컴플라이언스 의무를 반영하도록 반드시 맞춤 설정해야 합니다.

## 대상 사용자

- **상업 법무(Commercial Counsel)** -- 계약 협상, 벤더 관리, 거래 지원
- **제품 법무(Product Counsel)** -- 제품 검토, 서비스 약관, 개인정보 처리방침, IP 사항
- **개인정보 보호/컴플라이언스** -- 데이터 보호 규정, DPA 검토, 정보 주체 요청, 규제 모니터링
- **소송 지원** -- 증거 보존 명령, 문서 검토 준비, 사건 브리핑

## 설치

```
claude plugins add knowledge-work-plugins/legal
```

## 빠른 시작

### 1. 플러그인 설치

```
claude plugins add knowledge-work-plugins/legal
```

### 2. 플레이북 구성

조직의 표준 입장을 정의하는 로컬 설정 파일을 생성합니다. 팀의 협상 플레이북, 위험 허용 범위 및 표준 조건을 여기에 인코딩합니다.

Claude가 찾을 수 있는 위치에 `legal.local.md` 파일을 생성합니다:

- **Cowork**: Cowork와 공유한 폴더(폴더 선택기 사용)에 저장합니다. 플러그인이 자동으로 찾습니다.
- **Claude Code**: 프로젝트의 `.claude/` 디렉토리에 저장합니다.

```markdown
# Legal Playbook Configuration

## Contract Review Positions

### Limitation of Liability
- Standard position: Mutual cap at 12 months of fees paid/payable
- Acceptable range: 6-24 months of fees
- Escalation trigger: Uncapped liability, consequential damages inclusion

### Indemnification
- Standard position: Mutual indemnification for IP infringement and data breach
- Acceptable: Indemnification limited to third-party claims only
- Escalation trigger: Unilateral indemnification obligations, uncapped indemnification

### IP Ownership
- Standard position: Each party retains pre-existing IP; customer owns customer data
- Escalation trigger: Broad IP assignment clauses, work-for-hire provisions for pre-existing IP

### Data Protection
- Standard position: Require DPA for any personal data processing
- Requirements: Sub-processor notification, data deletion on termination, breach notification within 72 hours
- Escalation trigger: No DPA offered, cross-border transfer without safeguards

### Term and Termination
- Standard position: Annual term with 30-day termination for convenience
- Acceptable: Multi-year with termination for convenience after initial term
- Escalation trigger: Auto-renewal without notice period, no termination for convenience

### Governing Law
- Preferred: [Your jurisdiction]
- Acceptable: Major commercial jurisdictions (NY, DE, CA, England & Wales)
- Escalation trigger: Non-standard jurisdictions, mandatory arbitration in unfavorable venue

## NDA Defaults
- Mutual obligations required
- Term: 2-3 years standard, 5 years for trade secrets
- Standard carveouts: independently developed, publicly available, rightfully received from third party
- Residuals clause: acceptable if narrowly scoped

## Response Templates
Configure paths to your template files or define inline templates for common inquiries.
```

### 3. 도구 연결

플러그인은 MCP를 통해 기존 도구와 연결될 때 최적으로 작동합니다. 미리 구성된 서버에는 Slack, Box, Egnyte, Atlassian, Microsoft 365가 포함됩니다. 지원되는 카테고리 및 옵션의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참조하십시오.

## 명령어

### `/review-contract` -- 플레이북 기준 계약 검토

조직의 협상 플레이북에 따라 계약을 검토합니다. 이탈 사항을 표시하고, 수정 제안을 생성하며, 비즈니스 영향 분석을 제공합니다.

```
/review-contract
```

파일 업로드, URL, 또는 붙여넣은 계약 텍스트를 허용합니다. 컨텍스트(귀사 측, 마감일, 중점 영역)를 요청하고 구성된 플레이북에 따라 조항별로 검토합니다.

### `/triage-nda` -- NDA 사전 심사

표준 기준에 따라 수신된 NDA를 신속하게 분류합니다. GREEN(표준 승인), YELLOW(법무 검토 필요), 또는 RED(중대한 문제)로 분류합니다.

```
/triage-nda
```

### `/vendor-check` -- 벤더 계약 상태 확인

연결된 시스템 전반에서 벤더와의 기존 계약 상태를 확인합니다.

```
/vendor-check [vendor name]
```

기존 NDA, MSA, DPA, 만료일 및 주요 조건을 보고합니다.

### `/brief` -- 법무팀 브리핑

법률 업무에 대한 맥락적 브리핑을 생성합니다.

```
/brief daily          # 법적 관련 항목의 오전 브리핑
/brief topic [query]  # 특정 법적 질문에 대한 리서치 브리핑
/brief incident       # 진행 중인 상황에 대한 신속 브리핑
```

### `/respond` -- 템플릿 기반 응답 생성

일반적인 문의 유형에 대해 구성된 템플릿으로 응답을 생성합니다.

```
/respond [inquiry-type]
```

지원되는 문의 유형에는 정보 주체 요청, 증거 보존 명령, 벤더 질문, NDA 요청, 그리고 사용자가 정의한 맞춤 카테고리가 포함됩니다.

## Skills

| Skill | 설명 |
|-------|-------------|
| `contract-review` | 플레이북 기반 계약 분석, 이탈 분류, 수정 제안 생성 |
| `nda-triage` | NDA 심사 기준, 분류 규칙, 라우팅 권장 사항 |
| `compliance` | 개인정보 보호 규정 (GDPR, CCPA), DPA 검토, 정보 주체 요청 |
| `canned-responses` | 템플릿 관리, 응답 카테고리, 에스컬레이션 트리거 |
| `legal-risk-assessment` | 위험 심각도 프레임워크, 분류 수준, 에스컬레이션 기준 |
| `meeting-briefing` | 회의 준비 방법론, 컨텍스트 수집, 실행 항목 추적 |

## 예시 워크플로

### 계약 검토

1. 이메일로 벤더 계약서를 받음
2. `/review-contract`를 실행하고 문서를 업로드
3. 컨텍스트 제공: "저희가 고객 측이며, 분기말까지 마감해야 하고, 데이터 보호와 책임 조항에 집중해 주세요"
4. GREEN/YELLOW/RED 표시와 함께 조항별 분석 수신
5. YELLOW 및 RED 항목에 대한 구체적인 수정 언어 확인
6. 분석 내용을 거래 팀과 공유

### NDA 분류

1. 영업팀이 새 잠재고객의 NDA를 보냄
2. `/triage-nda`를 실행하고 NDA를 붙여넣거나 업로드
3. 즉각적인 분류 수신: GREEN(서명 진행), YELLOW(검토가 필요한 특정 문제), 또는 RED(법무 전체 검토 필요)
4. GREEN NDA는 직접 승인; YELLOW/RED는 표시된 문제 해결

### 일일 브리핑

1. `/brief daily`로 업무 시작
2. 야간 계약 요청, 컴플라이언스 질문, 다가오는 마감일, 법무 준비가 필요한 캘린더 항목 요약 수신
3. 긴급도와 마감일을 기준으로 하루 우선순위 결정

### 벤더 확인

1. 비즈니스 팀이 기존 벤더와의 새 거래에 대해 문의
2. `/vendor-check Acme Corp` 실행
3. 기존 계약, 만료일, 주요 조건을 한눈에 확인
4. 새 NDA가 필요한지 또는 기존 조건으로 진행할 수 있는지 즉시 파악

## MCP 통합

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하십시오.

플러그인은 MCP (Model Context Protocol) 서버를 통해 도구에 연결됩니다:

| 카테고리 | 예시 | 목적 |
|----------|----------|---------|
| Chat | Slack, Teams | 팀 요청, 알림, 분류 |
| Cloud storage | Box, Egnyte | 플레이북, 템플릿, 선례 |
| Office suite | Microsoft 365 | 이메일, 캘린더, 문서 |
| Project tracker | Atlassian (Jira/Confluence) | 사건 추적, 태스크 |

CLM, CRM, e-signature 및 추가 옵션을 포함한 지원되는 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)를 참조하십시오.

`.mcp.json`에서 연결을 구성합니다. 플러그인은 도구를 사용할 수 없을 때 자동으로 성능을 낮추며 — 격차를 알리고 수동 확인을 제안합니다.

## 맞춤 설정

### 플레이북 구성

플레이북은 계약 검토 시스템의 핵심입니다. `legal.local.md`에 입장을 정의합니다:

- **표준 입장**: 각 주요 조항 유형에 대한 조직의 선호 조건
- **허용 범위**: 에스컬레이션 없이 동의할 수 있는 조건
- **에스컬레이션 트리거**: 시니어 검토 또는 외부 법무 개입이 필요한 조건

### 응답 템플릿

일반적인 문의에 대한 템플릿을 정의합니다. 템플릿은 변수 치환을 지원하며 템플릿 응답을 사용하지 않아야 하는 상황에 대한 내장된 에스컬레이션 트리거를 포함합니다.

### 위험 프레임워크

조직의 위험 성향과 분류 체계에 맞게 위험 평가 매트릭스를 맞춤 설정합니다.

## 파일 구조

```
legal/
├── .claude-plugin/plugin.json
├── .mcp.json
├── README.md
├── commands/
│   ├── review-contract.md
│   ├── triage-nda.md
│   ├── vendor-check.md
│   ├── brief.md
│   └── respond.md
└── skills/
    ├── contract-review/SKILL.md
    ├── nda-triage/SKILL.md
    ├── compliance/SKILL.md
    ├── canned-responses/SKILL.md
    ├── legal-risk-assessment/SKILL.md
    └── meeting-briefing/SKILL.md
```
