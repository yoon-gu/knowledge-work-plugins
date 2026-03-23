# Slack 플러그인

이 저장소에는 Slack을 Cursor IDE 및 Claude Code와 통합하기 위해 필요한 구성이 포함되어 있습니다. 이 플러그인을 통해 에이전트가 Slack 워크스페이스와 직접 상호작용하여, 자연어로 메시지 검색, 커뮤니케이션 전송, 캔버스 관리 등을 수행할 수 있습니다.

## 기능

Slack MCP 서버는 다음 기능을 제공합니다:

- **검색**: 메시지, 파일, 사용자, 채널 검색 (공개 및 비공개 모두)
- **메시징**: 메시지 전송, 채널 기록 조회, 스레드 대화 접근
- **캔버스**: 포맷된 문서 생성 및 공유, 마크다운으로 콘텐츠 내보내기
- **사용자 관리**: 사용자 정의 필드 및 상태 정보를 포함한 사용자 프로필 조회

## 사전 요구 사항

Slack MCP 서버를 설정하기 전에 다음을 확인하세요:

- Cursor IDE 또는 Claude Code CLI가 설치되어 있어야 합니다
- 워크스페이스 관리자가 MCP 통합을 승인한 Slack 워크스페이스에 접근할 수 있어야 합니다

## 설치

IDE에 맞는 설치 방법을 선택하세요:

### Claude Code

Claude Code CLI를 사용하는 경우, 로컬에 클론하여 플러그인으로 설치할 수 있습니다:

```bash
git clone https://github.com/slackapi/slack-mcp-plugin.git
cd slack-mcp-plugin
claude --plugin-dir ./
```

플러그인이 로드되면 Slack MCP 서버가 자동으로 구성됩니다. OAuth를 통해 Slack 워크스페이스에 인증하라는 메시지가 표시됩니다.

Claude 플러그인은 다음 MCP 구성 (`.mcp.json`)을 사용합니다:

```json
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "oauth": {
        "clientId": "1601185624273.8899143856786",
        "callbackPort": 3118
      }
    }
  }
}
```

### Cursor

아래의 Add to Cursor 버튼을 사용하거나 다음 단계를 따라 Cursor에서 Slack MCP 서버를 수동으로 구성할 수 있습니다:

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=slack&config=eyJ1cmwiOiJodHRwczovL21jcC5zbGFjay5jb20vbWNwIiwiYXV0aCI6eyJDTElFTlRfSUQiOiIzNjYwNzUzMTkyNjI2Ljg5MDM0NjkyMjg5ODIifX0%3D)

#### 1단계: Cursor 설정 열기

**Cursor → Settings → Cursor Settings**로 이동합니다 (또는 macOS에서 `Cmd+,`, Windows/Linux에서 `Ctrl+,` 키보드 단축키 사용).

#### 2단계: MCP 탭으로 이동

설정 인터페이스에서 **MCP** 탭을 클릭하여 MCP 서버 구성에 접근합니다.

#### 3단계: Slack MCP 구성 추가

원격 Slack MCP 서버에 연결하기 위해 다음 구성을 추가합니다:

```json
{
  "mcpServers": {
    "slack": {
      "url": "https://mcp.slack.com/mcp",
      "auth": {
        "CLIENT_ID": "3660753192626.8903469228982"
      }
    }
  }
}
```

구성을 저장합니다. 추가된 후 연결 버튼도 표시됩니다. 이를 클릭하여 Slack 워크스페이스에 인증합니다.

## 사용 예시

구성이 완료되면 자연어를 통해 AI 어시스턴트와 Slack을 상호작용할 수 있습니다:

- **메시지 검색**: "지난주 제품 출시에 대한 메시지를 검색해줘"
- **메시지 보내기**: "#general 채널에 배포가 완료되었다는 메시지를 보내줘"
- **사용자 찾기**: "이메일이 john@example.com인 사용자는 누구야?"
- **스레드 접근**: "해당 메시지의 대화 스레드를 보여줘"
- **캔버스 생성**: "회의록으로 캔버스 문서를 만들어줘"

## 문서 및 리소스

- [공식 Slack MCP 서버 문서](https://docs.slack.dev/ai/mcp-server/)

## 참고 사항 및 제한 사항

- **원격 서버만 지원**: 이 구성은 Slack의 호스팅 MCP 서버에 연결합니다. 로컬 설치는 필요하지 않으며 지원되지 않습니다.
- **관리자 승인 필요**: Slack 워크스페이스 관리자가 이 기능을 사용하기 전에 MCP 통합을 승인해야 합니다.

## 질문이나 문제가 있으신가요?

Slack MCP 서버 또는 통합 문제에 대한 질문은 [공식 Slack 문서](https://docs.slack.dev/ai/mcp-server/)를 참조하거나 워크스페이스 관리자에게 문의하세요.
