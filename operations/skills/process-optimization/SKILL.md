---
name: process-optimization
description: Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.
---

# 프로세스 최적화

기존 프로세스를 분석하고 개선안을 권고합니다.

## 분석 프레임워크

### 1. 현재 상태 맵핑
- 모든 단계, 의사결정 지점, 인계점을 문서화합니다.
- 누가 무엇을 하고 각 단계가 얼마나 걸리는지 식별합니다.
- 수동 단계, 승인, 대기 시간을 기록합니다.

### 2. 낭비 식별
- **대기**: 큐에서 기다리거나 승인을 기다리는 시간
- **재작업**: 실패해서 다시 해야 하는 단계
- **인계**: 각 인계는 실패나 지연의 가능 지점
- **과잉 처리**: 가치를 더하지 않는 단계
- **수동 작업**: 자동화할 수 있는 업무

### 3. 미래 상태 설계
- 불필요한 단계를 제거합니다.
- 가능하면 자동화합니다.
- 인계 횟수를 줄입니다.
- 독립적인 단계는 병렬화합니다.
- 게이트가 아닌 체크포인트를 추가합니다.

### 4. 영향 측정
- 사이클당 절감된 시간
- 오류율 감소
- 비용 절감
- 직원 만족도 향상

## 출력

구체적인 개선 권고, 예상 영향, 실행 계획이 포함된 전후 프로세스 비교를 작성합니다.
