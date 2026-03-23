---
name: discover-brand
description: >
  이 스킬은 엔터프라이즈 플랫폼(Notion, Confluence, Google Drive, Box, SharePoint,
  Figma, Gong, Granola, Slack) 전반에서 브랜드 자료를 자율적으로 찾도록 조율합니다.
  사용자가 "brand materials 찾기", "brand documents 찾기", "brand guidelines 검색",
  "brand content 감사", "우리에게 어떤 브랜드 자료가 있나", "style guide 찾기",
  "brand docs는 어디 있나", "style guide가 있나", "brand voice 찾기",
  "brand content audit", "brand assets 찾기" 같은 요청을 할 때 사용합니다.
---

# 브랜드 탐색

엔터프라이즈 플랫폼 전반에서 브랜드 자료를 자율적으로 찾도록 조율합니다.
이 스킬은 discover-brand 에이전트를 조정해 연결된 플랫폼(Notion, Confluence,
Google Drive, Box, Microsoft 365, Figma, Gong, Granola, Slack)을 검색하고,
출처를 선별하며, 열린 질문이 포함된 구조화된 탐색 보고서를 작성합니다.

## 탐색 워크플로

### 0. 사용자 안내

시작하기 전에 무엇이 일어날지 간단히 설명해 사용자가 기대할 수 있게 합니다.

"Here's how brand discovery works:

1. **검색** — 연결된 플랫폼(Notion, Google Drive, Slack 등)에서 스타일 가이드, 피치 덱, 템플릿, 전사 기록 등 브랜드 관련 자료를 찾습니다.
2. **분석** — 발견한 자료를 분류하고 순위화한 뒤, 가장 좋은 출처를 추려서 발견 내용, 충돌, 열린 질문이 포함된 보고서를 만듭니다.
3. **가이드 생성** — 보고서를 검토한 뒤에는 결과를 바탕으로 구조화된 브랜드 보이스 가이드 문서를 만들 수 있습니다.
4. **저장** — 가이드가 승인되면 작업 폴더의 `.claude/brand-voice-guidelines.md`에 저장합니다. 그 전에는 아무 것도 쓰지 않습니다.

검색은 연결된 플랫폼 수에 따라 보통 몇 분 걸립니다. 시작할 준비가 되셨나요?"

진행하기 전에 사용자의 확인을 기다립니다. 과정에 대해 질문이 있으면 먼저 답합니다.

### 1. 설정 확인

`.claude/brand-voice.local.md`가 있으면 읽습니다. 다음을 추출합니다.
- Company name
- Which platforms are enabled (notion, confluence, google-drive, box, microsoft-365, figma, gong, granola, slack)
- Search depth preference (standard or deep)
- Max sources limit
- Any known brand material locations listed under "Known Brand Materials"

설정 파일이 없으면 연결된 모든 플랫폼과 standard search depth로 진행합니다.

### 2. 플랫폼 커버리지 검증

범위를 확정하기 전에 실제로 어떤 플랫폼이 연결되어 있는지 확인하고 분류합니다.

**문서 플랫폼**(브랜드 가이드, 스타일 가이드, 템플릿, 덱이 있는 곳):
- Notion, Confluence, Google Drive, Box, Microsoft 365 (SharePoint/OneDrive)

**보조 플랫폼**(패턴 파악에는 유용하지만 브랜드 문서가 저장되는 곳은 아님):
- Slack, Gong, Granola, Figma

Apply these rules:

1. **문서 플랫폼이 0개라면**: **중단합니다.** 사용자에게 다음을 말합니다. "문서 저장 플랫폼(Google Drive, SharePoint, Notion, Confluence, Box)이 연결되어 있지 않습니다. 브랜드 가이드와 스타일 가이드는 거의 항상 이 중 하나에 있습니다. 탐색을 실행하기 전에 최소 하나를 연결해 주세요. Gong/Granola/Slack 전사 기록은 유용한 보조 자료이지만, 정식 브랜드 문서를 담고 있을 가능성은 낮습니다."

2. **Google Drive도 없고 Microsoft 365도 없고 Box도 없다면**: **경고하되 진행합니다.** "주요 파일 저장 플랫폼(Google Drive, SharePoint, Box)이 하나도 연결되어 있지 않습니다. 브랜드 문서는 이런 플랫폼에 있는 경우가 많습니다. 탐색은 [연결된 플랫폼]으로 진행되지만, 결과에 큰 공백이 있을 수 있습니다. Google Drive나 SharePoint 연결을 고려하세요."

3. **전체적으로 한 플랫폼만 연결되어 있다면**: **경고하되 진행합니다.** "현재 [platform]만 연결되어 있습니다. 탐색은 출처 교차 검증을 위해 2개 이상의 플랫폼에서 가장 잘 작동합니다. 단일 플랫폼 결과는 신뢰도 점수가 더 낮습니다."

### 3. 사용자와 범위 확인

탐색을 시작하기 전에 다음을 확인합니다.
- Which platforms to search (default: all connected)
- Whether to include conversation transcripts (Gong, Granola) or just documents
- Any known locations to prioritize

짧게 묻습니다. 설문지가 아니라 한 번의 질문이어야 합니다.

### 4. Discover-Brand 에이전트에 위임

Task 도구를 통해 discover-brand 에이전트를 실행합니다. 다음을 제공합니다.
- Company name (from settings or user input)
- Enabled platforms
- Search depth
- Any known URLs or locations to check first

에이전트는 4단계 탐색 알고리즘을 자율적으로 실행합니다.
1. **Broad Discovery** — parallel searches across platforms
2. **Source Triage** — categorize and rank sources
3. **Deep Fetch** — retrieve and extract from top sources
4. **Discovery Report** — structured output with open questions

### 5. 탐색 보고서 제시

에이전트가 돌아오면 보고서를 요약과 함께 사용자에게 제시합니다.
- Total sources found and analyzed
- Key brand elements discovered
- Any conflicts between sources
- Open questions requiring team input

### 6. 다음 단계 제안

After presenting the report, offer:
1. **지금 가이드 생성** — 탐색 보고서를 입력으로 사용해 `/brand-voice:generate-guidelines`로 이어갑니다
2. **열린 질문 먼저 해결** — 생성 전에 높은 우선순위 질문을 먼저 풀어 갑니다
3. **보고서 저장** — 탐색 보고서를 Notion 또는 로컬 파일로 저장합니다
4. **검색 확장** — 커버리지가 낮다면 추가 플랫폼을 더 깊게 검색합니다

## 열린 질문

열린 질문은 탐색 에이전트가 해결하지 못하는 모호성을 만났을 때 생깁니다.
- Conflicting documents (e.g., 2023 style guide vs. 2024 brand update)
- Missing critical sections (e.g., no social media guidelines found)
- Inconsistent terminology across platforms

모든 열린 질문에는 에이전트 권고가 포함됩니다. 질문은 막다른 길이 아니라 "확인하거나 변경"할 수 있는 형태로 제시합니다.

## 다른 스킬과의 연계

- **가이드라인 생성**: 탐색 보고서는 Task 도구를 통해 discover-brand 에이전트가 반환합니다. 사용자가 직접 출처를 모을 필요 없이 이를 guideline-generation 스킬의 구조화된 입력으로 바로 넘깁니다.
- **브랜드 보이스 적용**: 탐색으로 가이드가 생성되면, 적용 단계는 이를 자동으로 사용합니다.

## 오류 처리

- 플랫폼이 하나도 연결되어 있지 않다면, 플러그인이 지원하는 플랫폼과 연결 방법을 사용자에게 알려 줍니다.
- 모든 검색 결과가 비어 있으면 탐색을 "low coverage"로 표시하고, 사용자가 문서를 직접 제공하거나 플랫폼 연결을 확인하라고 안내합니다.
- 플랫폼은 연결되어 있지만 권한 오류가 나면 그 공백을 기록하고 다른 플랫폼으로 계속 진행합니다.

## 참고 파일

자세한 탐색 패턴과 알고리즘은 다음을 참고하세요.

- **`references/search-strategies.md`** — 플랫폼별 검색 쿼리, 플랫폼별 쿼리 패턴, 탐색 커버리지를 높이는 팁
- **`references/source-ranking.md`** — 출처 범주 정의, 순위 알고리즘 가중치, 선별 기준
