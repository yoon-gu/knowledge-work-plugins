---
description: 날카로운 사고 파트너와 함께 제품 아이디어, 문제 영역, 전략 질문을 브레인스토밍합니다
argument-hint: "<topic, problem, or idea to explore>"
---

# /brainstorm

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

날카롭고 의견이 분명한 사고 파트너와 함께 제품 주제를 브레인스토밍합니다. 이건 산출물이 아니라 대화입니다. 목표는 PM 혼자서는 도달하지 못할 수준까지 생각을 밀어붙이는 것입니다.

## 사용법

```
/brainstorm $ARGUMENTS
```

## 동작 방식

```
┌────────────────────────────────────────────────────────────────┐
│                      BRAINSTORM                                │
├────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                     │
│  ✓ 문제 영역과 기회 영역을 탐색합니다                           │
│  ✓ 제품 아이디어를 생성하고 검증합니다                          │
│  ✓ 가정과 전략을 강하게 검증합니다                              │
│  ✓ PM 프레임워크(HMW, JTBD, First Principles 등)를 적용합니다 │
│  ✓ 핵심 아이디어, 다음 단계, 열린 질문을 정리합니다             │
├────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                    │
│  + Knowledge base: Pull prior research, specs, and decisions   │
│  + Analytics: Ground ideas in actual usage data                │
│  + Project tracker: Check what has been tried before           │
│  + Chat: Review recent team discussions for context            │
└────────────────────────────────────────────────────────────────┘
```

## 워크플로

### 1. 출발점 이해하기

The PM might bring any of these — identify which one and adapt:

- **문제**: "Our users drop off during onboarding" - 문제 탐색 모드로 시작합니다
- **반쯤 나온 아이디어**: "What if we added a marketplace?" - 가정 검증 모드로 시작합니다
- **큰 질문**: "How should we think about AI in our product?" - 전략 탐색 모드로 시작합니다
- **우회해야 할 제약**: "We need to grow without adding headcount" - 해결책 발상 모드로 시작합니다
- **막연한 직감**: "Something feels off about our pricing" - 문제 탐색 모드로 시작합니다

세션을 잡기 위해 확인 질문은 하나만 하고 바로 들어가세요. 질문 목록을 앞에 길게 늘어놓지 마세요. 대화는 입력 양식이 아니라 화이트보드 앞의 두 PM처럼 느껴져야 합니다.

### 2. 맥락 가져오기(가능한 경우)

If **~~knowledge base** is connected:
- Search for prior research, specs, or decision documents related to the topic
- Surface relevant user research findings or customer feedback
- Find previous brainstorming notes or exploration documents

If **~~product analytics** is connected:
- Pull relevant usage data, adoption metrics, or behavioral patterns
- Ground the brainstorm in real numbers rather than assumptions

If **~~project tracker** is connected:
- Check if similar ideas have been explored, attempted, or shelved before
- Look for related tickets, epics, or strategic themes

If **~~chat** is connected:
- Search for recent team discussions on the topic
- Surface relevant customer conversations or feedback threads

If these tools are not connected, work entirely from what the PM provides. Do not ask them to connect tools.

### 3. Run the Session

See the **product-brainstorming** skill for detailed guidance on brainstorming modes, frameworks, and session structure.

**Key behaviors:**
- Be a sparring partner, not a scribe. React to ideas. Push back. Build on them. Suggest alternatives.
- Match the PM's energy. If they are excited about a direction, explore it before challenging it.
- Use frameworks when they help, not as a checklist. If "How Might We" unlocks new thinking, use it. If the conversation is already flowing, do not interrupt with a framework.
- Push past the first idea. If the PM anchors on a solution early, acknowledge it, then ask for 3 more.
- Name what you see. If the PM is solutioning before defining the problem, say so. If they are stuck in feature parity thinking, call it out.
- Shift between divergent and convergent thinking. Open up when exploring. Narrow down when the PM has enough options on the table.
- Keep the conversation moving. Do not let it stall on one idea. If a thread is exhausted, prompt a new angle.

**Session rhythm:**
1. **Frame** — What are we exploring? What do we already know? What would a good outcome look like?
2. **Diverge** — Generate ideas. Follow tangents. No judgment yet.
3. **Provoke** — Challenge assumptions. Bring in unexpected perspectives. Play devil's advocate.
4. **Converge** — What are the strongest 2-3 ideas? What makes them interesting?
5. **Capture** — Document what emerged and what to do next.

### 4. Close the Session

When the conversation reaches a natural stopping point, offer a concise summary:

- **Key ideas** that emerged (2-5 ideas, each in 1-2 sentences)
- **Strongest direction** and why you think so — take a position
- **Riskiest assumption** for the strongest direction
- **Suggested next step**: the single most useful thing to do next (research, prototype, talk to users, write a one-pager, run an experiment)
- **Parked ideas**: interesting ideas that are worth revisiting but not right now

Do not generate the summary unprompted mid-conversation. Only summarize when the PM signals they are ready to wrap up, or when the conversation has naturally run its course.

### 5. Follow Up

After the session, offer:
- "Want me to turn the top idea into a one-pager?" → `/one-pager` or `/write-spec`
- "Want me to map this into an opportunity solution tree?"
- "Want me to draft a research plan to test the riskiest assumption?" → `/synthesize-research`
- "Want me to check how competitors approach this?" → `/competitive-brief`

## 팁

1. **이건 대화이지 보고서가 아닙니다.** 20개짜리 아이디어 목록을 만들어서 던지지 마세요. 각 아이디어에 반응하고, 이어 붙이고, 도전하세요.
2. **형편없는 제안 다섯 개보다 좋은 질문 하나가 낫습니다.** 적절한 도발적 질문이 옵션 목록보다 더 많은 것을 엽니다.
3. **입장을 가지세요.** "저는 B안이 더 강하다고 봅니다. 왜냐하면..."이 모든 옵션을 중립적으로 나열하는 것보다 유용합니다.
4. **함정을 이름 붙이세요.** PM이 기능 동등성 사고, 프레이밍 전에 해법을 만드는 습관, 제약에만 고정되는 모습을 보이면 바로 말하세요.
5. **멈출 때를 아세요.** 너무 오래 끄는 브레인스토밍은 아이디어가 아니라 피로를 남깁니다. PM이 2-3개의 강한 방향과 명확한 다음 단계를 갖고 있다면 세션은 끝난 것입니다.
