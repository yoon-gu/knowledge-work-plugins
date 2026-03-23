---
name: capacity-plan
description: Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you need the numbers, deciding whether to hire or deprioritize, or stress-testing whether upcoming projects fit the people you have.
argument-hint: "<team or project scope>"
---

# /capacity-plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

팀 용량을 분석하고 리소스 배분을 계획합니다.

## 사용법

```
/capacity-plan $ARGUMENTS
```

## 필요한 정보

- **팀 규모와 역할**: 현재 누구를 보유하고 있나요?
- **현재 업무량**: 지금 무엇을 하고 있나요? (프로젝트 추적기에서 업로드하거나 설명)
- **다가오는 업무**: 다음 분기에 무엇이 들어오나요?
- **제약 사항**: 예산, 채용 일정, 기술 요구사항

## 계획 차원

### 사람
- 사용 가능한 인원과 기술
- 현재 배치와 활용도
- 예정된 채용과 일정
- 계약직과 벤더 용량

### 예산
- 범주별 운영 예산
- 프로젝트별 예산
- 차이 추적
- 예측 대비 실적

### 시간
- 프로젝트 일정과 의존성
- 크리티컬 패스 분석
- 버퍼 및 비상 계획
- 마감일 관리

## 활용도 목표

| 역할 유형 | 목표 활용도 | 비고 |
|-----------|-------------------|-------|
| IC / Specialist | 75-80% | 대응 업무와 성장 여지를 남겨두세요 |
| Manager | 60-70% | 관리 오버헤드, 회의, 1:1 |
| On-call / Support | 50-60% | 인터럽트 중심 업무는 예측하기 어렵습니다 |

## 흔한 함정

- 100% 활용도로 계획하기(예상 밖 상황을 위한 버퍼가 없음)
- 회의 부담과 컨텍스트 전환 비용을 무시하기
- 휴가, 공휴일, 병가를 반영하지 않기
- 모든 시간을 동일하게 취급하기(창의적 업무 ≠ 행정 업무)

## 출력

```markdown
## 용량 계획: [팀/프로젝트]
**기간:** [날짜 범위] | **팀 규모:** [X]

### 현재 활용도
| 사람/역할 | 용량 | 배정됨 | 사용 가능 | 활용도 |
|-------------|----------|-----------|-----------|-------------|
| [Name/Role] | [hrs/wk] | [hrs/wk] | [hrs/wk] | [X]% |

### 용량 요약
- **총 용량**: [X] 시간/주
- **현재 배정됨**: [X] 시간/주 ([X]%)
- **사용 가능**: [X] 시간/주 ([X]%)
- **과배정**: [100%를 초과한 인원 X명]

### 다가오는 수요
| 프로젝트/이니셔티브 | 시작 | 종료 | 필요한 리소스 | 격차 |
|--------------------|-------|-----|-----------------|-----|
| [Project] | [Date] | [Date] | [X FTEs] | [Covered/Gap] |

### 병목
- [과부하된 기술 또는 역할]
- [업무가 몰리는 시기]

### 권고 사항
1. [Hire / Contract / Reprioritize / Delay]
2. [Specific action]

### 시나리오
| 시나리오 | 결과 |
|----------|---------|
| 아무것도 하지 않음 | [무슨 일이 일어나는지] |
| [X]명 채용 | [무엇이 바뀌는지] |
| [Y] 우선순위 낮춤 | [무엇이 확보되는지] |
```

## 연결 도구가 있을 경우

If **~~project tracker** is connected:
- 현재 업무량과 티켓 배정을 자동으로 가져옵니다.
- 개인별 다음 스프린트 또는 분기 약속을 표시합니다.

If **~~calendar** is connected:
- PTO, 공휴일, 반복 회의 부담을 반영합니다.
- 개인별 실제 사용 가능 시간을 계산합니다.

## 팁

1. **모든 업무를 포함하세요** - BAU, 프로젝트, 지원, 회의까지. 사람들은 프로젝트 업무에 100% 투입될 수 없습니다.
2. **버퍼를 계획하세요** - 목표 활용도는 80%로 잡으세요. 100%는 예상 밖 상황을 수용할 여지가 없다는 뜻입니다.
3. **정기적으로 업데이트하세요** - 용량 계획은 금방 낡습니다. 매월 검토하세요.
