# Claude Code 및 Cowork용 Apollo 플러그인

[Apollo.io](https://www.apollo.io/)를 활용하여 잠재 고객 탐색, 리드 보강, 아웃리치 시퀀스 로딩을 수행하세요 — Apollo MCP 서버를 통해 **원클릭 통합**으로 구동됩니다.

---

## 🔌 원클릭 MCP 서버 통합

이 플러그인은 설치 시 **Apollo MCP 서버를 자동으로 구성**합니다. 수동 서버 설정이나 설정 파일 편집이 필요 없습니다 — 플러그인을 설치하고 Apollo 계정으로 인증하기만 하면 됩니다.

---

## ✅ 강력한 스킬

이 플러그인은 여러 Apollo API를 완전한 워크플로로 연결하는 고부가가치 스킬을 제공합니다:

| 스킬 | 기능 |
|---|---|
| `/apollo:enrich-lead` | 이름, LinkedIn URL, 또는 이메일 입력 — 이메일, 전화번호, 회사 정보, 다음 행동 방안이 포함된 완전한 연락처 카드 제공 |
| `/apollo:prospect` | 이상적인 고객 프로필(ICP)을 평문으로 설명 — 보강된 의사결정권자 리드의 순위표 제공 |
| `/apollo:sequence-load` | 리드 탐색, 보강 후 아웃리치 시퀀스에 일괄 로딩 — 중복 처리 및 등록 자동화 |

### `/apollo:enrich-lead`

이름, 회사, LinkedIn URL, 또는 이메일을 입력하면 이메일, 전화번호, 직함, 위치, 회사 세부 정보, 권장 다음 행동이 포함된 완전한 연락처 카드를 반환합니다. 퍼지 조회(예: "Figma의 CEO")를 처리하고 정확한 일치가 실패하면 검색으로 전환합니다.

### `/apollo:prospect`

ICP를 평문으로 설명하면 파이프라인이 일치하는 회사를 검색하고, 기업 데이터를 일괄 보강하며, 의사결정권자를 찾고, 일괄 보강을 통해 연락처 정보를 제공하여 ICP 적합 점수가 포함된 순위 리드 테이블을 반환합니다.

### `/apollo:sequence-load`

타겟팅 기준에 맞는 연락처를 찾아 보강하고, 중복 제거를 통해 연락처를 생성한 후 기존 Apollo 시퀀스에 일괄 추가합니다. 등록 전에 후보를 미리보고 완료 후 전체 요약을 표시합니다.

---

## 📦 설치

### Cowork

아래 링크를 클릭하여 한 번에 설치하세요:

[Cowork에서 설치](https://claude.ai/desktop/customize/plugins/new?marketplace=apolloio/apollo-mcp-plugin&plugin=apollo)

설치 후 MCP 서버가 올바르게 시작되도록 Cowork를 다시 시작하세요.

### Claude Code

#### 1. 이 플러그인의 마켓플레이스 추가

Claude Code에서 실행하세요:

```
/plugin marketplace add apolloio/apollo-mcp-plugin
```

#### 2. 플러그인 설치

```
/plugin install apollo@apollo-plugin-marketplace
```

#### 3. Claude Code 재시작

MCP 서버가 올바르게 시작되도록 합니다.

---

## 🔑 인증

Apollo MCP 서버는 **OAuth**를 지원합니다:

1. 설치 후 Claude Code 또는 Cowork에서 `/mcp` 실행
2. **Apollo** 서버를 선택하고 **인증(Authenticate)** 클릭
3. 브라우저에서 Apollo.io 로그인 완료
4. 완료 — 모든 명령어를 사용할 준비가 되었습니다

---

## ⚠️ Apollo 크레딧

일부 작업은 [Apollo 크레딧](https://docs.apollo.io/)을 소비합니다:

- **인물 보강**(세 가지 스킬 모두 사용) — 1인당 1 크레딧
- **일괄 보강**(`/apollo:prospect`, `/apollo:sequence-load`) — 배치 내 1인당 1 크레딧
- 플러그인은 크레딧 소비 전에 항상 경고합니다

---

## 🙌 크레딧

- **MCP 서버** by [Apollo.io](https://docs.apollo.io/)
- **플러그인 사양** by [Anthropic](https://docs.anthropic.com/)

---

## 라이선스

MIT — 자세한 내용은 [LICENSE](LICENSE)를 참조하세요.
