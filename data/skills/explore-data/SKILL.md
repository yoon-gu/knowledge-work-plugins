---
name: explore-data
description: 데이터셋의 형태, 품질, 패턴을 이해하기 위해 프로파일링하고 탐색합니다. 새 테이블이나 파일을 접할 때, NULL 비율과 열 분포를 확인할 때, 중복이나 수상한 값 같은 데이터 품질 문제를 찾을 때, 또는 어떤 차원과 지표를 분석할지 정할 때 사용합니다.
argument-hint: "<table or file>"
---

# /explore-data - 데이터셋 프로파일링 및 탐색

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

테이블이나 업로드된 파일에 대한 종합적인 데이터 프로파일을 생성합니다. 분석에 들어가기 전에 형태, 품질, 패턴을 파악하세요.

## 사용법

```
/explore-data <table_name or file>
```

## 워크플로

### 1. 데이터에 접근하기

**데이터 웨어하우스 MCP 서버가 연결되어 있다면:**

1. 테이블 이름을 해석합니다(스키마 접두어를 처리하고, 모호하면 후보를 제안)
2. 테이블 메타데이터를 조회합니다: 열 이름, 타입, 가능한 경우 설명
3. 실데이터에 대해 프로파일링 쿼리를 실행합니다

**파일(CSV, Excel, Parquet, JSON)이 제공되었다면:**

1. 파일을 읽어 작업용 데이터셋으로 불러옵니다
2. 데이터로부터 열 타입을 추론합니다

**둘 다 아니라면:**

1. 사용자에게 테이블 이름(웨어하우스가 연결된 경우) 또는 파일 업로드를 요청합니다
2. 테이블 스키마를 설명해 준다면, 어떤 프로파일링 쿼리를 실행할지 안내합니다

### 2. 구조 이해하기

어떤 데이터도 분석하기 전에 구조를 이해하세요:

**테이블 수준 질문:**
- 행과 열은 몇 개인가요?
- 그레인은 무엇인가요(한 행이 무엇을 의미하나요)?
- 기본 키는 무엇인가요? 유일한가요?
- 데이터는 언제 마지막으로 갱신되었나요?
- 데이터는 얼마나 오래 전까지 거슬러 올라가나요?

**열 분류** - 각 열을 다음 중 하나로 분류합니다:
- **Identifier**: 고유 키, 외래 키, 엔터티 ID
- **Dimension**: 그룹화/필터링용 범주형 속성(status, type, region, category)
- **Metric**: 측정용 수치 값(revenue, count, duration, score)
- **Temporal**: 날짜와 타임스탬프(created_at, updated_at, event_date)
- **Text**: 자유 형식 텍스트 필드(description, notes, name)
- **Boolean**: 참/거짓 플래그
- **Structural**: JSON, 배열, 중첩 구조

### 3. 데이터 프로파일 생성

다음 프로파일링 검사를 실행합니다:

**테이블 수준 지표:**
- 총 행 수
- 열 수와 타입 분포
- 가능한 경우 추정 테이블 크기(메타데이터 기준)
- 날짜 범위 커버리지(날짜 열의 min/max)

**모든 열:**
- NULL 개수와 NULL 비율
- 고유 개수와 카디널리티 비율(고유 / 전체)
- 가장 흔한 값(빈도 상위 5-10개)
- 가장 드문 값(이상치 확인용 하위 5개)

**숫자 열(지표):**
```text
min, max, mean, median (p50)
standard deviation
percentiles: p1, p5, p25, p75, p95, p99
zero count
negative count (if unexpected)
```

**문자열 열(차원, 텍스트):**
```text
min length, max length, avg length
empty string count
pattern analysis (values follow a format?)
case consistency (all upper, all lower, mixed?)
leading/trailing whitespace count
```

**날짜/타임스탬프 열:**
```text
min date, max date
null dates
future dates (if unexpected)
distribution by month/week
gaps in time series
```

**불리언 열:**
```text
true count, false count, null count
true rate
```

**열 유형(차원, 지표, 날짜, ID)별로 묶은 깔끔한 요약 표**로 프로파일을 제시합니다.

### 4. 데이터 품질 문제 식별

아래 품질 평가 프레임워크를 적용합니다. 다음 문제를 표시하세요:

- **높은 NULL 비율**: NULL이 >5%인 열(경고), >20%인 열(알림)
- **낮은 카디널리티의 의외성**: 높은 카디널리티여야 하는데 그렇지 않은 열(예: 고유값이 50개뿐인 `user_id`)
- **높은 카디널리티의 의외성**: 범주형이어야 하는데 고유값이 너무 많은 열
- **수상한 값**: 양수만 기대되는 음수 금액, 과거 데이터의 미래 날짜, 명백한 자리표시자 값(예: "N/A", "TBD", "test", "999999")
- **중복 탐지**: 자연 키가 있는지, 중복이 있는지 확인
- **분포 왜도**: 평균에 영향을 줄 수 있는 극단적으로 치우친 숫자 분포
- **인코딩 문제**: 범주형 필드의 대소문자 혼용, 후행 공백, 불일치한 형식

### 5. 관계와 패턴 발견

개별 열을 프로파일링한 뒤:

- **외래 키 후보**: 다른 테이블과 연결될 수 있는 ID 열
- **계층 구조**: 자연스러운 드릴다운 경로를 이루는 열(country > state > city)
- **상관관계**: 함께 움직이는 숫자 열
- **파생 열**: 다른 열로부터 계산된 것으로 보이는 열
- **중복 열**: 동일하거나 거의 동일한 정보를 담은 열

### 6. 흥미로운 차원과 지표 제안

열 프로파일을 바탕으로 다음을 추천합니다:

- **데이터를 자르기에 좋은 차원 열**(적절한 카디널리티를 가진 범주형 열, 3-50개 값)
- **측정에 좋은 핵심 지표 열**(의미 있는 분포를 가진 숫자 열)
- **추세 분석에 적합한 시간 열**
- **데이터에서 드러나는 자연스러운 그룹 또는 계층**
- **다른 테이블과 연결할 수 있는 조인 키 후보**(ID 열, 외래 키)

### 7. 후속 분석 추천

사용자가 다음에 실행할 수 있는 3-5개의 구체적 분석을 제안합니다:

- "[차원]별로 묶은 [시간 열] 기준 [지표] 추세 분석"
- "[이상치가 많은 열]의 분포를 깊게 파고들어 이상치를 이해"
- "[문제 열]에 대한 데이터 품질 조사"
- "[metric_a]와 [metric_b] 사이의 상관관계 분석"
- "[날짜 열]과 [상태 열]을 사용하는 코호트 분석"

## 출력 형식

```
## Data Profile: [table_name]

### Overview
- Rows: 2,340,891
- Columns: 23 (8 dimensions, 6 metrics, 4 dates, 5 IDs)
- Date range: 2021-03-15 to 2024-01-22

### Column Details
[summary table]

### Data Quality Issues
[flagged issues with severity]

### Recommended Explorations
[numbered list of suggested follow-up analyses]
```

---

## 품질 평가 프레임워크

### 완전성 점수

각 열을 다음 기준으로 평가합니다:
- **완전** (>99% non-null): 초록
- **대체로 완전** (95-99%): 노랑 - NULL의 원인을 조사
- **불완전** (80-95%): 주황 - 왜 그런지, 그리고 중요한지 확인
- **희소** (<80%): 빨강 - 대체 없이 사용하기 어려울 수 있음

### 일관성 검사

다음 항목을 확인하세요:
- **값 형식 불일치**: 같은 개념이 다르게 표현됨("USA", "US", "United States", "us")
- **형식 불일치**: 숫자가 문자열로 저장되거나 날짜 형식이 제각각
- **참조 무결성**: 부모 레코드와 일치하지 않는 외래 키
- **비즈니스 규칙 위반**: 음수 수량, 시작일보다 이른 종료일, 100보다 큰 비율
- **열 간 일관성**: status = "completed"인데 completed_at이 NULL

### 정확성 지표

정확성 문제를 시사하는 적신호:
- **자리표시자 값**: 0, -1, 999999, "N/A", "TBD", "test", "xxx"
- **기본값**: 하나의 값이 지나치게 자주 나타남
- **오래된 데이터**: 활성 시스템인데 updated_at에 최근 변경이 없음
- **불가능한 값**: 150보다 큰 나이, 아주 먼 미래의 날짜, 음수 지속시간
- **반올림 편향**: 모든 값이 0이나 5로 끝남(측정이 아니라 추정일 수 있음)

### 시의성 평가

- 테이블은 언제 마지막으로 갱신되었나요?
- 예상 갱신 빈도는 어떻게 되나요?
- 이벤트 시간과 적재 시간 사이에 지연이 있나요?
- 시계열에 공백이 있나요?

## 패턴 발견 기법

### 분포 분석

숫자 열의 분포를 다음처럼 특성화하세요:
- **정규**: 평균과 중앙값이 가깝고 종 모양
- **우측 편향**: 큰 값 쪽 꼬리가 김(매출, 세션 지속시간에 흔함)
- **좌측 편향**: 작은 값 쪽 꼬리가 김(덜 흔함)
- **이봉분포**: 두 개의 봉우리(서로 다른 두 집단을 시사)
- **멱법칙**: 매우 큰 값은 소수, 작은 값은 다수(사용자 활동에 흔함)
- **균등분포**: 범위 전반에 걸쳐 빈도가 대체로 같음(종종 합성 또는 무작위)

### 시간적 패턴

시계열 데이터에서는 다음을 찾으세요:
- **추세**: 지속적인 상승 또는 하락
- **계절성**: 반복되는 패턴(주간, 월간, 분기, 연간)
- **요일 효과**: 평일과 주말의 차이
- **휴일 효과**: 알려진 휴일 전후의 하락 또는 급증
- **변화점**: 수준이나 추세의 급격한 변화
- **이상치**: 패턴을 깨는 개별 데이터 포인트

### 세그먼트 발견

다음으로 자연스러운 세그먼트를 식별하세요:
- 고유값이 3-20개인 범주형 열 찾기
- 세그먼트 값에 따라 지표 분포 비교
- 행동이 유의하게 다른 세그먼트 찾기
- 세그먼트가 동질적인지, 하위 세그먼트를 포함하는지 확인

### 상관관계 탐색

숫자 열 간에는:
- 모든 지표 쌍에 대한 상관행렬 계산
- 강한 상관관계(|r| > 0.7)를 조사 대상으로 표시
- 주의: 상관관계가 인과를 뜻하는 것은 아닙니다. 이를 명시적으로 표시하세요
- 비선형 관계(예: 이차, 로그)도 확인

## 스키마 이해와 문서화

### 스키마 문서화 템플릿

팀용으로 데이터셋을 문서화할 때:

```markdown
## Table: [schema.table_name]

**Description**: [이 테이블이 무엇을 나타내는지]
**Grain**: [한 행이 무엇을 뜻하는지]
**Primary Key**: [column(s)]
**Row Count**: [날짜를 포함한 대략치]
**Update Frequency**: [실시간 / 매시간 / 매일 / 매주]
**Owner**: [책임 팀 또는 담당자]

### Key Columns

| Column | Type | Description | Example Values | Notes |
|--------|------|-------------|----------------|-------|
| user_id | STRING | 고유 사용자 식별자 | "usr_abc123" | users.id로 가는 FK |
| event_type | STRING | 이벤트 유형 | "click", "view", "purchase" | 고유값 15개 |
| revenue | DECIMAL | USD 기준 거래 매출 | 29.99, 149.00 | 구매가 아닌 이벤트는 Null |
| created_at | TIMESTAMP | 이벤트가 발생한 시점 | 2024-01-15 14:23:01 | 이 열을 기준으로 파티션됨 |

### Relationships
- `user_id`로 `users`와 조인
- `product_id`로 `products`와 조인
- `event_details`의 부모( event_id 기준 1:many)

### Known Issues
- [알려진 데이터 품질 문제를 나열]
- [분석자가 주의할 점을 메모]

### Common Query Patterns
- [이 테이블의 일반적인 사용 사례]
```

### 스키마 탐색 쿼리

데이터 웨어하우스에 연결되어 있다면, 아래 패턴으로 스키마를 탐색하세요:

```sql
-- 스키마의 모든 테이블 나열(PostgreSQL)
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

-- 열 세부 정보(PostgreSQL)
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'my_table'
ORDER BY ordinal_position;

-- 테이블 크기(PostgreSQL)
SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- 모든 테이블의 행 수(일반 패턴)
-- 테이블별로 실행: SELECT COUNT(*) FROM table_name
```

### 계보와 의존성

익숙하지 않은 데이터 환경을 탐색할 때:

1. "출력" 테이블부터 시작합니다(보고서나 대시보드가 소비하는 것)
2. 상류를 추적합니다: 어떤 테이블이 이들을 입력하나요?
3. raw/staging/mart 계층을 식별합니다
4. 원본 데이터에서 분석 테이블까지의 변환 체인을 맵핑합니다
5. 데이터가 어디서 보강, 필터링, 집계되는지 기록합니다

## 팁

- 매우 큰 테이블(1억 행 이상)은 프로파일링 쿼리가 기본적으로 샘플링을 사용합니다. 정확한 개수가 필요하면 그 점을 말하세요
- 새 데이터셋을 처음 탐색한다면, 이 명령은 구체적인 쿼리를 쓰기 전에 전체 지형을 파악하게 해 줍니다
- 품질 플래그는 휴리스틱입니다. 모든 플래그가 실제 문제는 아니지만, 각각 빠르게 살펴볼 가치는 있습니다
