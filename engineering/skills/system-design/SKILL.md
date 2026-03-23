---
name: system-design
description: 시스템, 서비스, 아키텍처를 설계합니다. "design a system for", "how should we architect", "system design for", "what's the right architecture for" 같은 요청이 있거나, API 설계, 데이터 모델링, 서비스 경계 설정에 도움이 필요할 때 사용하세요.
---

# System Design

시스템 설계와 아키텍처 결정을 돕습니다.

## 프레임워크

### 1. Requirements Gathering
- 기능 요구사항(무엇을 하는지)
- 비기능 요구사항(규모, 지연 시간, 가용성, 비용)
- 제약 조건(팀 규모, 일정, 기존 기술 스택)

### 2. High-Level Design
- 컴포넌트 다이어그램
- 데이터 흐름
- API 계약
- 저장소 선택

### 3. Deep Dive
- 데이터 모델 설계
- API 엔드포인트 설계(REST, GraphQL, gRPC)
- 캐싱 전략
- 큐/이벤트 설계
- 오류 처리와 재시도 로직

### 4. Scale and Reliability
- 부하 추정
- 수평 확장 vs 수직 확장
- 페일오버와 중복성
- 모니터링과 알림

### 5. Trade-off Analysis
- 모든 결정에는 트레이드오프가 있습니다. 이를 명시적으로 드러내세요.
- 고려할 사항: 복잡도, 비용, 팀 숙련도, 출시 속도, 유지보수성

## Output

다이어그램(ASCII 또는 서술형), 명시적인 가정, 트레이드오프 분석이 포함된 명확하고 구조적인 설계 문서를 작성합니다. 시스템이 성장하면 무엇을 다시 검토해야 할지도 항상 밝혀야 합니다.
