---
name: sql-queries
description: Snowflake, BigQuery, Databricks, PostgreSQL 등 주요 데이터 웨어하우스 방언에서 올바르고 성능이 좋은 SQL을 작성합니다. 쿼리를 디버깅할 때, SQL을 최적화할 때, 방언 간 변환을 할 때, 또는 CTE와 윈도 함수가 포함된 쿼리를 만들 때 참고하세요.
user-invocable: false
---

# SQL 쿼리 스킬

주요 데이터 웨어하우스 방언에서 올바르고 성능이 좋은 SQL을 작성합니다.

## 방언별 참조

### PostgreSQL(Aurora, RDS, Supabase, Neon 포함)

**날짜/시간:**
```sql
-- 현재 날짜/시간
CURRENT_DATE, CURRENT_TIMESTAMP, NOW()

-- 날짜 산술
date_column + INTERVAL '7 days'
date_column - INTERVAL '1 month'

-- 기간 단위 절사
DATE_TRUNC('month', created_at)

-- 구성 요소 추출
EXTRACT(YEAR FROM created_at)
EXTRACT(DOW FROM created_at)  -- 0=일요일

-- 서식 지정
TO_CHAR(created_at, 'YYYY-MM-DD')
```

**문자열:**
```sql
-- 연결
first_name || ' ' || last_name
CONCAT(first_name, ' ', last_name)

-- 패턴 일치
column ILIKE '%pattern%'  -- 대소문자 구분 없음
column ~ '^regex_pattern$'  -- 정규식

-- 문자열 조작
LEFT(str, n), RIGHT(str, n)
SPLIT_PART(str, delimiter, position)
REGEXP_REPLACE(str, pattern, replacement)
```

**배열과 JSON:**
```sql
-- JSON 접근
data->>'key'  -- 텍스트
data->'nested'->'key'  -- JSON
data#>>'{path,to,key}'  -- 중첩 텍스트

-- 배열 연산
ARRAY_AGG(column)
ANY(array_column)
array_column @> ARRAY['value']
```

**검토 팁:**
- 쿼리 프로파일링에는 `EXPLAIN ANALYZE`를 사용하세요
- 조인 조건에는 인덱스가 잘 맞는 열을 사용하세요
- 상관 서브쿼리에는 `IN`보다 `EXISTS`를 사용하세요
- 자주 찾는 조건에는 다른 절을 사용하는 편이 좋습니다
- 연결에는 커넥션 풀링을 사용하세요

---

### Snowflake

**날짜/시간:**
```sql
-- 현재 날짜/시간
CURRENT_DATE(), CURRENT_TIMESTAMP(), SYSDATE()

-- 날짜 산술
DATEADD(day, 7, date_column)
DATEDIFF(day, start_date, end_date)

-- 기간 단위 절사
DATE_TRUNC('month', created_at)

-- 구성 요소 추출
YEAR(created_at), MONTH(created_at), DAY(created_at)
DAYOFWEEK(created_at)

-- 서식 지정
TO_CHAR(created_at, 'YYYY-MM-DD')
```

**문자열:**
```sql
-- 기본적으로 대소문자 비구분(정렬 규칙에 따라 다름)
column ILIKE '%pattern%'
REGEXP_LIKE(column, 'pattern')

-- JSON 파싱
column:key::string  -- VARIANT는 점 표기법
PARSE_JSON('{"key": "value"}')
GET_PATH(variant_col, 'path.to.key')

-- 배열/객체 펼치기
SELECT f.value FROM table, LATERAL FLATTEN(input => array_col) f
```

**반구조 데이터:**
```sql
-- VARIANT 타입 접근
data:customer:name::STRING
data:items[0]:price::NUMBER

-- 중첩 구조 펼치기
SELECT
    t.id,
    item.value:name::STRING as item_name,
    item.value:qty::NUMBER as quantity
FROM my_table t,
LATERAL FLATTEN(input => t.data:items) item
```

**검토 팁:**
- 큰 테이블에는 클러스터링 키를 사용하세요
- 클러스터링 키는 자주 필터링하는 열 중심으로 설계하세요
- 웨어하우스 크기를 적절히 설정하세요
- 비용이 많이 드는 쿼리를 다시 실행하지 않으려면 `RESULT_SCAN(LAST_QUERY_ID())`를 사용하세요
- 스테이징/임시 데이터에는 임시 테이블을 사용하세요

---

### BigQuery (Google Cloud)

**날짜/시간:**
```sql
-- 현재 날짜/시간
CURRENT_DATE(), CURRENT_TIMESTAMP()

-- 날짜 산술
DATE_ADD(date_column, INTERVAL 7 DAY)
DATE_SUB(date_column, INTERVAL 1 MONTH)
DATE_DIFF(end_date, start_date, DAY)
TIMESTAMP_DIFF(end_ts, start_ts, HOUR)

-- 기간 단위 절사
DATE_TRUNC(created_at, MONTH)
TIMESTAMP_TRUNC(created_at, HOUR)

-- 구성 요소 추출
EXTRACT(YEAR FROM created_at)
EXTRACT(DAYOFWEEK FROM created_at)  -- 1=일요일

-- 서식 지정
FORMAT_DATE('%Y-%m-%d', date_column)
FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', ts_column)
```

**문자열:**
```sql
-- ILIKE는 없으므로 LOWER() 사용
LOWER(column) LIKE '%pattern%'
REGEXP_CONTAINS(column, r'pattern')
REGEXP_EXTRACT(column, r'pattern')

-- 문자열 조작
SPLIT(str, delimiter)  -- 배열을 반환합니다
ARRAY_TO_STRING(array, delimiter)
```

**배열과 구조:**
```sql
-- 배열 연산
ARRAY_AGG(column)
UNNEST(array_column)
ARRAY_LENGTH(array_column)
value IN UNNEST(array_column)

-- 구조체 접근
struct_column.field_name
```

**검토 팁:**
- 스캔 바이트를 줄이려면 파티션 열(보통 날짜)로 필터링하세요
- 자주 제외되는 열에는 클러스터링을 사용하세요
- 높은 카디널리티 집계에는 `APPROX_COUNT_DISTINCT()`를 사용하세요
- `SELECT *`는 피하세요. 비용은 스캔한 바이트 단위로 청구됩니다.
- 변수 값은 `DECLARE`와 `SET`으로 관리하세요
- BigQuery는 실행 전에 드라이 런으로 비용을 미리 확인하세요

---

### Redshift (Amazon)

**날짜/시간:**
```sql
-- 현재 날짜/시간
CURRENT_DATE, GETDATE(), SYSDATE

-- 날짜 산술
DATEADD(day, 7, date_column)
DATEDIFF(day, start_date, end_date)

-- 기간 단위 절사
DATE_TRUNC('month', created_at)

-- 구성 요소 추출
EXTRACT(YEAR FROM created_at)
DATE_PART('dow', created_at)
```

**문자열:**
```sql
-- 대소문자 비구분
column ILIKE '%pattern%'
REGEXP_INSTR(column, 'pattern') > 0

-- 문자열 조작
SPLIT_PART(str, delimiter, position)
LISTAGG(column, ', ') WITHIN GROUP (ORDER BY column)
```

**검토 팁:**
- 함께 조인되는 테이블에는 DISTKEY를 설계하세요
- 자주 필터링하거나 정렬하는 열에는 SORTKEY를 사용하세요
- `EXPLAIN`으로 쿼리 계획을 확인하세요
- 데이터 이동을 최소화하세요(DS_BCAST, DS_DIST를 주의)
- `ANALYZE`와 `VACUUM`을 실행하세요
- 필요할 때는 late-binding view를 사용하세요

---

### 데이터브릭스 SQL

**날짜/시간:**
```sql
-- 현재 날짜/시간
CURRENT_DATE(), CURRENT_TIMESTAMP()

-- 날짜 산술
DATE_ADD(date_column, 7)
DATEDIFF(end_date, start_date)
ADD_MONTHS(date_column, 1)

-- 기간 단위 절사
DATE_TRUNC('MONTH', created_at)
TRUNC(date_column, 'MM')

-- 구성 요소 추출
YEAR(created_at), MONTH(created_at)
DAYOFWEEK(created_at)
```

**Delta Lake에서 사용할 수 있는 기능:**
```sql
-- 시점 조회
SELECT * FROM my_table TIMESTAMP AS OF '2024-01-15'
SELECT * FROM my_table VERSION AS OF 42

-- 이력 확인
DESCRIBE HISTORY my_table

-- 병합(upsert)
MERGE INTO target USING source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
```

**검토 팁:**
- 쿼리 성능을 위해 Delta Lake의 `OPTIMIZE`와 `ZORDER`를 사용하세요
- 집계가 많은 쿼리에서는 Photon 엔진을 활용하세요
- 자주 접근하는 데이터셋에는 `CACHE TABLE`을 사용하세요
- 자주 필터링하는 날짜 열처럼 카디널리티가 낮은 열에 적합합니다

---

## 일반적인 SQL 패턴

### 윈도 함수

```sql
-- 순위
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC)
RANK() OVER (PARTITION BY category ORDER BY revenue DESC)
DENSE_RANK() OVER (ORDER BY score DESC)

-- 누적 합계 / 이동 평균
SUM(revenue) OVER (ORDER BY date_col ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total
AVG(revenue) OVER (ORDER BY date_col ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg_7d

-- Lag / Lead
LAG(value, 1) OVER (PARTITION BY entity ORDER BY date_col) as prev_value
LEAD(value, 1) OVER (PARTITION BY entity ORDER BY date_col) as next_value

-- 첫 / 마지막 값
FIRST_VALUE(status) OVER (PARTITION BY user_id ORDER BY created_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
LAST_VALUE(status) OVER (PARTITION BY user_id ORDER BY created_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)

-- 전체 대비 비율
revenue / SUM(revenue) OVER () as pct_of_total
revenue / SUM(revenue) OVER (PARTITION BY category) as pct_of_category
```

### 읽기 쉬운 CTE

```sql
WITH
-- 1단계: 기준 모집단 정의
base_users AS (
    SELECT user_id, created_at, plan_type
    FROM users
    WHERE created_at >= DATE '2024-01-01'
      AND status = 'active'
),

-- 2단계: 사용자 수준 지표 계산
user_metrics AS (
    SELECT
        u.user_id,
        u.plan_type,
        COUNT(DISTINCT e.session_id) as session_count,
        SUM(e.revenue) as total_revenue
    FROM base_users u
    LEFT JOIN events e ON u.user_id = e.user_id
    GROUP BY u.user_id, u.plan_type
),

-- 3단계: 요약 수준으로 집계
summary AS (
    SELECT
        plan_type,
        COUNT(*) as user_count,
        AVG(session_count) as avg_sessions,
        SUM(total_revenue) as total_revenue
    FROM user_metrics
    GROUP BY plan_type
)

SELECT * FROM summary ORDER BY total_revenue DESC;
```

### 코호트 리텐션

```sql
WITH cohorts AS (
    SELECT
        user_id,
        DATE_TRUNC('month', first_activity_date) as cohort_month
    FROM users
),
activity AS (
    SELECT
        user_id,
        DATE_TRUNC('month', activity_date) as activity_month
    FROM user_activity
)
SELECT
    c.cohort_month,
    COUNT(DISTINCT c.user_id) as cohort_size,
    COUNT(DISTINCT CASE
        WHEN a.activity_month = c.cohort_month THEN a.user_id
    END) as month_0,
    COUNT(DISTINCT CASE
        WHEN a.activity_month = c.cohort_month + INTERVAL '1 month' THEN a.user_id
    END) as month_1,
    COUNT(DISTINCT CASE
        WHEN a.activity_month = c.cohort_month + INTERVAL '3 months' THEN a.user_id
    END) as month_3
FROM cohorts c
LEFT JOIN activity a ON c.user_id = a.user_id
GROUP BY c.cohort_month
ORDER BY c.cohort_month;
```

### 퍼널 분석

```sql
WITH funnel AS (
    SELECT
        user_id,
        MAX(CASE WHEN event = 'page_view' THEN 1 ELSE 0 END) as step_1_view,
        MAX(CASE WHEN event = 'signup_start' THEN 1 ELSE 0 END) as step_2_start,
        MAX(CASE WHEN event = 'signup_complete' THEN 1 ELSE 0 END) as step_3_complete,
        MAX(CASE WHEN event = 'first_purchase' THEN 1 ELSE 0 END) as step_4_purchase
    FROM events
    WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT
    COUNT(*) as total_users,
    SUM(step_1_view) as viewed,
    SUM(step_2_start) as started_signup,
    SUM(step_3_complete) as completed_signup,
    SUM(step_4_purchase) as purchased,
    ROUND(100.0 * SUM(step_2_start) / NULLIF(SUM(step_1_view), 0), 1) as view_to_start_pct,
    ROUND(100.0 * SUM(step_3_complete) / NULLIF(SUM(step_2_start), 0), 1) as start_to_complete_pct,
    ROUND(100.0 * SUM(step_4_purchase) / NULLIF(SUM(step_3_complete), 0), 1) as complete_to_purchase_pct
FROM funnel;
```

### 중복 제거

```sql
-- 키별로 가장 최근 레코드만 유지
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY entity_id
            ORDER BY updated_at DESC
        ) as rn
    FROM source_table
)
SELECT * FROM ranked WHERE rn = 1;
```

## 오류 처리

쿼리가 실패하면:

1. **문법 오류**: 방언별 차이를 확인하세요. 예를 들어 BigQuery는 `ILIKE`를 지원하지 않고, `SAFE_DIVIDE()`를 제공합니다.
2. **열을 찾을 수 없음**: 로그와 대조해 열 이름을 확인하세요. PostgreSQL은 따옴표로 식별자 대소문자를 구분하므로 특히 주의하세요.
3. **형식 오류**: 필요한 경우 명시적으로 형변환하세요(`CAST(col AS DATE)`, `col::DATE`).
4. **0으로 나누기**: `NULLIF(denominator, 0)` 또는 방언별 안전 함수를 사용해 보호하세요.
5. **모호한 열**: JOIN에서는 항상 테이블 별칭으로 열 이름을 명시하세요.
6. **GROUP BY 오류**: 집계하지 않은 모든 열은 `GROUP BY`에 포함해야 합니다(BigQuery는 일부 별칭 그룹화를 허용합니다).
