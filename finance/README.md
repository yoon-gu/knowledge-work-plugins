# Finance & Accounting 플러그인

[Cowork](https://claude.com/product/cowork)을 위해 주로 설계된 재무 및 회계 플러그인입니다. Anthropic의 에이전틱 데스크톱 앱이지만 Claude Code에서도 작동합니다. 월말 마감, 분개 준비, 계정 조정, 재무제표 생성, 차이 분석, SOX 감사 지원을 돕습니다.

> **중요**: 이 플러그인은 재무 및 회계 워크플로를 지원하지만 재무, 세무, 감사 조언을 제공하지 않습니다. 모든 출력은 재무 보고, 규제 제출, 감사 문서에 사용하기 전에 자격을 갖춘 재무 전문가가 검토해야 합니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/finance
```

## 명령

| Command | Description |
|---------|-------------|
| `/journal-entry` | 분개 준비 - 적절한 차변/대변과 지원 세부 정보로 미지급비용, 고정자산, 선급비용, 급여, 매출 인식 분개 생성 |
| `/reconciliation` | 계정 조정 - GL 잔액을 보조원장, 은행 또는 제3자 잔액과 비교하고 조정 항목 식별 |
| `/income-statement` | 손익계산서 생성 - 기간 대비 비교와 차이 분석이 포함된 P&L 작성 |
| `/variance-analysis` | 차이/변동 분석 - 차이를 동인으로 분해하고 서술 설명과 워터폴 분석 제공 |
| `/sox-testing` | SOX 준수 테스트 - 샘플 선택, 테스트 워크페이퍼, 통제 평가 생성 |

## 스킬

| Skill | Description |
|-------|-------------|
| `journal-entry-prep` | JE 준비 모범 사례, 표준 미지급 유형, 지원 문서 요구사항, 검토 워크플로 |
| `reconciliation` | GL-보조원장, 은행 조정, 인터컴퍼니 조정을 위한 조정 방법론과 조정 항목 분류 및 aging |
| `financial-statements` | GAAP 표시와 변동 분석 방법론을 갖춘 손익계산서, 대차대조표, 현금흐름표 형식 |
| `variance-analysis` | 가격/수량, 비율/구성, 중요성 기준, 서술 생성, 워터폴 차트 기법 |
| `close-management` | 월말 마감 체크리스트, 작업 순서, 의존성, 상태 추적, 일자별 일반 마감 활동 |
| `audit-support` | SOX 404 통제 테스트 방법론, 샘플 선택, 문서 표준, 결함 분류 |

## 예시 워크플로

### 월말 마감

1. `/journal-entry ap-accrual 2024-12`를 실행해 AP 미지급비용 분개 생성
2. `/journal-entry prepaid 2024-12`를 실행해 선급비용 상각
3. `/journal-entry fixed-assets 2024-12`를 실행해 감가상각 인식
4. `/reconciliation cash 2024-12`를 실행해 은행 계좌 조정
5. `/reconciliation accounts-receivable 2024-12`를 실행해 AR 보조원장 조정
6. `/income-statement monthly 2024-12`를 실행해 변동 분석이 포함된 P&L 생성

### 차이 분석

1. `/variance-analysis revenue 2024-Q4 vs 2024-Q3`를 실행해 매출 차이 분석
2. `/variance-analysis opex 2024-12 vs budget`를 실행해 운영비 차이 조사
3. 워터폴 분석을 검토하고 설명되지 않은 차이에 맥락을 제공합니다

### SOX 테스트

1. `/sox-testing revenue-recognition 2024-Q4`를 실행해 매출 통제 테스트 워크페이퍼 생성
2. `/sox-testing procure-to-pay 2024-Q4`를 실행해 조달 통제 테스트
3. 샘플 선택을 검토하고 테스트 결과를 문서화

## MCP 통합

> 익숙하지 않은 플레이스홀더가 보이거나 어떤 도구가 연결되어 있는지 확인해야 한다면 [CONNECTORS.md](CONNECTORS.md)를 참고하세요.

이 플러그인은 MCP 서버를 통해 재무 데이터 소스에 연결될 때 가장 잘 작동합니다. 관련 서버를 `.mcp.json`에 추가하세요:

### ERP / 회계 시스템

ERP(예: NetSuite, SAP) MCP 서버를 연결해 시산표, 보조원장 데이터, 분개를 자동으로 가져옵니다.

### 데이터 웨어하우스

데이터 웨어하우스(예: Snowflake, BigQuery) MCP 서버를 연결해 재무 데이터를 조회하고, 차이 분석을 실행하고, 과거 비교를 가져옵니다.

### 스프레드시트

스프레드시트 도구(예: Google Sheets, Excel)를 연결해 워크페이퍼 생성, 조정 템플릿, 재무 모델 업데이트를 지원합니다.

### 분석 / BI

BI 플랫폼(예: Tableau, Looker)을 연결해 대시보드, KPI, 추세 데이터를 가져와 차이 설명에 활용합니다.

> **참고:** ERP와 데이터 웨어하우스 MCP 서버를 연결하면 재무 데이터를 자동으로 가져올 수 있습니다. 이들이 없으면 데이터를 붙여넣거나 파일을 업로드해 분석할 수 있습니다.

## 설정

이 플러그인 디렉터리의 `.mcp.json` 파일에서 `mcpServers` 섹션에 데이터 소스 MCP 서버를 추가하세요. `recommendedCategories` 필드는 이 플러그인의 기능을 강화하는 통합 유형을 나열합니다:

- `erp-accounting` — GL, 보조원장, JE 데이터를 위한 ERP 또는 회계 시스템
- `data-warehouse` — 재무 쿼리와 과거 데이터를 위한 데이터 웨어하우스
- `spreadsheets` — 워크페이퍼 생성을 위한 스프레드시트 도구
- `analytics-bi` — 대시보드와 KPI 데이터를 위한 BI 도구
- `documents` — 정책, 메모, 지원 문서를 위한 문서 저장소
- `email` — 보고서를 보내고 승인을 요청하기 위한 이메일
- `chat` — 마감 상태 업데이트와 질문을 위한 팀 커뮤니케이션
