# Slack 플러그인

이 플러그인은 Slack을 Claude Code와 통합하여 Slack에서 메시지를 검색, 읽기, 보내기 위한 도구를 제공합니다.

## 명령어

- `/slack:summarize-channel <channel-name>` — Slack 채널의 최근 활동을 요약합니다
- `/slack:find-discussions <topic>` — Slack 채널 전체에서 특정 주제에 대한 토론을 찾습니다
- `/slack:draft-announcement <topic>` — 잘 포맷된 Slack 공지를 작성하고 초안으로 저장합니다
- `/slack:standup` — 최근 Slack 활동을 기반으로 스탠드업 업데이트를 생성합니다
- `/slack:channel-digest <channel1, channel2, ...>` — 여러 Slack 채널의 최근 활동 다이제스트를 제공합니다

## 스킬

- **slack-messaging** — mrkdwn 구문을 사용하여 잘 포맷된 Slack 메시지를 작성하기 위한 지침
- **slack-search** — Slack에서 메시지, 파일, 채널, 사람을 효과적으로 검색하기 위한 지침
