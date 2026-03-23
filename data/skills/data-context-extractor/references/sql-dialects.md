# SQL 방언 참조

사용자의 데이터 웨어하우스에 따라 생성된 스킬에 적절한 섹션을 포함하세요.

---

## BigQuery

```markdown
## SQL 방언: BigQuery

- **테이블 참조**: 백틱 사용: \`project.dataset.table\`
- **안전한 나눗셈**: `SAFE_DIVIDE(a, b)` 오류 대신 NULL 반환
- **날짜 함수**:
  - `DATE_TRUNC(date_col, MONTH)`
  - `DATE_SUB(date_col, INTERVAL 1 DAY)`
  - `DATE_DIFF(end_date, start_date, DAY)`
- **컬럼 제외**: `SELECT * EXCEPT(column_to_exclude)`
- **배열**: `UNNEST(array_column)`으로 펼치기
- **구조체**: 점 표기법으로 접근 `struct_col.field_name`
- **타임스탬프**: `TIMESTAMP_TRUNC()`, 기본적으로 UTC
- **문자열 매칭**: `LIKE`, `REGEXP_CONTAINS(col, r'pattern')`
- **집계의 NULL**: 대부분의 함수가 NULL을 무시; `IFNULL()` 또는 `COALESCE()` 사용
```

---

## Snowflake

```markdown
## SQL 방언: Snowflake

- **테이블 참조**: `DATABASE.SCHEMA.TABLE` 또는 대소문자 구분이 필요한 경우 따옴표: `"Column_Name"`
- **안전한 나눗셈**: `DIV0(a, b)`는 0 반환, `DIV0NULL(a, b)`는 NULL 반환
- **날짜 함수**:
  - `DATE_TRUNC('MONTH', date_col)`
  - `DATEADD(DAY, -1, date_col)`
  - `DATEDIFF(DAY, start_date, end_date)`
- **컬럼 제외**: `SELECT * EXCLUDE (column_to_exclude)`
- **배열**: `FLATTEN(array_column)`으로 펼치기, `value`로 접근
- **Variant/JSON**: 콜론 표기법으로 접근 `variant_col:field_name`
- **타임스탬프**: `TIMESTAMP_NTZ` (시간대 없음), `TIMESTAMP_TZ` (시간대 포함)
- **문자열 매칭**: `LIKE`, `REGEXP_LIKE(col, 'pattern')`
- **대소문자 구분**: 따옴표가 없으면 식별자가 기본적으로 대문자
```

---

## PostgreSQL / Redshift

```markdown
## SQL 방언: PostgreSQL/Redshift

- **테이블 참조**: `schema.table` (소문자 규칙)
- **안전한 나눗셈**: `NULLIF(b, 0)` 패턴: `a / NULLIF(b, 0)`
- **날짜 함수**:
  - `DATE_TRUNC('month', date_col)`
  - `date_col - INTERVAL '1 day'`
  - `DATE_PART('day', end_date - start_date)`
- **컬럼 선택**: EXCEPT 없음; 컬럼을 명시적으로 나열해야 함
- **배열**: `UNNEST(array_column)` (PostgreSQL), Redshift에서는 제한적
- **JSON**: `json_col->>'field_name'`은 텍스트, `json_col->'field_name'`은 JSON
- **타임스탬프**: 시간대 변환에 `AT TIME ZONE 'UTC'`
- **문자열 매칭**: `LIKE`, 정규식에 `col ~ 'pattern'`
- **부울**: 네이티브 BOOLEAN 타입; `TRUE`/`FALSE` 사용
```

---

## Databricks / Spark SQL

```markdown
## SQL 방언: Databricks/Spark SQL

- **테이블 참조**: `catalog.schema.table` (Unity Catalog) 또는 `schema.table`
- **안전한 나눗셈**: `NULLIF` 사용: `a / NULLIF(b, 0)` 또는 `TRY_DIVIDE(a, b)`
- **날짜 함수**:
  - `DATE_TRUNC('MONTH', date_col)`
  - `DATE_SUB(date_col, 1)`
  - `DATEDIFF(end_date, start_date)`
- **컬럼 제외**: `SELECT * EXCEPT (column_to_exclude)` (Databricks SQL)
- **배열**: `EXPLODE(array_column)`으로 펼치기
- **구조체**: 점 표기법으로 접근 `struct_col.field_name`
- **JSON**: `json_col:field_name` 또는 `GET_JSON_OBJECT()`
- **문자열 매칭**: `LIKE`, 정규식에 `RLIKE`
- **Delta 기능**: `DESCRIBE HISTORY`, `VERSION AS OF`를 사용한 시간 여행
```

---

## MySQL

```markdown
## SQL 방언: MySQL

- **테이블 참조**: 백틱으로 \`database\`.\`table\`
- **안전한 나눗셈**: 수동: `IF(b = 0, NULL, a / b)` 또는 `a / NULLIF(b, 0)`
- **날짜 함수**:
  - `DATE_FORMAT(date_col, '%Y-%m-01')`로 절단
  - `DATE_SUB(date_col, INTERVAL 1 DAY)`
  - `DATEDIFF(end_date, start_date)`
- **컬럼 선택**: EXCEPT 없음; 컬럼을 명시적으로 나열해야 함
- **배열**: 제한적인 네이티브 지원; 종종 JSON으로 저장
- **JSON**: `JSON_EXTRACT(col, '$.field')` 또는 `col->>'$.field'`
- **타임스탬프**: 시간대 변환에 `CONVERT_TZ()`
- **문자열 매칭**: `LIKE`, 정규식에 `REGEXP`
- **대소문자 구분**: Linux에서는 테이블 이름이 대소문자 구분, Windows에서는 아님
```

---

## 방언 간 공통 패턴

| 연산 | BigQuery | Snowflake | PostgreSQL | Databricks |
|-----------|----------|-----------|------------|------------|
| 현재 날짜 | `CURRENT_DATE()` | `CURRENT_DATE()` | `CURRENT_DATE` | `CURRENT_DATE()` |
| 현재 타임스탬프 | `CURRENT_TIMESTAMP()` | `CURRENT_TIMESTAMP()` | `NOW()` | `CURRENT_TIMESTAMP()` |
| 문자열 연결 | `CONCAT()` 또는 `\|\|` | `CONCAT()` 또는 `\|\|` | `CONCAT()` 또는 `\|\|` | `CONCAT()` 또는 `\|\|` |
| Coalesce | `COALESCE()` | `COALESCE()` | `COALESCE()` | `COALESCE()` |
| Case when | `CASE WHEN` | `CASE WHEN` | `CASE WHEN` | `CASE WHEN` |
| Count distinct | `COUNT(DISTINCT x)` | `COUNT(DISTINCT x)` | `COUNT(DISTINCT x)` | `COUNT(DISTINCT x)` |
