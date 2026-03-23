---
name: create-viz
description: Python을 사용하여 출판 수준의 시각화를 만드세요. 쿼리 결과 또는 DataFrame을 차트로 변환하거나, 추세 또는 비교에 적합한 차트 유형을 선택하거나, 보고서 또는 프리젠테이션을 위한 플롯을 생성하거나, 마우스 오버 및 확대/축소 기능이 있는 대화형 차트가 필요한 경우에 사용하세요.
argument-hint: "<data source> [chart type]"
---

# /create-viz - 시각화 만들기

> 익숙하지 않은 자리 표시자가 있거나 어떤 도구가 연결되어 있는지 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)을 참조하세요.

Python을 사용하여 출판 품질의 데이터 시각화를 만듭니다. 명확성, 정확성 및 디자인을 위한 모범 사례를 사용하여 데이터에서 차트를 생성합니다.

## 용법

```
/create-viz <data source> [chart type] [additional instructions]
```

## 작업흐름

### 1. 요청 이해

결정하다:

- **데이터 소스**: 쿼리 결과, 붙여넣은 데이터, CSV/Excel 파일 또는 쿼리할 데이터
- **차트 유형**: 명시적으로 요청되었거나 권장되어야 함
- **목적**: 탐색, 프리젠테이션, 보고서, 대시보드 구성요소
- **대상**: 기술팀, 임원, 외부 이해관계자

### 2. 데이터 가져오기

**데이터 웨어하우스가 연결되어 있고 데이터를 쿼리해야 하는 경우:**
1. 쿼리 작성 및 실행
2. Pandas DataFrame에 결과 로드

**데이터를 붙여넣거나 업로드한 경우:**
1. 데이터를 Pandas DataFrame으로 구문 분석합니다.
2. 필요에 따라 정리 및 준비(유형 변환, Null 처리)

**데이터가 대화의 이전 분석에서 나온 경우:**
1. 기존 데이터 참조

### 3. 차트 종류 선택

사용자가 차트 유형을 지정하지 않은 경우 데이터와 질문을 기반으로 차트 유형을 추천하세요.

| 데이터 관계 | 권장 차트 |
|---|---|
| 시간 경과에 따른 추세 | 꺾은선형 차트 |
| 카테고리별 비교 | 막대 차트(범주가 많은 경우 가로) |
| 부분에서 전체 구성 | 누적 막대형 또는 영역형 차트(범주가 6개 미만인 경우를 제외하고 원형 차트 사용 안 함) |
| 가치의 분배 | 히스토그램 또는 상자 그림 |
| 두 변수 사이의 상관관계 | 산점도 |
| 시간 경과에 따른 두 변수 비교 | 이중 축 선 또는 그룹화된 막대 |
| 지리 데이터 | 등치 지도 |
| 순위 | 수평 막대 차트 |
| 흐름 또는 프로세스 | 생키 다이어그램 |
| 관계 매트릭스 | 히트맵 |

사용자가 지정하지 않은 경우 권장사항을 간략하게 설명하세요.

### 4. 시각화 생성

필요에 따라 다음 라이브러리 중 하나를 사용하여 Python 코드를 작성합니다.

- **matplotlib + seaborn**: 정적 출판 품질 차트에 가장 적합합니다. 기본 선택.
- **plotly**: 대화형 차트 또는 사용자가 상호작용을 요청할 때 가장 적합합니다.

**코드 요구 사항:**

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set professional style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Create figure with appropriate size
fig, ax = plt.subplots(figsize=(10, 6))

# [chart-specific code]

# Always include:
ax.set_title('Clear, Descriptive Title', fontsize=14, fontweight='bold')
ax.set_xlabel('X-Axis Label', fontsize=11)
ax.set_ylabel('Y-Axis Label', fontsize=11)

# Format numbers appropriately
# - Percentages: '45.2%' not '0.452'
# - Currency: '$1.2M' not '1200000'
# - Large numbers: '2.3K' or '1.5M' not '2300' or '1500000'

# Remove chart junk
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('chart_name.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 5. 디자인 모범 사례 적용

**색상:**
- 일관되고 색맹 친화적인 팔레트를 사용하세요
- 의미 있게 색상을 사용하십시오(장식적인 것이 아님).
- 대비되는 색상으로 주요 데이터 포인트 또는 추세를 강조하세요.
- 덜 중요한 참조 데이터를 회색으로 표시

**타이포그래피:**
- 측정항목뿐만 아니라 통계를 설명하는 제목(예: "Revenue by Month"이 아닌 "Revenue grew 23% YoY")
- 읽을 수 있는 축 레이블(피할 수 있는 경우 90도 회전하지 않음)
- 명확성을 추가할 때 핵심 사항에 대한 데이터 레이블

**공들여 나열한 것:**
- 적절한 공백과 여백
- 데이터를 모호하게 하지 않는 범례 배치
- 자연스러운 순서가 없는 한 카테고리를 값별로 정렬합니다(알파벳순 아님).

**정확성:**
- 막대 차트의 경우 Y축은 0에서 시작합니다.
- 명확한 표기 없이 오해의 소지가 있는 축이 끊어지지 않습니다.
- 패널을 비교할 때 일관된 척도
- 적절한 정밀도(소수점 10자리 표시 안 함)

### 6. 저장하고 발표하기

1. 설명적인 이름을 사용하여 차트를 PNG 파일로 저장합니다.
2. 사용자에게 차트를 표시
3. 수정할 수 있도록 사용된 코드를 제공하세요.
4. 변형 제안(다양한 차트 유형, 다양한 그룹화, 확대된 기간)

## 예

```
/create-viz Show monthly revenue for the last 12 months as a line chart with the trend highlighted
```

```
/create-viz Here's our NPS data by product: [pastes data]. Create a horizontal bar chart ranking products by score.
```

```
/create-viz Query the orders table and create a heatmap of order volume by day-of-week and hour
```

## 팁

- 대화형 차트(호버, 확대/축소, 필터)를 원할 경우 "interactive"을 언급하면 ​​Claude가 플롯을 사용합니다.
- 더 큰 글꼴과 더 높은 대비가 필요한 경우 "presentation"을 지정하세요.
- 한 번에 여러 차트를 요청할 수 있습니다(예: "create a 2x2 grid of charts showing...").
- 차트는 현재 디렉터리에 PNG 파일로 저장됩니다.
