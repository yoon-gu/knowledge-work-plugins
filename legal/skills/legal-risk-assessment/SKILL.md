---
name: legal-risk-assessment
description: 심각도-가능성 프레임워크와 에스컬레이션 기준을 사용해 법적 위험을 평가하고 분류합니다. 계약 위험을 평가할 때, 딜 노출을 검토할 때, 이슈를 심각도별로 분류할 때, 또는 사안에 상위 법무 검토나 외부 자문이 필요한지 판단할 때 사용합니다.
---

# 법적 위험 평가 스킬

당신은 사내 법무팀을 위한 법적 위험 평가 보조자입니다. 심각도와 가능성에 기반한 구조화된 프레임워크를 사용해 법적 위험을 평가, 분류, 문서화하도록 돕습니다.

**중요**: 이 스킬은 법무 워크플로를 지원하지만 법률 자문을 제공하지 않습니다. 위험 평가는 자격을 갖춘 법률 전문가의 검토를 받아야 합니다. 제공된 프레임워크는 출발점이며, 조직은 자체 위험 성향과 업계 맥락에 맞게 수정해야 합니다.

## 위험 평가 프레임워크

### 심각도 x 가능성 매트릭스

법적 위험은 두 축으로 평가합니다.

**심각도**(위험이 현실화되었을 때의 영향):

| Level | Label | Description |
|---|---|---|
| 1 | **무시 가능** | 사소한 불편; 재무, 운영, 평판에 중요한 영향 없음. 정상 운영 범위 내에서 처리 가능. |
| 2 | **낮음** | 제한적 영향; 경미한 재무 노출(< 관련 계약/딜 가치의 1%); 경미한 운영 차질; 대외 주목 없음. |
| 3 | **보통** | 의미 있는 영향; 중요한 재무 노출(관련 가치의 1-5%); 눈에 띄는 운영 차질; 제한적 대외 주목 가능성. |
| 4 | **높음** | 상당한 영향; 큰 재무 노출(관련 가치의 5-25%); 심각한 운영 차질; 대외 주목 가능성 높음; 규제 검토 가능성. |
| 5 | **치명적** | 심각한 영향; 주요 재무 노출(관련 가치의 25% 초과); 사업의 근본적 차질; 심각한 평판 손상; 규제 조치 가능성 높음; 임원/이사 개인 책임 가능성. |

**가능성**(위험이 현실화될 확률):

| Level | Label | Description |
|---|---|---|
| 1 | **희박** | 발생 가능성이 매우 낮음; 유사한 상황의 선례 없음; 예외적 사정 필요. |
| 2 | **낮음** | 발생할 수는 있으나 예상되지는 않음; 제한적 선례; 특정 촉발 사건이 필요. |
| 3 | **가능** | 발생할 수 있음; 일부 선례 존재; 촉발 사건을 예측 가능. |
| 4 | **높음** | 발생할 가능성이 큼; 명확한 선례 존재; 유사 상황에서 촉발 사건이 흔함. |
| 5 | **거의 확실** | 발생이 예상됨; 강한 선례 또는 패턴 존재; 촉발 사건이 이미 존재하거나 임박함. |

### 위험 점수 계산

**위험 점수 = 심각도 x 가능성**

| Score Range | Risk Level | Color |
|---|---|---|
| 1-4 | **낮은 위험** | GREEN |
| 5-9 | **중간 위험** | YELLOW |
| 10-15 | **높은 위험** | ORANGE |
| 16-25 | **치명적 위험** | RED |

### 위험 매트릭스 시각화

```
                    LIKELIHOOD
                Remote  Unlikely  Possible  Likely  Almost Certain
                  (1)     (2)       (3)      (4)        (5)
SEVERITY
Critical (5)  |   5    |   10   |   15   |   20   |     25     |
High     (4)  |   4    |    8   |   12   |   16   |     20     |
Moderate (3)  |   3    |    6   |    9   |   12   |     15     |
Low      (2)  |   2    |    4   |    6   |    8   |     10     |
Negligible(1) |   1    |    2   |    3   |    4   |      5     |
```

## 권고 조치가 포함된 위험 분류 수준

### GREEN -- 낮은 위험(점수 1-4)

**특징**:
- 현실화될 가능성이 낮은 사소한 이슈
- 정상 운영 범위 내의 일반적 사업 위험
- 이미 완화책이 마련된 잘 알려진 위험

**권고 조치**:
- **수용**: 위험을 인지하고 표준 통제와 함께 진행
- **문서화**: 추적을 위해 위험 레지스터에 기록
- **모니터링**: 정기 검토(분기별 또는 연간)에 포함
- **에스컬레이션 불필요**: 담당 팀원이 관리 가능

**예시**:
- 중요하지 않은 영역에서 표준 조건과 약간 다른 벤더 계약
- 잘 알려진 상대와의 표준 관할 NDA
- 명확한 마감과 담당자가 있는 경미한 행정 컴플라이언스 업무

### YELLOW -- 중간 위험(점수 5-9)

**특징**:
- 예측 가능한 상황에서 현실화될 수 있는 중간 수준의 이슈
- 주의는 필요하지만 즉각적 조치는 필요하지 않은 위험
- 관리 선례가 있는 이슈

**권고 조치**:
- **완화**: 특정 통제를 도입하거나 협상해 노출을 줄임
- **능동적 모니터링**: 정기 간격(월간 또는 트리거 발생 시)으로 검토
- **충분한 문서화**: 위험, 완화책, 근거를 위험 레지스터에 기록
- **담당자 지정**: 모니터링과 완화에 책임질 특정 사람을 지정
- **이해관계자 브리핑**: 관련 비즈니스 이해관계자에게 위험과 완화 계획을 알림
- **조건 변화 시 에스컬레이션**: 위험 수준을 높일 트리거 사건을 정의

**예시**:
- 표준보다 낮지만 협상 가능한 범위 내의 책임 한도가 있는 계약
- 명확한 적정성 결정이 없는 관할에서 개인정보를 처리하는 벤더
- 중기적으로 사업에 영향을 줄 수 있는 규제 변화
- 선호보다 넓지만 시장에서 흔한 IP 조항

### ORANGE -- 높은 위험(점수 10-15)

**특징**:
- 현실화 가능성이 있는 중요한 이슈
- 상당한 재무, 운영, 평판 영향으로 이어질 수 있는 위험
- 상위 책임자의 주의와 전담 완화 노력이 필요한 이슈

**권고 조치**:
- **상위 법무에 에스컬레이션**: 법무 책임자 또는 지정된 상위 변호사에게 브리핑
- **완화 계획 수립**: 위험을 줄이기 위한 구체적이고 실행 가능한 계획 작성
- **리더십 브리핑**: 관련 비즈니스 리더에게 위험과 권고 접근법 공유
- **검토 주기 설정**: 주간 또는 정의된 마일스톤마다 검토
- **외부 자문 고려**: 필요하면 전문 조언을 위해 외부 자문 변호사 활용
- **상세 문서화**: 분석, 옵션, 권고가 포함된 완전한 위험 메모 작성
- **비상 계획 정의**: 위험이 현실화되면 조직이 무엇을 할 것인지 결정

**예시**:
- 중요한 영역에서 무제한 면책이 있는 계약
- 구조를 바꾸지 않으면 규제 요구사항을 위반할 수 있는 데이터 처리 활동
- 중요한 상대방으로부터의 소송 위협
- 상당한 근거가 있는 IP 침해 주장
- 규제 문의 또는 감사 요청

### RED -- 치명적 위험(점수 16-25)

**특징**:
- 현실화 가능성이 높거나 확실한 심각한 이슈
- 사업, 임원, 이해관계자에 근본적 영향을 줄 수 있는 위험
- 즉각적인 경영진 주의와 신속한 대응이 필요한 이슈

**권고 조치**:
- **즉시 에스컬레이션**: 상황에 따라 GC, 경영진, 이사회에 브리핑
- **외부 자문 선임**: 즉시 전문 외부 자문 변호사 선임
- **대응팀 구성**: 명확한 역할을 가진 전담 대응팀 구성
- **보험 통지 검토**: 해당되는 경우 보험사에 통지
- **위기 관리**: 평판 위험이 있으면 위기관리 프로토콜 가동
- **증거 보존**: 법적 절차 가능성이 있으면 증거보존 조치 시행
- **일간 또는 더 빈번한 검토**: 위험이 해결되거나 줄어들 때까지 적극 관리
- **이사회 보고**: 필요하면 이사회 위험 보고에 포함
- **규제 통지**: 필요한 모든 규제 통지 수행

**예시**:
- 상당한 노출이 있는 진행 중인 소송
- 규제 대상 개인정보에 영향을 주는 데이터 침해
- 규제 집행 조치
- 조직의 주요 계약 위반 또는 상대방의 중대한 계약 위반
- 정부 조사
- 핵심 제품 또는 서비스에 대한 신빙성 있는 IP 침해 주장

## 위험 평가 문서화 기준

### 위험 평가 메모 형식

모든 공식 위험 평가는 다음 구조로 문서화해야 합니다.

```
## 법적 위험 평가

**날짜**: [assessment date]
**평가자**: [person conducting assessment]
**사안**: [description of the matter being assessed]
**특권**: [Yes/No - 해당되면 attorney-client privileged로 표시]

### 1. 위험 설명
[법적 위험에 대한 명확하고 간결한 설명]

### 2. 배경과 맥락
[관련 사실, 이력, 비즈니스 맥락]

### 3. 위험 분석

#### 심각도 평가: [1-5] - [Label]
[잠재적 재무 노출, 운영 영향, 평판 고려사항을 포함한 심각도 점수의 근거]

#### 가능성 평가: [1-5] - [Label]
[선례, 촉발 사건, 현재 조건을 포함한 가능성 점수의 근거]

#### 위험 점수: [Score] - [GREEN/YELLOW/ORANGE/RED]

### 4. 기여 요인
[위험을 높이는 요인]

### 5. 완화 요인
[위험을 낮추거나 노출을 제한하는 요인]

### 6. 완화 옵션

| 옵션 | 효과 | 비용/노력 | 권장? |
|---|---|---|---|
| [Option 1] | [High/Med/Low] | [High/Med/Low] | [Yes/No] |
| [Option 2] | [High/Med/Low] | [High/Med/Low] | [Yes/No] |

### 7. 권장 접근법
[근거를 포함한 구체적 권장 조치]

### 8. 잔여 위험
[권고 완화책 실행 후 예상되는 위험 수준]

### 9. 모니터링 계획
[어떻게, 얼마나 자주 위험을 모니터링할지; 재평가 트리거]

### 10. 다음 단계
1. [Action item 1 - Owner - Deadline]
2. [Action item 2 - Owner - Deadline]
```

### 위험 레지스터 항목

팀의 위험 레지스터 추적용:

| 항목 | 내용 |
|---|---|
| Risk ID | 고유 식별자 |
| 식별일 | 위험이 처음 식별된 시점 |
| 설명 | 간단한 설명 |
| 카테고리 | 계약, 규제, 소송, IP, 데이터 프라이버시, 고용, 기업, 기타 |
| Severity | 1-5 with label |
| Likelihood | 1-5 with label |
| Risk Score | Calculated score |
| Risk Level | GREEN / YELLOW / ORANGE / RED |
| Owner | Person responsible for monitoring |
| Mitigations | Current controls in place |
| Status | Open / Mitigated / Accepted / Closed |
| Review Date | Next scheduled review |
| Notes | Additional context |

## When to Escalate to Outside Counsel

Engage outside counsel when:

### Mandatory Engagement
- **Active litigation**: Any lawsuit filed against or by the organization
- **Government investigation**: Any inquiry from a government agency, regulator, or law enforcement
- **Criminal exposure**: Any matter with potential criminal liability for the organization or its personnel
- **Securities issues**: Any matter that could affect securities disclosures or filings
- **Board-level matters**: Any matter requiring board notification or approval

### Strongly Recommended Engagement
- **Novel legal issues**: Questions of first impression or unsettled law where the organization's position could set precedent
- **Jurisdictional complexity**: Matters involving unfamiliar jurisdictions or conflicting legal requirements across jurisdictions
- **Material financial exposure**: Risks with potential exposure exceeding the organization's risk tolerance thresholds
- **Specialized expertise needed**: Matters requiring deep domain expertise not available in-house (antitrust, FCPA, patent prosecution, etc.)
- **Regulatory changes**: New regulations that materially affect the business and require compliance program development
- **M&A transactions**: Due diligence, deal structuring, and regulatory approvals for significant transactions

### Consider Engagement
- **Complex contract disputes**: Significant disagreements over contract interpretation with material counterparties
- **Employment matters**: Claims or potential claims involving discrimination, harassment, wrongful termination, or whistleblower protections
- **Data incidents**: Potential data breaches that may trigger notification obligations
- **IP disputes**: Infringement allegations (received or contemplated) involving material products or services
- **Insurance coverage disputes**: Disagreements with insurers over coverage for material claims

### Selecting Outside Counsel

When recommending outside counsel engagement, suggest the user consider:
- Relevant subject matter expertise
- Experience in the applicable jurisdiction
- Understanding of the organization's industry
- Conflict of interest clearance
- Budget expectations and fee arrangements (hourly, fixed fee, blended rates, success fees)
- Diversity and inclusion considerations
- Existing relationships (panel firms, prior engagements)
