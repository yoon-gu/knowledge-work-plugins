# 데이터 애널리스트 플러그인

주로 Anthropic의 에이전트 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계된 데이터 애널리스트 플러그인으로, Claude Code에서도 작동합니다. SQL 쿼리, 데이터 탐색, 시각화, 대시보드, 인사이트 생성을 지원합니다. 모든 data warehouse, 모든 SQL 방언, 모든 애널리틱스 스택과 호환됩니다.

## 설치

```
claude plugins add knowledge-work-plugins/data
```

## 기능 설명

이 플러그인은 Claude를 데이터 애널리스트 협력자로 변환합니다. 데이터셋 탐색, 최적화된 SQL 작성, 시각화 구축, 인터랙티브 대시보드 생성, 이해관계자와 공유하기 전 분석 검증을 도와줍니다.

### Data Warehouse 연결 시

최상의 경험을 위해 data warehouse MCP 서버(예: Snowflake, Databricks, BigQuery, 또는 SQL 호환 데이터베이스)를 연결하세요. Claude는 다음을 수행합니다:

- data warehouse에 직접 쿼리
- 스키마 및 테이블 메타데이터 탐색
- 복사-붙여넣기 없이 분석 전 과정 실행
- 결과를 기반으로 쿼리 반복 개선

### Data Warehouse 미연결 시

data warehouse 연결 없이도 SQL 결과를 붙여넣거나 CSV/Excel 파일을 업로드하여 분석 및 시각화할 수 있습니다. Claude는 수동으로 실행할 SQL 쿼리를 작성하고, 제공된 결과를 분석할 수도 있습니다.

## 명령어

| 명령어 | 설명 |
|---------|-------------|
| `/analyze` | 간단한 조회부터 전체 분석까지 데이터 질문에 답변 |
| `/explore-data` | 데이터셋의 형태, 품질, 패턴을 이해하기 위한 프로파일링 및 탐색 |
| `/write-query` | 방언에 맞는 모범 사례를 적용한 최적화된 SQL 작성 |
| `/create-viz` | Python으로 출판 품질의 시각화 생성 |
| `/build-dashboard` | 필터와 차트가 포함된 인터랙티브 HTML 대시보드 구축 |
| `/validate` | 공유 전 분석 QA — 방법론, 정확성, 편향 검사 |

## 스킬

| 스킬 | 설명 |
|-------|-------------|
| `sql-queries` | 방언별 SQL 모범 사례, 공통 패턴, 성능 최적화 |
| `data-exploration` | 데이터 프로파일링, 품질 평가, 패턴 발견 |
| `data-visualization` | 차트 선택, Python 시각화 코드 패턴, 디자인 원칙 |
| `statistical-analysis` | 기술 통계, 트렌드 분석, 이상값 탐지, 가설 검정 |
| `data-validation` | 공유 전 QA, 정합성 검사, 문서화 기준 |
| `interactive-dashboard-builder` | Chart.js, 필터, 스타일링을 활용한 HTML/JS 대시보드 구축 |

## 예제 워크플로우

### 임시 분석

```
You: /analyze What was our monthly revenue trend for the past 12 months, broken down by product line?

Claude: [SQL 쿼리 작성] → [data warehouse에 실행] → [트렌드 차트 생성]
       → [주요 패턴 식별: "Product line A grew 23% YoY while B was flat"]
       → [정합성 검사로 결과 검증]
```

### 데이터 탐색

```
You: /explore-data users table

Claude: [테이블 프로파일링: 2.3M 행, 47 열]
       → [보고: created_at은 0.2% null, email은 99.8% 카디널리티]
       → [플래그: status 열에 340개 행에 예상치 못한 "UNKNOWN" 값 존재]
       → [제안: "탐색할 고가치 차원: plan_type, signup_source, country"]
```

### 쿼리 작성

```
You: /write-query I need a cohort retention analysis -- users grouped by signup month,
     showing what % are still active 1, 3, 6, and 12 months later. We use Snowflake.

Claude: [CTE가 포함된 최적화된 Snowflake SQL 작성]
       → [각 단계를 설명하는 주석 추가]
       → [파티션 프루닝에 대한 성능 메모 포함]
```

### 대시보드 구축

```
You: /build-dashboard Create a sales dashboard with monthly revenue, top products,
     and regional breakdown. Here's the data: [pastes CSV]

Claude: [독립형 HTML 파일 생성]
       → [인터랙티브 Chart.js 시각화 포함]
       → [지역 및 기간 드롭다운 필터 추가]
       → [검토를 위해 브라우저에서 열기]
```

### 공유 전 검증

```
You: /validate [shares analysis document]

Claude: [방법론 검토] → [이탈 분석의 생존 편향 확인]
       → [집계 로직 검증] → [플래그: "분모에서 체험판 사용자 제외로
          전환율이 약 5pp 과대평가될 수 있음"]
       → [신뢰도: "언급된 주의사항과 함께 공유 가능"]
```

## 데이터 스택 연결

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 하는 경우, [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

이 플러그인은 데이터 인프라에 연결될 때 가장 잘 작동합니다. 다음에 대한 MCP 서버를 추가하세요:

- **Data Warehouse**: Snowflake, Databricks, BigQuery, Definite, 또는 SQL 호환 데이터베이스
- **Analytics/BI**: Amplitude, Looker, Tableau, 또는 유사한 도구
- **Notebooks**: Jupyter, Hex, 또는 유사한 도구
- **스프레드시트**: Google Sheets, Excel
- **Data Orchestration**: Airflow, dbt, Dagster, Prefect
- **Data Ingestion**: Fivetran, Airbyte, Stitch

`.mcp.json` 또는 Claude Code 설정에서 MCP 서버를 구성하여 직접 데이터 액세스를 활성화하세요.
