# 예: 생성된 스킬

이는 부트스트랩 프로세스 후에 생성된 스킬이 어떻게 보이는지에 대한 예입니다. 이 예는 Snowflake를 사용하는 "ShopCo"이라는 가상의 전자 상거래 회사에 대한 것입니다.

---

## 예 SKILL.md

```markdown
---
name: shopco-data-analyst
description: "ShopCo data analysis skill for Snowflake. Provides context for querying e-commerce data including customer, order, and product analytics. Use when analyzing ShopCo data for: (1) Revenue and order metrics, (2) Customer behavior and retention, (3) Product performance, or any data questions requiring ShopCo-specific context."
---

# ShopCo Data Analysis

## SQL Dialect: Snowflake

- **Table references**: `SHOPCO_DW.SCHEMA.TABLE` or with quotes for case-sensitive: `"Column_Name"`
- **Safe division**: `DIV0(a, b)` returns 0, `DIV0NULL(a, b)` returns NULL
- **Date functions**:
  - `DATE_TRUNC('MONTH', date_col)`
  - `DATEADD(DAY, -1, date_col)`
  - `DATEDIFF(DAY, start_date, end_date)`
- **Column exclusion**: `SELECT * EXCLUDE (column_to_exclude)`

---

## Entity Disambiguation

**"Customer" can mean:**
- **User**: A login account that can browse and save items (CORE.DIM_USERS: user_id)
- **Customer**: A user who has made at least one purchase (CORE.DIM_CUSTOMERS: customer_id)
- **Account**: A billing entity, can have multiple users in B2B (CORE.DIM_ACCOUNTS: account_id)

**Relationships:**
- User → Customer: 1:1 (customer_id = user_id for purchasers)
- Account → User: 1:many (join on account_id)

---

## Business Terminology

| Term | Definition | Notes |
|------|------------|-------|
| GMV | Gross Merchandise Value - total order value before returns/discounts | Use for top-line reporting |
| NMV | Net Merchandise Value - GMV minus returns and discounts | Use for actual revenue |
| AOV | Average Order Value - NMV / order count | Exclude $0 orders |
| LTV | Lifetime Value - total NMV per customer since first order | Rolling calc, updates daily |
| CAC | Customer Acquisition Cost - marketing spend / new customers | By cohort month |

---

## Standard Filters

Always apply these filters unless explicitly told otherwise:

```sql
-- Exclude test and internal orders
WHERE order_status != 'TEST'
  AND customer_type != 'INTERNAL'
  AND is_employee_order = FALSE

-- Exclude cancelled orders for revenue metrics
  AND order_status NOT IN ('CANCELLED', 'FRAUDULENT')
```

---

## 주요 지표

### 총 상품 가치(GMV)
- **정의**: 접수된 모든 주문의 총 가치
- **공식**: `SUM(order_total_gross)`
- **출처**: `CORE.FCT_ORDERS.order_total_gross`
- **시간 단위**: 일별, 주별/월별로 집계됨
- **주의사항**: 나중에 취소되거나 반품될 수 있는 주문이 포함됩니다.

### 순수익
- **정의**: 반품 및 할인 후 실제 수익
- **공식**: `SUM(order_total_gross - return_amount - discount_amount)`
- **출처**: `CORE.FCT_ORDERS`
- **주의사항**: 반품은 주문 후 최대 90일까지 가능합니다. 확정된 숫자에 Seted_revenue를 사용하세요.

---

## 기술 자료 탐색

| 도메인 | 참조 파일 | 사용 대상 |
| -------- | ---------------- | --------- |
| 명령 | `references/orders.md` | 주문표, GMV/NMV 계산 |
| 고객 | `references/customers.md` | 사용자/고객 엔터티, LTV, 코호트 |
| 제품 | `references/products.md` | 카탈로그, 재고, 카테고리 |

---

## 일반적인 쿼리 패턴

### 채널별 일일 GMV
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

### 고객 집단 유지
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

## Example references/orders.md

```markdown
# 주문 테이블

ShopCo의 주문 및 거래 데이터입니다.

---

## 주요 테이블

### FCT_ORDERS
**위치**: `SHOPCO_DW.CORE.FCT_ORDERS` **설명**: 모든 주문에 대한 팩트 테이블입니다. 주문당 한 행입니다. **기본 키**: `order_id` **업데이트 빈도**: 매시간(15분 지연) **파티션 기준**: `order_date`

| 열 | 유형 | 설명 | 메모 |
| -------- | ------ | ------------- | ------- |
| **주문_ID** | VARCHAR | 고유 주문 식별자 | |
| **고객_ID** | VARCHAR | DIM_CUSTOMERS에 대한 FK | 비회원 결제의 경우 NULL |
| **주문_타임스탬프** | TIMESTAMP_NTZ | 주문이 접수되었을 때 | UTC |
| **주문_날짜** | 날짜 | order_timestamp의 날짜 부분 | 파티션 컬럼 |
| **주문_상태** | VARCHAR | 현황 | 보류 중, 배송됨, 배송됨, 취소됨, 반품됨 |
| **채널** | VARCHAR | 획득 채널 | 웹, 앱, 마켓플레이스 |
| **주문_총_총액** | 십진수(12,2) | 할인 전 총액 | |
| **할인_금액** | 십진수(12,2) | 총 할인 적용 | |
| **반품_금액** | 십진수(12,2) | 반품된 상품의 가치 | 비동기 업데이트 |

**관계**:
- `customer_id`에서 `DIM_CUSTOMERS`에 조인
- `order_id`을(를) 통해 `FCT_ORDER_ITEMS`의 상위

---

## 샘플 쿼리

### 반품률이 있는 주문
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

This example demonstrates:
- Complete frontmatter with triggering description
- Dialect-specific SQL notes
- Clear entity disambiguation
- Terminology glossary
- Standard filters as copy-paste SQL
- Metric definitions with formulas
- Navigation to reference files
- Real, runnable query examples
