# SQL 방언 참조

사용자의 데이터 웨어하우스에 맞는 표를 적절한 위치에 포함하세요.

---

## BigQuery

```markdown
## SQL 방언: BigQuery

- **테이블 참조**: 백틱을 사용합니다: \`project.dataset.table\`
- **안전한 나눗셈**: `SAFE_DIVIDE(a, b)`는 오류 대신 NULL을 반환합니다
- **날짜 함수**:
  - `DATE_TRUNC(date_col, MONTH)`
  - `DATE_SUB(date_col, INTERVAL 1 DAY)`
  - `DATE_DIFF(end_date, start_date, DAY)`
- **열 제외**: `SELECT * EXCEPT(column_to_exclude)`
- **배열**: 펼칠 때 `UNNEST(array_column)`을 사용합니다
- **구조체**: 점 표기법 `struct_col.field_name`으로 접근합니다
- **타임스탬프**: `TIMESTAMP_TRUNC()`, 기본 시간대는 UTC입니다
- **문자열 일치**: `LIKE`, `REGEXP_CONTAINS(col, r'pattern')`
- **집계에서의 NULL**: 대부분의 함수는 NULL을 무시합니다. `IFNULL()` 또는 `COALESCE()`를 사용하세요
```

---

## Snowflake

```markdown
## SQL 방언: Snowflake

- **테이블 참조**: `DATABASE.SCHEMA.TABLE` 또는 대소문자 구분이 필요하면 따옴표를 사용합니다: `"Column_Name"`
- **안전한 나눗셈**: `DIV0(a, b)`는 0을 반환하고, `DIV0NULL(a, b)`는 NULL을 반환합니다
- **날짜 함수**:
  - `DATE_TRUNC('MONTH', date_col)`
  - `DATEADD(DAY, -1, date_col)`
  - `DATEDIFF(DAY, start_date, end_date)`
- **열 제외**: `SELECT * EXCLUDE (column_to_exclude)`
- **배열**: 펼칠 때 `FLATTEN(array_column)`을 사용하고 `value`로 접근합니다
- **Variant/JSON**: 콜론 표기법 `variant_col:field_name`으로 접근합니다
- **타임스탬프**: `TIMESTAMP_NTZ`(시간대 없음), `TIMESTAMP_TZ`(시간대 포함)
- **문자열 일치**: `LIKE`, `REGEXP_LIKE(col, 'pattern')`
- **대소문자 구분**: 따옴표로 감싸지 않으면 식별자는 기본적으로 대문자로 처리됩니다
```

---

## PostgreSQL/Redshift

```markdown
## SQL 방언: PostgreSQL/Redshift

- **테이블 참조**: `schema.table` (소문자 관례)
- **안전한 나눗셈**: `NULLIF(b, 0)` 패턴: `a / NULLIF(b, 0)`
- **날짜 함수**:
  - `DATE_TRUNC('month', date_col)`
  - `date_col - INTERVAL '1 day'`
  - `DATE_PART('day', end_date - start_date)`
- **열 선택**: EXCEPT가 없습니다. 열을 명시적으로 나열해야 합니다
- **배열**: `UNNEST(array_column)` (PostgreSQL), Redshift에서는 제한적입니다
- **JSON**: 텍스트는 `json_col->>'field_name'`, JSON은 `json_col->'field_name'`
- **타임스탬프**: 시간대 변환에는 `AT TIME ZONE 'UTC'`를 사용합니다
- **문자열 일치**: `LIKE`, 정규식은 `col ~ 'pattern'`
- **불리언**: 기본 BOOLEAN 타입을 사용하며 `TRUE`/`FALSE`를 사용합니다
```

---

## Databricks/Spark SQL

```markdown
## SQL 방언: Databricks/Spark SQL

- **테이블 참조**: `catalog.schema.table`(Unity Catalog) 또는 `schema.table`
- **안전한 나눗셈**: `a / NULLIF(b, 0)` 또는 `TRY_DIVIDE(a, b)`
- **날짜 함수**:
  - `DATE_TRUNC('MONTH', date_col)`
  - `DATE_SUB(date_col, 1)`
  - `DATEDIFF(end_date, start_date)`
- **열 제외**: `SELECT * EXCEPT (column_to_exclude)` (Databricks SQL)
- **배열**: 펼칠 때 `EXPLODE(array_column)`을 사용합니다
- **구조체**: 점 표기법 `struct_col.field_name`으로 접근합니다
- **JSON**: `json_col:field_name` 또는 `GET_JSON_OBJECT()`
- **문자열 일치**: `LIKE`, 정규식은 `RLIKE`
- **Delta 기능**: `DESCRIBE HISTORY`, `VERSION AS OF`를 사용한 시점 조회
```

---

## MySQL

```markdown
## SQL 방언: MySQL

- **테이블 참조**: 백틱으로 \`database\`.\`table\`을 사용합니다
- **안전한 나눗셈**: 수동 방식: `IF(b = 0, NULL, a / b)` 또는 `a / NULLIF(b, 0)`
- **날짜 함수**:
  - `DATE_FORMAT(date_col, '%Y-%m-01')`로 절사
  - `DATE_SUB(date_col, INTERVAL 1 DAY)`
  - `DATEDIFF(end_date, start_date)`
- **열 선택**: EXCEPT가 없습니다. 열을 명시적으로 나열해야 합니다
- **배열**: 기본 지원이 제한적이며, 종종 JSON으로 저장됩니다
- **JSON**: `JSON_EXTRACT(col, '$.field')` 또는 `col->>'$.field'`
- **타임스탬프**: 시간대 변환에는 `CONVERT_TZ()`를 사용합니다
- **문자열 일치**: `LIKE`, 정규식은 `REGEXP`
- **대소문자 구분**: Linux에서는 테이블 이름이 대소문자를 구분하지만 Windows에서는 그렇지 않습니다
```

---

## 방언 패턴

| 기능 | BigQuery | Snowflake | PostgreSQL | Databricks |
|-----------|----------|-----------|------------|------------|
| 현재 날짜 | `CURRENT_DATE()` | `CURRENT_DATE()` | `CURRENT_DATE` | `CURRENT_DATE()` |
| 현재 타임스탬프 | `CURRENT_TIMESTAMP()` | `CURRENT_TIMESTAMP()` | `NOW()` | `CURRENT_TIMESTAMP()` |
| 문자열 연결 | `CONCAT()` 또는 `||` | `CONCAT()` 또는 `||` | `CONCAT()` 또는 `||` | `CONCAT()` 또는 `||` |
| NULL 대체 | `COALESCE()` | `COALESCE()` | `COALESCE()` | `COALESCE()` |
| 조건 분기 | `CASE WHEN` | `CASE WHEN` | `CASE WHEN` | `CASE WHEN` |
| 고유 개수 | `COUNT(DISTINCT x)` | `COUNT(DISTINCT x)` | `COUNT(DISTINCT x)` | `COUNT(DISTINCT x)` |
