---
name: status-report
description: Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.
argument-hint: "[weekly | monthly | quarterly] [project or team]"
---

# /status-report

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

리더십이나 이해관계자를 위한 세련된 상태 보고서를 생성합니다. 리스크 매트릭스 프레임워크와 심각도 정의는 **risk-assessment** 스킬을 참고하세요.

## 사용법

```
/status-report $ARGUMENTS
```

## 출력

```markdown
## 상태 보고서: [프로젝트/팀] — [기간]
**작성자:** [이름] | **날짜:** [날짜]

### 요약
[3-4문장 개요 - 무엇이 정상 진행 중인지, 무엇이 주의가 필요한지, 주요 성과]

### 전체 상태: 🟢 정상 진행 / 🟡 위험 / 🔴 지연

### 핵심 지표
| 지표 | 목표 | 실제 | 추세 | 상태 |
|--------|--------|--------|-------|--------|
| [KPI] | [목표] | [실제] | [상승/하락/유지] | 🟢/🟡/🔴 |

### 이번 기간 성과
- [성과 1]
- [성과 2]

### 진행 중
| 항목 | 담당자 | 상태 | 예상 완료일 | 메모 |
|------|-------|--------|-----|-------|
| [항목] | [사람] | [상태] | [날짜] | [맥락] |

### 리스크와 이슈
| 리스크/이슈 | 영향 | 완화 방안 | 담당자 |
|------------|--------|------------|-------|
| [리스크] | [영향] | [무엇을 하고 있는지] | [누구] |

### 필요한 결정
| 결정 | 맥락 | 마감일 | 권고 조치 |
|----------|---------|----------|--------------------|
| [결정] | [왜 중요한지] | [언제] | [권고 사항] |

### 다음 기간 우선순위
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

## 연결 도구가 있을 경우

If **~~project tracker** is connected:
- 프로젝트 상태, 완료된 항목, 다가오는 마일스톤을 자동으로 가져옵니다.
- 위험 항목과 기한이 지난 작업을 식별합니다.

If **~~chat** is connected:
- 최근 팀 대화에서 포함할 결정과 블로커를 검색합니다.
- 완성된 보고서를 채널에 게시할지 제안합니다.

If **~~calendar** is connected:
- 보고 기간의 주요 회의와 결정을 참고합니다.

## 팁

1. **헤드라인으로 시작하세요** - 바쁜 리더는 첫 3줄을 읽습니다. 그 부분을 중요하게 만드세요.
2. **리스크는 솔직하게** - 문제를 일찍 드러내면 신뢰가 쌓입니다. 놀라움은 신뢰를 깎습니다.
3. **결정을 쉽게 만드세요** - 필요한 각 결정마다 맥락과 권고를 제시하세요.
