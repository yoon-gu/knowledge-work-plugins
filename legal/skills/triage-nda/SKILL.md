---
name: triage-nda
description: 들어온 NDA를 신속히 분류해 GREEN(표준 승인), YELLOW(법무 검토), RED(정식 법무 검토)로 구분합니다. 영업 또는 사업개발에서 새로운 NDA가 들어왔을 때, 내장된 비권유/경업금지/누락 예외 조항을 점검할 때, 또는 표준 권한 내에서 서명 가능한지 판단할 때 사용합니다.
argument-hint: "<NDA file or text>"
---

# /triage-nda -- NDA 사전 검토

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인해야 한다면 [CONNECTORS.md](../../CONNECTORS.md)를 참고하세요.

NDA 분류: @$1

들어온 NDA를 표준 검토 기준에 따라 빠르게 분류합니다. 라우팅을 위해 NDA를 표준 승인, 법무 검토, 정식 법무 검토로 분류합니다.

**중요**: 이 스킬은 법무 워크플로를 지원하지만 법률 자문을 제공하지 않습니다. 모든 분석은 의존하기 전에 자격을 갖춘 법률 전문가의 검토를 받아야 합니다.

## 호출

```
/triage-nda
```

## 워크플로

### 1단계: NDA 수락

NDA는 어떤 형식이든 받을 수 있습니다.
- **파일 업로드**: PDF, DOCX 또는 기타 문서 형식
- **URL**: 문서 시스템의 NDA 링크
- **붙여넣은 텍스트**: 직접 붙여넣은 NDA 본문

NDA가 제공되지 않으면 사용자에게 하나를 제공해 달라고 요청합니다.

### 2단계: NDA 플레이북 로드

로컬 설정(예: `legal.local.md`)에서 NDA 검토 기준을 찾습니다.

NDA 플레이북에는 다음이 정의되어 있어야 합니다.
- 상호 vs 일방 요건
- 허용 가능한 기간
- 필수 예외 조항
- 금지 조항
- 조직별 요구사항

**NDA 플레이북이 설정되어 있지 않다면:**
- 합리적인 시장 표준 기본값으로 진행합니다
- 기본값을 사용하고 있음을 분명히 표시합니다
- 적용되는 기본값:
  - 상호 의무 필요(조직이 일방적 공개만 하는 경우 제외)
  - 기간: 일반적으로 2-3년, 영업비밀은 최대 5년
  - 필수 표준 예외: 독자 개발, 공개 정보, 제3자로부터 적법하게 수령, 법률상 요구
  - 비권유 또는 경업금지 조항 없음
  - 리저설 조항 없음(있더라도 매우 좁게 정의)
  - 합리적인 상사 관할의 준거법

### 3단계: 신속 검토

각 검토 기준에 따라 NDA를 체계적으로 평가합니다.

#### 1. 계약 구조
- [ ] **유형 식별**: 상호 NDA, 일방(공개자), 또는 일방(수령자)
- [ ] **맥락 적합성**: NDA 유형이 비즈니스 관계에 적절한가? (예: 탐색적 논의에는 상호, 일방 공개에는 일방)
- [ ] **독립 계약**: NDA가 더 큰 상업 계약 안의 비밀유지 조항이 아니라 독립 계약인지 확인

#### 2. 기밀 정보 정의
- [ ] **합리적 범위**: 과도하게 넓지 않은가 ("기밀로 표시되었는지 여부와 무관한 모든 정보" 같은 문구 회피)
- [ ] **표시 요건**: 표시가 필요하다면 실무적으로 가능한가? (구두 공개 후 30일 내 서면 표시가 표준)
- [ ] **예외 존재**: 표준 예외가 정의되어 있는가(아래 표준 예외 참고)
- [ ] **문제적 포함 없음**: 공개 정보나 독자 개발 자료를 기밀로 정의하지 않는가

#### 3. 수령자의 의무
- [ ] **주의 의무 수준**: 합리적 주의 또는 최소한 자사 기밀 정보와 같은 수준의 주의
- [ ] **사용 제한**: 명시된 목적에만 사용
- [ ] **공개 제한**: 유사한 의무를 부담하는 need-to-know 인원으로 제한
- [ ] **과도한 의무 없음**: 비현실적인 요구가 없는가(예: 모든 커뮤니케이션 암호화, 물리적 로그 보관)

#### 4. 표준 예외
다음 예외가 모두 포함되어야 합니다.
- [ ] **공개 정보**: 수령자의 귀책 없이 공개되었거나 공개되는 정보
- [ ] **사전 보유**: 공개 전에 이미 수령자가 알고 있던 정보
- [ ] **독자 개발**: 기밀 정보를 사용하거나 참조하지 않고 독자적으로 개발한 정보
- [ ] **제3자 수령**: 제한 없이 제3자로부터 적법하게 수령한 정보
- [ ] **법적 강제**: 법, 규제, 또는 법적 절차에 따라 공개가 필요한 경우 공개할 권리(법적으로 허용되면 공개자에게 통지)

#### 5. 허용된 공개
- [ ] **직원**: 알 필요가 있는 직원과 공유 가능
- [ ] **계약자/자문**: 유사한 비밀유지 의무를 부담하는 계약자, 자문, 전문 컨설턴트와 공유 가능
- [ ] **계열사**: 비즈니스 목적상 필요하면 계열사와 공유 가능
- [ ] **법률/규제**: 법 또는 규정에 따라 공개 가능

#### 6. 기간과 존속
- [ ] **계약 기간**: 비즈니스 관계에 합리적인 기간(1-3년이 표준)
- [ ] **비밀유지 존속**: 종료 후 합리적인 기간 동안 의무 존속(2-5년이 표준, 영업비밀은 더 길 수 있음)
- [ ] **영구 아님**: 무기한 또는 영구적 비밀유지 의무를 피함(예외: 영업비밀)

#### 7. 반환 및 파기
- [ ] **의무 발생 시점**: 종료 시 또는 요청 시
- [ ] **합리적 범위**: 기밀 정보와 모든 사본을 반환 또는 파기
- [ ] **보관 예외**: 법, 규제, 내부 컴플라이언스/백업 정책상 필요한 사본 보관 허용
- [ ] **증명**: 파기 증명은 합리적이어야 하며, 공증 진술서는 과도함

#### 8. 구제
- [ ] **금지명령 구제**: 위반이 돌이킬 수 없는 손해를 야기할 수 있고 형평상 구제가 적절할 수 있다는 인정은 표준
- [ ] **사전 확정 손해배상 없음**: NDA의 예정손해배상 조항은 피함
- [ ] **일방적이지 않음**: 구제 조항이 양 당사자에게 동등하게 적용됨(상호 NDA의 경우)

#### 9. 표시해야 할 문제 조항
- [ ] **비권유 없음**: NDA에 직원 비권유 조항이 있으면 안 됨
- [ ] **경업금지 없음**: NDA에 경업금지 조항이 있으면 안 됨
- [ ] **독점성 없음**: NDA가 어느 쪽도 다른 상대와 유사한 논의를 못 하게 해서는 안 됨
- [ ] **스탠드스틸 없음**: NDA에 스탠드스틸 또는 유사한 제한 조항이 있으면 안 됨(M&A 맥락 제외)
- [ ] **리저설 조항 없음**(또는 매우 좁게): 있더라도 사람의 비보조 기억에 남은 일반적 아이디어/개념/노하우/기법으로 제한하고, 영업비밀이나 특허 정보에는 적용하지 않아야 함
- [ ] **IP 양도 또는 라이선스 없음**: NDA가 어떤 지적재산권도 부여하지 않아야 함
- [ ] **감사 권리 없음**: 표준 NDA에서는 드묾

#### 10. 준거법과 관할
- [ ] **합리적 관할**: 잘 정립된 상사 관할
- [ ] **일관성**: 준거법과 관할은 같거나 관련 관할이어야 함
- [ ] **강제 중재 없음**(표준 NDA의 경우): NDA 분쟁은 일반적으로 소송이 선호됨

### 4단계: 분류

검토 결과를 바탕으로 분류를 지정합니다.

#### GREEN -- 표준 승인

다음이 모두 충족되어야 합니다.
- NDA가 상호이거나(또는 관계에 맞는 방향의 일방 NDA)
- 모든 표준 예외가 포함됨
- 기간이 표준 범위 내(1-3년, 존속 2-5년)
- 비권유, 경업금지, 독점성 조항 없음
- 리저설 조항 없음 또는 매우 좁음
- 합리적인 준거법 관할
- 표준 구제(예정손해배상 없음)
- 허용 공개에 직원, 계약자, 자문 포함
- 반환/파기 조항에 법률/컴플라이언스 보관 예외 포함
- 기밀 정보 정의가 합리적 범위

**라우팅**: 표준 위임권한으로 승인합니다. 법무 검토는 필요하지 않습니다.
- **조치**: 표준 위임권한으로 서명 진행

#### YELLOW -- 법무 검토 필요

다음 중 하나 이상이 있지만 NDA가 근본적으로 문제되지는 않습니다.
- 기밀 정보 정의가 선호보다 넓지만 비합리적이지는 않음
- 기간이 표준보다 길지만 시장 범위 내(예: 계약 기간 5년, 존속 7년)
- 쉽게 추가할 수 있는 표준 예외 하나가 빠짐
- 리저설 조항이 있지만 비보조 기억으로 제한됨
- 허용하지만 선호하지 않는 관할의 준거법
- 상호 NDA에서의 경미한 비대칭(예: 한쪽만 허용 공개가 조금 더 넓음)
- 표시 요건이 있지만 실무적으로 가능함
- 반환/파기에 명시적 보관 예외가 없음(암묵적일 수 있으나 추가하는 것이 좋음)
- 해를 끼치지 않는 특이 조항(예: 잠재적 위반 통지 의무)

**라우팅**: 구체적 이슈를 표시해 법무 검토에 회부합니다. 법무가 한 번의 검토로 경미한 레드라인만으로 해결할 가능성이 높습니다.
- **조치**: 법무가 단일 검토로 해결 가능

#### RED -- Significant Issues

**One or more** of the following are present:
- **상호가 필요한데 일방인 경우**(또는 관계에 맞지 않는 방향)
- **핵심 예외 누락**(특히 독자 개발 또는 법적 강제)
- NDA에 내장된 비권유 또는 경업금지 조항
- 적절한 비즈니스 맥락 없는 독점성 또는 스탠드스틸 조항
- **불합리한 기간**(10년 이상 또는 영업비밀 정당화 없이 영구)
- 공개 정보나 독자 개발 자료를 포착할 수 있는 지나치게 넓은 정의
- 기밀 정보 사용 라이선스를 사실상 부여하는 광범위한 리저설 조항
- NDA에 숨겨진 IP 양도 또는 라이선스 부여
- 예정손해배상 또는 벌칙 조항
- 합리적 범위나 통지 요건 없는 감사 권리
- 강제 중재가 있는 매우 불리한 관할
- 문서가 실제 NDA가 아님(기밀유지 외의 실질적 상업 조건, 독점성 또는 기타 의무 포함)

**라우팅**: 정식 법무 검토가 필요합니다. 서명하지 마세요. 협상, 조직의 표준 NDA에 따른 반대 제안, 또는 거부가 필요합니다.
- **조치**: 서명하지 않음; 협상 또는 반대 제안 필요

### 5단계: 분류 보고서 생성

구조화된 보고서를 출력합니다.

```
## NDA 분류 보고서

**분류**: [GREEN / YELLOW / RED]
**당사자**: [party names]
**유형**: [Mutual / Unilateral (disclosing) / Unilateral (receiving)]
**기간**: [duration]
**준거법**: [jurisdiction]
**검토 기준**: [Playbook / Default Standards]

## 검토 결과

| 기준 | 상태 | 메모 |
|-----------|--------|-------|
| 상호 의무 | [PASS/FLAG/FAIL] | [details] |
| 정의 범위 | [PASS/FLAG/FAIL] | [details] |
| 기간 | [PASS/FLAG/FAIL] | [details] |
| 표준 예외 | [PASS/FLAG/FAIL] | [details] |
| [etc.] | | |

## 발견된 이슈

### [Issue 1 -- YELLOW/RED]
**내용**: [description]
**위험**: [what could go wrong]
**권장 수정**: [specific language or approach]

[각 이슈마다 반복]

## 권고

[구체적 다음 단계: 승인, 특정 메모와 함께 검토 회부, 또는 거부/반대]

## 다음 단계

1. [Action item 1]
2. [Action item 2]
```

### 6단계: 라우팅 권고

Based on the classification, recommend the appropriate next step:

| Classification | Recommended Action | Typical Timeline |
|---|---|---|
| GREEN | Approve and route for signature per delegation of authority | Same day |
| YELLOW | Send to designated reviewer with specific issues flagged | 1-2 business days |
| RED | Engage counsel for full review; prepare counterproposal or standard form | 3-5 business days |

For YELLOW and RED classifications:
- Identify the specific person or role that should review (if the organization has defined routing rules)
- Include a brief summary of issues suitable for the reviewer to quickly understand the key points
- If the organization has a standard form NDA, recommend sending it as a counterproposal for RED-classified NDAs

## Common NDA Issues and Standard Positions

### Issue: Overbroad Definition of Confidential Information
**Standard position**: Confidential information should be limited to non-public information disclosed in connection with the stated purpose, with clear exclusions.
**Redline approach**: Narrow the definition to information that is marked or identified as confidential, or that a reasonable person would understand to be confidential given the nature of the information and circumstances of disclosure.

### Issue: Missing Independent Development Carveout
**Standard position**: Must include a carveout for information independently developed without reference to or use of the disclosing party's confidential information.
**Risk if missing**: Could create claims that internally-developed products or features were derived from the counterparty's confidential information.
**Redline approach**: Add standard independent development carveout.

### Issue: Non-Solicitation of Employees
**Standard position**: Non-solicitation provisions do not belong in NDAs. They are appropriate in employment agreements, M&A agreements, or specific commercial agreements.
**Redline approach**: Delete the provision entirely. If the counterparty insists, limit to targeted solicitation (not general recruitment) and set a short term (12 months).

### Issue: Broad Residuals Clause
**Standard position**: Resist residuals clauses. If required, limit to: (a) general ideas, concepts, know-how, or techniques retained in the unaided memory of individuals who had authorized access; (b) explicitly exclude trade secrets and patentable information; (c) does not grant any IP license.
**Risk if too broad**: Effectively grants a license to use the disclosing party's confidential information for any purpose.

### Issue: Perpetual Confidentiality Obligation
**Standard position**: 2-5 years from disclosure or termination, whichever is later. Trade secrets may warrant protection for as long as they remain trade secrets.
**Redline approach**: Replace perpetual obligation with a defined term. Offer a trade secret carveout for longer protection of qualifying information.

## Notes

- If the document is not actually an NDA (e.g., it's labeled as an NDA but contains substantive commercial terms), flag this immediately as a RED and recommend full contract review instead
- For NDAs that are part of a larger agreement (e.g., confidentiality section in an MSA), note that the broader agreement context may affect the analysis
- Always note that this is a screening tool and counsel should review any items the user is uncertain about
