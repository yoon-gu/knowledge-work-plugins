---
name: scientific-problem-selection
description: This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".
---

# 과학적 문제 선택 스킬

Fischbach & Walsh의 "Problem choice and decision trees in science and engineering" (Cell, 2024)에 기반한 체계적 과학적 문제 선택을 위한 대화형 프레임워크입니다.

## 시작하기

사용자에게 세 가지 진입점을 제시합니다:

**1) 새 프로젝트를 위한 아이디어 발표** — 함께 구체화하기 위해

**2) 현재 프로젝트의 문제 공유** — 함께 해결하기 위해

**3) 전략적 질문하기** — 의사결정 트리를 함께 탐색하기 위해

이 대화형 진입점은 과학자들이 현재 위치에서 출발하며 협력적인 분위기를 조성합니다.

---

## 옵션 1: 아이디어 발표

### 초기 프롬프트
질문: **"아이디어의 짧은 버전을 알려주세요 (1-2문장)."**

### 응답 접근 방식
사용자가 아이디어를 공유한 후, 이해를 보여주는 간단한 요약(한 문단 이하)을 반환합니다. 연구의 일반적 영역을 언급하고 핵심을 강조하는 방식으로 아이디어를 재구성하여 정렬과 세부사항 탐구 준비가 되었음을 보여줍니다.

### 후속 프롬프트
그런 다음 더 자세한 내용을 요청합니다: "이제 좀 더 자세히 알려주세요. 간략하게라도, 확신이 없는 부분도 괜찮습니다:
1. 정확히 무엇을 하고 싶은지
2. 현재 어떻게 할 계획인지
3. 성공하면 왜 중요한 일이 되는지
4. 주요 리스크가 무엇이라고 생각하는지"

### 워크플로
이후 문제 선택과 평가의 초기 단계를 안내합니다:
- **스킬 1: 직관 펌프** - 아이디어를 다듬고 강화
- **스킬 2: 리스크 평가** - 프로젝트 리스크 식별 및 관리
- **스킬 3: 최적화 함수** - 성공 지표 정의
- **스킬 4: 파라미터 전략** - 고정할 것과 유연하게 유지할 것 결정

자세한 안내는 `references/01-intuition-pumps.md`, `references/02-risk-assessment.md`, `references/03-optimization-function.md`, `references/04-parameter-strategy.md`를 참조하세요.

---

## 옵션 2: 문제 해결

### 초기 프롬프트
질문: **"문제의 짧은 버전을 알려주세요 (1-2문장 또는 쉽게 설명할 수 있는 만큼)."**

### 응답 접근 방식
사용자가 문제를 공유한 후, 이해를 보여주는 간단한 요약(한 문단 이하)을 반환합니다. 문제가 발생한 프로젝트의 맥락을 언급하고 핵심 본질을 강조하는 방식으로 문제를 재구성하여 상황이 이해되었음을 보여줍니다. 또한 논의해야 할 중요한 추가 질문을 제기합니다.

### 후속 프롬프트
그런 다음 질문합니다: "이제 좀 더 자세히 알려주세요. 간략하게라도:
1. 프로젝트의 전체 목표 (이전에 논의하지 않았다면)
2. 정확히 무엇이 잘못되었는지
3. 현재 해결 아이디어"

### 워크플로
이후 문제 해결과 의사결정 트리 탐색을 안내합니다:
- **스킬 5: 의사결정 트리 탐색** - 결정 포인트를 계획하고 실행과 전략적 사고 사이를 탐색
- **스킬 4: 파라미터 전략** - 한 번에 하나의 파라미터를 고정하고 나머지는 유동적으로 유지
- **스킬 6: 역경 대응** - 문제를 성장의 기회로 프레이밍
- **스킬 7: 문제 반전** - 장애물을 우회하는 전략

문제의 쉬운 해결 여부와 관계없이 유용할 수 있는 해결 방법을 항상 포함합니다.

자세한 안내는 `references/05-decision-tree.md`, `references/06-adversity-planning.md`, `references/07-problem-inversion.md`, `references/04-parameter-strategy.md`를 참조하세요.

---

## 옵션 3: 전략적 질문

### 초기 프롬프트
질문: **"질문의 짧은 버전을 알려주세요 (1-2문장)."**

### 응답 접근 방식
사용자가 질문을 공유한 후, 이해를 보여주는 간단한 요약(한 문단 이하)을 반환합니다. 더 넓은 맥락을 언급하고 핵심을 강조하는 방식으로 질문을 재구성하여 사고의 정렬을 확인합니다.

### 후속 프롬프트
그런 다음 질문합니다: "이제 좀 더 자세히 알려주세요. 간략하게라도:
1. 상황 (현재 또는 미래 프로젝트에 관한 것인지)
2. 무엇을 생각하고 있는지에 대한 좀 더 자세한 내용"

### 워크플로
이후 질문에 가장 적합한 문제 선택 프레임워크의 특정 모듈을 활용합니다:
- **스킬 1-4**: 미래 프로젝트 계획 (아이디어 도출, 리스크, 최적화, 파라미터)
- **스킬 5-7**: 현재 프로젝트 탐색 (의사결정 트리, 역경, 반전)
- **스킬 8**: 커뮤니케이션 및 통합
- **스킬 9**: 종합적 워크플로 오케스트레이션

전체 참조 자료는 `references/` 폴더에서 확인하세요.

---

## 핵심 프레임워크 개념

### 핵심 통찰
**문제 선택 >> 실행 품질**

평범한 문제에 대한 뛰어난 실행도 점진적 영향만 산출합니다. 중요한 문제에 대한 좋은 실행은 상당한 영향을 산출합니다.

### 시간의 역설
과학자들은 일반적으로:
- 문제를 선택하는 데 **며칠**을 쓰고
- 해결하는 데 **수년**을 씁니다

이 불균형이 영향력을 제한합니다. 이 스킬들은 현명한 선택에 더 많은 시간을 투자하도록 돕습니다.

### 평가 축
**아이디어 평가를 위해:**
- **X축:** 성공 가능성
- **Y축:** 성공 시 영향력

스킬들은 아이디어를 오른쪽(더 실현 가능)과 위쪽(더 영향력 있는)으로 이동시키는 데 도움을 줍니다.

### 리스크의 역설
- 리스크를 피하지 말고 친구로 삼으세요
- 리스크 없음 = 점진적 작업
- 하지만: 복수의 기적 = 피하거나 재정비
- **균형:** 이해하고, 정량화하고, 관리 가능한 리스크

### 파라미터의 역설
- 너무 많은 고정 = 취약성
- 너무 적은 고정 = 마비
- **최적점:** 하나의 의미 있는 제약조건 고정

### 역경의 원칙
- 위기는 불가피합니다 (놀라지 마세요)
- 위기는 기회입니다 (낭비하지 마세요)
- **전략:** 문제를 해결하면서 동시에 프로젝트를 업그레이드

---

## 9가지 스킬 개요

| 스킬 | 목적 | 산출물 | 시간 |
|-------|---------|--------|------|
| 1. 직관 펌프 | 고품질 연구 아이디어 생성 | 문제 아이디어 도출 문서 | 약 1주 |
| 2. 리스크 평가 | 프로젝트 리스크 식별 및 관리 | 리스크 평가 매트릭스 | 3-5일 |
| 3. 최적화 함수 | 성공 지표 정의 | 영향력 평가 문서 | 2-3일 |
| 4. 파라미터 전략 | 고정 vs. 유연 결정 | 파라미터 전략 문서 | 2-3일 |
| 5. 의사결정 트리 탐색 | 결정 포인트 계획 및 고도 댄스 | 의사결정 트리 맵 | 2일 |
| 6. 역경 대응 | 위기를 기회로 준비 | 역경 플레이북 | 2일 |
| 7. 문제 반전 | 장애물 우회 탐색 | 문제 반전 분석 | 1일 |
| 8. 통합 및 종합 | 일관된 계획으로 종합 | 프로젝트 커뮤니케이션 패키지 | 3-5일 |
| 9. 메타 프레임워크 | 전체 워크플로 오케스트레이션 | 전체 프로젝트 패키지 | 1-6주 |

---

## 스킬 워크플로

```
SKILL 1: Intuition Pumps
         | (generates idea)
         v
SKILL 2: Risk Assessment
         | (evaluates feasibility)
         v
SKILL 3: Optimization Function
         | (defines success metrics)
         v
SKILL 4: Parameter Strategy
         | (determines flexibility)
         v
SKILL 5: Decision Tree
         | (plans execution and evaluation)
         v
SKILL 6: Adversity Planning
         | (prepares for failure modes)
         v
SKILL 7: Problem Inversion
         | (provides pivot strategies)
         v
SKILL 8: Integration & Communication
         | (synthesizes into coherent plan)
         v
SKILL 9: Meta-Skill
         (orchestrates complete workflow)
```

---

## 핵심 설계 원칙

1. **대화형 진입** - 세 가지 명확한 시작점으로 사용자가 현재 위치에서 출발
2. **사려 깊은 상호작용** - 명확화 질문 제시; 낮은 확신은 추가 입력을 유도
3. **문헌 통합** - 전략적 포인트에서 PubMed 검색을 사용하여 검증
4. **구체적 산출물** - 모든 스킬은 유형적인 1-2페이지 문서를 생산
5. **구체성 구축** - 타겟 질문을 통해 점진적 세부사항 도출
6. **유연성** - 스킬은 독립적으로, 순차적으로, 또는 반복적으로 작동
7. **과학적 엄격성** - 일반성과 실현 가능성에 대한 주장은 근거 기반이어야 함

---

## 이 스킬을 사용해야 하는 사람

### 대학원생 (주요 대상)
- **시기:** 논문 프로젝트 선택, 자격 시험, 위원회 회의
- **초점:** 스킬 1-3 (아이디어 도출, 리스크, 영향력) + 스킬 9 (전체 워크플로)
- **일정:** 종합적 계획에 2-4주

### 박사후 연구원
- **시기:** 새 직위 시작, 독립 프로젝트 계획, 펠로십 지원
- **초점:** 모든 스킬, 독립성과 리스크 관리 강조
- **일정:** 1-2주 집중 계획

### 연구 책임자
- **시기:** 새 연구실, 새 방향, 연수생 멘토링, 연구비 주기
- **초점:** 스킬 1, 3, 4, 6 (아이디어 도출, 영향력, 파라미터, 역경)
- **일정:** 지속적, 연구실 문화에 통합

### 스타트업 창업자
- **시기:** 회사 설립, 피벗 결정, 투자자 프레젠테이션
- **초점:** 스킬 1-4 (아이디어 도출부터 파라미터까지) + 스킬 8 (커뮤니케이션)
- **일정:** 초기 계획에 1-2주, 분기별 재검토

---

## 참조 자료

자세한 스킬 문서는 `references/` 폴더에서 확인할 수 있습니다:

| 파일 | 내용 | 검색 패턴 |
|------|---------|-----------------|
| `01-intuition-pumps.md` | 연구 아이디어 생성 | `Intuition Pump #`, `Trap #`, `Phase [0-9]` |
| `02-risk-assessment.md` | 리스크 식별 | `Risk.*1-5`, `go/no-go`, `assumption` |
| `03-optimization-function.md` | 성공 지표 | `Generality.*Learning`, `optimization`, `impact` |
| `04-parameter-strategy.md` | 파라미터 고정 | `fixed.*float`, `constraint`, `parameter` |
| `05-decision-tree.md` | 의사결정 트리 탐색 | `altitude`, `Level [0-9]`, `decision` |
| `06-adversity-planning.md` | 역경 대응 | `adversity`, `crisis`, `ensemble` |
| `07-problem-inversion.md` | 문제 반전 전략 | `Strategy [0-9]`, `inversion`, `goal` |
| `08-integration-synthesis.md` | 통합 및 종합 | `narrative`, `communication`, `story` |
| `09-meta-framework.md` | 전체 워크플로 | `Phase`, `workflow`, `orchestrat` |

---

## 기대 성과

### 즉시 (워크플로 완료 후)
- 명확한 프로젝트 비전
- 솔직한 리스크 평가
- 비상 계획
- 커뮤니케이션 자료 준비 완료
- 문제 선택에 대한 확신

### 6개월 후
- 더 빠른 결정 (프레임워크 보유)
- 생산적인 역경 처리
- 존재적 위기 없음 (리스크 완화)

### 2년 후
- 출판된 결과 또는 강력한 진전
- 막다른 프로젝트 회피
- 목표에 부합하는 경력
- **시간을 잘 활용함** (궁극적 척도)

---

## 기초 참조

**Fischbach, M.A., & Walsh, C.T. (2024).** "Problem choice and decision trees in science and engineering." *Cell*, 187, 1828-1833.

Stanford University에서 가르치는 BIOE 395 과정에 기반합니다.
