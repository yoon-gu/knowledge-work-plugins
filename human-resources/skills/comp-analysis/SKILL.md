---
name: comp-analysis
description: Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.
argument-hint: "<role, level, or dataset>"
---

# /comp-analysis

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우, [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

벤치마킹, 밴드 배치, 계획 수립을 위한 보상 데이터를 분석합니다. 채용, 유지, 주식 계획을 위해 시장 데이터와 보상을 비교 분석합니다.

## 사용법

```
/comp-analysis $ARGUMENTS
```

## 필요한 정보

**옵션 A: 단일 역할 분석**
"SF에서 시니어 소프트웨어 엔지니어에게 얼마를 지급해야 하나요?"

**옵션 B: 보상 데이터 업로드**
CSV를 업로드하거나 보상 밴드를 붙여넣으세요. 배치를 분석하고 이상값을 파악하며 시장과 비교합니다.

**옵션 C: 주식 모델링**
"주가 $50에서 4년에 걸쳐 10,000주 갱신 그랜트를 모델링해 주세요."

## 보상 프레임워크

### 총 보상의 구성 요소
- **기본급**: 현금 보상
- **주식**: RSU, 스톡옵션 또는 기타 주식
- **보너스**: 연간 목표 보너스, 사이닝 보너스
- **복리후생**: 건강보험, 퇴직금, 복지 혜택 (정량화 어려움)

### 주요 변수
- **역할**: 직무 및 전문 분야
- **레벨**: IC 레벨, 관리자 레벨
- **위치**: 지역별 급여 조정
- **회사 단계**: 스타트업 vs. 성장기 vs. 상장사
- **산업**: 기술 vs. 금융 vs. 의료

### 데이터 출처
- **~~compensation data 연결 시**: 검증된 벤치마크 조회
- **미연결 시**: 웹 조사, 공개 급여 데이터, 사용자 제공 정보 활용
- 데이터 최신성과 출처 한계를 항상 명시

## 출력 결과

기본급, 주식, 총 보상에 대한 백분위 밴드(25th, 50th, 75th, 90th)를 제공합니다. 위치 조정 및 회사 단계 맥락을 포함합니다.

```markdown
## Compensation Analysis: [Role/Scope]

### Market Benchmarks
| Percentile | Base | Equity | Total Comp |
|------------|------|--------|------------|
| 25th | $[X] | $[X] | $[X] |
| 50th | $[X] | $[X] | $[X] |
| 75th | $[X] | $[X] | $[X] |
| 90th | $[X] | $[X] | $[X] |

**Sources:** [Web research, compensation data tools, or user-provided data]

### Band Analysis (if data provided)
| Employee | Current Base | Band Min | Band Mid | Band Max | Position |
|----------|-------------|----------|----------|----------|----------|
| [Name] | $[X] | $[X] | $[X] | $[X] | [Below/At/Above] |

### Recommendations
- [Specific compensation recommendations]
- [Equity considerations]
- [Retention risks if applicable]
```

## 커넥터 사용 시

**~~compensation data**가 연결된 경우:
- 역할, 레벨, 위치별 검증된 시장 벤치마크 조회
- 실시간 시장 데이터와 밴드 비교

**~~HRIS**가 연결된 경우:
- 밴드 분석을 위한 현재 직원 보상 데이터 조회
- 이상값 및 유지 위험 자동 파악

## 팁

1. **위치가 중요합니다** — 벤치마킹 시 항상 위치를 명시하세요. SF, Austin, London은 매우 다릅니다.
2. **기본급만이 아닌 총 보상** — 완전한 그림을 위해 주식, 보너스, 복리후생을 포함하세요.
3. **데이터 기밀을 유지하세요** — 보상 데이터는 민감합니다. 결과는 대화 내에 유지됩니다.
