---
name: data-visualization
description: Python(matplotlib, seaborn, plotly)으로 효과적인 데이터 시각화를 만듭니다. 차트를 만들 때, 데이터셋에 맞는 차트 유형을 고를 때, 출판용 품질의 그림을 만들 때, 또는 접근성과 색채 이론 같은 디자인 원칙을 적용할 때 사용합니다.
user-invocable: false
---

# 데이터 시각화 스킬

효과적인 데이터 시각화를 위한 차트 선택 가이드, Python 시각화 코드 패턴, 디자인 원칙, 접근성 고려 사항입니다.

## 차트 선택 가이드

### 데이터 관계에 따라 선택하기

| 보여주려는 것 | 가장 좋은 차트 | 대안 |
|---|---|---|
| **시간에 따른 추세** | 선 그래프 | 누적 또는 구성 비중을 보여줄 때는 면적 그래프 |
| **범주 간 비교** | 세로 막대 그래프 | 범주가 많으면 가로 막대, 롤리팝 차트 |
| **순위** | 가로 막대 그래프 | 도트 플롯, 슬로프 차트(두 기간 비교) |
| **부분과 전체의 구성** | 누적 막대 그래프 | 트리맵(계층형), 와플 차트 |
| **시간에 따른 구성** | 누적 면적 그래프 | 비율에 초점을 둘 때는 100% 누적 막대 |
| **분포** | 히스토그램 | 박스 플롯(그룹 비교), 바이올린 플롯, 스트립 플롯 |
| **상관관계(변수 2개)** | 산점도 | 버블 차트(3번째 변수를 크기로 추가) |
| **상관관계(여러 변수)** | 히트맵(상관행렬) | 페어 플롯 |
| **지리 패턴** | 코로플레스 지도 | 버블 맵, 헥스 맵 |
| **흐름 / 프로세스** | 생키 다이어그램 | 퍼널 차트(순차 단계) |
| **관계 네트워크** | 네트워크 그래프 | 코드 다이어그램 |
| **목표 대비 성과** | 불릿 차트 | 게이지(단일 KPI 전용) |
| **여러 KPI를 한 번에** | 스몰 멀티플 | 차트를 분리한 대시보드 |

### 특정 차트를 쓰지 말아야 할 때

- **원형 차트**: 범주가 6개 미만이고 정확한 비율보다 대략적 비교가 덜 중요한 경우가 아니면 피하세요. 사람은 각도 비교를 잘 못합니다. 대신 막대 그래프를 쓰세요.
- **3D 차트**: 절대 쓰지 마세요. 인식을 왜곡하고 정보를 더하지 않습니다.
- **이중 축 차트**: 신중하게 사용하세요. 상관관계를 암시해 오해를 부를 수 있습니다. 사용한다면 양쪽 축을 분명히 라벨링하세요.
- **누적 막대(범주가 많을 때)**: 가운데 구간 비교가 어렵습니다. 대신 스몰 멀티플이나 그룹 막대를 쓰세요.
- **도넛 차트**: 원형 차트보다 조금 낫지만 근본적인 문제는 같습니다. 많아야 단일 KPI 표시용으로만 쓰세요.

## Python 시각화 코드 패턴

### 설정과 스타일

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd
import numpy as np

# 전문적인 스타일 설정
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
})

# 색각 이상 친화 팔레트
PALETTE_CATEGORICAL = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3', '#937860']
PALETTE_SEQUENTIAL = 'YlOrRd'
PALETTE_DIVERGING = 'RdBu_r'
```

### 선 그래프(시계열)

```python
fig, ax = plt.subplots(figsize=(10, 6))

for label, group in df.groupby('category'):
    ax.plot(group['date'], group['value'], label=label, linewidth=2)

ax.set_title('Metric Trend by Category', fontweight='bold')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend(loc='upper left', frameon=True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# x축 날짜 형식 지정
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig('trend_chart.png', dpi=150, bbox_inches='tight')
```

### 막대 그래프(비교)

```python
fig, ax = plt.subplots(figsize=(10, 6))

# 읽기 쉽도록 값순 정렬
df_sorted = df.sort_values('metric', ascending=True)

bars = ax.barh(df_sorted['category'], df_sorted['metric'], color=PALETTE_CATEGORICAL[0])

# 값 레이블 추가
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width:,.0f}', ha='left', va='center', fontsize=10)

ax.set_title('Metric by Category (Ranked)', fontweight='bold')
ax.set_xlabel('Metric Value')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('bar_chart.png', dpi=150, bbox_inches='tight')
```

### 히스토그램(분포)

```python
fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(df['value'], bins=30, color=PALETTE_CATEGORICAL[0], edgecolor='white', alpha=0.8)

# 평균과 중앙값 선 추가
mean_val = df['value'].mean()
median_val = df['value'].median()
ax.axvline(mean_val, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_val:,.1f}')
ax.axvline(median_val, color='green', linestyle='--', linewidth=1.5, label=f'Median: {median_val:,.1f}')

ax.set_title('Distribution of Values', fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('histogram.png', dpi=150, bbox_inches='tight')
```

### 히트맵

```python
fig, ax = plt.subplots(figsize=(10, 8))

# 히트맵 형식으로 피벗
pivot = df.pivot_table(index='row_dim', columns='col_dim', values='metric', aggfunc='sum')

sns.heatmap(pivot, annot=True, fmt=',.0f', cmap='YlOrRd',
            linewidths=0.5, ax=ax, cbar_kws={'label': 'Metric Value'})

ax.set_title('Metric by Row Dimension and Column Dimension', fontweight='bold')
ax.set_xlabel('Column Dimension')
ax.set_ylabel('Row Dimension')

plt.tight_layout()
plt.savefig('heatmap.png', dpi=150, bbox_inches='tight')
```

### 스몰 멀티플

```python
categories = df['category'].unique()
n_cats = len(categories)
n_cols = min(3, n_cats)
n_rows = (n_cats + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows), sharex=True, sharey=True)
axes = axes.flatten() if n_cats > 1 else [axes]

for i, cat in enumerate(categories):
    ax = axes[i]
    subset = df[df['category'] == cat]
    ax.plot(subset['date'], subset['value'], color=PALETTE_CATEGORICAL[i % len(PALETTE_CATEGORICAL)])
    ax.set_title(cat, fontsize=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# 빈 서브플롯 숨기기
for j in range(i+1, len(axes)):
    axes[j].set_visible(False)

fig.suptitle('Trends by Category', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('small_multiples.png', dpi=150, bbox_inches='tight')
```

### 숫자 서식 도우미

```python
def format_number(val, format_type='number'):
    """차트 레이블용 숫자 서식 지정."""
    if format_type == 'currency':
        if abs(val) >= 1e9:
            return f'${val/1e9:.1f}B'
        elif abs(val) >= 1e6:
            return f'${val/1e6:.1f}M'
        elif abs(val) >= 1e3:
            return f'${val/1e3:.1f}K'
        else:
            return f'${val:,.0f}'
    elif format_type == 'percent':
        return f'{val:.1f}%'
    elif format_type == 'number':
        if abs(val) >= 1e9:
            return f'{val/1e9:.1f}B'
        elif abs(val) >= 1e6:
            return f'{val/1e6:.1f}M'
        elif abs(val) >= 1e3:
            return f'{val/1e3:.1f}K'
        else:
            return f'{val:,.0f}'
    return str(val)

# 축 포맷터와 함께 사용
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format_number(x, 'currency')))
```

### Plotly로 만드는 인터랙티브 차트

```python
import plotly.express as px
import plotly.graph_objects as go

# 간단한 인터랙티브 선 그래프
fig = px.line(df, x='date', y='value', color='category',
              title='Interactive Metric Trend',
              labels={'value': 'Metric Value', 'date': 'Date'})
fig.update_layout(hovermode='x unified')
fig.write_html('interactive_chart.html')
fig.show()

# hover 데이터가 있는 인터랙티브 산점도
fig = px.scatter(df, x='metric_a', y='metric_b', color='category',
                 size='size_metric', hover_data=['name', 'detail_field'],
                 title='Correlation Analysis')
fig.show()
```

## 디자인 원칙

### 색

- **색은 목적 있게 사용**: 색은 데이터를 인코딩해야지 장식이 되어서는 안 됩니다
- **이야기를 강조**: 핵심 인사이트에는 밝은 강조색을 쓰고, 나머지는 회색으로 둡니다
- **순차 데이터**: 정렬된 값에는 단일 색조의 그라데이션(연한색에서 진한색)을 씁니다
- **분기형 데이터**: 의미 있는 중심값이 있으면 두 색조와 중립 중간값을 쓰는 그라데이션을 사용합니다
- **범주형 데이터**: 서로 다른 색조를 사용하되, 6-8개를 넘으면 혼란스러워집니다
- **빨강/초록만 쓰지 않기**: 남성의 8%는 적록 색각 이상입니다. 파랑/주황을 기본 조합으로 쓰세요

### 타이포그래피

- **제목은 인사이트를 말해야 함**: "Revenue grew 23% YoY"가 "Revenue by Month"보다 낫습니다
- **부제는 맥락을 더함**: 날짜 범위, 적용한 필터, 데이터 소스
- **축 레이블은 읽기 쉬워야 함**: 가능하면 90도로 돌리지 말고, 짧게 하거나 줄바꿈하세요
- **데이터 레이블은 정밀도를 높임**: 모든 막대가 아니라 핵심 포인트에만 사용하세요
- **주석은 강조를 돕는다**: 텍스트 주석으로 특정 지점을 짚어 주세요

### 레이아웃

- **차트 잡음을 줄이기**: 정보를 담지 않는 격자선, 테두리, 배경을 제거하세요
- **의미 있게 정렬**: 자연스러운 순서(월, 단계)가 없다면 범주는 알파벳이 아니라 값순으로 정렬하세요
- **적절한 종횡비**: 시계열은 세로보다 가로가 넓어야 합니다(3:1~2:1). 비교 차트는 더 정사각형이어도 됩니다
- **여백은 좋다**: 차트를 빽빽하게 넣지 마세요. 각 시각화에 숨 쉴 공간을 주세요

### 정확성

- **막대 그래프는 0에서 시작**: 항상 그래야 합니다. 95에서 100까지의 막대는 5% 차이를 과장합니다
- **선 그래프는 0이 아닌 기준선도 가능**: 변동 범위가 의미 있을 때는 괜찮습니다
- **패널 간 스케일 통일**: 여러 차트를 비교할 때는 같은 축 범위를 쓰세요
- **불확실성 표시**: 데이터가 불확실하면 오차막대, 신뢰구간, 범위를 보여 주세요
- **축에 라벨 달기**: 숫자가 무엇을 뜻하는지 독자가 추측하게 만들지 마세요

## 접근성 고려 사항

### 색각 이상

- 데이터 시리즈를 구분할 때 색에만 의존하지 마세요
- 패턴 채우기, 다른 선 스타일(실선, 점선, 점선), 직접 레이블을 추가하세요
- 색각 이상 시뮬레이터(Coblis, Sim Daltonism 등)로 테스트하세요
- 색각 이상 친화 팔레트 `sns.color_palette("colorblind")`를 사용하세요

### 스크린 리더

- 차트의 핵심 발견을 설명하는 대체 텍스트를 넣으세요
- 시각화와 함께 데이터 표 대안을 제공하세요
- 의미 있는 제목과 레이블을 사용하세요

### 일반 접근성

- 데이터 요소와 배경 사이에 충분한 대비를 두세요
- 텍스트 크기는 레이블 최소 10pt, 제목 12pt를 권장합니다
- 공간 위치만으로 정보를 전달하지 마세요(레이블을 추가하세요)
- 인쇄를 고려하세요. 흑백에서도 차트가 잘 작동하나요?

### 접근성 체크리스트

시각화를 공유하기 전에:
- [ ] 색 없이도 차트가 작동합니다(패턴, 레이블, 선 스타일로 시리즈를 구분)
- [ ] 기본 확대 수준에서 텍스트가 읽힙니다
- [ ] 제목은 데이터가 아니라 인사이트를 설명합니다
- [ ] 축에 단위가 표시되어 있습니다
- [ ] 범례가 명확하고 데이터를 가리지 않습니다
- [ ] 데이터 소스와 날짜 범위가 표시되어 있습니다
