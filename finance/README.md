# Finance & Accounting Plugin

재무 및 회계 플러그인으로, 주로 Anthropic의 에이전틱 데스크톱 애플리케이션인 [Cowork](https://claude.com/product/cowork)을 위해 설계되었습니다 — Claude Code에서도 동작합니다. 월말 결산, 분개 작성, 계정 조정, 재무제표 생성, 차이 분석, SOX 감사 지원을 제공합니다.

> **중요**: 이 플러그인은 재무 및 회계 워크플로우를 보조하지만 재무, 세무, 또는 감사 조언을 제공하지 않습니다. 모든 결과물은 재무 보고, 규제 신고, 또는 감사 문서에 사용하기 전에 자격을 갖춘 재무 전문가의 검토를 받아야 합니다.

## 설치

```bash
claude plugins add knowledge-work-plugins/finance
```

## 명령어

| 명령어 | 설명 |
|---------|-------------|
| `/journal-entry` | 분개 작성 — 발생주의 항목, 유형자산 항목, 선급금, 급여, 수익 항목을 적절한 차변/대변 및 지원 세부 내용과 함께 생성 |
| `/reconciliation` | 계정 조정 — GL 잔액을 보조원장, 은행, 또는 제3자 잔액과 비교하여 조정 항목 식별 |
| `/income-statement` | 손익계산서 생성 — 기간 비교 및 차이 분석이 포함된 P&L 작성 |
| `/variance-analysis` | 차이/변동 분석 — 차이를 원인별로 분해하고 설명 내러티브 및 워터폴 분석 제공 |
| `/sox-testing` | SOX 준수 테스트 — 샘플 선택, 테스트 워킹페이퍼, 통제 평가 생성 |

## 스킬

| 스킬 | 설명 |
|-------|-------------|
| `journal-entry-prep` | 분개 작성 모범 사례, 표준 발생주의 유형, 지원 문서 요건, 검토 워크플로우 |
| `reconciliation` | GL-보조원장, 은행 조정, 내부거래에 대한 조정 방법론 및 조정 항목 분류와 노령화 분석 |
| `financial-statements` | GAAP 표시 및 변동 분석 방법론이 포함된 손익계산서, 재무상태표, 현금흐름표 형식 |
| `variance-analysis` | 차이 분해 기법(가격/수량, 비율/구성), 중요성 기준, 내러티브 생성, 워터폴 차트 |
| `close-management` | 월말 결산 체크리스트, 작업 순서, 의존성, 상태 추적, 일별 일반적인 결산 활동 |
| `audit-support` | SOX 404 통제 테스트 방법론, 샘플 선택, 문서화 기준, 결함 분류 |

## 예시 워크플로우

### 월말 결산

1. `/journal-entry ap-accrual 2024-12` 실행하여 AP 발생주의 분개 생성
2. `/journal-entry prepaid 2024-12` 실행하여 선급비용 상각
3. `/journal-entry fixed-assets 2024-12` 실행하여 감가상각 처리
4. `/reconciliation cash 2024-12` 실행하여 은행 계좌 조정
5. `/reconciliation accounts-receivable 2024-12` 실행하여 AR 보조원장 조정
6. `/income-statement monthly 2024-12` 실행하여 변동 분석이 포함된 P&L 생성

### 차이 분석

1. `/variance-analysis revenue 2024-Q4 vs 2024-Q3` 실행하여 수익 차이 분석
2. `/variance-analysis opex 2024-12 vs budget` 실행하여 운영비 차이 조사
3. 워터폴 분석을 검토하고 설명되지 않은 차이에 대한 맥락 제공

### SOX 테스트

1. `/sox-testing revenue-recognition 2024-Q4` 실행하여 수익 인식 통제 테스트 워킹페이퍼 생성
2. `/sox-testing procure-to-pay 2024-Q4` 실행하여 조달 통제 테스트
3. 샘플 선택을 검토하고 테스트 결과 문서화

## MCP 통합

> 낯선 자리 표시자가 보이거나 연결된 도구를 확인해야 할 경우 [CONNECTORS.md](CONNECTORS.md)를 참조하세요.

이 플러그인은 MCP 서버를 통해 재무 데이터 소스에 연결될 때 최적으로 작동합니다. 관련 서버를 `.mcp.json`에 추가하세요:

### ERP / 회계 시스템

ERP(예: NetSuite, SAP) MCP 서버를 연결하여 시산표, 보조원장 데이터, 분개를 자동으로 가져옵니다.

### 데이터 웨어하우스

데이터 웨어하우스(예: Snowflake, BigQuery) MCP 서버를 연결하여 재무 데이터를 쿼리하고, 차이 분석을 실행하며, 과거 비교 데이터를 가져옵니다.

### 스프레드시트

스프레드시트 도구(예: Google Sheets, Excel)를 연결하여 워킹페이퍼 생성, 조정 템플릿, 재무 모델 업데이트를 수행합니다.

### Analytics / BI

BI 플랫폼(예: Tableau, Looker)을 연결하여 대시보드, KPI, 차이 설명을 위한 트렌드 데이터를 가져옵니다.

> **참고:** ERP 및 데이터 웨어하우스 MCP 서버를 연결하면 재무 데이터를 자동으로 가져올 수 있습니다. 이러한 연결 없이도 데이터를 붙여넣거나 파일을 업로드하여 분석할 수 있습니다.

## 구성

이 플러그인 디렉토리의 `.mcp.json` 내 `mcpServers` 섹션에 데이터 소스 MCP 서버를 추가하세요. `recommendedCategories` 필드에는 이 플러그인의 기능을 향상시키는 통합 유형이 나열됩니다:

- `erp-accounting` — GL, 보조원장, 분개 데이터를 위한 ERP 또는 회계 시스템
- `data-warehouse` — 재무 쿼리 및 과거 데이터를 위한 데이터 웨어하우스
- `spreadsheets` — 워킹페이퍼 생성을 위한 스프레드시트 도구
- `analytics-bi` — 대시보드 및 KPI 데이터를 위한 BI 도구
- `documents` — 정책, 메모, 지원 문서를 위한 문서 저장소
- `email` — 보고서 전송 및 승인 요청을 위한 이메일
- `chat` — 결산 현황 업데이트 및 질의를 위한 팀 커뮤니케이션
