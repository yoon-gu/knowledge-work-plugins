---
name: build-dashboard
description: 차트, 필터, 테이블이 포함된 인터랙티브 HTML 대시보드를 빌드합니다. KPI 카드가 포함된 경영진 개요를 만들거나, 쿼리 결과를 공유 가능한 독립형 보고서로 변환하거나, 팀 모니터링 스냅샷을 구축하거나, 브라우저에서 열 수 있는 하나의 파일에 필터가 포함된 여러 차트가 필요할 때 사용합니다.
argument-hint: "<설명> [데이터 소스]"
---

# /build-dashboard - 인터랙티브 대시보드 빌드

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 할 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

차트, 필터, 테이블 및 전문적인 스타일링이 포함된 독립형 인터랙티브 HTML 대시보드를 빌드합니다. 서버나 의존성 없이 브라우저에서 직접 열 수 있습니다.

## 사용법

```
/build-dashboard <대시보드 설명> [데이터 소스]
```

## 워크플로우

### 1. 대시보드 요구사항 파악

결정 사항:

- **목적**: 경영진 개요, 운영 모니터링, 심층 분석, 팀 보고
- **대상**: 누가 이 대시보드를 사용할 것인가?
- **핵심 지표**: 가장 중요한 수치는 무엇인가?
- **차원**: 사용자가 필터링하거나 분할할 수 있어야 하는 항목은?
- **데이터 소스**: 라이브 쿼리, 붙여넣기 데이터, CSV 파일 또는 샘플 데이터

### 2. 데이터 수집

**데이터 웨어하우스가 연결된 경우:**
1. 필요한 데이터를 쿼리
2. 결과를 HTML 파일 내에 JSON으로 포함

**데이터가 붙여넣기 또는 업로드된 경우:**
1. 데이터를 파싱하고 정리
2. 대시보드에 JSON으로 포함

**데이터 없이 설명만으로 작업하는 경우:**
1. 설명된 스키마와 일치하는 현실적인 샘플 데이터셋 생성
2. 대시보드에 샘플 데이터를 사용한다고 표기
3. 실제 데이터로 교체하는 방법에 대한 지침 제공

### 3. 대시보드 레이아웃 설계

표준 대시보드 레이아웃 패턴을 따릅니다:

```
┌──────────────────────────────────────────────────┐
│  대시보드 제목                      [필터 ▼]  │
├────────────┬────────────┬────────────┬───────────┤
│  KPI 카드  │  KPI 카드  │  KPI 카드  │ KPI 카드  │
├────────────┴────────────┼────────────┴───────────┤
│                         │                        │
│    주요 차트            │   보조 차트            │
│    (가장 큰 영역)       │                        │
│                         │                        │
├─────────────────────────┴────────────────────────┤
│                                                  │
│    상세 테이블 (정렬 가능, 스크롤 가능)           │
│                                                  │
└──────────────────────────────────────────────────┘
```

**콘텐츠에 맞게 레이아웃을 조정합니다:**
- 상단에 2-4개의 KPI 카드로 핵심 수치 표시
- 중간 섹션에 1-3개의 차트로 추세와 분석
- 하단에 드릴다운 데이터를 위한 선택적 상세 테이블
- 복잡도에 따라 헤더 또는 사이드바에 필터

### 4. HTML 대시보드 빌드

아래 기본 템플릿을 사용하여 단일 독립형 HTML 파일을 생성합니다. 파일에 포함되는 내용:

**구조 (HTML):**
- 시맨틱 HTML5 레이아웃
- CSS Grid 또는 Flexbox를 사용한 반응형 그리드
- 필터 컨트롤 (드롭다운, 날짜 선택기, 토글)
- 값과 레이블이 있는 KPI 카드
- 차트 컨테이너
- 정렬 가능한 헤더가 있는 데이터 테이블

**스타일링 (CSS):**
- 전문적인 색상 체계 (깔끔한 흰색, 회색, 데이터를 위한 강조 색상)
- 미묘한 그림자가 있는 카드 기반 레이아웃
- 일관된 타이포그래피 (빠른 로딩을 위한 시스템 폰트)
- 다양한 화면 크기에서 작동하는 반응형 디자인
- 인쇄 친화적 스타일

**인터랙티비티 (JavaScript):**
- 인터랙티브 차트를 위한 Chart.js (CDN을 통해 포함)
- 모든 차트와 테이블을 동시에 업데이트하는 필터 드롭다운
- 정렬 가능한 테이블 컬럼
- 차트의 호버 툴팁
- 숫자 서식 (쉼표, 통화, 백분율)

**데이터 (내장 JSON):**
- 모든 데이터가 JavaScript 변수로 HTML에 직접 내장
- 외부 데이터 가져오기 필요 없음
- 대시보드가 완전히 오프라인으로 작동

### 5. 차트 유형 구현

모든 차트에 Chart.js를 사용합니다. 일반적인 대시보드 차트 패턴:

- **꺾은선 차트**: 시계열 추세
- **막대 차트**: 카테고리 비교
- **도넛 차트**: 구성 (<6개 카테고리인 경우)
- **누적 막대**: 시간에 따른 구성
- **혼합 (막대 + 꺾은선)**: 비율 오버레이가 있는 볼륨

각 차트 유형에 대해 아래의 Chart.js 통합 패턴을 사용합니다.

### 6. 인터랙티비티 추가

드롭다운 필터, 날짜 범위 필터, 결합 필터 로직, 정렬 가능한 테이블 및 차트 업데이트를 위해 아래의 필터 및 인터랙티비티 구현 패턴을 사용합니다.

### 7. 저장 및 열기

1. 대시보드를 설명적인 이름으로 HTML 파일로 저장 (예: `sales_dashboard.html`)
2. 사용자의 기본 브라우저에서 열기
3. 올바르게 렌더링되는지 확인
4. 데이터 업데이트 또는 커스터마이징 방법에 대한 지침 제공

---

## 기본 템플릿

모든 대시보드는 이 구조를 따릅니다:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Title</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1" integrity="sha384-jb8JQMbMoBUzgWatfe6COACi2ljcDdZQ2OxczGA3bGNeWe+6DChMTBJemed7ZnvJ" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0" integrity="sha384-cVMg8E3QFwTvGCDuK+ET4PD341jF3W8nO1auiXfuZNQkzbUUiBGLsIQUE+b1mxws" crossorigin="anonymous"></script>
    <style>
        /* 대시보드 스타일은 여기에 */
    </style>
</head>
<body>
    <div class="dashboard-container">
        <header class="dashboard-header">
            <h1>Dashboard Title</h1>
            <div class="filters">
                <!-- 필터 컨트롤 -->
            </div>
        </header>

        <section class="kpi-row">
            <!-- KPI 카드 -->
        </section>

        <section class="chart-row">
            <!-- 차트 컨테이너 -->
        </section>

        <section class="table-section">
            <!-- 데이터 테이블 -->
        </section>

        <footer class="dashboard-footer">
            <span>Data as of: <span id="data-date"></span></span>
        </footer>
    </div>

    <script>
        // 내장 데이터
        const DATA = [];

        // 대시보드 로직
        class Dashboard {
            constructor(data) {
                this.rawData = data;
                this.filteredData = data;
                this.charts = {};
                this.init();
            }

            init() {
                this.setupFilters();
                this.renderKPIs();
                this.renderCharts();
                this.renderTable();
            }

            applyFilters() {
                // 필터 로직
                this.filteredData = this.rawData.filter(row => {
                    // 각 활성 필터 적용
                    return true; // 플레이스홀더
                });
                this.renderKPIs();
                this.updateCharts();
                this.renderTable();
            }

            // ... 각 섹션에 대한 메서드
        }

        const dashboard = new Dashboard(DATA);
    </script>
</body>
</html>
```

## KPI 카드 패턴

```html
<div class="kpi-card">
    <div class="kpi-label">Total Revenue</div>
    <div class="kpi-value" id="kpi-revenue">$0</div>
    <div class="kpi-change positive" id="kpi-revenue-change">+0%</div>
</div>
```

```javascript
function renderKPI(elementId, value, previousValue, format = 'number') {
    const el = document.getElementById(elementId);
    const changeEl = document.getElementById(elementId + '-change');

    // 값 서식 지정
    el.textContent = formatValue(value, format);

    // 변화율 계산 및 표시
    if (previousValue && previousValue !== 0) {
        const pctChange = ((value - previousValue) / previousValue) * 100;
        const sign = pctChange >= 0 ? '+' : '';
        changeEl.textContent = `${sign}${pctChange.toFixed(1)}% vs prior period`;
        changeEl.className = `kpi-change ${pctChange >= 0 ? 'positive' : 'negative'}`;
    }
}

function formatValue(value, format) {
    switch (format) {
        case 'currency':
            if (value >= 1e6) return `$${(value / 1e6).toFixed(1)}M`;
            if (value >= 1e3) return `$${(value / 1e3).toFixed(1)}K`;
            return `$${value.toFixed(0)}`;
        case 'percent':
            return `${value.toFixed(1)}%`;
        case 'number':
            if (value >= 1e6) return `${(value / 1e6).toFixed(1)}M`;
            if (value >= 1e3) return `${(value / 1e3).toFixed(1)}K`;
            return value.toLocaleString();
        default:
            return value.toString();
    }
}
```

## Chart.js 통합

### 차트 컨테이너 패턴

```html
<div class="chart-container">
    <h3 class="chart-title">Monthly Revenue Trend</h3>
    <canvas id="revenue-chart"></canvas>
</div>
```

### 꺾은선 차트

```javascript
function createLineChart(canvasId, labels, datasets) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets.map((ds, i) => ({
                label: ds.label,
                data: ds.data,
                borderColor: COLORS[i % COLORS.length],
                backgroundColor: COLORS[i % COLORS.length] + '20',
                borderWidth: 2,
                fill: ds.fill || false,
                tension: 0.3,
                pointRadius: 3,
                pointHoverRadius: 6,
            }))
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: { usePointStyle: true, padding: 20 }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${formatValue(context.parsed.y, 'currency')}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: { display: false }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return formatValue(value, 'currency');
                        }
                    }
                }
            }
        }
    });
}
```

### 막대 차트

```javascript
function createBarChart(canvasId, labels, data, options = {}) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    const isHorizontal = options.horizontal || labels.length > 8;

    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: options.label || 'Value',
                data: data,
                backgroundColor: options.colors || COLORS.map(c => c + 'CC'),
                borderColor: options.colors || COLORS,
                borderWidth: 1,
                borderRadius: 4,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: isHorizontal ? 'y' : 'x',
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return formatValue(context.parsed[isHorizontal ? 'x' : 'y'], options.format || 'number');
                        }
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    grid: { display: isHorizontal },
                    ticks: isHorizontal ? {
                        callback: function(value) {
                            return formatValue(value, options.format || 'number');
                        }
                    } : {}
                },
                y: {
                    beginAtZero: !isHorizontal,
                    grid: { display: !isHorizontal },
                    ticks: !isHorizontal ? {
                        callback: function(value) {
                            return formatValue(value, options.format || 'number');
                        }
                    } : {}
                }
            }
        }
    });
}
```

### 도넛 차트

```javascript
function createDoughnutChart(canvasId, labels, data) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: COLORS.map(c => c + 'CC'),
                borderColor: '#ffffff',
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '60%',
            plugins: {
                legend: {
                    position: 'right',
                    labels: { usePointStyle: true, padding: 15 }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const pct = ((context.parsed / total) * 100).toFixed(1);
                            return `${context.label}: ${formatValue(context.parsed, 'number')} (${pct}%)`;
                        }
                    }
                }
            }
        }
    });
}
```

### 필터 변경 시 차트 업데이트

```javascript
function updateChart(chart, newLabels, newData) {
    chart.data.labels = newLabels;

    if (Array.isArray(newData[0])) {
        // 다중 데이터셋
        newData.forEach((data, i) => {
            chart.data.datasets[i].data = data;
        });
    } else {
        chart.data.datasets[0].data = newData;
    }

    chart.update('none'); // 'none'은 즉시 업데이트를 위해 애니메이션을 비활성화
}
```

## 필터 및 인터랙티비티 구현

### 드롭다운 필터

```html
<div class="filter-group">
    <label for="filter-region">Region</label>
    <select id="filter-region" onchange="dashboard.applyFilters()">
        <option value="all">All Regions</option>
    </select>
</div>
```

```javascript
function populateFilter(selectId, data, field) {
    const select = document.getElementById(selectId);
    const values = [...new Set(data.map(d => d[field]))].sort();

    // "전체" 옵션 유지, 고유값 추가
    values.forEach(val => {
        const option = document.createElement('option');
        option.value = val;
        option.textContent = val;
        select.appendChild(option);
    });
}

function getFilterValue(selectId) {
    const val = document.getElementById(selectId).value;
    return val === 'all' ? null : val;
}
```

### 날짜 범위 필터

```html
<div class="filter-group">
    <label>Date Range</label>
    <input type="date" id="filter-date-start" onchange="dashboard.applyFilters()">
    <span>to</span>
    <input type="date" id="filter-date-end" onchange="dashboard.applyFilters()">
</div>
```

```javascript
function filterByDateRange(data, dateField, startDate, endDate) {
    return data.filter(row => {
        const rowDate = new Date(row[dateField]);
        if (startDate && rowDate < new Date(startDate)) return false;
        if (endDate && rowDate > new Date(endDate)) return false;
        return true;
    });
}
```

### 결합 필터 로직

```javascript
applyFilters() {
    const region = getFilterValue('filter-region');
    const category = getFilterValue('filter-category');
    const startDate = document.getElementById('filter-date-start').value;
    const endDate = document.getElementById('filter-date-end').value;

    this.filteredData = this.rawData.filter(row => {
        if (region && row.region !== region) return false;
        if (category && row.category !== category) return false;
        if (startDate && row.date < startDate) return false;
        if (endDate && row.date > endDate) return false;
        return true;
    });

    this.renderKPIs();
    this.updateCharts();
    this.renderTable();
}
```

### 정렬 가능한 테이블

```javascript
function renderTable(containerId, data, columns) {
    const container = document.getElementById(containerId);
    let sortCol = null;
    let sortDir = 'desc';

    function render(sortedData) {
        let html = '<table class="data-table">';

        // 헤더
        html += '<thead><tr>';
        columns.forEach(col => {
            const arrow = sortCol === col.field
                ? (sortDir === 'asc' ? ' ▲' : ' ▼')
                : '';
            html += `<th onclick="sortTable('${col.field}')" style="cursor:pointer">${col.label}${arrow}</th>`;
        });
        html += '</tr></thead>';

        // 본문
        html += '<tbody>';
        sortedData.forEach(row => {
            html += '<tr>';
            columns.forEach(col => {
                const value = col.format ? formatValue(row[col.field], col.format) : row[col.field];
                html += `<td>${value}</td>`;
            });
            html += '</tr>';
        });
        html += '</tbody></table>';

        container.innerHTML = html;
    }

    window.sortTable = function(field) {
        if (sortCol === field) {
            sortDir = sortDir === 'asc' ? 'desc' : 'asc';
        } else {
            sortCol = field;
            sortDir = 'desc';
        }
        const sorted = [...data].sort((a, b) => {
            const aVal = a[field], bVal = b[field];
            const cmp = aVal < bVal ? -1 : aVal > bVal ? 1 : 0;
            return sortDir === 'asc' ? cmp : -cmp;
        });
        render(sorted);
    };

    render(data);
}
```

## 대시보드 CSS 스타일링

### 색상 시스템

```css
:root {
    /* 배경 레이어 */
    --bg-primary: #f8f9fa;
    --bg-card: #ffffff;
    --bg-header: #1a1a2e;

    /* 텍스트 */
    --text-primary: #212529;
    --text-secondary: #6c757d;
    --text-on-dark: #ffffff;

    /* 데이터용 강조 색상 */
    --color-1: #4C72B0;
    --color-2: #DD8452;
    --color-3: #55A868;
    --color-4: #C44E52;
    --color-5: #8172B3;
    --color-6: #937860;

    /* 상태 색상 */
    --positive: #28a745;
    --negative: #dc3545;
    --neutral: #6c757d;

    /* 간격 */
    --gap: 16px;
    --radius: 8px;
}
```

### 레이아웃

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.5;
}

.dashboard-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: var(--gap);
}

.dashboard-header {
    background: var(--bg-header);
    color: var(--text-on-dark);
    padding: 20px 24px;
    border-radius: var(--radius);
    margin-bottom: var(--gap);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
}

.dashboard-header h1 {
    font-size: 20px;
    font-weight: 600;
}
```

### KPI 카드

```css
.kpi-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: var(--gap);
    margin-bottom: var(--gap);
}

.kpi-card {
    background: var(--bg-card);
    border-radius: var(--radius);
    padding: 20px 24px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.kpi-label {
    font-size: 13px;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}

.kpi-value {
    font-size: 28px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.kpi-change {
    font-size: 13px;
    font-weight: 500;
}

.kpi-change.positive { color: var(--positive); }
.kpi-change.negative { color: var(--negative); }
```

### 차트 컨테이너

```css
.chart-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: var(--gap);
    margin-bottom: var(--gap);
}

.chart-container {
    background: var(--bg-card);
    border-radius: var(--radius);
    padding: 20px 24px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.chart-container h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 16px;
}

.chart-container canvas {
    max-height: 300px;
}
```

### 필터

```css
.filters {
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
}

.filter-group {
    display: flex;
    align-items: center;
    gap: 6px;
}

.filter-group label {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.7);
}

.filter-group select,
.filter-group input[type="date"] {
    padding: 6px 10px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-on-dark);
    font-size: 13px;
}

.filter-group select option {
    background: var(--bg-header);
    color: var(--text-on-dark);
}
```

### 데이터 테이블

```css
.table-section {
    background: var(--bg-card);
    border-radius: var(--radius);
    padding: 20px 24px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    overflow-x: auto;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

.data-table thead th {
    text-align: left;
    padding: 10px 12px;
    border-bottom: 2px solid #dee2e6;
    color: var(--text-secondary);
    font-weight: 600;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    white-space: nowrap;
    user-select: none;
}

.data-table thead th:hover {
    color: var(--text-primary);
    background: #f8f9fa;
}

.data-table tbody td {
    padding: 10px 12px;
    border-bottom: 1px solid #f0f0f0;
}

.data-table tbody tr:hover {
    background: #f8f9fa;
}

.data-table tbody tr:last-child td {
    border-bottom: none;
}
```

### 반응형 디자인

```css
@media (max-width: 768px) {
    .dashboard-header {
        flex-direction: column;
        align-items: flex-start;
    }

    .kpi-row {
        grid-template-columns: repeat(2, 1fr);
    }

    .chart-row {
        grid-template-columns: 1fr;
    }

    .filters {
        flex-direction: column;
        align-items: flex-start;
    }
}

@media print {
    body { background: white; }
    .dashboard-container { max-width: none; }
    .filters { display: none; }
    .chart-container { break-inside: avoid; }
    .kpi-card { border: 1px solid #dee2e6; box-shadow: none; }
}
```

## 대규모 데이터셋의 성능 고려사항

### 데이터 크기 가이드라인

| 데이터 크기 | 접근 방식 |
|---|---|
| <1,000행 | HTML에 직접 포함. 완전한 인터랙티비티. |
| 1,000 - 10,000행 | HTML에 포함. 차트를 위해 사전 집계가 필요할 수 있음. |
| 10,000 - 100,000행 | 서버 측에서 사전 집계. 집계된 데이터만 포함. |
| >100,000행 | 클라이언트 측 대시보드에 적합하지 않음. BI 도구 사용 또는 페이지네이션. |

### 사전 집계 패턴

원시 데이터를 포함하고 브라우저에서 집계하는 대신:

```javascript
// 하지 마세요: 50,000개의 원시 행 포함
const RAW_DATA = [/* 50,000 rows */];

// 이렇게 하세요: 포함 전에 사전 집계
const CHART_DATA = {
    monthly_revenue: [
        { month: '2024-01', revenue: 150000, orders: 1200 },
        { month: '2024-02', revenue: 165000, orders: 1350 },
        // ... 50,000개 대신 12개 행
    ],
    top_products: [
        { product: 'Widget A', revenue: 45000 },
        // ... 10개 행
    ],
    kpis: {
        total_revenue: 1980000,
        total_orders: 15600,
        avg_order_value: 127,
    }
};
```

### 차트 성능

- 꺾은선 차트는 시리즈당 <500 데이터 포인트로 제한 (필요시 다운샘플링)
- 막대 차트는 <50 카테고리로 제한
- 산점도는 1,000포인트로 제한 (더 큰 데이터셋에는 샘플링 사용)
- 많은 차트가 있는 대시보드에서 애니메이션 비활성화: Chart.js 옵션에서 `animation: false`
- 필터 트리거 업데이트에는 `Chart.update()` 대신 `Chart.update('none')` 사용

### DOM 성능

- 데이터 테이블을 100-200개의 표시 행으로 제한. 더 많으면 페이지네이션 추가.
- 조정된 차트 업데이트에 `requestAnimationFrame` 사용
- 필터 변경 시 전체 DOM을 재구축하지 않음 -- 변경된 요소만 업데이트

```javascript
// 효율적인 테이블 페이지네이션
function renderTablePage(data, page, pageSize = 50) {
    const start = page * pageSize;
    const end = Math.min(start + pageSize, data.length);
    const pageData = data.slice(start, end);
    // pageData만 렌더링
    // 페이지네이션 컨트롤 표시: "1-50 of 2,340 표시 중"
}
```

## 예시

```
/build-dashboard 월별 매출 대시보드. 매출 추세, 상위 제품, 지역별 분석 포함. 데이터는 orders 테이블에 있음.
```

```
/build-dashboard 여기 지원 티켓 데이터가 있습니다 [CSV 붙여넣기]. 우선순위별 볼륨, 응답 시간 추세, 해결율을 보여주는 대시보드를 만들어주세요.
```

```
/build-dashboard MRR, 이탈률, 신규 고객, NPS를 보여주는 SaaS 회사용 경영진 대시보드 템플릿을 만들어주세요. 샘플 데이터를 사용하세요.
```

## 팁

- 대시보드는 완전히 독립형 HTML 파일입니다 -- 파일을 보내서 누구와도 공유 가능
- 실시간 대시보드의 경우 BI 도구에 연결하는 것을 고려하세요. 이 대시보드는 특정 시점의 스냅샷입니다
- 다른 스타일링을 위해 "다크 모드" 또는 "프레젠테이션 모드"를 요청할 수 있습니다
- 브랜드에 맞는 특정 색상 체계를 요청할 수 있습니다
