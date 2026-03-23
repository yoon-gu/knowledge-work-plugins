---
name: update
description: Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.
argument-hint: "[--comprehensive]"
---

# Update 명령어

> 낯선 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

작업 목록과 메모리를 최신 상태로 유지합니다. 두 가지 모드:

- **기본:** 외부 도구에서 작업 동기화, 오래된 항목 분류, 메모리 갭 확인
- **`--comprehensive`:** 채팅, 이메일, 캘린더, 문서 심층 스캔 — 놓친 할 일 플래그 지정 및 새 메모리 제안

## 사용법

```bash
/productivity:update
/productivity:update --comprehensive
```

## 기본 모드

### 1. 현재 상태 로드

`TASKS.md`와 `memory/` 디렉터리를 읽습니다. 없으면 먼저 `/productivity:start`를 제안합니다.

### 2. 외부 소스에서 작업 동기화

사용 가능한 작업 소스를 확인합니다:
- **프로젝트 트래커** (예: Asana, Linear, Jira) (MCP 사용 가능한 경우)
- **GitHub Issues** (저장소에 있는 경우): `gh issue list --assignee=@me`

소스를 사용할 수 없으면 3단계로 건너뜁니다.

**사용자에게 배정된 작업(열림/진행 중)을 가져옵니다.** TASKS.md와 비교합니다:

| 외부 작업 | TASKS.md 일치? | 조치 |
|---------------|-----------------|--------|
| 발견됨, TASKS.md에 없음 | 일치 없음 | 추가 제안 |
| 발견됨, 이미 TASKS.md에 있음 | 제목 유사 일치 | 건너뜀 |
| TASKS.md에 있음, 외부에 없음 | 일치 없음 | 잠재적으로 오래됨으로 플래그 |
| 외부에서 완료됨 | Active 섹션에 있음 | 완료 표시 제안 |

변경 사항을 제시하고 사용자가 추가/완료할 항목을 결정하게 합니다.

### 3. 오래된 항목 분류

TASKS.md의 Active 작업을 검토하고 플래그 지정:
- 마감일이 지난 작업
- Active에서 30일 이상 된 작업
- 컨텍스트 없는 작업 (담당자 없음, 프로젝트 없음)

각각을 분류합니다: 완료 표시? 일정 재조정? Someday로 이동?

### 4. 메모리 갭을 위한 작업 해독

각 작업에서 모든 엔티티(사람, 프로젝트, 약어, 도구, 링크)를 해독합니다:

```
작업: "Send PSR to Todd re: Phoenix blockers"

해독:
- PSR → ✓ Pipeline Status Report (용어집에 있음)
- Todd → ✓ Todd Martinez (people/에 있음)
- Phoenix → ? 메모리에 없음
```

완전히 해독된 것과 갭이 있는 것을 추적합니다.

### 5. 갭 채우기

알 수 없는 용어를 그룹화하여 제시합니다:
```
작업에서 컨텍스트가 없는 용어를 발견했습니다:

1. "Phoenix" (출처: "Send PSR to Todd re: Phoenix blockers")
   → Phoenix가 무엇인가요?

2. "Maya" (출처: "sync with Maya on API design")
   → Maya는 누구인가요?
```

답변을 적절한 메모리 파일(people/, projects/, glossary.md)에 추가합니다.

### 6. 보강 정보 캡처

작업에는 종종 메모리보다 풍부한 컨텍스트가 포함됩니다. 추출하고 업데이트합니다:
- 작업의 **링크** → 프로젝트/사람 파일에 추가
- **상태 변경** ("launch done") → 프로젝트 상태 업데이트, CLAUDE.md에서 강등
- **관계** ("Todd's sign-off on Maya's proposal") → 사람 간 상호 참조
- **마감일** → 프로젝트 파일에 추가

### 7. 보고

```
업데이트 완료:
- 작업: 프로젝트 트래커(예: Asana)에서 +3개, 1개 완료, 2개 분류
- 메모리: 2개 갭 채움, 1개 프로젝트 보강
- 모든 작업 해독됨 ✓
```

## 종합 모드 (`--comprehensive`)

기본 모드의 모든 것에 더해 최근 활동의 심층 스캔.

### 추가 단계: 활동 소스 스캔

사용 가능한 MCP 소스에서 데이터를 수집합니다:
- **채팅:** 최근 메시지 검색, 활성 채널 읽기
- **이메일:** 발송 메시지 검색
- **문서:** 최근에 건드린 문서 목록
- **캘린더:** 최근 + 예정된 이벤트 목록

### 추가 단계: 놓친 할 일 플래그

활동을 TASKS.md와 비교합니다. 추적되지 않은 실행 항목을 표시합니다:

```
## 놓쳤을 수 있는 작업

활동에서 캡처하지 않은 할 일처럼 보이는 항목들:

1. 채팅에서 (1월 18일):
   "금요일까지 업데이트된 목업을 보내겠습니다"
   → TASKS.md에 추가할까요?

2. 회의 "Phoenix Standup"에서 (1월 17일):
   반복 회의가 있지만 활성 Phoenix 작업이 없습니다
   → 필요한 것이 있나요?

3. 이메일에서 (1월 16일):
   "이번 주에 API 스펙을 검토하겠습니다"
   → TASKS.md에 추가할까요?
```

사용자가 추가할 항목을 선택하게 합니다.

### 추가 단계: 새 메모리 제안

메모리에 없는 새 엔티티를 표시합니다:

```
## 새 사람 (메모리에 없음)
| 이름 | 빈도 | 컨텍스트 |
|------|-----------|---------|
| Maya Rodriguez | 12회 언급 | 디자인, UI 리뷰 |
| Alex K | 8회 언급 | API에 대한 DM |

## 새 프로젝트/주제
| 이름 | 빈도 | 컨텍스트 |
|------|-----------|---------|
| Starlight | 15회 언급 | 계획 문서, 제품 |

## 정리 제안
- **Horizon 프로젝트** — 30일 동안 언급 없음. 완료로 표시할까요?
```

신뢰도별로 그룹화하여 제시합니다. 높은 신뢰도 항목은 직접 추가 제안, 낮은 신뢰도 항목은 질문합니다.

## 참고사항

- 사용자 확인 없이 작업이나 메모리를 자동으로 추가하지 않습니다
- 외부 소스 링크는 사용 가능한 경우 보존됩니다
- 작업 제목의 유사 일치로 사소한 단어 차이를 처리합니다
- 자주 실행해도 안전합니다 — 새 정보가 있을 때만 업데이트됩니다
- `--comprehensive`는 항상 대화형으로 실행됩니다
