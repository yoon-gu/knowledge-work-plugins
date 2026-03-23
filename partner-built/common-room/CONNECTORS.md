# Connectors

## 도구 참조가 작동하는 방식

플러그인 파일은 해당 카테고리에서 사용자가 연결하는 도구의 자리 표시자로 `~~category`를 사용합니다. 이 플러그인은 Common Room을 주요 데이터 소스로 구축되어 있으나, 일부 워크플로우는 선택적 캘린더 통합을 통해 더 잘 작동합니다.

## 이 플러그인의 Connectors

| 카테고리 | 자리 표시자 | 포함된 서버 | 기타 옵션 |
|----------|-------------|-----------------|---------------|
| Calendar | `~~calendar` | Google Calendar (via MCP) | Outlook / Microsoft 365 Calendar |

## Common Room MCP

Common Room MCP 서버(`mcp.commonroom.io/mcp`)는 이 플러그인의 모든 skill과 command의 주요 데이터 소스입니다. `.mcp.json`에 등록되어 있으며, 플러그인이 작동하려면 연결 및 인증이 완료되어야 합니다.

## Calendar (선택 사항)

`~~calendar` connector는 두 가지 skill에서 사용됩니다:
- **call-prep** — 예정된 회의에서 참석자 이름을 자동으로 가져옴
- **weekly-prep-brief** — 향후 7일간 예정된 모든 외부 회의를 가져옴

캘린더가 연결되지 않은 경우, 두 skill 모두 사용자에게 회의 세부 정보를 수동으로 요청하는 방식으로 대체됩니다. 캘린더 connector는 완전히 선택 사항입니다.

캘린더를 연결하려면 호환 가능한 캘린더 MCP 서버를 설치하고 인증이 완료되었는지 확인하십시오. 플러그인은 사용 가능할 때 자동으로 감지하여 사용합니다.
