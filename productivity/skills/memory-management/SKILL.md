---
name: memory-management
description: Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.
user-invocable: false
---

# 메모리 관리

메모리는 Claude를 여러분의 직장 동료로 만들어 줍니다 — 내부 언어를 구사하는 누군가로.

## 목표

약어를 이해로 변환합니다:

```
사용자: "ask todd to do the PSR for oracle"
              ↓ Claude가 해독
"Todd Martinez(재무 팀장)에게 Oracle Systems 거래($2.3M, Q2 마감)에 대한
 Pipeline Status Report 작성을 요청하세요"
```

메모리 없이는 그 요청이 의미가 없습니다. 메모리가 있으면 Claude는 알고 있습니다:
- **todd** → Todd Martinez, 재무 팀장, Slack 선호
- **PSR** → Pipeline Status Report (주간 영업 문서)
- **oracle** → Oracle Systems 거래, 회사가 아님

## 아키텍처

```
CLAUDE.md          ← 핫 캐시 (상위 ~30명, 공통 용어)
memory/
  glossary.md      ← 전체 해독 목록 (모든 것)
  people/          ← 완전한 프로필
  projects/        ← 프로젝트 세부사항
  context/         ← 회사, 팀, 도구
```

**CLAUDE.md (핫 캐시):**
- 가장 자주 교류하는 상위 ~30명
- ~30개의 가장 일반적인 약어/용어
- 활성 프로젝트 (5-15개)
- 여러분의 선호도
- **목표: 일상적인 해독 필요의 90% 커버**

**memory/glossary.md (전체 용어집):**
- 완전한 해독 목록 — 모든 사람, 모든 용어
- CLAUDE.md에 없을 때 검색
- 무한히 성장 가능

**memory/people/, projects/, context/:**
- 실행에 필요할 때 풍부한 세부사항
- 전체 프로필, 기록, 컨텍스트

## 조회 흐름

```
사용자: "ask todd about the PSR for phoenix"

1. CLAUDE.md 확인 (핫 캐시)
   → Todd? ✓ Todd Martinez, 재무
   → PSR? ✓ Pipeline Status Report
   → Phoenix? ✓ DB 마이그레이션 프로젝트

2. 없으면 → memory/glossary.md 검색
   → 전체 용어집에 모든 사람/모든 것 있음

3. 그래도 없으면 → 사용자에게 질문
   → "X가 무슨 의미인가요? 기억해 두겠습니다."
```

이 계층적 접근 방식은 CLAUDE.md를 간결하게 유지하면서 (~100줄) memory/에서 무제한 확장을 지원합니다.

## 파일 위치

- **작업 메모리:** 현재 작업 디렉터리의 `CLAUDE.md`
- **심층 메모리:** `memory/` 하위 디렉터리

## 작업 메모리 형식 (CLAUDE.md)

간결성을 위해 표를 사용합니다. 목표 총 ~50-80줄.

```markdown
# Memory

## Me
[Name], [Role] on [Team]. [One sentence about what I do.]

## People
| Who | Role |
|-----|------|
| **Todd** | Todd Martinez, Finance lead |
| **Sarah** | Sarah Chen, Engineering (Platform) |
| **Greg** | Greg Wilson, Sales |
→ Full list: memory/glossary.md, profiles: memory/people/

## Terms
| Term | Meaning |
|------|---------|
| PSR | Pipeline Status Report |
| P0 | Drop everything priority |
| standup | Daily 9am sync |
→ Full glossary: memory/glossary.md

## Projects
| Name | What |
|------|------|
| **Phoenix** | DB migration, Q2 launch |
| **Horizon** | Mobile app redesign |
→ Details: memory/projects/

## Preferences
- 25-min meetings with buffers
- Async-first, Slack over email
- No meetings Friday afternoons
```

## 심층 메모리 형식 (memory/)

**memory/glossary.md** - 해독 목록:
```markdown
# Glossary

Workplace shorthand, acronyms, and internal language.

## Acronyms
| Term | Meaning | Context |
|------|---------|---------|
| PSR | Pipeline Status Report | Weekly sales doc |
| OKR | Objectives & Key Results | Quarterly planning |
| P0/P1/P2 | Priority levels | P0 = drop everything |

## Internal Terms
| Term | Meaning |
|------|---------|
| standup | Daily 9am sync in #engineering |
| the migration | Project Phoenix database work |
| ship it | Deploy to production |
| escalate | Loop in leadership |

## Nicknames → Full Names
| Nickname | Person |
|----------|--------|
| Todd | Todd Martinez (Finance) |
| T | Also Todd Martinez |

## Project Codenames
| Codename | Project |
|----------|---------|
| Phoenix | Database migration |
| Horizon | New mobile app |
```

**memory/people/{name}.md:**
```markdown
# Todd Martinez

**Also known as:** Todd, T
**Role:** Finance Lead
**Team:** Finance
**Reports to:** CFO (Michael Chen)

## Communication
- Prefers Slack DM
- Quick responses, very direct
- Best time: mornings

## Context
- Handles all PSRs and financial reporting
- Key contact for deal approvals over $500k
- Works closely with Sales on forecasting

## Notes
- Cubs fan, likes talking baseball
```

**memory/projects/{name}.md:**
```markdown
# Project Phoenix

**Codename:** Phoenix
**Also called:** "the migration"
**Status:** Active, launching Q2

## What It Is
Database migration from legacy Oracle to PostgreSQL.

## Key People
- Sarah - tech lead
- Todd - budget owner
- Greg - stakeholder (sales impact)

## Context
$1.2M budget, 6-month timeline. Critical path for Horizon project.
```

**memory/context/company.md:**
```markdown
# Company Context

## Tools & Systems
| Tool | Used for | Internal name |
|------|----------|---------------|
| Slack | Communication | - |
| Asana | Engineering tasks | - |
| Salesforce | CRM | "SF" or "the CRM" |
| Notion | Docs/wiki | - |

## Teams
| Team | What they do | Key people |
|------|--------------|------------|
| Platform | Infrastructure | Sarah (lead) |
| Finance | Money stuff | Todd (lead) |
| Sales | Revenue | Greg |

## Processes
| Process | What it means |
|---------|---------------|
| Weekly sync | Monday 10am all-hands |
| Ship review | Thursday deploy approval |
```

## 상호작용 방법

### 사용자 입력 해독 (계층적 조회)

요청에 따라 행동하기 전에 **항상** 약어를 해독합니다:

```
1. CLAUDE.md (핫 캐시)     → 먼저 확인, 90% 케이스 커버
2. memory/glossary.md        → 핫 캐시에 없으면 전체 용어집
3. memory/people/, projects/ → 필요할 때 풍부한 세부사항
4. 사용자에게 질문          → 모르는 용어? 배우기
```

예시:
```
사용자: "ask todd to do the PSR for oracle"

CLAUDE.md 조회:
  "todd" → Todd Martinez, Finance ✓
  "PSR" → Pipeline Status Report ✓
  "oracle" → (핫 캐시에 없음)

memory/glossary.md 조회:
  "oracle" → Oracle Systems deal ($2.3M) ✓

이제 Claude가 전체 컨텍스트로 행동할 수 있습니다.
```

### 메모리 추가

사용자가 "remember this" 또는 "X means Y"라고 말할 때:

1. **용어집 항목** (약어, 용어, 약칭):
   - memory/glossary.md에 추가
   - 자주 사용되면 CLAUDE.md Quick Glossary에 추가

2. **사람:**
   - memory/people/{name}.md 생성/업데이트
   - 중요하면 CLAUDE.md Key People에 추가
   - **별명 캡처** — 해독에 중요

3. **프로젝트:**
   - memory/projects/{name}.md 생성/업데이트
   - 현재 진행 중이면 CLAUDE.md Active Projects에 추가
   - **코드명 캡처** — "Phoenix", "the migration" 등

4. **선호도:** CLAUDE.md Preferences 섹션에 추가

### 메모리 회상

사용자가 "who is X" 또는 "what does X mean"이라고 물을 때:

1. 먼저 CLAUDE.md 확인
2. 전체 세부사항을 위해 memory/ 확인
3. 없으면: "X가 무슨 의미인지 아직 모릅니다. 알려주시겠어요?"

### 점진적 공개

1. 요청을 빠르게 파싱하기 위해 CLAUDE.md 로드
2. 실행을 위한 전체 컨텍스트가 필요할 때 memory/ 탐색
3. 예시: todd에게 PSR에 대한 이메일 초안 작성
   - CLAUDE.md는 Todd = Todd Martinez, PSR = Pipeline Status Report임을 알려줌
   - memory/people/todd-martinez.md는 그가 Slack을 선호하고 직설적임을 알려줌

## 부트스트래핑

`/productivity:start`를 사용하여 채팅, 캘린더, 이메일, 문서를 스캔하여 초기화합니다. 사람, 프로젝트를 추출하고 용어집 구축을 시작합니다.

## 규칙

- CLAUDE.md에서 **굵게** 표시하여 스캔 가능성 향상
- CLAUDE.md를 ~100줄 이하로 유지 ("hot 30" 규칙)
- 파일명: 소문자, 하이픈 사용 (`todd-martinez.md`, `project-phoenix.md`)
- 항상 별명과 대체 이름 캡처
- 쉬운 조회를 위한 용어집 표 사용
- 자주 사용되면 CLAUDE.md로 승격
- 오래되면 memory/로 강등

## 무엇이 어디에 속하는가

| 유형 | CLAUDE.md (핫 캐시) | memory/ (전체 저장소) |
|------|----------------------|------------------------|
| 사람 | 상위 ~30명 자주 연락하는 사람 | glossary.md + people/{name}.md |
| 약어/용어 | ~30개 가장 일반적인 것 | glossary.md (완전한 목록) |
| 프로젝트 | 활성 프로젝트만 | glossary.md + projects/{name}.md |
| 별명 | 상위 30명이면 Key People에 | glossary.md (모든 별명) |
| 회사 컨텍스트 | 빠른 참조만 | context/company.md |
| 선호도 | 모든 선호도 | - |
| 기록/오래된 것 | ✗ 제거 | ✓ memory/에 보관 |

## 승격 / 강등

**CLAUDE.md로 승격할 때:**
- 용어/사람을 자주 사용할 때
- 활성 작업의 일부일 때

**memory/로만 강등할 때:**
- 프로젝트 완료
- 더 이상 자주 연락하지 않는 사람
- 거의 사용하지 않는 용어

이렇게 하면 CLAUDE.md가 신선하고 관련성 있게 유지됩니다.
