# 지식 MCP 검색 전략

플러그인 사용자 정의 중 조직 컨텍스트를 수집하기 위한 쿼리 패턴입니다.

## 도구 이름 찾기

**소스 제어:**
- 검색: "GitHub" 또는 "GitLab" 또는 "Bitbucket"
- 검색: "pull request" 또는 "merge request"
- 검색: 저장소 링크, CI/CD 언급

**프로젝트 관리:**
- 검색: "Asana" 또는 "Jira" 또는 "Linear" 또는 "Monday"
- 검색: "sprint" 및 "tickets"
- 검색: 작업 링크, 프로젝트 보드 언급

**채팅:**
- 검색: "Slack" 또는 "Teams" 또는 "Discord"
- 검색: 채널 언급, 통합 토론

**해석학:**
- 검색: "Datadog" 또는 "Grafana" 또는 "Mixpanel"
- 검색: "monitoring" 또는 "observability"
- 검색: 대시보드 링크, 경고 구성

**설계:**
- 검색: "Figma" 또는 "Sketch" 또는 "Adobe XD"
- 검색: 디자인 파일 링크, 핸드오프 토론

**CRM:**
- 검색: "Salesforce" 또는 "HubSpot"
- 검색: 거래 언급, 고객 기록 링크

## 조직 가치 찾기

**작업공간/프로젝트 ID:**
- 기존 통합 또는 북마크된 링크 검색
- 관리/설정 문서를 찾으세요.

**팀 규칙:**
- 검색: "story points" 또는 "estimation"
- 검색: "workflow" 또는 "ticket status"
- 엔지니어링 프로세스 문서를 찾아보세요

**채널/팀 이름:**
- 검색: "standup" 또는 "engineering" 또는 "releases"
- 채널 이름 지정 패턴 찾기

## 지식 MCP를 사용할 수 없는 경우

지식 MCP가 구성되지 않은 경우 자동 검색을 건너뛰고 모든 범주에 대해 AskUserQuestion으로 직접 진행합니다. 참고: AskUserQuestion에는 항상 건너뛰기 버튼과 맞춤 답변을 위한 자유 텍스트 입력 상자가 포함되어 있으므로 `None` 또는 `Other`을 옵션으로 포함하지 마세요.
