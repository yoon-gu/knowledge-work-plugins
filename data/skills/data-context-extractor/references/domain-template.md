# 도메인 참조 파일 템플릿

특정 데이터 도메인(예: 수익, 사용자, 마케팅)에 대한 참조 파일을 생성할 때 이 템플릿을 사용하십시오.

---

```markdown
# [DOMAIN_NAME] Tables

This document contains [domain]-related tables, metrics, and query patterns.

---

## Quick Reference

### Business Context

[2-3 sentences explaining what this domain covers and key concepts]

### Entity Clarification

**"[AMBIGUOUS_TERM]" can mean:**
- **[MEANING_1]**: [DEFINITION] ([TABLE]: [ID_FIELD])
- **[MEANING_2]**: [DEFINITION] ([TABLE]: [ID_FIELD])

Always clarify which one before querying.

### Standard Filters

For [domain] queries, always:
```sql
[STANDARD_FILTER_1] 및 [STANDARD_FILTER_2] 위치
```

---

## Key Tables

### [TABLE_1_NAME]
**Location**: `[project.dataset.table]` or `[schema.table]`
**Description**: [What this table contains, when to use it]
**Primary Key**: [COLUMN(S)]
**Update Frequency**: [Daily/Hourly/Real-time] ([LAG] lag)
**Partitioned By**: [PARTITION_COLUMN] (if applicable)

| Column | Type | Description | Notes |
|--------|------|-------------|-------|
| **[column_1]** | [TYPE] | [DESCRIPTION] | [GOTCHA_OR_CONTEXT] |
| **[column_2]** | [TYPE] | [DESCRIPTION] | |
| **[column_3]** | [TYPE] | [DESCRIPTION] | Nullable |

**Relationships**:
- Joins to `[OTHER_TABLE]` on `[JOIN_KEY]`
- Parent of `[CHILD_TABLE]` via `[FOREIGN_KEY]`

**Nested/Struct Fields** (if applicable):
- `[struct_name].[field_1]`: [DESCRIPTION]
- `[struct_name].[field_2]`: [DESCRIPTION]

---

### [TABLE_2_NAME]
[REPEAT FORMAT]

---

## Key Metrics

| Metric | Definition | Table | Formula | Notes |
|--------|------------|-------|---------|-------|
| [METRIC_1] | [DEFINITION] | [TABLE] | `[FORMULA]` | [CAVEATS] |
| [METRIC_2] | [DEFINITION] | [TABLE] | `[FORMULA]` | |

---

## Sample Queries

### [QUERY_PURPOSE_1]
```sql
-- [이 쿼리의 기능에 대한 간략한 설명] SELECT [열] FROM [테이블] WHERE [표준_필터] GROUP BY [그룹화] ORDER BY [순서]
```

### [QUERY_PURPOSE_2]
```sql
[ANOTHER_COMMON_QUERY]
```

### [QUERY_PURPOSE_3]: [More Complex Pattern]
```sql
WITH [cte_name] AS ( [CTE_LOGIC] ) SELECT [최종_열] FROM [cte_name] [joins_and_filters]
```

---

## Common Gotchas

1. **[GOTCHA_1]**: [EXPLANATION]
   - Wrong: `[INCORRECT_APPROACH]`
   - Right: `[CORRECT_APPROACH]`

2. **[GOTCHA_2]**: [EXPLANATION]

---

## Related Dashboards (if applicable)

| Dashboard | Link | Use For |
|-----------|------|---------|
| [DASHBOARD_1] | [URL] | [DESCRIPTION] |
| [DASHBOARD_2] | [URL] | [DESCRIPTION] |
```

---

## 도메인 파일 생성 팁

1. **가장 많이 검색되는 테이블부터 시작하세요** - 모든 것을 문서화하려고 하지 마세요.
2. **중요한 열에 대해서만 열 수준 세부정보 포함** - `created_at`과 같은 명백한 항목은 건너뛰세요.
3. **실제 쿼리 예 > 추상 설명** - 표시하지 않음
4. **문제점을 눈에 띄게 문서화하세요** - 시간이 가장 많이 절약됩니다.
5. **샘플 쿼리를 실행 가능하게 유지** - 실제 테이블/열 이름 사용
6. **중첩/구조체 필드를 명시적으로 기록해두세요** - 이러한 여행 사람들은

## 제안된 도메인 파일

문서화할 공통 도메인(각 도메인에 대해 별도의 파일 생성):

- `revenue.md` - 청구, 구독, ARR, 거래
- `users.md` - 계정, 인증, 사용자 속성
- `product.md` - 기능 사용, 이벤트, 세션
- `growth.md` - DAU/WAU/MAU, 보존, 활성화
- `sales.md` - CRM, 파이프라인, 기회
- `marketing.md` - 캠페인, 기여, 리드
- `support.md` - 티켓, CSAT, 응답 시간
