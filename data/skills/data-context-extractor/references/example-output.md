# 예시: 생성된 스킬

이것은 부트스트랩 과정 후 생성된 스킬의 예시입니다. 이 예시는 Snowflake를 사용하는 가상의 전자상거래 회사 "ShopCo"를 대상으로 합니다.

---

## SKILL.md 예시

```markdown
---
name: shopco-data-analyst
description: "ShopCo data analysis skill for Snowflake. Provides context for querying e-commerce data including customer, order, and product analytics. Use when analyzing ShopCo data for: (1) Revenue and order metrics, (2) Customer behavior and retention, (3) Product performance, or any data questions requiring ShopCo-specific context."
---

# ShopCo 데이터 분석

## SQL 방언: Snowflake

- **테이블 참조**: `SHOPCO_DW.SCHEMA.TABLE` 또는 대소문자 구분이 필요한 경우 따옴표 사용: `"Column_Name"`
- **안전한 나눗셈**: `DIV0(a, b)`는 0 반환, `DIV0NULL(a, b)`는 NULL 반환
- **날짜 함수**:
  - `DATE_TRUNC('MONTH', date_col)`
  - `DATEADD(DAY, -1, date_col)`
  - `DATEDIFF(DAY, start_date, end_date)`
- **컬럼 제외**: `SELECT * EXCLUDE (column_to_exclude)`

---

## 엔티티 구분

**"Customer"의 의미:**
- **User**: 브라우징 및 항목 저장이 가능한 로그인 계정 (CORE.DIM_USERS: user_id)
- **Customer**: 최소 한 번 이상 구매한 사용자 (CORE.DIM_CUSTOMERS: customer_id)
- **Account**: 청구 엔티티, B2B에서 여러 사용자를 가질 수 있음 (CORE.DIM_ACCOUNTS: account_id)

**관계:**
- User → Customer: 1:1 (구매자의 경우 customer_id = user_id)
- Account → User: 1:다수 (account_id로 조인)

---

## 비즈니스 용어

| 용어 | 정의 | 비고 |
|------|------------|-------|
| GMV | Gross Merchandise Value - 반품/할인 전 총 주문 금액 | 상위 매출 보고에 사용 |
| NMV | Net Merchandise Value - GMV에서 반품 및 할인 차감 | 실제 매출에 사용 |
| AOV | Average Order Value - NMV / 주문 수 | $0 주문 제외 |
| LTV | Lifetime Value - 첫 주문 이후 고객당 총 NMV | 롤링 계산, 매일 업데이트 |
| CAC | Customer Acquisition Cost - 마케팅 지출 / 신규 고객 수 | 코호트 월별 |

---

## 표준 필터

명시적으로 달리 지시하지 않는 한 항상 이 필터를 적용합니다:

```sql
-- 테스트 및 내부 주문 제외
WHERE order_status != 'TEST'
  AND customer_type != 'INTERNAL'
  AND is_employee_order = FALSE

-- 매출 지표에서 취소된 주문 제외
  AND order_status NOT IN ('CANCELLED', 'FRAUDULENT')
```

---

## 핵심 지표

### Gross Merchandise Value (GMV)
- **정의**: 주문된 모든 주문의 총 가치
- **수식**: `SUM(order_total_gross)`
- **출처**: `CORE.FCT_ORDERS.order_total_gross`
- **시간 단위**: 일별, 주별/월별로 집계
- **주의사항**: 나중에 취소되거나 반품될 수 있는 주문이 포함됨

### 순매출(Net Revenue)
- **정의**: 반품 및 할인 후 실제 매출
- **수식**: `SUM(order_total_gross - return_amount - discount_amount)`
- **출처**: `CORE.FCT_ORDERS`
- **주의사항**: 반품은 주문 후 최대 90일까지 발생 가능; 확정된 수치는 settled_revenue 사용

---

## 지식 베이스 탐색

| 도메인 | 참조 파일 | 용도 |
|--------|----------------|---------|
| 주문 | `references/orders.md` | 주문 테이블, GMV/NMV 계산 |
| 고객 | `references/customers.md` | 사용자/고객 엔티티, LTV, 코호트 |
| 제품 | `references/products.md` | 카탈로그, 재고, 카테고리 |

---

## 일반적인 쿼리 패턴

### 채널별 일별 GMV
```sql
SELECT
    DATE_TRUNC('DAY', order_timestamp) AS order_date,
    channel,
    SUM(order_total_gross) AS gmv,
    COUNT(DISTINCT order_id) AS order_count
FROM SHOPCO_DW.CORE.FCT_ORDERS
WHERE order_status NOT IN ('TEST', 'CANCELLED', 'FRAUDULENT')
  AND order_timestamp >= DATEADD(DAY, -30, CURRENT_DATE())
GROUP BY 1, 2
ORDER BY 1 DESC, 3 DESC
```

### 고객 코호트 리텐션
```sql
WITH cohorts AS (
    SELECT
        customer_id,
        DATE_TRUNC('MONTH', first_order_date) AS cohort_month
    FROM SHOPCO_DW.CORE.DIM_CUSTOMERS
)
SELECT
    c.cohort_month,
    DATEDIFF(MONTH, c.cohort_month, DATE_TRUNC('MONTH', o.order_timestamp)) AS months_since_first,
    COUNT(DISTINCT c.customer_id) AS active_customers
FROM cohorts c
JOIN SHOPCO_DW.CORE.FCT_ORDERS o ON c.customer_id = o.customer_id
WHERE o.order_status NOT IN ('TEST', 'CANCELLED')
GROUP BY 1, 2
ORDER BY 1, 2
```
```

---

## references/orders.md 예시

```markdown
# 주문 테이블

ShopCo의 주문 및 거래 데이터입니다.

---

## 주요 테이블

### FCT_ORDERS
**위치**: `SHOPCO_DW.CORE.FCT_ORDERS`
**설명**: 모든 주문의 팩트 테이블. 주문당 한 행.
**기본 키**: `order_id`
**업데이트 빈도**: 시간별 (15분 지연)
**파티션 기준**: `order_date`

| 컬럼 | 타입 | 설명 | 비고 |
|--------|------|-------------|-------|
| **order_id** | VARCHAR | 고유 주문 식별자 | |
| **customer_id** | VARCHAR | DIM_CUSTOMERS FK | 게스트 체크아웃의 경우 NULL |
| **order_timestamp** | TIMESTAMP_NTZ | 주문 시점 | UTC |
| **order_date** | DATE | order_timestamp의 날짜 부분 | 파티션 컬럼 |
| **order_status** | VARCHAR | 현재 상태 | PENDING, SHIPPED, DELIVERED, CANCELLED, RETURNED |
| **channel** | VARCHAR | 획득 채널 | WEB, APP, MARKETPLACE |
| **order_total_gross** | DECIMAL(12,2) | 할인 전 총액 | |
| **discount_amount** | DECIMAL(12,2) | 적용된 총 할인 | |
| **return_amount** | DECIMAL(12,2) | 반품된 항목의 가치 | 비동기적으로 업데이트 |

**관계**:
- `customer_id`로 `DIM_CUSTOMERS`와 조인
- `order_id`를 통해 `FCT_ORDER_ITEMS`의 부모

---

## 샘플 쿼리

### 반품율이 포함된 주문
```sql
SELECT
    DATE_TRUNC('WEEK', order_date) AS week,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN return_amount > 0 THEN 1 ELSE 0 END) AS orders_with_returns,
    DIV0(SUM(CASE WHEN return_amount > 0 THEN 1 ELSE 0 END), COUNT(*)) AS return_rate
FROM SHOPCO_DW.CORE.FCT_ORDERS
WHERE order_status NOT IN ('TEST', 'CANCELLED')
  AND order_date >= DATEADD(MONTH, -3, CURRENT_DATE())
GROUP BY 1
ORDER BY 1
```
```

---

이 예시는 다음을 보여줍니다:
- 트리거 설명이 포함된 완전한 frontmatter
- 방언별 SQL 참고사항
- 명확한 엔티티 구분
- 용어 사전
- 복사-붙여넣기 가능한 SQL로 된 표준 필터
- 수식이 포함된 지표 정의
- 참조 파일로의 탐색
- 실제 실행 가능한 쿼리 예시
