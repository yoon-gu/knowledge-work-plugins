# 생성된 스킬 템플릿

새로운 데이터 분석 기술을 생성할 때 이 템플릿을 사용하세요. `[PLACEHOLDER]` 값을 모두 바꾸세요.

---

```markdown
---
name: [company]-data-analyst
description: "[COMPANY] data analysis skill. Provides context for querying [WAREHOUSE_TYPE] including entity definitions, metric calculations, and common query patterns. Use when analyzing [COMPANY] data for: (1) [PRIMARY_USE_CASE_1], (2) [PRIMARY_USE_CASE_2], (3) [PRIMARY_USE_CASE_3], or any data questions requiring [COMPANY]-specific context."
---

# [COMPANY] Data Analysis

## SQL Dialect: [WAREHOUSE_TYPE]

[INSERT APPROPRIATE DIALECT SECTION FROM sql-dialects.md]

---

## Entity Disambiguation

When users mention these terms, clarify which entity they mean:

[EXAMPLE FORMAT - customize based on discovery:]

**"User" can mean:**
- **Account**: An individual login/profile ([PRIMARY_TABLE]: [ID_FIELD])
- **Organization**: A billing entity that can have multiple accounts ([ORG_TABLE]: [ORG_ID])
- **[OTHER_TYPE]**: [DEFINITION] ([TABLE]: [ID])

**Relationships:**
- [ENTITY_1] → [ENTITY_2]: [RELATIONSHIP_TYPE] (join on [JOIN_KEY])

---

## Business Terminology

| Term | Definition | Notes |
|------|------------|-------|
| [TERM_1] | [DEFINITION] | [CONTEXT/GOTCHA] |
| [TERM_2] | [DEFINITION] | [CONTEXT/GOTCHA] |
| [ACRONYM] | [FULL_NAME] - [EXPLANATION] | |

---

## Standard Filters

Always apply these filters unless explicitly told otherwise:

```sql
-- Exclude test/internal data
WHERE [TEST_FLAG_COLUMN] = FALSE
  AND [INTERNAL_FLAG_COLUMN] = FALSE

-- Exclude invalid/fraud
  AND [STATUS_COLUMN] != '[EXCLUDED_STATUS]'

-- [OTHER STANDARD EXCLUSIONS]
```

**재정의하는 경우:**
- [SCENARIO_1]: [CONDITION]인 경우 [NORMALLY_EXCLUDED]를 포함합니다.

---

## 주요 지표

### [METRIC_1_NAME]
- **정의**: [PLAIN_ENGLISH_EXPLANATION]
- **공식**: `[EXACT_CALCULATION]`
- **출처**: `[TABLE_NAME].[COLUMN_NAME]`
- **시간 단위**: [매일/매주/매월]
- **주의사항**: [EDGE_CASES_OR_GOTCHAS]

### [METRIC_2_NAME]
[반복 형식]

---

## 데이터 신선도

| 테이블 | 업데이트 빈도 | 일반적인 지연 |
| ------- | ------------------ | ------------- |
| [표_1] | [빈도] | [지연] |
| [표_2] | [빈도] | [지연] |

데이터 최신성을 확인하려면 다음 안내를 따르세요.
```sql
SELECT MAX([DATE_COLUMN]) as latest_data FROM [TABLE]
```

---

## 기술 자료 탐색

자세한 테이블 문서를 보려면 다음 참조 파일을 사용하세요.

| 도메인 | 참조 파일 | 사용 대상 |
| -------- | ---------------- | --------- |
| [DOMAIN_1] | `references/[domain1].md` | [BRIEF_DESCRIPTION] |
| [DOMAIN_2] | `references/[domain2].md` | [BRIEF_DESCRIPTION] |
| 엔터티 | `references/entities.md` | 엔터티 정의 및 관계 |
| 측정항목 | `references/metrics.md` | KPI 계산 및 수식 |

---

## 일반적인 쿼리 패턴

### [PATTERN_1_NAME]
```sql
[SAMPLE_QUERY]
```

### [PATTERN_2_NAME]
```sql
[SAMPLE_QUERY]
```

---

## 문제 해결

### 일반적인 실수
- **[실수_1]**: [설명] → [올바른_접근]
- **[실수_2]**: [설명] → [올바른_접근]

### 액세스 문제
- `[TABLE]`에서 권한 오류가 발생하는 경우: [해결 방법]
- PII 제한 열의 경우: [ALTERNATIVE_APPROACH]

### 성능 팁
- 스캔된 데이터를 줄이려면 먼저 `[PARTITION_COLUMN]`로 필터링하세요.
- 큰 테이블의 경우 탐색 중에 `LIMIT`을(를) 사용하세요.
- 가능하면 `[RAW_TABLE]`보다 `[AGGREGATED_TABLE]`을(를) 선호하세요.
```

---

## Customization Notes

When generating a skill:

1. **Fill all placeholders** - Don't leave any `[PLACEHOLDER]` text
2. **Remove unused sections** - If they don't have dashboards, remove that section
3. **Add specificity** - Generic advice is less useful than specific column names and values
4. **Include real examples** - Sample queries should use actual table/column names
5. **Keep it scannable** - Use tables and code blocks liberally
