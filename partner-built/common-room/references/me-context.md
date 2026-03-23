# `Me` 객체 - 사용자 컨텍스트 가이드

## `Me`란 무엇인가

Common Room의 `Me` 객체는 현재 인증된 사용자를 나타냅니다. 세션 시작 시 이를 가져오면 LLM이 출력을 개인화하고 쿼리 범위를 올바르게 설정하는 데 필요한 컨텍스트를 얻습니다.

계정 조사, 프로스펙팅, 또는 사용자의 담당 범위에 맞춰야 하는 워크플로를 실행하기 전에 항상 `Me`를 가져오세요.

## `Me`가 반환하는 정보

### 사용자 프로필
- Login identifier (email or username)
- Full name and display name
- Job title and role
- Persona in CR (e.g., AE, SDR, CSM, Manager)
- All linked profiles (e.g., Salesforce user ID, LinkedIn handle)

### 사용자 세그먼트("My Segments")
- A list of all segments that belong to this user (name and segment ID each)
- Corresponds to the **"My Segments" tab** in the Common Room product

## `Me` 컨텍스트를 사용하는 방법

### 1. 쿼리 범위를 설정하고 담당 구역 경계를 존중하기
계정 조사, 프로스펙팅, 또는 브리핑 생성 시에는 사용자가 더 넓은 범위를 원한다고 명시하지 않는 한 결과를 사용자 자신의 세그먼트로 필터링하세요.

> 기본값: "구매 신호를 보이는 계정을 보여줘" -> My Segments 범위로 제한
> 재정의: "워크스페이스의 모든 구매 신호 계정을 보여줘" -> 세그먼트 범위 제거

사용자가 세그먼트에 없는 계정에 대해 묻는 경우 다음처럼 알려주세요: "이 계정은 세그먼트에 없는 것으로 보입니다. 그래도 조사해 드릴까요?"

### 2. 아웃리치와 브리핑을 개인화하기
사용자의 이름, 직함, 역할을 활용해 출력을 개인화하세요. 예를 들어 주간 브리핑에서 담당 구역을 언급하거나, 작성한 이메일에 이름을 넣을 수 있습니다.

### 3. 추론용 컨텍스트로 활용하기
Common Room의 사용자 Persona는 출력의 초점에 영향을 줍니다.
- **AE / AM / Account Executive / Account Manager** - 파이프라인, 딜, 확장, 클로징 일정에 집중
- **SDR / BDR / Sales Development Representative / Business Development Representative** - 프로스펙팅, 따뜻한 신호, 첫 접촉 아웃리치에 집중
- **CSM / Customer Success Manager** - 건강도, 유지, 확장, 챔피언 참여에 집중
- **Manager / Director / VP** - 개별 아웃리치보다 팀 수준의 추세에 집중
