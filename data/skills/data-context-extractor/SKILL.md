---
name: data-context-extractor
description: >
  분석가로부터 부족 지식을 추출하여 회사별 데이터 분석 기술을 생성하거나 향상시킵니다.

  BOOTSTRAP MODE - Triggers: "Create a data context skill", "Set up data analysis for our warehouse",
  "Help me create a skill for our database", "Generate a data skill for [company]"
  → Discovers schemas, asks key questions, generates initial skill with reference files

  ITERATION MODE - Triggers: "Add context about [domain]", "The skill needs more info about [topic]",
  "Update the data skill with [metrics/tables/terminology]", "Improve the [domain] reference"
  → Loads existing skill, asks targeted questions, appends/updates reference files

  Use when data analysts want Claude to understand their company's specific data warehouse,
  terminology, metrics definitions, and common query patterns.
---

# 데이터 컨텍스트 추출기

분석가로부터 기업별 데이터 지식을 추출하여 맞춤형 데이터 분석 스킬을 생성하는 메타 스킬입니다.

## 작동 방식

이 스킬에는 두 가지 모드가 있습니다.

1. **부트스트랩 모드**: 처음부터 새로운 데이터 분석 기술 만들기
2. **반복 모드**: 도메인별 참조 파일을 추가하여 기존 기술을 향상시킵니다.

---

## 부트스트랩 모드

사용 시기: 사용자가 웨어하우스에 대한 새 데이터 컨텍스트 기술을 생성하려고 합니다.

### 1단계: 데이터베이스 연결 및 검색

**1단계: 데이터베이스 유형 식별**

질문: "What data warehouse are you using?"

일반적인 옵션:
- **빅쿼리**
- **눈송이**
- **PostgreSQL/레드시프트**
- **데이터브릭스**

`~~data warehouse` 도구(쿼리 및 스키마)를 사용하여 연결하세요. 확실하지 않은 경우 현재 세션에서 사용 가능한 MCP 도구를 확인하세요.

**2단계: 스키마 탐색**

`~~data warehouse` 스키마 도구를 사용하여 다음을 수행합니다.
1. 사용 가능한 데이터 세트/스키마 나열
2. 가장 중요한 테이블 식별(사용자에게 문의: "Which 3-5 tables do analysts query most often?")
3. 해당 주요 테이블에 대한 스키마 세부정보 가져오기

방언별 샘플 탐색 쿼리:
```sql
-- BigQuery: List datasets
SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA

-- BigQuery: List tables in a dataset
SELECT table_name FROM `project.dataset.INFORMATION_SCHEMA.TABLES`

-- Snowflake: List schemas
SHOW SCHEMAS IN DATABASE my_database

-- Snowflake: List tables
SHOW TABLES IN SCHEMA my_schema
```

### 2단계: 핵심 질문(이것을 물어보세요)

스키마 검색 후 다음 질문을 대화식으로 질문하십시오(한 번에 모두가 아님).

**엔티티 명확성(중요)**
> "When people here say 'user' or 'customer', what exactly do they mean? Are there different types?"

다음 내용을 들어보세요:
- 다양한 엔터티 유형(사용자, 계정, 조직)
- 이들 간의 관계(1:1, 1:다, 다대다)
- 이들을 서로 연결하는 ID 필드

**기본 식별자**
> "What's the main identifier for a [customer/user/account]? Are there multiple IDs for the same entity?"

다음 내용을 들어보세요:
- 기본 키와 비즈니스 키
- UUID와 정수 ID
- 레거시 ID 시스템

**주요 측정항목**
> "What are the 2-3 metrics people ask about most? How is each one calculated?"

다음 내용을 들어보세요:
- 정확한 수식(ARR = 월별_수익 × 12)
- 각 측정항목을 제공하는 테이블/열
- 기간 규칙(후행 7일, 역월 등)

**데이터 위생**
> "What should ALWAYS be filtered out of queries? (test data, fraud, internal users, etc.)"

다음 내용을 들어보세요:
- 항상 포함할 표준 WHERE 절
- 제외를 나타내는 플래그 열(is_test, is_internal, is_fraud)
- 제외할 특정 값(상태 = 'deleted')

**일반적인 문제점**
> "What mistakes do new analysts typically make with this data?"

다음 내용을 들어보세요:
- 혼란스러운 열 이름
- 시간대 문제
- NULL 처리 문제
- 과거 및 현재 상태 테이블

### 3단계: 기술 생성

다음 구조로 스킬을 만듭니다.

```
[company]-data-analyst/
├── SKILL.md
└── references/
    ├── entities.md          # Entity definitions and relationships
    ├── metrics.md           # KPI calculations
    ├── tables/              # One file per domain
    │   ├── [domain1].md
    │   └── [domain2].md
    └── dashboards.json      # Optional: existing dashboards catalog
```

**SKILL.md 템플릿**: `references/skill-template.md` 참조

**SQL 언어 섹션**: `references/sql-dialects.md`을 참조하고 적절한 언어 설명을 포함하세요.

**참조 파일 템플릿**: `references/domain-template.md` 참조

### 4단계: 포장 및 배송

1. 스킬 디렉터리에 모든 파일을 생성합니다.
2. zip 파일로 패키지
3. 캡처된 내용의 요약을 사용자에게 제시

---

## 반복 모드

사용 시기: 사용자에게 기존 기술이 있지만 더 많은 컨텍스트를 추가해야 합니다.

### 1단계: 기존 스킬 로드

사용자에게 기존 기술(zip 또는 폴더)을 업로드하도록 요청하거나 이미 세션에 있는 경우 해당 기술을 찾으십시오.

이미 문서화된 내용을 이해하려면 최신 SKILL.md 및 참조 파일을 읽어보세요.

### 2단계: 격차 식별

질문: "What domain or topic needs more context? What queries are failing or producing wrong results?"

일반적인 격차:
- 새로운 데이터 도메인(마케팅, 재무, 제품 등)
- 측정항목 정의가 누락되었습니다.
- 문서화되지 않은 테이블 관계
- 새로운 용어

### 3단계: 타겟 검색

식별된 도메인의 경우:

1. **관련 테이블 탐색**: `~~data warehouse` 스키마 도구를 사용하여 해당 도메인에서 테이블을 찾습니다.
2. **도메인별 질문을 해보세요**:
   - "What tables are used for [domain] analysis?"
   - "What are the key metrics for [domain]?"
   - "Any special filters or gotchas for [domain] data?"

3. **새 참조 파일 생성**: 도메인 템플릿을 사용하여 `references/[domain].md` 생성

### 4단계: 업데이트 및 재패키지

1. 새 참조 파일 추가
2. 새 도메인을 포함하도록 SKILL.md의 "Knowledge Base Navigation" 섹션을 업데이트하세요.
3. 스킬을 다시 패키징하세요
4. 업데이트된 스킬을 사용자에게 제시

---

## 참조 파일 표준

각 참조 파일에는 다음이 포함되어야 합니다.

### 테이블 문서의 경우
- **위치**: 전체 테이블 경로
- **설명**: 이 표에 포함된 내용, 사용 시기
- **기본 키**: 행을 고유하게 식별하는 방법
- **업데이트 빈도**: 데이터가 새로고침되는 빈도
- **주요 열**: 열 이름, 유형, 설명, 메모가 포함된 테이블
- **관계**: 이 테이블이 다른 테이블과 조인되는 방식
- **샘플 쿼리**: 2~3개의 일반적인 쿼리 패턴

### 측정항목 문서의 경우
- **측정항목 이름**: 사람이 읽을 수 있는 이름
- **정의**: 일반 영어 설명
- **공식**: 열 참조를 사용한 정확한 계산
- **소스 테이블**: 데이터의 출처
- **주의사항**: 극단적인 경우, 제외, 문제점

### 엔터티 문서의 경우
- **단체 이름**: 명칭
- **정의**: 비즈니스에서 나타내는 것
- **기본 테이블**: 이 항목을 찾을 수 있는 위치
- **ID 필드**: 식별 방법
- **관계**: 다른 항목과의 관계
- **공통 필터**: 표준 제외(내부, 테스트 등)

---

## 품질 체크리스트

생성된 기술을 제공하기 전에 다음을 확인하십시오.

- [ ] SKILL.md에는 완전한 머리말(이름, 설명)이 있습니다.
- [ ] 엔터티 명확성 섹션이 명확함
- [ ] 주요 ​​용어가 정의되어 있습니다.
- [ ] 표준 필터/제외 사항이 문서화되어 있습니다.
- [ ] 도메인당 최소 2-3개의 샘플 쿼리
- [ ] SQL이 올바른 방언 구문을 사용합니다.
- [ ] 참조 파일은 SKILL.md 탐색 섹션에 링크되어 있습니다.
