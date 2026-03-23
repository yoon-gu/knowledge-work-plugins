# Claude Code와 Cowork용 Apollo 플러그인

[Apollo.io](https://www.apollo.io/)를 사용해 잠재 고객을 찾고, 리드를 보강하고, 아웃리치 시퀀스를 불러옵니다. Apollo MCP 서버의 **원클릭 통합**으로 동작합니다.

---

## 🔌 원클릭 MCP 서버 통합

이 플러그인은 설치 시 **Apollo MCP 서버를 자동으로 구성**합니다. 수동 서버 설정도, 편집할 설정 파일도 없습니다. 플러그인을 설치하고 Apollo 계정으로 인증하기만 하면 됩니다.

---

## ✅ 강력한 스킬

이 플러그인에는 여러 Apollo API를 연결해 완전한 워크플로를 만드는 고가치 스킬이 포함되어 있습니다.

| 스킬 | 하는 일 |
|---|---|
| `/apollo:enrich-lead` | 이름, LinkedIn URL, 이메일을 넣으면 이메일, 전화번호, 회사 정보, 다음 행동이 포함된 완전한 연락처 카드를 제공합니다 |
| `/apollo:prospect` | ICP를 평이한 영어로 설명하면 보강된 의사결정자 리드의 순위표를 제공합니다 |
| `/apollo:sequence-load` | 리드를 찾고, 보강하고, 아웃리치 시퀀스에 대량으로 불러옵니다 - 중복 제거와 등록까지 처리합니다 |

### `/apollo:enrich-lead`

이름, 회사, LinkedIn URL, 이메일을 넣으면 이메일, 전화번호, 직함, 위치, 회사 세부 정보, 다음 행동 제안이 포함된 완전한 연락처 카드를 돌려줍니다. "Figma의 CEO" 같은 애매한 조회도 처리하며, 정확한 일치가 없으면 검색으로 전환합니다.

### `/apollo:prospect`

ICP를 평이한 영어로 설명하세요. 이 파이프라인은 일치하는 회사를 찾고, firmographic 데이터를 대량 보강하고, 의사결정자를 찾고, 대량 보강으로 연락처 정보를 드러내고, ICP 적합도 점수가 포함된 순위형 리드 표를 반환합니다.

### `/apollo:sequence-load`

타게팅 기준에 맞는 연락처를 찾고, 보강하고, 중복 제거를 적용해 연락처로 만든 뒤, 기존 Apollo 시퀀스에 대량 추가합니다. 등록 전에 후보를 미리 보여주고, 완료 후 전체 요약을 표시합니다.

---

## 📦 설치

### Cowork

아래 링크를 클릭하면 한 번에 설치할 수 있습니다.

[Install in Cowork](https://claude.ai/desktop/customize/plugins/new?marketplace=apolloio/apollo-mcp-plugin&plugin=apollo)

그다음 Cowork를 다시 시작해 MCP 서버가 정상적으로 시작되도록 하세요.

### Claude Code

#### 1. 이 플러그인의 마켓플레이스를 추가합니다

Claude Code에서 다음을 실행합니다.

```
/plugin marketplace add apolloio/apollo-mcp-plugin
```

#### 2. 플러그인을 설치합니다

```
/plugin install apollo@apollo-plugin-marketplace
```

#### 3. Claude Code를 다시 시작합니다

이렇게 하면 MCP 서버가 정상적으로 시작됩니다.

---

## 🔑 인증

Apollo MCP 서버는 **OAuth**를 지원합니다.

1. 설치 후 Claude Code 또는 Cowork에서 `/mcp`를 실행합니다
2. **Apollo** 서버를 선택하고 **Authenticate**를 클릭합니다
3. 브라우저에서 Apollo.io 로그인을 완료합니다
4. 완료 - 이제 모든 명령을 사용할 수 있습니다

---

## ⚠️ Apollo 크레딧

일부 작업은 [Apollo 크레딧](https://docs.apollo.io/)을 사용합니다.

- **사람 보강**(세 스킬 모두에서 사용)은 사람당 1크레딧이 듭니다
- **대량 보강**(`/apollo:prospect`, `/apollo:sequence-load`)은 배치의 사람당 1크레딧이 듭니다
- 플러그인은 크레딧을 사용하기 전에 항상 경고합니다

---

## 🙌 크레딧

- **MCP Server** by [Apollo.io](https://docs.apollo.io/)
- **Plugin Specification** by [Anthropic](https://docs.anthropic.com/)

---

## 라이선스

MIT - 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
