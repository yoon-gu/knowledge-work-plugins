---
name: code-review
description: Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.
argument-hint: "<PR URL, diff, or file path>"
---

# /code-review

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

보안, 성능, 정확성, 유지보수성의 구조화된 관점으로 코드 변경 사항을 리뷰합니다.

## 사용법

```
/code-review <PR URL or file path>
```

제공된 코드 변경 사항을 리뷰합니다: @$1

특정 파일이나 URL이 제공되지 않은 경우 무엇을 리뷰할지 질문합니다.

## 동작 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                      CODE REVIEW                                   │
├─────────────────────────────────────────────────────────────────┤
│  STANDALONE (항상 동작)                                           │
│  ✓ diff, PR URL 붙여넣기 또는 파일 지정                           │
│  ✓ 보안 감사 (OWASP top 10, injection, auth)                    │
│  ✓ 성능 리뷰 (N+1, 메모리 누수, 복잡도)                          │
│  ✓ 정확성 (엣지 케이스, 오류 처리, race condition)               │
│  ✓ 스타일 (명명, 구조, 가독성)                                    │
│  ✓ 코드 예제를 포함한 실행 가능한 제안                            │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (도구 연결 시)                                      │
│  + Source control: URL에서 PR diff 자동 가져오기                  │
│  + Project tracker: 발견 사항을 티켓에 연결                       │
│  + Knowledge base: 팀 코딩 표준 대조 확인                         │
└─────────────────────────────────────────────────────────────────┘
```

## 리뷰 항목

### 보안
- SQL injection, XSS, CSRF
- 인증 및 권한 부여 취약점
- 코드 내 secrets 또는 credentials
- 안전하지 않은 역직렬화
- Path traversal
- SSRF

### 성능
- N+1 쿼리
- 불필요한 메모리 할당
- 알고리즘 복잡도 (핫 패스에서의 O(n²))
- 누락된 데이터베이스 인덱스
- 제한 없는 쿼리 또는 루프
- 리소스 누수

### 정확성
- 엣지 케이스 (빈 입력, null, 오버플로우)
- Race condition 및 동시성 문제
- 오류 처리 및 전파
- off-by-one 오류
- 타입 안전성

### 유지보수성
- 명명 명확성
- 단일 책임
- 중복
- 테스트 커버리지
- 자명하지 않은 로직에 대한 문서화

## 출력

```markdown
## Code Review: [PR 제목 또는 파일]

### Summary
[변경 사항 및 전반적인 품질에 대한 1-2문장 개요]

### Critical Issues
| # | File | Line | Issue | Severity |
|---|------|------|-------|----------|
| 1 | [file] | [line] | [description] | 🔴 Critical |

### Suggestions
| # | File | Line | Suggestion | Category |
|---|------|------|------------|----------|
| 1 | [file] | [line] | [description] | Performance |

### What Looks Good
- [긍정적인 관찰 사항]

### Verdict
[Approve / Request Changes / Needs Discussion]
```

## 커넥터 사용 가능 시

**~~source control**이 연결된 경우:
- URL에서 PR diff 자동 가져오기
- CI 상태 및 테스트 결과 확인

**~~project tracker**가 연결된 경우:
- 발견 사항을 관련 티켓에 연결
- PR이 명시된 요구 사항을 충족하는지 확인

**~~knowledge base**가 연결된 경우:
- 팀 코딩 표준 및 스타일 가이드와 변경 사항 대조 확인

## 팁

1. **맥락을 제공하세요** — "이것은 핫 패스입니다" 또는 "이것은 PII를 처리합니다"와 같은 정보가 집중 방향을 잡아줍니다.
2. **관심 사항을 명시하세요** — "보안에 집중"과 같이 지정하면 리뷰 범위가 좁아집니다.
3. **테스트를 포함하세요** — 테스트 커버리지와 품질도 확인해 드립니다.
