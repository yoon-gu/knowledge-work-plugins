# 데이터 분석가 플러그인

주로 Anthropic의 에이전트 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)용으로 설계된 데이터 분석 플러그인입니다. 단, Claude Code에서도 작동합니다. SQL 쿼리, 데이터 탐색, 시각화, 대시보드 및 통찰력 생성. 모든 데이터 웨어하우스, SQL 언어 및 분석 스택과 함께 작동합니다.

## 설치

```
claude plugins add knowledge-work-plugins/data
```

## 그것이 하는 일

이 플러그인은 Claude를 데이터 분석가 공동 작업자로 변모시킵니다. 이해관계자와 공유하기 전에 데이터세트를 탐색하고, 최적화된 SQL을 작성하고, 시각화를 구축하고, 대화형 대시보드를 만들고, 분석을 검증하는 데 도움이 됩니다.

### 데이터 웨어하우스 연결 사용

최상의 경험을 위해 데이터 웨어하우스 MCP 서버(예: Snowflake, Databricks, BigQuery 또는 모든 SQL 호환 데이터베이스)를 연결하세요. 클로드는 다음을 수행합니다.

- 데이터 웨어하우스에 직접 쿼리
- 스키마 및 테이블 메타데이터 탐색
- 복사-붙여넣기 없이 엔드투엔드 분석 실행
- 결과를 기반으로 쿼리 반복

### 데이터 웨어하우스 연결 없이

데이터 웨어하우스 연결 없이 SQL 결과를 붙여넣거나 분석 및 시각화를 위해 CSV/Excel 파일을 업로드하세요. Claude는 또한 수동으로 실행할 SQL 쿼리를 작성한 다음 제공한 결과를 분석할 수 있습니다.

## 명령

| 명령 | 설명 |
|---------|-------------|
| `/analyze` | 빠른 조회부터 전체 분석까지 데이터 질문에 답하세요. |
| `/explore-data` | 데이터 세트의 프로파일링 및 탐색을 통해 데이터 세트의 모양, 품질 및 패턴을 이해합니다. |
| `/write-query` | 모범 사례를 사용하여 방언에 최적화된 SQL 작성 |
| `/create-viz` | Python을 사용하여 출판 수준의 시각화 만들기 |
| `/build-dashboard` | 필터와 차트를 사용하여 대화형 HTML 대시보드 구축 |
| `/validate` | 공유 전 분석 QA - 방법론, 정확성 및 편향 확인 |

## 기술

| 기능 | 설명 |
|-------|-------------|
| `sql-queries` | 방언, 공통 패턴 및 성능 최적화에 대한 SQL 모범 사례 |
| `data-exploration` | 데이터 프로파일링, 품질 평가 및 패턴 발견 |
| `data-visualization` | 차트 선택, Python viz 코드 패턴 및 디자인 원칙 |
| `statistical-analysis` | 기술 통계, 추세 분석, 이상치 탐지 및 가설 테스트 |
| `data-validation` | 납품 전 QA, 온전성 검사 및 문서화 표준 |
| `interactive-dashboard-builder` | Chart.js, 필터 및 스타일링을 사용한 HTML/JS 대시보드 구성 |

## 예시 워크플로

### 임시 분석

```
You: /analyze What was our monthly revenue trend for the past 12 months, broken down by product line?

Claude: [Writes SQL query] → [Executes against data warehouse] → [Generates trend chart]
       → [Identifies key patterns: "Product line A grew 23% YoY while B was flat"]
       → [Validates results with sanity checks]
```

### 데이터 탐색

```
You: /explore-data users table

Claude: [Profiles table: 2.3M rows, 47 columns]
       → [Reports: created_at has 0.2% nulls, email has 99.8% cardinality]
       → [Flags: status column has unexpected value "UNKNOWN" in 340 rows]
       → [Suggests: "High-value dimensions to explore: plan_type, signup_source, country"]
```

### 쿼리 작성

```
You: /write-query I need a cohort retention analysis -- users grouped by signup month,
     showing what % are still active 1, 3, 6, and 12 months later. We use Snowflake.

Claude: [Writes optimized Snowflake SQL with CTEs]
       → [Adds comments explaining each step]
       → [Includes performance notes about partition pruning]
```

### 대시보드 구축

```
You: /build-dashboard Create a sales dashboard with monthly revenue, top products,
     and regional breakdown. Here's the data: [pastes CSV]

Claude: [Generates self-contained HTML file]
       → [Includes interactive Chart.js visualizations]
       → [Adds dropdown filters for region and time period]
       → [Opens in browser for review]
```

### 사전 공유 검증

```
You: /validate [shares analysis document]

Claude: [Reviews methodology] → [Checks for survivorship bias in churn analysis]
       → [Verifies aggregation logic] → [Flags: "Denominator excludes trial users
          which could overstate conversion rate by ~5pp"]
       → [Confidence: "Ready to share with noted caveat"]
```

## 데이터 스택 연결

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](CONNECTORS.md)을 참조하세요.

이 플러그인은 데이터 인프라에 연결되어 있을 때 가장 잘 작동합니다. 다음에 대한 MCP 서버 추가:

- **데이터 웨어하우스**: Snowflake, Databricks, BigQuery, Definite 또는 모든 SQL 호환 데이터베이스
- **분석/BI**: Amplitude, Looker, Tableau 또는 유사
- **노트북**: Jupyter, Hex 또는 유사
- **스프레드시트**: Google 스프레드시트, Excel
- **데이터 오케스트레이션**: Airflow, dbt, Dagster, Prefect
- **데이터 수집**: Fivetran, Airbyte, Stitch

직접 데이터 액세스를 활성화하려면 `.mcp.json` 또는 Claude Code 설정에서 MCP 서버를 구성하세요.
