---
name: memory-management
description: Claude를 진짜 업무 동료로 만들어 주는 2단계 기억 시스템입니다. 약어, 별명, 내부 언어를 해독해 Claude가 동료처럼 요청을 이해하도록 합니다. 작업 기억은 CLAUDE.md, 전체 지식 베이스는 memory/ 디렉터리입니다.
user-invocable: false
---

# 기억 관리

기억은 Claude를 당신의 업무 동료로 만듭니다. 내부 언어를 함께 쓰는 사람처럼요.

## 목표

약어를 이해로 바꿉니다.

```
사용자: "ask todd to do the PSR for oracle"
              ↓ Claude가 해독합니다
"Todd Martinez(Finance lead)에게 Oracle Systems 거래($2.3M, Q2 마감)의
 Pipeline Status Report를 준비해 달라고 요청하세요"
```

기억이 없으면 이 요청은 의미가 없습니다. 기억이 있으면 Claude는 다음을 압니다.
- **todd** → Todd Martinez, Finance lead, Slack 선호
- **PSR** → Pipeline Status Report(주간 세일즈 문서)
- **oracle** → 회사가 아니라 Oracle Systems 거래

## 아키텍처

```
CLAUDE.md          ← 핫 캐시(~30명, 흔한 용어)
memory/
  glossary.md      ← 전체 해독표(모든 것)
  people/          ← 전체 프로필
  projects/        ← 프로젝트 세부 정보
  context/         ← 회사, 팀, 도구
```

**CLAUDE.md (핫 캐시):**
- 가장 자주 상호작용하는 상위 약 30명
- 가장 흔한 약어/용어 약 30개
- 활성 프로젝트(5-15개)
- 당신의 선호
- **목표: 일상적인 해독 수요의 90%를 커버**

**memory/glossary.md (전체 용어집):**
- 완전한 해독표 - 모든 사람, 모든 용어
- CLAUDE.md에 없을 때 검색
- 무한히 확장 가능

**memory/people/, projects/, context/:**
- 실행에 필요할 때 풍부한 세부 정보
- 전체 프로필, 이력, 맥락

## 조회 흐름

```
사용자: "ask todd about the PSR for phoenix"

1. CLAUDE.md 확인(핫 캐시)
   → Todd? ✓ Todd Martinez, Finance
   → PSR? ✓ Pipeline Status Report
   → Phoenix? ✓ DB migration project

2. 없으면 → memory/glossary.md를 검색
   → 전체 용어집에 모든 사람/모든 것이 있음

3. 그래도 없으면 → 사용자에게 질문
   → "X가 무슨 뜻인가요? 기억해 두겠습니다."
```

이 단계적 접근은 CLAUDE.md를 가볍게 유지(~100줄)하면서 memory/에서 무한한 확장을 지원합니다.

## 파일 위치

- **작업 기억:** 현재 작업 디렉터리의 `CLAUDE.md`
- **심층 기억:** `memory/` 하위 디렉터리

## 작업 기억 형식(CLAUDE.md)

간결하게 표를 사용합니다. 전체 50-80줄을 목표로 합니다.

```markdown
# 기억

## 나
[이름], [팀]의 [역할].

## 사람
| 누구 | 역할 |
|-----|------|
| **Todd** | Todd Martinez, Finance lead |
| **Sarah** | Sarah Chen, Engineering(Platform) |
| **Greg** | Greg Wilson, Sales |
→ 전체 목록: memory/glossary.md, 프로필: memory/people/

## 용어
| 용어 | 의미 |
|------|---------|
| PSR | Pipeline Status Report |
| P0 | 모든 걸 제쳐두는 우선순위 |
| standup | 매일 오전 9시 싱크 |
→ 전체 용어집: memory/glossary.md

## 프로젝트
| 이름 | 내용 |
|------|------|
| **Phoenix** | DB 마이그레이션, Q2 출시 |
| **Horizon** | 모바일 앱 리디자인 |
→ 세부 정보: memory/projects/

## 선호
- 버퍼가 있는 25분 회의
- 비동기 우선, 이메일보다 Slack
- 금요일 오후 회의 없음
```

## 심층 기억 형식(memory/)

**memory/glossary.md** - 해독표:
```markdown
# 용어집

업무 약어, 내부 용어, 내부 언어.

## 약어
| 용어 | 의미 | 맥락 |
|------|---------|---------|
| PSR | Pipeline Status Report | 주간 세일즈 문서 |
| OKR | Objectives & Key Results | 분기 계획 |
| P0/P1/P2 | 우선순위 수준 | P0 = 모든 걸 제쳐둠 |

## 내부 용어
| 용어 | 의미 |
|------|---------|
| standup | #engineering에서 하는 매일 오전 9시 싱크 |
| the migration | Project Phoenix의 데이터베이스 작업 |
| ship it | 프로덕션에 배포 |
| escalate | 리더십을 끌어들이다 |

## 별명 → 정식 이름
| 별명 | 사람 |
|----------|--------|
| Todd | Todd Martinez(Finance) |
| T | 역시 Todd Martinez |

## 프로젝트 코드명
| 코드명 | 프로젝트 |
|----------|--------|
| Phoenix | 데이터베이스 마이그레이션 |
| Horizon | 새 모바일 앱 |
```

**memory/people/{name}.md:**
```markdown
# Todd Martinez

**다른 이름:** Todd, T
**역할:** Finance Lead
**팀:** Finance
**보고 대상:** CFO(Michael Chen)

## 커뮤니케이션
- Slack DM 선호
- 응답이 빠르고 매우 직설적
- 최적 시간: 아침

## 맥락
- 모든 PSR과 재무 보고를 담당
- $500k를 넘는 딜 승인 핵심 연락처
- Sales와 예측에서 긴밀히 협업

## 메모
- Cubs 팬, 야구 이야기 좋아함
```

**memory/projects/{name}.md:**
```markdown
# Project Phoenix

**코드명:** Phoenix
**다른 이름:** "the migration"
**상태:** 진행 중, Q2 출시

## 무엇인가
기존 Oracle에서 PostgreSQL로의 데이터베이스 마이그레이션.

## 핵심 인물
- Sarah - 기술 리드
- Todd - 예산 담당
- Greg - 이해관계자(세일즈 영향)

## 맥락
$1.2M 예산, 6개월 일정. Horizon 프로젝트의 핵심 경로.
```

**memory/context/company.md:**
```markdown
# 회사 맥락

## 도구 및 시스템
| 도구 | 용도 | 내부 이름 |
|------|----------|---------------|
| Slack | Communication | - |
| Asana | Engineering tasks | - |
| Salesforce | CRM | "SF" or "the CRM" |
| Notion | 문서/위키 | - |

## 팀
| 팀 | 하는 일 | 핵심 인물 |
|------|--------------|------------|
| Platform | 인프라 | Sarah(리드) |
| Finance | 돈 관련 업무 | Todd(리드) |
| Sales | 매출 | Greg |

## 프로세스
| 프로세스 | 의미 |
|---------|---------------|
| 주간 싱크 | 월요일 오전 10시 전체 회의 |
| 배포 검토 | 목요일 배포 승인 |
```
