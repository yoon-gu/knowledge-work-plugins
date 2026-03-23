# Legal Productivity Plugin

사내 법무팀을 위한 AI 기반 생산성 플러그인입니다. Anthropic의 에이전트 데스크톱 앱인 [Cowork](https://claude.com/product/cowork)용으로 설계되었지만 Claude Code에서도 사용할 수 있습니다. 계약 검토, NDA 분류, 규정 준수 워크플로, 법무 브리핑, 템플릿 응답을 자동화하며, 조직의 플레이북과 위험 허용 범위에 맞게 조정할 수 있습니다.

> **면책 조항:** 이 플러그인은 법무 워크플로를 지원하지만 법률 자문을 제공하지는 않습니다. 항상 자격을 갖춘 법률 전문가와 함께 결론을 확인하세요. AI가 생성한 분석은 법적 결정을 내리기 전에 변호사의 검토를 받아야 합니다. 이 플러그인의 기본 플레이북 예시는 미국의 법적 위치와 관할권(델라웨어, 뉴욕, 캘리포니아)을 반영합니다. EU, 영국, 네덜란드, 호주 등 다른 법체계에서 운영하는 경우, 플러그인 분석에 의존하기 전에 `.claude/legal.local.md`에서 해당 관할권의 요건, 표준 계약 조건, 규정 준수 의무를 반영하도록 플레이북을 직접 조정해야 합니다.

## 대상 페르소나

- **Commercial Counsel** - 계약 협상, 공급업체 관리, 거래 지원
- **Product Counsel** - 제품 리뷰, 서비스 약관, 개인정보 처리방침, IP 문제
- **개인정보 보호/규정 준수** - 데이터 보호 규정, DPA 검토, 데이터 주체 요청, 규제 모니터링
- **소송 지원** - 증거 자료 보관, 문서 검토 준비, 사례 브리핑

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

조직의 표준 입장을 정의하는 로컬 설정 파일을 만드세요. 여기에서 팀의 협상 플레이북, 위험 허용 범위, 표준 조항을 설정합니다.

Claude가 찾을 수 있는 `legal.local.md` 파일을 만듭니다.

- **Cowork**: 폴더 선택기를 통해 Cowork와 공유한 폴더에 저장하세요. 플러그인이 자동으로 찾아냅니다.
- **Claude Code**: 프로젝트의 `.claude/` 디렉터리에 저장하세요.

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

### 3. 도구를 연결하세요

플러그인은 MCP를 통해 기존 도구에 연결할 때 가장 잘 작동합니다. 사전 구성된 서버에는 Slack, Box, Egnyte, Atlassian, Microsoft 365가 포함됩니다. 지원되는 범주와 옵션의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)을 참고하세요.

## 명령

### `/review-contract` - 플레이북 기준 계약 검토

조직의 협상 플레이북을 기준으로 계약을 검토합니다. 편차를 표시하고 수정 지시를 생성하며 비즈니스 영향 분석을 제공합니다.

```
/review-contract
```

파일 업로드, URL, 붙여넣은 계약서 텍스트를 모두 지원합니다. 맥락(당사자 입장, 마감일, 중점 검토 영역)을 묻고 구성된 플레이북을 기준으로 조항별 검토를 진행합니다.

### `/triage-nda` - NDA 사전 분류

표준 기준에 따라 들어오는 NDA를 신속하게 분류합니다. GREEN(표준 승인), YELLOW(추가 검토 필요), RED(중대한 이슈)로 나눕니다.

```
/triage-nda
```

### `/vendor-check` - 공급업체 계약 상태

연결된 시스템 전체에서 공급업체와의 기존 계약 상태를 확인합니다.

```
/vendor-check [vendor name]
```

기존 NDA, MSA, DPA, 만료일, 주요 용어를 보고합니다.

### `/brief` - 법무팀 브리핑

법무 업무에 대한 상황별 브리핑을 생성합니다.

```
/brief daily          # 법무 관련 항목에 대한 아침 브리핑
/brief topic [query]  # 특정 법률 질문에 대한 조사 브리핑
/brief incident       # 진행 중인 상황에 대한 신속한 브리핑
```

### `/respond` - 템플릿 응답 생성

일반적인 문의 유형에 대해 구성된 템플릿에서 응답을 생성합니다.

```
/respond [inquiry-type]
```

지원되는 문의 유형에는 데이터 주체 요청, 소송 보류, 공급업체 질문, NDA 요청, 사용자가 정의하는 사용자 지정 범주가 포함됩니다.

## 기술

| 기능 | 설명 |
| ------- | ------------- |
| `contract-review` | 플레이북 기반 계약 분석, 편차 분류, 레드라인 생성 |
| `nda-triage` | NDA 심사 기준, 분류 규칙, 라우팅 권장 사항 |
| `compliance` | 개인정보 보호 규정(GDPR, CCPA), DPA 검토, 데이터 주체 요청 |
| `canned-responses` | 템플릿 관리, 응답 카테고리, 에스컬레이션 트리거 |
| `legal-risk-assessment` | 위험 심각도 프레임워크, 분류 수준, 에스컬레이션 기준 |
| `meeting-briefing` | 회의 준비 방법론, 상황 수집, 조치 항목 추적 |

## 예시 워크플로

### 계약 검토

1. 이메일로 공급업체 계약을 받습니다.
2. `/review-contract`을 실행하고 문서를 업로드합니다.
3. 맥락을 제공합니다: "우리는 고객입니다. 분기 말까지 마감해야 하며 데이터 보호와 책임에 중점을 두어야 합니다."
4. GREEN/YELLOW/RED 플래그가 포함된 조항별 분석을 받습니다.
5. 노란색과 빨간색 항목에 대한 구체적인 레드라인 문구를 얻습니다.
6. 분석을 거래 팀과 공유합니다.

### NDA 분류

1. 영업팀이 새로운 잠재 고객으로부터 NDA를 전달합니다.
2. `/triage-nda`를 실행하고 NDA를 붙여넣거나 업로드합니다.
3. 즉시 분류를 받습니다: GREEN(서명 진행 가능), YELLOW(특정 이슈 검토 필요), RED(전체 법무 검토 필요)
4. GREEN NDA는 직접 승인하고, 노란색/빨간색은 표시된 문제를 해결합니다.

### 일일 브리핑

1. `/brief daily`로 아침을 시작합니다.
2. 익일 계약 요청, 규정 준수 관련 질문, 예정된 마감일, 법무 준비가 필요한 일정 항목에 대한 요약을 받습니다.
3. 긴급성과 기한을 기준으로 하루의 우선순위를 정합니다.

### 공급업체 확인

1. 비즈니스 팀이 기존 공급업체와의 새로운 계약에 대해 문의합니다.
2. `/vendor-check Acme Corp`을 실행합니다.
3. 기존 계약, 만료일, 주요 약관을 한눈에 확인합니다.
4. 새로운 NDA가 필요한지 또는 기존 조건으로 진행할 수 있는지 즉시 확인합니다.

## MCP 통합

> 익숙하지 않은 자리 표시자가 보이거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)을 참고하세요.

플러그인은 MCP(모델 컨텍스트 프로토콜) 서버를 통해 도구에 연결됩니다.

| 범주 | 예 | 목적 |
| ---------- | ---------- | --------- |
| 채팅 | Slack, Teams | 팀 요청, 알림, 분류 |
| 클라우드 스토리지 | Box, Egnyte | 플레이북, 템플릿, 선례 |
| 오피스 스위트 | Microsoft 365 | 이메일, 캘린더, 문서 |
| 프로젝트 트래커 | Atlassian(Jira/Confluence) | 사안 추적, 업무 관리 |

CLM, CRM, 전자 서명, 기타 추가 옵션을 포함한 지원 통합의 전체 목록은 [CONNECTORS.md](CONNECTORS.md)을 참고하세요.

`.mcp.json`에서 연결을 구성합니다. 도구를 사용할 수 없을 때는 플러그인의 기능이 점차 줄어듭니다. 따라서 공백을 확인하고 수동 확인을 제안하세요.

## 맞춤화

### 플레이북 구성

플레이북은 계약 검토 시스템의 핵심입니다. `legal.local.md`에서 귀하의 입장을 정의하세요.

- **표준 입장**: 선호하는 계약 조건
- **허용 범위**: 에스컬레이션 없이 동의할 수 있는 범위
- **에스컬레이션 트리거**: 상위 검토나 외부 변호사가 필요한 조건

### 응답 템플릿

일반적인 문의에 대한 템플릿을 정의합니다. 템플릿은 변수 대체를 지원하고, 템플릿 응답을 사용해서는 안 되는 상황에 대한 기본 에스컬레이션 트리거를 포함합니다.

### 위험 프레임워크

조직의 위험 성향과 분류 체계에 맞게 위험 평가 매트릭스를 사용자 정의합니다.

## 파일 구조

```text
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
