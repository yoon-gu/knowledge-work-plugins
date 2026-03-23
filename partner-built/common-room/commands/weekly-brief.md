---
description: Generate a weekly prep briefing from your calendar and Common Room
argument-hint: [date range, defaults to next 7 days]
---

Common Room과 캘린더를 사용하여 주간 준비 브리핑을 생성합니다.

weekly-prep-brief skill을 따릅니다:
1. ~~calendar connector를 사용하여 향후 7일간(또는 "$ARGUMENTS"에 지정된 날짜 범위) 예정된 모든 외부 고객 대면 회의를 가져옵니다. 내부 회의는 필터링하고, 고객, 잠재 고객, 파트너와의 콜에 집중합니다.
2. ~~calendar connector를 사용할 수 없는 경우, 사용자에게 외부 콜 목록(회사명, 날짜, 참석자)을 제공하도록 요청합니다.
3. 각 외부 회의에 대해 계정 리서치와 참석자 컨택 리서치를 병렬로 실행합니다.
4. 날짜순으로 정렬된 주 개요 + 회의별 섹션으로 구성된 단일 주간 브리핑으로 컴파일합니다.

각 회의별 섹션은 간결하고 스캔하기 쉽게 유지합니다. 전체 브리핑은 10분 이내에 읽을 수 있어야 합니다.
