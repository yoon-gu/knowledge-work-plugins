# Enterprise Search

주로 Anthropic의 에이전틱 데스크탑 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 엔터프라이즈 검색 플러그인 — Claude Code에서도 작동합니다. 앱 간 전환 없이 이메일, 채팅, 문서, 위키 등 회사의 모든 도구를 한 곳에서 검색하세요.

---

## 작동 방식

하나의 쿼리로 연결된 모든 도구를 동시에 검색합니다. Claude가 질문을 분해하고, 모든 소스에서 타겟 검색을 실행하며, 결과를 소스 출처와 함께 하나의 일관된 답변으로 종합합니다.

```
사용자: "API 재설계에 대해 어떤 결정을 내렸나요?"
              ↓ Claude 검색
~~chat: #engineering 스레드 화요일 결정 내용
~~email: Sarah가 보낸 사양이 담긴 후속 이메일
~~cloud storage: 업데이트된 API 설계 문서 (어제 수정됨)
              ↓ Claude 종합
"팀은 화요일에 GraphQL 대신 REST를 선택하기로 결정했습니다.
 Sarah가 목요일에 업데이트된 사양을 보냈습니다. 설계 문서에는
 최종 접근 방식이 반영되어 있습니다."
```

탭 전환 없음. 어떤 도구에 무엇이 있는지 기억할 필요 없음. 질문하면 답변이 나옵니다.

---

## 검색 대상

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

원하는 소스를 원하는 조합으로 연결하세요. 더 많이 연결할수록 답변이 더 완전해집니다.

| 소스 | 찾을 수 있는 것 |
|--------|---------------|
| **~~chat** | 메시지, 스레드, 채널, DM |
| **~~email** | 이메일, 첨부 파일, 대화 |
| **~~cloud storage** | 문서, 시트, 슬라이드, PDF |
| **Wiki / Knowledge Base** | 내부 문서, 런북 |
| **Project Management** | 태스크, 이슈, 에픽, 마일스톤 |
| **CRM** | 계정, 연락처, 영업 기회 |
| **Ticketing** | 지원 티켓, 고객 이슈 |

각 소스는 MCP 연결입니다. MCP 설정에서 더 많은 소스를 추가하면 Claude가 검색할 수 있는 범위가 확장됩니다.

---

## 명령어

| 명령어 | 기능 |
|---------|--------------|
| `/search` | 하나의 쿼리로 연결된 모든 소스를 검색 |
| `/digest` | 모든 소스의 활동에 대한 일간 또는 주간 다이제스트 생성 |

### Search

```
/enterprise-search:search Project Aurora의 현재 상태는?
/enterprise-search:search from:sarah about:budget after:2025-01-01
/enterprise-search:search 이번 주 #product에서 내려진 결정들
```

필터 지원: `from:`, `in:`, `after:`, `before:`, `type:` — 각 소스의 기본 쿼리 구문에 맞게 지능적으로 적용됩니다.

### Digest

```
/enterprise-search:digest --daily      # 오늘 모든 소스에서 발생한 일
/enterprise-search:digest --weekly     # 프로젝트/주제별로 그룹화된 주간 요약
```

실행 항목, 결정 사항, 나에 대한 언급을 강조합니다. 중요한 내용을 빠르게 훑어볼 수 있도록 활동을 주제별로 그룹화합니다.

---

## Skills

세 가지 스킬이 검색 경험을 지원합니다:

**Search Strategy** — 쿼리 분해 및 소스별 변환. 자연어 질문을 소스별 타겟 검색으로 분해하고, 모호성을 처리하며, 소스를 사용할 수 없을 때 gracefully하게 폴백합니다.

**Source Management** — 사용 가능한 MCP 소스를 파악하고, 새 소스 연결을 안내하며, 소스 우선순위를 관리하고, 속도 제한을 처리합니다.

**Knowledge Synthesis** — 여러 소스의 결과를 일관된 답변으로 결합합니다. 크로스 소스 정보의 중복을 제거하고, 소스를 출처로 표시하며, 최신성과 신뢰도를 기반으로 신뢰도 점수를 매기고, 대용량 결과 세트를 요약합니다.

---

## 워크플로우 예시

### 결정 사항 찾기

```
사용자: /enterprise-search:search Postgres로 전환하기로 결정한 게 언제였나요?

Claude 검색:
  ~~chat → #engineering, #infrastructure에서 "postgres" "switch" "decision" 검색
  ~~email → 제목에 "postgres"가 포함된 스레드
  ~~cloud storage → 데이터베이스 마이그레이션을 언급한 문서

결과: "결정은 3월 3일 #infrastructure에서 내려졌습니다 (링크).
       Sarah의 3월 4일 이메일에서 일정이 확인되었습니다.
       마이그레이션 계획 문서가 3월 5일에 업데이트되었습니다."
```

### 휴가 후 따라잡기

```
사용자: /enterprise-search:digest --weekly

Claude 스캔:
  ~~chat → 참여 중인 채널, DM, 언급
  ~~email → 받은 편지함 활동
  ~~cloud storage → 나와 공유되었거나 수정된 문서

결과: 실행 항목이 표시되고 결정 사항이
      강조된 프로젝트별 그룹화된 요약.
```

### 전문가 찾기

```
사용자: /enterprise-search:search Kubernetes 설정에 대해 아는 사람이 누구인가요?

Claude 검색:
  ~~chat → Kubernetes, k8s, 클러스터에 관한 메시지
  ~~cloud storage → 인프라에 대해 작성된 문서
  Wiki → 런북 및 아키텍처 문서

결과: "메시지 기록과 문서 저작권을 기반으로,
       Alex와 Priya가 k8s 담당자입니다.
       주요 런북은 여기 있습니다 (링크)."
```

---

## 시작하기

```bash
# 1. 설치
claude plugins add knowledge-work-plugins/enterprise-search

# 2. 모든 것을 검색
/enterprise-search:search [질문 입력]

# 3. 다이제스트 가져오기
/enterprise-search:digest --daily
```

MCP를 통해 더 많은 소스를 연결할수록 검색 결과가 더 완전해집니다. ~~chat, ~~email, ~~cloud storage부터 시작한 다음 필요에 따라 위키, 프로젝트 관리 도구, CRM을 추가하세요.

---

## 철학

지식 근로자들은 매주 도구 전반에 흩어진 정보를 찾는 데 수 시간을 소비합니다. 답변은 어딘가에 존재합니다 — Slack 스레드, 이메일 체인, 문서, 위키 페이지 — 하지만 찾으려면 각 도구를 개별적으로 검색하고, 결과를 교차 참조하며, 올바른 장소를 확인했기를 바라야 합니다.

Enterprise Search는 모든 도구를 하나의 검색 가능한 지식 베이스로 취급합니다. 하나의 쿼리, 모든 소스, 종합된 결과. 회사의 지식이 사일로에 갇혀 있어서는 안 됩니다. 모든 것을 한 번에 검색하세요.
