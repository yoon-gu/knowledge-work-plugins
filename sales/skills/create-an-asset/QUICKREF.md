# 자산 만들기 - 빠른 참고

## 호출
```
/create-an-asset
/create-an-asset [CompanyName]
"Create an asset for [Company]"
```

---

## 입력 한눈에 보기

| 입력 | 제공할 내용 |
|-------|-----------------|
| **(a) 잠재 고객** | 회사, 연락처, 딜 단계, 고통 지점, 녹취록 |
| **(b) 대상** | 임원 / 기술 / 운영 / 혼합 + 무엇을 중요하게 보는지 |
| **(c) 목적** | 소개 / 후속 / 심층 / 정렬 / POC / 종료 |
| **(d) 형식** | 랜딩 페이지 / 덱 / 원페이저 / 워크플로 데모 |

---

## 형식 선택기

| 필요할 때... | 선택... |
|----------------|-----------|
| 인상적인 멀티탭 경험 | **인터랙티브 랜딩 페이지** |
| 미팅에서 발표할 자료 | **덱 스타일** |
| 남겨둘 간단한 요약 | **원페이저** |
| 시스템 연결 방식의 시각화 | **워크플로 데모** |

---

## 샘플 프롬프트

**기본:**
```
Create an asset for Acme Corp
```

**맥락 포함:**
```
Create an asset for Acme Corp. They're a manufacturing company
struggling with supply chain visibility. Met with their COO
last week. Need something for the exec team.
```

**워크플로 데모:**
```
Mock up a workflow for Centric Brands showing how they'd use
our product to monitor contract compliance. Components: our AI,
their Snowflake warehouse, and scanned PDF contracts.
```

---

## 생성 후

| 하고 싶은 일 | 이렇게 말하세요 |
|------------|--------|
| 색상 변경 | "우리 브랜드 색상을 사용해 줘" |
| 섹션 추가 | "보안에 대한 섹션을 추가해 줘" |
| 더 짧게 | "더 간결하게 만들어 줘" |
| 수정 | "CEO 이름이 틀렸어. Jane Smith야" |
| PDF 받기 | "인쇄 친화적인 버전으로 줘" |

---

## 출력

- 독립형 HTML 파일
- 오프라인에서도 작동
- 어디서든 호스팅 가능(Netlify, Vercel, GitHub Pages 등)
- 호스팅 제공자를 통해 비밀번호 보호 가능

---

*그게 전부입니다. 맥락을 주면 → 질문에 답하고 → 자산을 만들고 → 반복하면 됩니다.*
