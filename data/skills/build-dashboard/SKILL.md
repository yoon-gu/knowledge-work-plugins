---
name: build-dashboard
description: 차트, 필터, 테이블을 사용하여 대화형 HTML 대시보드를 구축하세요. KPI 카드를 사용하여 전체 개요를 작성하거나, 쿼리 결과를 공유 가능한 독립형 보고서로 전환하거나, 팀 모니터링 스냅샷을 작성하거나, 브라우저에서 열 수 있는 하나의 파일에 필터가 포함된 여러 차트가 필요한 경우에 사용하세요.
argument-hint: "<description> [data source]"
---

# /build-dashboard - 대화형 대시보드 구축

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

차트, 필터, 테이블 및 전문적인 스타일을 갖춘 독립적인 대화형 HTML 대시보드를 구축하세요. 브라우저에서 직접 열립니다. 서버나 종속성이 필요하지 않습니다.

## 용법

```
/build-dashboard <description of dashboard> [data source]
```

## 작업흐름

### 1. 대시보드 요구 사항 이해

결정하다:

- **목적**: 전체 개요, 운영 모니터링, 심층 분석, 팀 보고
- **대상**: 이 대시보드를 누가 사용할 것인가?
- **주요 측정항목**: 가장 중요한 숫자는 무엇인가요?
- **측정기준**: 사용자가 무엇을 필터링하거나 분할할 수 있어야 합니까?
- **데이터 소스**: 라이브 쿼리, 붙여넣은 데이터, CSV 파일 또는 샘플 데이터

### 2. 데이터 수집

**데이터 웨어하우스가 연결된 경우:**
1. 필요한 데이터를 쿼리
2. HTML 파일 내에 결과를 JSON으로 포함

**데이터를 붙여넣거나 업로드한 경우:**
1. 데이터 구문 분석 및 정리
2. 대시보드에 JSON으로 포함

**데이터 없이 설명으로 작업하는 경우:**
1. 설명된 스키마와 일치하는 현실적인 샘플 데이터 세트 생성
2. 대시보드에서 샘플 데이터를 사용한다는 점을 참고하세요.
3. 실제 데이터 교환에 대한 지침 제공

### 3. 대시보드 레이아웃 디자인

표준 대시보드 레이아웃 패턴을 따르십시오.

```
┌──────────────────────────────────────────────────┐
│  Dashboard Title                    [Filters ▼]  │
├────────────┬────────────┬────────────┬───────────┤
│  KPI Card  │  KPI Card  │  KPI Card  │ KPI Card  │
├────────────┴────────────┼────────────┴───────────┤
│                         │                        │
│    Primary Chart        │   Secondary Chart      │
│    (largest area)       │                        │
│                         │                        │
├─────────────────────────┴────────────────────────┤
│                                                  │
│    Detail Table (sortable, scrollable)           │
│                                                  │
└──────────────────────────────────────────────────┘
```

**콘텐츠에 맞게 레이아웃을 조정하세요.**
- 헤드라인 번호 상단에 2~4개의 KPI 카드
- 추세 및 분석을 위한 중간 섹션의 1~3개 차트
- 드릴다운 데이터에 대한 하단의 선택적 세부정보 테이블
- 복잡성에 따라 헤더 또는 사이드바의 필터

### 4. HTML 대시보드 구축

아래 기본 템플릿을 사용하여 단일 독립형 HTML 파일을 생성합니다. 파일에는 다음이 포함됩니다.

**구조(HTML):**
- 시맨틱 HTML5 레이아웃
- CSS Grid 또는 Flexbox를 사용한 반응형 그리드
- 필터 컨트롤(드롭다운, 날짜 선택기, 토글)
- 값과 레이블이 포함된 KPI 카드
- 차트 컨테이너
- 정렬 가능한 헤더가 있는 데이터 테이블

**스타일링(CSS):**
- 전문적인 색상 구성(깨끗한 흰색, 회색, 데이터 강조 색상 포함)
- 미묘한 그림자가 있는 카드 기반 레이아웃
- 일관된 타이포그래피(빠른 로딩을 위한 시스템 글꼴)
- 다양한 화면 크기에서 작동하는 반응형 디자인
- 인쇄 친화적인 스타일

**상호작용성(자바스크립트):**
- 대화형 차트용 Chart.js(CDN을 통해 포함)
- 모든 차트와 표를 동시에 업데이트하는 필터 드롭다운
- 정렬 가능한 테이블 열
- 차트에 마우스를 올리면 도구 설명이 표시됩니다.
- 숫자 형식(쉼표, 통화, 백분율)

**데이터(내장형 JSON):**
- HTML에 JavaScript 변수로 직접 포함된 모든 데이터
- 외부 데이터 가져오기가 필요하지 않습니다.
- 대시보드는 완전히 오프라인으로 작동합니다.

### 5. 차트 유형 구현

모든 차트에는 Chart.js를 사용하세요. 일반적인 대시보드 차트 패턴:

- **선 차트**: 시계열 추세
- **막대형 차트**: 카테고리 비교
- **도넛 차트**: 구성(<6개 카테고리인 경우)
- **누적 막대**: 시간 경과에 따른 구성
- **혼합(막대 + 선)**: 비율 오버레이가 포함된 거래량

각 차트 유형에 대해 아래 Chart.js 통합 패턴을 사용하십시오.

### 6. 상호작용성 추가

드롭다운 필터, 날짜 범위 필터, 결합된 필터 논리, 정렬 가능한 표 및 차트 업데이트에 대해 아래의 필터 및 상호작용 구현 패턴을 사용하세요.

### 7. 저장하고 열기

1. 대시보드를 설명적인 이름(예: `sales_dashboard.html`)을 사용하여 HTML 파일로 저장합니다.
2. 사용자의 기본 브라우저에서 엽니다.
3. 올바르게 렌더링되는지 확인
4. 데이터 업데이트 또는 맞춤설정에 대한 지침 제공

---

## 기본 템플릿

모든 대시보드는 다음 구조를 따릅니다.

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
        /* Dashboard styles go here */
    </style>
</head>
<body>
    <div class="dashboard-container">
        <header class="dashboard-header">
            <h1>Dashboard Title</h1>
            <div class="filters">
                <!-- Filter controls -->
            </div>
        </header>

        <section class="kpi-row">
            <!-- KPI cards -->
        </section>

        <section class="chart-row">
            <!-- Chart containers -->
        </section>

        <section class="table-section">
            <!-- Data table -->
        </section>

        <footer class="dashboard-footer">
            <span>Data as of: <span id="data-date"></span></span>
        </footer>
    </div>

    <script>
        // Embedded data
        const DATA = [];

        // Dashboard logic
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
                // Filter logic
                this.filteredData = this.rawData.filter(row => {
                    // Apply each active filter
                    return true; // placeholder
                });
                this.renderKPIs();
                this.updateCharts();
                this.renderTable();
            }

            // ... methods for each section
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

    // Format the value
    el.textContent = formatValue(value, format);

    // Calculate and display change
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

### 꺾은선형 차트

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
        // Multiple datasets
        newData.forEach((data, i) => {
            chart.data.datasets[i].data = data;
        });
    } else {
        chart.data.datasets[0].data = newData;
    }

    chart.update('none'); // 'none' disables animation for instant update
}
```

## 필터 및 상호작용 구현

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

    // Keep the "All" option, add unique values
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

### 기간 필터

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

### 결합 필터 논리

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

        // Header
        html += '<thead><tr>';
        columns.forEach(col => {
            const arrow = sortCol === col.field
                ? (sortDir === 'asc' ? ' ▲' : ' ▼')
                : '';
            html += `<th onclick="sortTable('${col.field}')" style="cursor:pointer">${col.label}${arrow}</th>`;
        });
        html += '</tr></thead>';

        // Body
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

## 대시보드용 CSS 스타일링

### 컬러 시스템

```css
:root {
    /* Background layers */
    --bg-primary: #f8f9fa;
    --bg-card: #ffffff;
    --bg-header: #1a1a2e;

    /* Text */
    --text-primary: #212529;
    --text-secondary: #6c757d;
    --text-on-dark: #ffffff;

    /* Accent colors for data */
    --color-1: #4C72B0;
    --color-2: #DD8452;
    --color-3: #55A868;
    --color-4: #C44E52;
    --color-5: #8172B3;
    --color-6: #937860;

    /* Status colors */
    --positive: #28a745;
    --negative: #dc3545;
    --neutral: #6c757d;

    /* Spacing */
    --gap: 16px;
    --radius: 8px;
}
```

### 공들여 나열한 것

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

## 대규모 데이터 세트에 대한 성능 고려 사항

### 데이터 크기 지침

| 데이터 크기 | 접근하다 |
|---|---|
| 행 <1,000개 | HTML에 직접 삽입하세요. 완전한 상호작용. |
| 1,000 - 10,000행 | HTML에 삽입하세요. 차트를 위해 사전 집계가 필요할 수 있습니다. |
| 10,000 - 100,000행 | 서버 측 사전 집계. 집계된 데이터만 삽입하세요. |
| >100,000행 | 클라이언트측 대시보드에는 적합하지 않습니다. BI 도구를 사용하거나 페이지를 매깁니다. |

### 사전 집계 패턴

원시 데이터를 삽입하고 브라우저에 집계하는 대신:

```javascript
// DON'T: embed 50,000 raw rows
const RAW_DATA = [/* 50,000 rows */];

// DO: pre-aggregate before embedding
const CHART_DATA = {
    monthly_revenue: [
        { month: '2024-01', revenue: 150000, orders: 1200 },
        { month: '2024-02', revenue: 165000, orders: 1350 },
        // ... 12 rows instead of 50,000
    ],
    top_products: [
        { product: 'Widget A', revenue: 45000 },
        // ... 10 rows
    ],
    kpis: {
        total_revenue: 1980000,
        total_orders: 15600,
        avg_order_value: 127,
    }
};
```

### 차트 성과

- 꺾은선형 차트를 계열당 데이터 포인트 500개 미만으로 제한(필요한 경우 다운샘플링)
- 막대 차트를 50개 미만의 카테고리로 제한
- 산점도의 경우 최대 1,000개 지점으로 제한(더 큰 데이터세트에는 샘플링 사용)
- 차트가 많은 대시보드에 대한 애니메이션 비활성화: Chart.js 옵션의 `animation: false`
- 필터로 트리거되는 업데이트에는 `Chart.update()` 대신 `Chart.update('none')`을 사용하세요.

### DOM 성능

- 데이터 테이블을 표시 가능한 행 100~200개로 제한합니다. 더 많은 페이지 매김을 추가하세요.
- 좌표 업데이트에는 `requestAnimationFrame`을(를) 사용하세요
- 필터 변경 시 전체 DOM을 다시 빌드하지 마세요. 변경된 요소만 업데이트하세요.

```javascript
// Efficient table pagination
function renderTablePage(data, page, pageSize = 50) {
    const start = page * pageSize;
    const end = Math.min(start + pageSize, data.length);
    const pageData = data.slice(start, end);
    // Render only pageData
    // Show pagination controls: "Showing 1-50 of 2,340"
}
```

## 예

```
/build-dashboard Monthly sales dashboard with revenue trend, top products, and regional breakdown. Data is in the orders table.
```

```
/build-dashboard Here's our support ticket data [pastes CSV]. Build a dashboard showing volume by priority, response time trends, and resolution rates.
```

```
/build-dashboard Create a template executive dashboard for a SaaS company showing MRR, churn, new customers, and NPS. Use sample data.
```

## 팁

- 대시보드는 완전히 독립적인 HTML 파일입니다. 파일을 보내 누구와도 공유할 수 있습니다.
- 실시간 대시보드의 경우 대신 BI 도구에 연결하는 것을 고려해 보세요. 이 대시보드는 특정 시점의 스냅샷입니다.
- 다른 스타일을 원하시면 "dark mode" 또는 "presentation mode"을(를) 요청하세요
- 귀하의 브랜드에 맞는 특정 색상 구성을 요청할 수 있습니다
