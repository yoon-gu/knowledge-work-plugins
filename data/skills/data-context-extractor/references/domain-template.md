# 도메인 참조 파일 템플릿

특정 데이터 도메인(예: 매출, 사용자, 마케팅)에 대한 참조 파일을 생성할 때 이 템플릿을 사용하세요.

---

```markdown
# [DOMAIN_NAME] 테이블

이 문서는 [domain] 관련 테이블, 지표 및 쿼리 패턴을 포함합니다.

---

## 빠른 참조

### 비즈니스 맥락

[이 도메인이 다루는 내용과 핵심 개념을 설명하는 2-3문장]

### 엔티티 명확화

**"[AMBIGUOUS_TERM]"의 의미:**
- **[MEANING_1]**: [DEFINITION] ([TABLE]: [ID_FIELD])
- **[MEANING_2]**: [DEFINITION] ([TABLE]: [ID_FIELD])

쿼리 전에 항상 어느 것인지 명확히 하세요.

### 표준 필터

[domain] 쿼리의 경우, 항상:
```sql
WHERE [STANDARD_FILTER_1]
  AND [STANDARD_FILTER_2]
```

---

## 주요 테이블

### [TABLE_1_NAME]
**위치**: `[project.dataset.table]` 또는 `[schema.table]`
**설명**: [이 테이블이 포함하는 내용, 사용 시기]
**기본 키**: [COLUMN(S)]
**업데이트 빈도**: [일별/시간별/실시간] ([LAG] 지연)
**파티션 기준**: [PARTITION_COLUMN] (해당되는 경우)

| 컬럼 | 타입 | 설명 | 비고 |
|--------|------|-------------|-------|
| **[column_1]** | [TYPE] | [DESCRIPTION] | [GOTCHA_OR_CONTEXT] |
| **[column_2]** | [TYPE] | [DESCRIPTION] | |
| **[column_3]** | [TYPE] | [DESCRIPTION] | Nullable |

**관계**:
- `[OTHER_TABLE]`과 `[JOIN_KEY]`로 조인
- `[FOREIGN_KEY]`를 통해 `[CHILD_TABLE]`의 부모

**중첩/구조체 필드** (해당되는 경우):
- `[struct_name].[field_1]`: [DESCRIPTION]
- `[struct_name].[field_2]`: [DESCRIPTION]

---

### [TABLE_2_NAME]
[형식 반복]

---

## 핵심 지표

| 지표 | 정의 | 테이블 | 수식 | 비고 |
|--------|------------|-------|---------|-------|
| [METRIC_1] | [DEFINITION] | [TABLE] | `[FORMULA]` | [CAVEATS] |
| [METRIC_2] | [DEFINITION] | [TABLE] | `[FORMULA]` | |

---

## 샘플 쿼리

### [QUERY_PURPOSE_1]
```sql
-- [이 쿼리가 수행하는 작업에 대한 간략한 설명]
SELECT
    [columns]
FROM [table]
WHERE [standard_filters]
GROUP BY [grouping]
ORDER BY [ordering]
```

### [QUERY_PURPOSE_2]
```sql
[ANOTHER_COMMON_QUERY]
```

### [QUERY_PURPOSE_3]: [더 복잡한 패턴]
```sql
WITH [cte_name] AS (
    [CTE_LOGIC]
)
SELECT
    [final_columns]
FROM [cte_name]
[joins_and_filters]
```

---

## 일반적인 함정

1. **[GOTCHA_1]**: [EXPLANATION]
   - 잘못된 방법: `[INCORRECT_APPROACH]`
   - 올바른 방법: `[CORRECT_APPROACH]`

2. **[GOTCHA_2]**: [EXPLANATION]

---

## 관련 대시보드 (해당되는 경우)

| 대시보드 | 링크 | 용도 |
|-----------|------|---------|
| [DASHBOARD_1] | [URL] | [DESCRIPTION] |
| [DASHBOARD_2] | [URL] | [DESCRIPTION] |
```

---

## 도메인 파일 작성 팁

1. **가장 많이 쿼리되는 테이블부터 시작** - 모든 것을 문서화하려고 하지 마세요
2. **중요한 컬럼에 대해서만 컬럼 수준의 세부사항 포함** - `created_at`과 같은 명백한 것은 건너뛰세요
3. **실제 쿼리 예시 > 추상적 설명** - 말보다 보여주기
4. **함정을 눈에 띄게 문서화** - 이것이 가장 많은 시간을 절약합니다
5. **샘플 쿼리를 실행 가능하게 유지** - 실제 테이블/컬럼 이름 사용
6. **중첩/구조체 필드를 명시적으로 표기** - 이것이 사람들을 혼란스럽게 합니다

## 추천 도메인 파일

문서화할 일반적인 도메인 (각각 별도의 파일로 생성):

- `revenue.md` - 청구, 구독, ARR, 거래
- `users.md` - 계정, 인증, 사용자 속성
- `product.md` - 기능 사용, 이벤트, 세션
- `growth.md` - DAU/WAU/MAU, 리텐션, 활성화
- `sales.md` - CRM, 파이프라인, 기회
- `marketing.md` - 캠페인, 어트리뷰션, 리드
- `support.md` - 티켓, CSAT, 응답 시간
