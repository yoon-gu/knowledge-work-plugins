# Slack 플러그인

이 저장소는 Slack을 Cursor IDE와 Claude Code에 연동하는 데 필요한 설정을 담고 있습니다. 이 플러그인을 사용하면 에이전트가 Slack 워크스페이스와 직접 상호작용하면서 메시지 검색, 메시지 전송, 캔버스 관리 등을 모두 자연어로 수행할 수 있습니다.

## 기능

Slack MCP 서버는 다음 기능을 제공합니다:

- **검색**: 메시지, 파일, 사용자, 채널(공개/비공개 모두) 찾기
- **메시징**: 메시지 전송, 채널 기록 조회, 스레드 대화 접근
- **캔버스**: 서식이 있는 문서 생성 및 공유, 내용을 마크다운으로 내보내기
- **사용자 관리**: 사용자 프로필, 사용자 정의 필드, 상태 정보 조회

## 사전 요구 사항

Slack MCP 서버를 설정하기 전에 다음이 준비되어 있어야 합니다:

- Cursor IDE 또는 Claude Code CLI 설치
- 워크스페이스 관리자가 MCP 통합을 승인한 Slack 워크스페이스 접근 권한

## 설치

사용 중인 IDE에 맞는 설치 방법을 선택하세요:

### Claude Code

Claude Code CLI를 사용 중이라면, 저장소를 로컬에 클론해서 플러그인으로 설치할 수 있습니다:

```bash
git clone https://github.com/slackapi/slack-mcp-plugin.git
cd slack-mcp-plugin
claude --plugin-dir ./
```

플러그인이 로드되면 Slack MCP 서버가 자동으로 설정됩니다. 이어서 OAuth를 통해 Slack 워크스페이스 인증을 진행하라는 안내가 표시됩니다.

Claude 플러그인은 다음 MCP 설정(`.mcp.json`)을 사용합니다:

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

아래의 Add to Cursor 버튼을 사용하거나, 아래 단계를 따라 Cursor에서 Slack MCP 서버를 수동으로 설정할 수 있습니다:

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=slack&config=eyJ1cmwiOiJodHRwczovL21jcC5zbGFjay5jb20vbWNwIiwiYXV0aCI6eyJDTElFTlRfSUQiOiIzNjYwNzUzMTkyNjI2Ljg5MDM0NjkyMjg5ODIifX0%3D)

#### 1단계: Cursor 설정 열기

**Cursor → Settings → Cursor Settings**로 이동하세요(또는 macOS에서는 `Cmd+,`, Windows/Linux에서는 `Ctrl+,` 단축키를 사용하세요).

#### 2단계: MCP 탭으로 이동

설정 화면에서 **MCP** 탭을 클릭해 MCP 서버 구성을 확인합니다.

#### 3단계: Slack MCP 구성 추가

원격 Slack MCP 서버에 연결하려면 다음 구성을 추가하세요:

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

설정을 저장하면 연결 버튼도 표시됩니다. 그 버튼을 클릭해 Slack 워크스페이스 인증을 완료하세요.

## 사용 예시

설정이 끝나면 AI 어시스턴트를 통해 자연어로 Slack과 상호작용할 수 있습니다:

- **메시지 검색**: "지난주 제품 출시와 관련된 메시지를 찾아줘"
- **메시지 전송**: "#general 채널에 배포가 완료됐다고 메시지 보내줘"
- **사용자 찾기**: "john@example.com 이메일을 가진 사용자가 누구야?"
- **스레드 열기**: "그 메시지의 대화 스레드를 보여줘"
- **캔버스 생성**: "우리 회의 노트를 담은 캔버스 문서를 만들어줘"

## 문서 및 자료

- [공식 Slack MCP 서버 문서](https://docs.slack.dev/ai/mcp-server/)

## 참고 및 제한 사항

- **원격 서버만 지원**: 이 설정은 Slack이 호스팅하는 MCP 서버에 연결합니다. 로컬 설치는 필요하지 않으며 지원되지도 않습니다.
- **관리자 승인 필요**: 이 기능을 사용하려면 Slack 워크스페이스 관리자가 MCP 통합을 승인해야 합니다.

## 질문이나 문제가 있나요?

Slack MCP 서버나 통합 관련 문제는 [공식 Slack 문서](https://docs.slack.dev/ai/mcp-server/)를 참고하거나 워크스페이스 관리자에게 문의하세요.
