---
name: runbook
description: Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.
argument-hint: "<process or task name>"
---

# /runbook

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

반복 작업이나 절차를 위한 단계별 운영 runbook을 만듭니다.

## 사용법

```
/runbook $ARGUMENTS
```

## 출력

```markdown
## Runbook: [작업 이름]
**담당자:** [팀/사람] | **빈도:** [매일/매주/매월/필요 시]
**마지막 업데이트:** [날짜] | **마지막 실행:** [날짜]

### 목적
[이 runbook이 무엇을 달성하며 언제 사용하는지]

### 사전 조건
- [ ] [Access or permission needed]
- [ ] [Tool or system required]
- [ ] [Data or input needed]

### 절차

#### 단계 1: [이름]
```
[Exact command, action, or instruction]
```
**예상 결과:** [무엇이 일어나야 하는지]
**실패 시:** [어떻게 할지]

#### 단계 2: [이름]
```
[Exact command, action, or instruction]
```
**예상 결과:** [무엇이 일어나야 하는지]
**실패 시:** [어떻게 할지]

### 검증
- [ ] [작업이 성공적으로 완료되었는지 확인하는 방법]
- [ ] [무엇을 확인할지]

### 문제 해결
| 증상 | 가능성 있는 원인 | 해결 |
|---------|-------------|-----|
| [보이는 현상] | [이유] | [조치] |

### 롤백
[문제가 생겼을 때 이를 되돌리는 방법]

### 에스컬레이션
| 상황 | 연락처 | 방법 |
|-----------|---------|--------|
| [언제 에스컬레이션할지] | [누구] | [연락 방법] |

### 이력
| 날짜 | 실행자 | 메모 |
|------|--------|-------|
| [날짜] | [사람] | [문제나 관찰 사항] |
```

## 연결 도구가 있을 경우

If **~~knowledge base** is connected:
- 기존 runbook을 검색해 새로 만들기보다 업데이트합니다.
- 완성된 runbook을 운영 위키에 게시합니다.

If **~~ITSM** is connected:
- runbook을 관련 인시던트 유형과 변경 요청에 연결합니다.
- 온콜 일정에서 에스컬레이션 연락처를 자동 입력합니다.

## 팁

1. **아주 구체적으로 쓰세요** - "스크립트를 실행한다"는 단계가 아닙니다. "운영 서버에서 `python sync.py --prod --dry-run`를 실행한다"처럼 써야 합니다.
2. **실패 가능성을 포함하세요** - 각 단계에서 무엇이 잘못될 수 있고 어떻게 대응할지 적으세요.
3. **runbook을 테스트하세요** - 프로세스를 모르는 사람이 따라 하게 해 보세요. 막히는 지점을 고치세요.
