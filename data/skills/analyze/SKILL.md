---
name: analyze
description: Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeholders.
argument-hint: "<question>"
---

# /analyze - 데이터 질문에 답변

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 하는 경우, [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

간단한 조회부터 전체 분석, 공식 보고서까지 데이터 질문에 답변합니다.

## 사용법

```
/analyze <자연어 질문>
```

## 워크플로우

### 1. 질문 이해

사용자의 질문을 파악하고 다음을 결정합니다:

- **복잡도 수준**:
  - **빠른 답변**: 단일 지표, 간단한 필터, 사실 조회 (예: "지난 주에 몇 명이 가입했나요?")
  - **전체 분석**: 다차원 탐색, 트렌드 분석, 비교 (예: "전환율 하락의 원인은 무엇인가요?")
  - **공식 보고서**: 방법론, 주의사항, 권장사항이 포함된 포괄적인 조사 (예: "구독 지표에 대한 분기 비즈니스 리뷰 준비")
- **데이터 요구사항**: 필요한 테이블, 지표, 차원, 기간
- **출력 형식**: 숫자, 테이블, 차트, 내러티브, 또는 조합

### 2. 데이터 수집

**data warehouse MCP 서버가 연결된 경우:**

1. 관련 테이블 및 열을 찾기 위해 스키마 탐색
2. 필요한 데이터 추출을 위한 SQL 쿼리 작성
3. 쿼리 실행 및 결과 검색
4. 쿼리 실패 시 디버그 후 재시도 (열 이름, 테이블 참조, 특정 방언의 구문 확인)
5. 결과가 예상치 못한 경우 진행 전 정합성 검사 실행

**data warehouse가 연결되지 않은 경우:**

1. 사용자에게 다음 방법 중 하나로 데이터 제공 요청:
   - 쿼리 결과 직접 붙여넣기
   - CSV 또는 Excel 파일 업로드
   - 스키마 설명을 통해 수동 실행할 쿼리 작성
2. 수동 실행을 위한 쿼리 작성 시, 방언별 모범 사례를 위해 `sql-queries` 스킬 사용
3. 데이터가 제공되면 분석 진행

### 3. 분석

- 관련 지표, 집계, 비교 계산
- 패턴, 트렌드, 이상값, 이례 사항 식별
- 차원 간 비교 (기간, 세그먼트, 카테고리)
- 복잡한 분석의 경우 문제를 세부 질문으로 분해하여 각각 처리

### 4. 발표 전 검증

결과를 공유하기 전에 검증 검사를 수행합니다:

- **행 수 정합성**: 레코드 수가 합리적인가?
- **Null 확인**: 결과를 왜곡할 수 있는 예상치 못한 null이 있는가?
- **크기 확인**: 숫자가 합리적인 범위 내에 있는가?
- **트렌드 연속성**: 시계열에 예상치 못한 간격이 있는가?
- **집계 논리**: 소계가 합계에 올바르게 합산되는가?

문제가 발견되면 조사하고 주의사항을 기록합니다.

### 5. 결과 발표

**빠른 답변의 경우:**
- 관련 맥락과 함께 답변을 직접 제시
- 재현성을 위해 사용된 쿼리 포함 (접힌 형태 또는 코드 블록)

**전체 분석의 경우:**
- 핵심 발견 또는 인사이트를 앞에 제시
- 데이터 테이블 및/또는 시각화로 뒷받침
- 방법론 및 주의사항 기록
- 후속 질문 제안

**공식 보고서의 경우:**
- 핵심 시사점이 담긴 경영진 요약
- 접근 방식 및 데이터 소스를 설명하는 방법론 섹션
- 근거 자료를 포함한 상세 결과
- 주의사항, 한계, 데이터 품질 메모
- 권장사항 및 제안 후속 단계

### 6. 필요 시 시각화

차트가 테이블보다 결과를 더 효과적으로 전달하는 경우:

- `data-visualization` 스킬을 사용하여 적합한 차트 유형 선택
- Python 시각화 생성 또는 HTML 대시보드에 통합
- 명확성과 정확성을 위한 시각화 모범 사례 준수

## 예제

**빠른 답변:**
```
/analyze How many new users signed up in December?
```

**전체 분석:**
```
/analyze What's causing the increase in support ticket volume over the past 3 months? Break down by category and priority.
```

**공식 보고서:**
```
/analyze Prepare a data quality assessment of our customer table -- completeness, consistency, and any issues we should address.
```

## 팁

- 가능하면 기간, 세그먼트 또는 지표를 구체적으로 명시하세요
- 테이블 이름을 알고 있다면 언급하면 처리 속도가 빨라집니다
- 복잡한 질문의 경우 Claude가 여러 쿼리로 분해할 수 있습니다
- 결과는 항상 발표 전에 검증됩니다 — 이상한 점이 있으면 Claude가 알려드립니다
