---
name: vendor-review
description: Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contract, comparing two vendors side-by-side, or building a TCO breakdown and negotiation points before procurement sign-off.
argument-hint: "<vendor name or proposal>"
---

# /vendor-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

비용, 리스크, 성과, 적합성을 다루는 구조화된 분석으로 벤더를 평가합니다.

## 사용법

```
/vendor-review $ARGUMENTS
```

## 필요한 정보

- **벤더 이름**: 누구를 평가하나요?
- **맥락**: 신규 벤더 평가, 갱신 결정, 아니면 비교인가요?
- **세부 정보**: 계약 조건, 가격, 제안서 문서, 현재 성과 데이터

## 평가 프레임워크

### 비용 분석(Total Cost of Ownership)
- 총 소유 비용(라이선스 비용만이 아님)
- 구현 및 마이그레이션 비용
- 교육 및 온보딩 비용
- 지속적인 지원 및 유지보수
- 종료 비용(데이터 마이그레이션, 계약 종료)

### 리스크 평가
- 벤더의 재무 안정성
- 보안 및 컴플라이언스 상태
- 집중 리스크(단일 벤더 의존)
- 계약 종속성과 종료 조건
- 비즈니스 연속성 및 재해 복구

### 성과 지표
- SLA 준수
- 지원 응답 시간
- 가동 시간과 신뢰성
- 기능 제공 주기
- 고객 만족도

### 비교 매트릭스
벤더를 비교할 때는 가격, 기능, 통합, 보안, 지원, 계약 조건, 레퍼런스를 포함한 나란한 매트릭스를 만듭니다.

## 출력

```markdown
## 벤더 검토: [벤더 이름]
**날짜:** [날짜] | **유형:** [신규 / 갱신 / 비교]

### 요약
[2-3문장 권고]

### 비용 분석
| 항목 | 연간 비용 | 비고 |
|-----------|-------------|-------|
| 라이선스/구독 | $[X] | [좌석당, 정액, 사용량 기반] |
| 구현 | $[X] | [일회성] |
| 지원/유지보수 | $[X] | [포함 또는 추가] |
| **1년차 합계** | **$[X]** | |
| **3년 총합** | **$[X]** | |

### 리스크 평가
| 리스크 | 발생 가능성 | 영향 | 완화 방안 |
|------|-----------|--------|------------|
| [리스크] | 높음/중간/낮음 | 높음/중간/낮음 | [완화 방안] |

### 강점
- [강점 1]
- [강점 2]

### 우려 사항
- [우려 1]
- [우려 2]

### 권고
[진행 / 재협상 / 보류] - [이유]

### 협상 포인트
- [협상 지점 1]
- [협상 지점 2]
```

## 연결 도구가 있을 경우

If **~~knowledge base** is connected:
- 기존 벤더 평가, 계약, 성과 검토를 검색합니다.
- 조달 정책과 승인 기준을 가져옵니다.

If **~~procurement** is connected:
- 현재 계약 조건, 지출 이력, 갱신 날짜를 가져옵니다.
- 기존 벤더 계약과 가격을 비교합니다.

## 팁

1. **제안서를 업로드하세요** - 벤더 문서에서 가격, 조건, SLA를 추출할 수 있습니다.
2. **벤더를 비교하세요** - "Vendor A와 Vendor B를 비교해 줘"라고 하면 나란한 분석을 제공합니다.
3. **현재 지출을 포함하세요** - 갱신의 경우 현재 얼마를 내는지 알아야 가격 변화를 평가할 수 있습니다.
