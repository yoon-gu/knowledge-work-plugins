# Enterprise Search

[Cowork](https://claude.com/product/cowork)을 위해 주로 설계된 엔터프라이즈 검색 플러그인입니다. Anthropic의 에이전틱 데스크톱 앱이지만 Claude Code에서도 작동합니다. 이메일, 채팅, 문서, 위키를 오가며 앱을 전환하지 않고 회사의 모든 도구를 한 곳에서 검색할 수 있습니다.

---

## 작동 방식

한 번의 쿼리로 연결된 모든 도구를 동시에 검색합니다. Claude가 질문을 분해하고, 각 소스에 맞는 검색을 실행하고, 출처가 표시된 하나의 일관된 답변으로 종합합니다.

```
You: "What did we decide about the API redesign?"
              ↓ Claude searches
~~chat: #engineering thread from Tuesday with the decision
~~email: Follow-up email from Sarah with the spec
~~cloud storage: Updated API design doc (modified yesterday)
              ↓ Claude synthesizes
"The team decided on Tuesday to go with REST over GraphQL.
 Sarah sent the updated spec Thursday. The design doc
 reflects the final approach."
```

탭을 전환할 필요도 없고, 어떤 도구에 무엇이 있는지 기억할 필요도 없습니다. 질문만 하면 답이 나옵니다.

---

## 무엇을 검색하나

> 익숙하지 않은 플레이스홀더가 보이거나 어떤 도구가 연결되어 있는지 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

아무 소스 조합이나 연결할 수 있습니다. 더 많이 연결할수록 답변이 더 완전해집니다.

| Source | What it finds |
|--------|---------------|
| **~~chat** | 메시지, 스레드, 채널, DM |
| **~~email** | 이메일, 첨부파일, 대화 |
| **~~cloud storage** | 문서, 시트, 슬라이드, PDF |
| **Wiki / Knowledge Base** | 내부 문서, 런북 |
| **Project Management** | 작업, 이슈, 에픽, 마일스톤 |
| **CRM** | 계정, 연락처, 기회 |
| **Ticketing** | 지원 티켓, 고객 이슈 |

각 소스는 MCP 연결입니다. MCP 설정에 소스를 더 추가하면 Claude가 검색할 수 있는 범위가 넓어집니다.

---

## 명령

| Command | What it does |
|---------|--------------|
| `/search` | 연결된 모든 소스를 한 번의 쿼리로 검색 |
| `/digest` | 모든 소스의 활동을 일간 또는 주간으로 요약 |

### 검색

```
/enterprise-search:search what's the status of Project Aurora?
/enterprise-search:search from:sarah about:budget after:2025-01-01
/enterprise-search:search decisions made in #product this week
```

필터를 지원합니다: `from:`, `in:`, `after:`, `before:`, `type:` — 각 소스의 네이티브 쿼리 문법에 맞게 지능적으로 적용됩니다.

### 다이제스트

```
/enterprise-search:digest --daily      # 모든 소스에서 오늘 일어난 일
/enterprise-search:digest --weekly     # 프로젝트/주제별로 묶은 주간 요약
```

액션 아이템, 결정 사항, 당신에 대한 언급을 강조합니다. 활동을 주제별로 묶어 빠르게 훑어볼 수 있습니다.

---

## 스킬

검색 경험을 만드는 세 가지 스킬:

**Search Strategy** - 쿼리 분해와 소스별 번역. 자연어 질문을 소스별로 타깃팅된 검색으로 나누고, 모호성을 처리하며, 소스가 없을 때 우아하게 대체합니다.

**Source Management** - 어떤 MCP 소스를 사용할 수 있는지 알고, 새 소스를 연결하도록 안내하고, 소스 우선순위를 관리하며, 속도 제한을 다룹니다.

**Knowledge Synthesis** - 여러 소스의 결과를 일관된 답변으로 합칩니다. 소스 간 중복을 제거하고, 출처를 표시하며, 최신성과 권위를 바탕으로 신뢰도를 점수화하고, 큰 결과 집합을 요약합니다.

---

## 예시 워크플로

### 결정 찾기

```
You: /enterprise-search:search when did we decide to switch to Postgres?

Claude searches:
  ~~chat → #engineering, #infrastructure for "postgres" "switch" "decision"
  ~~email → threads with "postgres" in subject
  ~~cloud storage → docs mentioning database migration

Result: "The decision was made March 3 in #infrastructure (link).
         Sarah's email on March 4 confirmed the timeline.
         The migration plan doc was updated March 5."
```

### 휴가 후 따라잡기

```
You: /enterprise-search:digest --weekly

Claude scans:
  ~~chat → channels you're in, DMs, mentions
  ~~email → inbox activity
  ~~cloud storage → docs shared with you or modified

Result: 프로젝트별로 묶인 요약과 함께 액션 아이템,
        표시된 결정 사항.
```

### 전문가 찾기

```
You: /enterprise-search:search who knows about our Kubernetes setup?

Claude searches:
  ~~chat → messages about Kubernetes, k8s, clusters
  ~~cloud storage → docs authored about infrastructure
  Wiki → runbooks and architecture docs

Result: "메시지 기록과 문서 작성자를 보면,
         Alex와 Priya가 k8s 담당자로 보입니다.
         여기가 주요 런북입니다(link)."
```

---

## 시작하기

```bash
# 1. 설치
claude plugins add knowledge-work-plugins/enterprise-search

# 2. 모든 곳에서 검색 시작
/enterprise-search:search [your question here]

# 3. 다이제스트 받기
/enterprise-search:digest --daily
```

MCP를 통해 연결하는 소스가 많을수록 검색 결과가 더 완전해집니다. `~~chat`, `~~email`, `~~cloud storage`부터 시작하고, 필요에 따라 위키, 프로젝트 관리 도구, CRM을 추가하세요.

---

## 철학

지식 노동자들은 매주 도구마다 흩어진 정보를 찾느라 수 시간을 씁니다. 답은 어딘가에 있습니다. Slack 스레드, 이메일 체인, 문서, 위키 페이지. 하지만 찾으려면 각 도구를 따로 검색하고, 결과를 대조하고, 올바른 곳을 확인했는지 바래야 합니다.

Enterprise Search는 모든 도구를 하나의 검색 가능한 지식 베이스로 취급합니다. 한 번의 쿼리, 모든 소스, 종합된 결과. 회사의 지식은 사일로에 갇혀 있어서는 안 됩니다. 한 번에 모두 검색하세요.
