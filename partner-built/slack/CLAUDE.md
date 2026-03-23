# Slack 플러그인

이 플러그인은 Slack과 Claude Code를 연결해 Slack에서 메시지를 검색하고 읽고 전송할 수 있는 도구를 제공합니다.

## 명령

- `/slack:summarize-channel <channel-name>` — Slack 채널의 최근 활동을 요약합니다
- `/slack:find-discussions <topic>` — Slack 채널 전반에서 특정 주제에 대한 논의를 찾습니다
- `/slack:draft-announcement <topic>` — 형식이 잘 갖춰진 Slack 공지 초안을 만들고 임시 저장합니다
- `/slack:standup` — 최근 Slack 활동을 바탕으로 스탠드업 업데이트를 생성합니다
- `/slack:channel-digest <channel1, channel2, ...>` — 여러 Slack 채널의 최근 활동 요약을 제공합니다

## 스킬

- **slack-messaging** — mrkdwn 문법으로 형식이 잘 갖춰진 Slack 메시지를 작성하는 방법
- **slack-search** — 메시지, 파일, 채널, 사람을 효과적으로 찾기 위한 Slack 검색 가이드
