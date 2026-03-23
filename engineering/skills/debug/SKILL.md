---
name: debug
description: Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.
argument-hint: "<error message or problem description>"
---

# /debug

> 익숙하지 않은 자리 표시자가 보이거나 연결된 도구를 확인해야 하는 경우 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

체계적으로 문제를 찾아 수정하기 위한 구조화된 디버깅 세션을 실행합니다.

## 사용법

```
/debug $ARGUMENTS
```

## 동작 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                       DEBUG                                        │
├─────────────────────────────────────────────────────────────────┤
│  Step 1: REPRODUCE                                                │
│  ✓ 예상 동작 vs. 실제 동작 파악                                    │
│  ✓ 정확한 재현 단계 식별                                           │
│  ✓ 범위 파악 (언제 시작됐는가? 누가 영향을 받는가?)                 │
│                                                                    │
│  Step 2: ISOLATE                                                   │
│  ✓ 구성 요소, 서비스, 또는 코드 경로 범위 좁히기                    │
│  ✓ 최근 변경 사항 확인 (배포, 설정 변경, 의존성)                   │
│  ✓ 로그 및 오류 메시지 검토                                        │
│                                                                    │
│  Step 3: DIAGNOSE                                                  │
│  ✓ 가설 수립 및 검증                                               │
│  ✓ 코드 경로 추적                                                  │
│  ✓ 근본 원인 파악 (증상이 아닌 원인)                               │
│                                                                    │
│  Step 4: FIX                                                       │
│  ✓ 설명과 함께 수정 방안 제안                                      │
│  ✓ 부작용 및 엣지 케이스 고려                                      │
│  ✓ 회귀를 방지하기 위한 테스트 제안                                │
└─────────────────────────────────────────────────────────────────┘
```

## 필요한 정보

문제에 대해 알려주세요. 다음 중 어떤 것이든 도움이 됩니다:
- 오류 메시지 또는 stack trace
- 재현 단계
- 최근 변경된 사항
- 로그 또는 스크린샷
- 예상 동작 vs. 실제 동작

## 출력

```markdown
## Debug Report: [Issue Summary]

### Reproduction
- **Expected**: [예상되는 동작]
- **Actual**: [실제 발생하는 동작]
- **Steps**: [재현 방법]

### Root Cause
[버그가 발생하는 이유에 대한 설명]

### Fix
[필요한 코드 변경 또는 설정 수정]

### Prevention
- [추가할 테스트]
- [적용할 가드]
```

## 커넥터 사용 가능 시

**~~monitoring**이 연결된 경우:
- 이슈 발생 시점 주변의 로그, 오류율, 메트릭 가져오기
- 상관관계가 있을 수 있는 최근 배포 및 설정 변경 사항 표시

**~~source control**이 연결된 경우:
- 영향받은 코드 경로에 접근한 최근 커밋 및 PR 식별
- 이슈가 특정 변경 사항과 연관되는지 확인

**~~project tracker**가 연결된 경우:
- 관련 버그 보고서 또는 알려진 이슈 검색
- 수정 사항이 파악되면 티켓 생성

## 팁

1. **오류 메시지를 정확하게 공유하세요** — 바꿔 말하지 마세요. 정확한 텍스트가 중요합니다.
2. **변경된 사항을 언급하세요** — 최근 배포, 의존성 업데이트, 설정 변경이 주요 원인입니다.
3. **맥락을 포함하세요** — "스테이징에서는 동작하지만 프로덕션에서는 안 된다" 또는 "대용량 페이로드에서만 발생한다"와 같은 정보가 범위를 빠르게 좁힙니다.
