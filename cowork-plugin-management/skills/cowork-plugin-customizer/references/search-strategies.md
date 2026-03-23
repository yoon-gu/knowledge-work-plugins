# 지식 MCP 검색 전략

플러그인 커스터마이징 중 조직 컨텍스트를 수집하기 위한 쿼리 패턴입니다.

## 도구 이름 찾기

**소스 관리:**
- 검색: "GitHub" OR "GitLab" OR "Bitbucket"
- 검색: "pull request" OR "merge request"
- 확인: 저장소 링크, CI/CD 언급

**프로젝트 관리:**
- 검색: "Asana" OR "Jira" OR "Linear" OR "Monday"
- 검색: "sprint" AND "tickets"
- 확인: 작업 링크, 프로젝트 보드 언급

**채팅:**
- 검색: "Slack" OR "Teams" OR "Discord"
- 확인: 채널 언급, 통합 논의

**분석:**
- 검색: "Datadog" OR "Grafana" OR "Mixpanel"
- 검색: "monitoring" OR "observability"
- 확인: 대시보드 링크, 알림 설정

**디자인:**
- 검색: "Figma" OR "Sketch" OR "Adobe XD"
- 확인: 디자인 파일 링크, 핸드오프 논의

**CRM:**
- 검색: "Salesforce" OR "HubSpot"
- 확인: 거래 언급, 고객 레코드 링크

## 조직 값 찾기

**워크스페이스/프로젝트 ID:**
- 기존 통합이나 북마크된 링크 검색
- 관리자/설정 문서 확인

**팀 규칙:**
- 검색: "story points" OR "estimation"
- 검색: "workflow" OR "ticket status"
- 엔지니어링 프로세스 문서 확인

**채널/팀 이름:**
- 검색: "standup" OR "engineering" OR "releases"
- 채널 명명 패턴 확인

## 지식 MCP를 사용할 수 없는 경우

지식 MCP가 설정되어 있지 않으면, 자동 검색을 건너뛰고 모든 카테고리에 대해 AskUserQuestion으로 직접 진행합니다. 참고: AskUserQuestion에는 항상 건너뛰기 버튼과 사용자 지정 답변을 위한 자유 텍스트 입력창이 포함되어 있으므로, `없음` 또는 `기타`를 옵션으로 포함하지 마세요.
