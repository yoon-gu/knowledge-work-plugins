#!/usr/bin/env python3
"""Build a static HTML catalog page for knowledge-work-plugins."""

import json, os

REPO = os.path.dirname(os.path.abspath(__file__))

# 플러그인 이름 한국어 매핑
PLUGIN_NAME_KO = {
    'bio-research': '생명과학 연구',
    'cowork-plugin-management': '플러그인 관리',
    'customer-support': '고객 지원',
    'data': '데이터 분석',
    'design': '디자인',
    'engineering': '소프트웨어 엔지니어링',
    'enterprise-search': '전사 검색',
    'finance': '재무·회계',
    'human-resources': '인사 운영',
    'legal': '법무',
    'marketing': '마케팅',
    'operations': '비즈니스 운영',
    'product-management': '제품 관리',
    'productivity': '생산성',
    'sales': '영업',
    'apollo': 'Apollo 영업 자동화',
    'brand-voice': '브랜드 보이스',
    'common-room': 'GTM 워크플로우',
    'slack-by-salesforce': 'Slack 연동',
}

# 플러그인 설명 한국어 번역
PLUGIN_DESC_KO = {
    'bio-research': '전임상 연구 도구 및 데이터베이스(문헌 검색, 유전체 분석, 타겟 우선순위 지정)에 연결하여 초기 단계 생명과학 R&D를 가속화합니다.',
    'cowork-plugin-management': '조직의 도구와 워크플로우에 맞는 플러그인을 만들고, 커스터마이징하고, 관리합니다. MCP 서버를 구성하고, 플러그인 동작을 조정하고, 팀 업무 방식에 맞게 템플릿을 조정합니다.',
    'customer-support': '티켓을 분류하고, 응답을 초안하고, 이슈를 에스컬레이션하고, 지식 베이스를 구축합니다. 고객 컨텍스트를 조사하고 해결된 이슈를 셀프서비스 콘텐츠로 전환합니다.',
    'data': 'SQL 작성, 데이터셋 탐색, 인사이트 도출을 더 빠르게. 시각화와 대시보드를 구축하고, 원시 데이터를 이해관계자를 위한 명확한 스토리로 전환합니다.',
    'design': '디자인 워크플로우를 가속화합니다 — 크리틱, 디자인 시스템 관리, UX 라이팅, 접근성 감사, 리서치 종합, 개발자 핸드오프까지.',
    'engineering': '엔지니어링 워크플로우를 간소화합니다 — 스탠드업, 코드 리뷰, 아키텍처 결정, 인시던트 대응, 기술 문서화. 기존 도구와 함께 또는 단독으로 동작합니다.',
    'enterprise-search': '회사의 모든 도구를 한 곳에서 검색합니다. 이메일, 채팅, 문서, 위키를 앱 전환 없이 검색합니다.',
    'finance': '재무 및 회계 워크플로우를 간소화합니다. 분개 작성, 계정 조정, 재무제표 생성, 차이 분석. 감사 준비, 월말 결산을 빠르게.',
    'human-resources': '인사 운영을 간소화합니다 — 채용, 온보딩, 성과 리뷰, 보상 분석, 정책 안내. 컴플라이언스를 유지하고 팀이 원활하게 운영되도록 합니다.',
    'legal': '사내 법무팀을 위한 계약 검토, NDA 분류, 컴플라이언스 워크플로우를 가속화합니다. 법적 브리프 작성, 판례 조사 정리, 제도적 지식을 관리합니다.',
    'marketing': '콘텐츠 제작, 캠페인 기획, 채널별 성과 분석. 브랜드 보이스 일관성을 유지하고, 경쟁사를 추적하고, 효과적인 것을 보고합니다.',
    'operations': '비즈니스 운영을 최적화합니다 — 벤더 관리, 프로세스 문서화, 변경 관리, 역량 계획, 컴플라이언스 추적.',
    'product-management': '기능 스펙 작성, 로드맵 계획, 사용자 리서치 종합을 더 빠르게. 이해관계자에게 업데이트하고 경쟁 환경을 파악합니다.',
    'productivity': '작업 관리, 하루 계획, 업무 컨텍스트 기억. 캘린더, 이메일, 채팅과 동기화하여 모든 것을 체계적으로 관리합니다.',
    'sales': '잠재 고객 발굴, 아웃리치 작성, 딜 전략 수립을 더 빠르게. 통화 준비, 파이프라인 관리, 개인화된 메시지 작성.',
    'apollo': 'Apollo.io 기반 영업 워크플로우 — 리드 보강, ICP 기반 잠재 고객 탐색, 아웃리치 시퀀스 일괄 등록을 한 번에 처리합니다.',
    'brand-voice': '흩어진 브랜드 자료를 실행 가능한 AI 가이드라인으로 변환합니다. Notion, Drive, Slack 등에서 브랜드 신호를 수집하여 일관된 콘텐츠를 생성합니다.',
    'common-room': 'Common Room 데이터 기반 GTM 워크플로우. 계정/연락처 조사, 통화 준비, 개인화 아웃리치, 잠재 고객 목록 생성, 주간 브리핑.',
    'slack-by-salesforce': 'Slack 공식 MCP 서버. Claude Cowork에서 직접 인사이트를 표면화하고, 메시지를 초안하고, 팀과 협업합니다.',
}

# 스킬 이름 한국어 매핑
SKILL_NAME_KO = {
    'instrument-data-to-allotrope': '실험 데이터 변환',
    'nextflow-development': '바이오 파이프라인 실행',
    'scientific-problem-selection': '연구 문제 선정',
    'scvi-tools': '단일세포 딥러닝 분석',
    'single-cell-rna-qc': '단일세포 RNA QC',
    'start': '환경 설정',
    'cowork-plugin-customizer': '플러그인 커스터마이징',
    'create-cowork-plugin': '플러그인 생성',
    'customer-escalation': '에스컬레이션 패키징',
    'customer-research': '고객 조사',
    'draft-response': '응답 초안 작성',
    'kb-article': '지식 베이스 문서 작성',
    'ticket-triage': '티켓 분류',
    'analyze': '데이터 분석',
    'build-dashboard': '대시보드 구축',
    'create-viz': '시각화 생성',
    'data-context-extractor': '데이터 컨텍스트 추출',
    'data-visualization': '데이터 시각화',
    'explore-data': '데이터 탐색',
    'sql-queries': 'SQL 쿼리 작성',
    'statistical-analysis': '통계 분석',
    'validate-data': '데이터 검증',
    'write-query': '쿼리 작성',
    'accessibility-review': '접근성 감사',
    'design-critique': '디자인 크리틱',
    'design-handoff': '개발자 핸드오프',
    'design-system': '디자인 시스템 관리',
    'research-synthesis': '리서치 종합',
    'user-research': '사용자 리서치',
    'ux-copy': 'UX 카피 작성',
    'architecture': '아키텍처 결정 기록',
    'code-review': '코드 리뷰',
    'debug': '디버깅',
    'deploy-checklist': '배포 체크리스트',
    'documentation': '기술 문서 작성',
    'incident-response': '인시던트 대응',
    'standup': '스탠드업 생성',
    'system-design': '시스템 설계',
    'tech-debt': '기술 부채 관리',
    'testing-strategy': '테스트 전략',
    'digest': '활동 요약',
    'knowledge-synthesis': '지식 종합',
    'search': '통합 검색',
    'search-strategy': '검색 전략',
    'source-management': '소스 관리',
    'audit-support': '감사 지원',
    'close-management': '결산 관리',
    'financial-statements': '재무제표 생성',
    'journal-entry': '분개 작성',
    'journal-entry-prep': '분개 준비',
    'reconciliation': '계정 조정',
    'sox-testing': 'SOX 테스트',
    'variance-analysis': '차이 분석',
    'comp-analysis': '보상 분석',
    'draft-offer': '오퍼 레터 작성',
    'interview-prep': '면접 준비',
    'onboarding': '온보딩 계획',
    'org-planning': '조직 설계',
    'people-report': '인사 보고서',
    'performance-review': '성과 리뷰',
    'policy-lookup': '정책 조회',
    'recruiting-pipeline': '채용 파이프라인',
    'brief': '법무 브리핑',
    'compliance-check': '컴플라이언스 검토',
    'legal-response': '법적 응답 생성',
    'legal-risk-assessment': '법적 리스크 평가',
    'meeting-briefing': '미팅 브리핑',
    'review-contract': '계약 검토',
    'signature-request': '전자서명 요청',
    'triage-nda': 'NDA 분류',
    'vendor-check': '벤더 계약 확인',
    'brand-review': '브랜드 보이스 검토',
    'campaign-plan': '캠페인 기획',
    'competitive-brief': '경쟁사 분석',
    'content-creation': '콘텐츠 제작',
    'draft-content': '콘텐츠 초안 작성',
    'email-sequence': '이메일 시퀀스 설계',
    'performance-report': '성과 보고서',
    'seo-audit': 'SEO 감사',
    'capacity-plan': '역량 계획',
    'change-request': '변경 요청',
    'compliance-tracking': '컴플라이언스 추적',
    'process-doc': '프로세스 문서화',
    'process-optimization': '프로세스 최적화',
    'risk-assessment': '리스크 평가',
    'runbook': '런북 생성',
    'status-report': '상태 보고서',
    'vendor-review': '벤더 평가',
    'metrics-review': '지표 리뷰',
    'product-brainstorming': '제품 브레인스토밍',
    'roadmap-update': '로드맵 업데이트',
    'sprint-planning': '스프린트 계획',
    'stakeholder-update': '이해관계자 업데이트',
    'synthesize-research': '리서치 종합',
    'write-spec': '스펙 작성',
    'memory-management': '메모리 관리',
    'task-management': '작업 관리',
    'update': '동기화 및 새로고침',
    'account-research': '기업 조사',
    'call-prep': '통화 준비',
    'call-summary': '통화 요약',
    'competitive-intelligence': '경쟁 인텔리전스',
    'create-an-asset': '영업 자산 생성',
    'daily-briefing': '일일 브리핑',
    'draft-outreach': '아웃리치 초안',
    'forecast': '영업 예측',
    'pipeline-review': '파이프라인 리뷰',
    'enrich-lead': '리드 보강',
    'prospect': '잠재 고객 탐색',
    'sequence-load': '시퀀스 일괄 등록',
    'brand-voice-enforcement': '브랜드 보이스 적용',
    'discover-brand': '브랜드 발견',
    'guideline-generation': '가이드라인 생성',
    'compose-outreach': '아웃리치 작성',
    'contact-research': '연락처 조사',
    'weekly-prep-brief': '주간 브리핑',
}


def find_plugins():
    plugins = []
    for root, dirs, files in os.walk(REPO):
        if '.claude-plugin' in dirs:
            pjson = os.path.join(root, '.claude-plugin', 'plugin.json')
            if not os.path.exists(pjson):
                continue
            with open(pjson, 'r') as f:
                meta = json.load(f)
            rel = os.path.relpath(root, REPO)  # e.g. "sales" or "partner-built/apollo"
            # README.md 내용
            readme_content = ''
            readme_file = os.path.join(root, 'README.md')
            if os.path.exists(readme_file):
                with open(readme_file, 'r') as f:
                    readme_content = f.read()
            # 플러그인 루트 파일 수집
            TEXT_EXT = {'.md','.json','.py','.txt','.yml','.yaml','.toml','.cfg','.sh','.js','.ts'}
            root_files = []
            for rf in sorted(os.listdir(root)):
                rfp = os.path.join(root, rf)
                if os.path.isfile(rfp):
                    ext = os.path.splitext(rf)[1].lower()
                    content_str = ''
                    if ext in TEXT_EXT:
                        with open(rfp, 'r', errors='replace') as f:
                            content_str = f.read()
                    root_files.append({'name': rf, 'content': content_str, 'dir': False})
                elif os.path.isdir(rfp) and rf not in ('skills', '.claude-plugin', '__pycache__'):
                    root_files.append({'name': rf + '/', 'content': '', 'dir': True})
            # .claude-plugin/plugin.json도 추가
            root_files.append({'name': '.claude-plugin/', 'content': '', 'dir': True})
            pjson_content = ''
            with open(pjson, 'r') as f:
                pjson_content = f.read()
            root_files.append({'name': '  .claude-plugin/plugin.json', 'content': pjson_content, 'dir': False})

            plugin = {
                'name': meta.get('name', ''),
                'version': meta.get('version', ''),
                'description': meta.get('description', ''),
                'author': meta.get('author', {}).get('name', 'Unknown'),
                'is_partner': 'partner-built' in root,
                'rel': rel,
                'readme': readme_content,
                'root_files': root_files,
                'skills': [],
            }
            skills_dir = os.path.join(root, 'skills')
            if os.path.isdir(skills_dir):
                for sname in sorted(os.listdir(skills_dir)):
                    sdir = os.path.join(skills_dir, sname)
                    if not os.path.isdir(sdir):
                        continue
                    skill_md = os.path.join(sdir, 'SKILL.md')
                    fm_name = sname
                    fm_desc = ''
                    if os.path.exists(skill_md):
                        with open(skill_md, 'r') as f:
                            content = f.read()
                        if content.startswith('---'):
                            parts = content.split('---', 2)
                            if len(parts) >= 3:
                                for line in parts[1].strip().split('\n'):
                                    if line.startswith('name:'):
                                        fm_name = line.split(':', 1)[1].strip().strip('"\'')
                                    elif line.startswith('description:'):
                                        fm_desc = line.split(':', 1)[1].strip().strip('"\'')
                    TEXT_EXT = {'.md','.json','.py','.txt','.yml','.yaml','.toml','.cfg','.sh','.js','.ts'}
                    skill_files = []
                    for sf in sorted(os.listdir(sdir)):
                        sfp = os.path.join(sdir, sf)
                        if os.path.isfile(sfp):
                            ext = os.path.splitext(sf)[1].lower()
                            content_str = ''
                            if ext in TEXT_EXT:
                                with open(sfp, 'r', errors='replace') as f:
                                    content_str = f.read()
                            skill_files.append({'name': sf, 'content': content_str, 'dir': False})
                        elif os.path.isdir(sfp):
                            skill_files.append({'name': sf + '/', 'content': '', 'dir': True})
                            for ssf in sorted(os.listdir(sfp)):
                                ssfp = os.path.join(sfp, ssf)
                                if os.path.isfile(ssfp):
                                    ext = os.path.splitext(ssf)[1].lower()
                                    content_str = ''
                                    if ext in TEXT_EXT:
                                        with open(ssfp, 'r', errors='replace') as f:
                                            content_str = f.read()
                                    skill_files.append({'name': f'  {sf}/{ssf}', 'content': content_str, 'dir': False})
                    plugin['skills'].append({
                        'name': fm_name,
                        'dir_name': sname,
                        'desc': fm_desc,
                        'files': skill_files,
                    })
            plugins.append(plugin)
    plugins.sort(key=lambda p: (p['is_partner'], p['name']))
    return plugins


def build(plugins):
    data = []
    for p in plugins:
        desc_ko = PLUGIN_DESC_KO.get(p['name'], p['description'])
        skills = []
        for s in p['skills']:
            ko = SKILL_NAME_KO.get(s['dir_name'], '')
            label = f"{s['name']} ({ko})" if ko else s['name']
            # 영어 desc면 한국어 이름으로 대체
            desc = s['desc']
            if desc and ko and all(ord(c) < 0x1100 for c in desc.replace(' ','').replace('"','').replace("'",'')[:20]):
                desc = ko
            skills.append({
                'name': s['name'], 'label': label, 'dir': s['dir_name'],
                'desc': desc if desc else ko, 'files': s['files'],
            })
        name_ko = PLUGIN_NAME_KO.get(p['name'], '')
        data.append({
            'name': p['name'], 'nameKo': name_ko, 'ver': p['version'], 'desc': desc_ko,
            'author': p['author'], 'partner': p['is_partner'],
            'rel': p['rel'], 'readme': p.get('readme', ''),
            'rootFiles': p.get('root_files', []), 'skills': skills,
        })
    js = json.dumps(data, ensure_ascii=False)
    js = js.replace('</script>', '<\\/script>')
    total = sum(len(p['skills']) for p in data)
    anth = len([p for p in data if not p['partner']])
    part = len([p for p in data if p['partner']])

    # HTML을 3파트로 나눠서 JSON을 안전하게 삽입
    part1 = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>지식 업무 플러그인 카탈로그</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Text:ital@0;1&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#0c0c0f;--s1:#141419;--s2:#1c1c24;--bd:#2a2a38;--bd2:#38384d;
--t:#e8e6f0;--td:#9896a8;--tm:#5c5b70;--ac:#c4a1ff;--acd:#9b7ad8;
--acg:rgba(196,161,255,.07);--pt:#ffb86c;--r:14px}}
body{{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--t);line-height:1.6}}

.hero{{padding:72px 32px 56px;text-align:center;position:relative}}
.hero::before{{content:'';position:absolute;top:-120px;left:50%;transform:translateX(-50%);
width:700px;height:500px;background:radial-gradient(ellipse,rgba(196,161,255,.05) 0%,transparent 70%);pointer-events:none}}
.htag{{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
color:var(--acd);padding:5px 14px;border-radius:100px;border:1px solid rgba(196,161,255,.15);
background:rgba(196,161,255,.06);margin-bottom:24px}}
h1{{font-family:'Outfit',sans-serif;font-size:clamp(2.2rem,5vw,3.6rem);font-weight:700;
line-height:1.15;letter-spacing:-.02em;margin-bottom:14px}}
h1 em{{font-style:normal;color:var(--ac);font-weight:700}}
.hdesc{{font-size:16px;color:var(--td);font-weight:300;max-width:520px;margin:0 auto 32px}}
.hstats{{display:flex;justify-content:center;gap:40px}}
.hs-n{{font-family:'Outfit',sans-serif;font-size:28px;font-weight:700}}
.hs-l{{font-size:11px;color:var(--tm);letter-spacing:.08em;text-transform:uppercase}}

.bar{{position:sticky;top:0;z-index:100;padding:14px 32px;
background:rgba(12,12,15,.88);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
border-bottom:1px solid var(--bd);display:flex;gap:12px;align-items:center}}
.swrap{{flex:1;position:relative}}
.swrap svg{{position:absolute;left:13px;top:50%;transform:translateY(-50%);
width:16px;height:16px;stroke:var(--tm);fill:none;stroke-width:2;pointer-events:none}}
.swrap input{{width:100%;padding:9px 14px 9px 38px;font-family:inherit;font-size:14px;
color:var(--t);background:var(--s1);border:1px solid var(--bd);border-radius:100px;outline:none}}
.swrap input::placeholder{{color:var(--tm)}}
.swrap input:focus{{border-color:var(--acd)}}
.pills{{display:flex;gap:5px}}
.pill{{padding:7px 15px;font-family:inherit;font-size:13px;font-weight:500;border-radius:100px;
border:1px solid var(--bd);background:transparent;color:var(--td);cursor:pointer;transition:all .2s}}
.pill:hover{{border-color:var(--bd2);color:var(--t)}}
.pill.on{{background:var(--ac);border-color:var(--ac);color:var(--bg)}}

.wrap{{max-width:1200px;margin:0 auto;padding:36px 32px 60px}}
.slbl{{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
color:var(--tm);margin-bottom:16px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:14px;margin-bottom:40px}}

.card{{background:var(--s1);border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;
transition:border-color .2s,transform .2s,box-shadow .2s}}
.card:hover{{border-color:var(--bd2);transform:translateY(-2px);box-shadow:0 6px 32px rgba(0,0,0,.3)}}
.card.pt{{border-color:rgba(255,184,108,.12)}}.card.pt:hover{{border-color:rgba(255,184,108,.28)}}
.ch{{padding:20px 20px 0;display:flex;align-items:center;justify-content:space-between;gap:10px}}
.cn{{font-family:'JetBrains Mono',monospace;font-size:15px;font-weight:500;color:var(--t);text-decoration:none}}
.cn:hover{{color:var(--ac)}}
.cn-ko{{font-family:'Outfit',sans-serif;font-size:13px;font-weight:400;color:var(--td)}}
.cm{{display:flex;gap:5px}}
.tg{{font-size:11px;padding:2px 9px;border-radius:100px;font-weight:500}}
.rbtn{{font-size:11px;padding:2px 9px;border-radius:100px;font-weight:500;cursor:pointer;
color:var(--td);border:1px solid var(--bd);background:rgba(255,255,255,.03);transition:all .2s}}
.rbtn:hover{{color:var(--ac);border-color:rgba(196,161,255,.3);background:var(--acg)}}
.tv{{color:var(--acd);border:1px solid rgba(196,161,255,.14);background:rgba(196,161,255,.06)}}
.tp{{color:var(--pt);border:1px solid rgba(255,184,108,.18);background:rgba(255,184,108,.08)}}
.cd{{padding:10px 20px 0;font-size:13.5px;color:var(--td);font-weight:300;line-height:1.6;
display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.cs{{padding:14px 20px 18px}}
.cst{{font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--tm);margin-bottom:8px}}
.stags{{display:flex;flex-wrap:wrap;gap:5px}}
.st{{font-family:'JetBrains Mono',monospace;font-size:12px;padding:4px 11px;border-radius:100px;
border:1px solid var(--bd);background:rgba(255,255,255,.02);color:var(--td);cursor:pointer;transition:all .18s}}
.st:hover{{background:var(--acg);border-color:rgba(196,161,255,.25);color:var(--ac);transform:translateY(-1px)}}
.pt .st:hover{{background:rgba(255,184,108,.07);border-color:rgba(255,184,108,.25);color:var(--pt)}}
.ce{{font-size:12px;color:var(--tm);font-style:italic}}

/* Side panel */
.ov{{position:fixed;inset:0;z-index:1000;background:rgba(0,0,0,.6);backdrop-filter:blur(6px);
opacity:0;pointer-events:none;transition:opacity .25s}}
.ov.open{{opacity:1;pointer-events:auto}}
.pn{{position:fixed;top:0;right:0;width:min(600px,92vw);height:100vh;background:var(--bg);
border-left:1px solid var(--bd);z-index:1001;transform:translateX(100%);
transition:transform .32s cubic-bezier(.22,1,.36,1);display:flex;flex-direction:column}}
.pn.open{{transform:translateX(0)}}
.ptop{{padding:18px 24px;border-bottom:1px solid var(--bd);display:flex;align-items:center;
justify-content:space-between;flex-shrink:0}}
.ptit{{display:flex;align-items:center;gap:10px}}
.ppb{{font-size:11px;padding:3px 10px;border-radius:100px;background:rgba(196,161,255,.08);
border:1px solid rgba(196,161,255,.15);color:var(--acd);font-weight:500}}
.pnm{{font-family:'JetBrains Mono',monospace;font-size:17px;font-weight:500}}
.px{{width:34px;height:34px;border-radius:50%;border:1px solid var(--bd);background:var(--s1);
color:var(--td);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s}}
.px:hover{{background:var(--s2);color:var(--t)}}
.pbody{{flex:1;overflow-y:auto;padding:28px}}

.ppath{{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--tm);margin-bottom:20px;
padding:10px 14px;background:var(--s1);border-radius:8px;border:1px solid var(--bd)}}
.pdlbl{{font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--tm);margin-bottom:6px}}
.pdtxt{{font-size:14px;color:var(--td);font-weight:300;line-height:1.7;margin-bottom:24px;
padding-bottom:20px;border-bottom:1px solid var(--bd)}}
.ftree{{list-style:none}}
.ftree li{{display:flex;align-items:center;gap:8px;padding:6px 12px;
font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--td);border-radius:8px;transition:background .15s}}
.ftree li:hover{{background:var(--s1)}}
.ftree li.sub{{padding-left:32px;color:var(--tm);font-size:12px}}
.ftree li.mdlink{{cursor:pointer}}
.ftree li.mdlink:hover{{background:var(--s2);color:var(--ac)}}
.fi{{width:16px;height:16px;flex-shrink:0;stroke:var(--tm);fill:none;stroke-width:1.5}}
.fi-md{{stroke:var(--ac)}}.fi-dir{{stroke:var(--pt)}}

/* Md popup */
.mdpop{{position:fixed;inset:0;z-index:2000;display:flex;align-items:center;justify-content:center;
background:rgba(0,0,0,.7);backdrop-filter:blur(8px);opacity:0;pointer-events:none;transition:opacity .25s}}
.mdpop.open{{opacity:1;pointer-events:auto}}
.mdbox{{width:min(780px,92vw);max-height:88vh;background:var(--bg);border:1px solid var(--bd);
border-radius:16px;display:flex;flex-direction:column;transform:scale(.96) translateY(12px);
transition:transform .3s cubic-bezier(.22,1,.36,1);box-shadow:0 24px 80px rgba(0,0,0,.5)}}
.mdpop.open .mdbox{{transform:scale(1) translateY(0)}}
.mdbox-top{{padding:16px 24px;border-bottom:1px solid var(--bd);display:flex;align-items:center;
justify-content:space-between;flex-shrink:0}}
.mdbox-file{{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--ac);display:flex;align-items:center;gap:8px}}
.mdbox-x{{width:30px;height:30px;border-radius:50%;border:1px solid var(--bd);background:var(--s1);
color:var(--td);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s}}
.mdbox-x:hover{{background:var(--s2);color:var(--t)}}
.mdbox-body{{flex:1;overflow-y:auto;padding:28px 32px 36px}}
.mdbox-loading{{text-align:center;padding:40px;color:var(--tm);font-size:14px}}

/* Rendered markdown */
.md{{font-size:14.5px;line-height:1.75;color:var(--td)}}
.md h1{{font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;color:var(--t);margin:24px 0 12px;line-height:1.3}}
.md h1:first-child{{margin-top:0}}
.md h2{{font-size:18px;font-weight:600;color:var(--t);margin:22px 0 10px}}
.md h3{{font-size:15px;font-weight:600;color:var(--t);margin:18px 0 8px}}
.md h4{{font-size:14px;font-weight:600;color:var(--t);margin:14px 0 6px}}
.md p{{margin-bottom:12px}}
.md strong{{color:var(--t);font-weight:500}}
.md a{{color:var(--ac);text-decoration:none;border-bottom:1px solid rgba(196,161,255,.3)}}
.md a:hover{{border-color:var(--ac)}}
.md ul,.md ol{{margin:10px 0;padding-left:22px}}
.md li{{margin-bottom:4px}}
.md li strong{{color:var(--t)}}
.md code{{font-family:'JetBrains Mono',monospace;font-size:12.5px;padding:2px 6px;border-radius:4px;
background:rgba(196,161,255,.07);color:var(--ac);border:1px solid rgba(196,161,255,.1)}}
.md pre{{margin:14px 0;padding:16px;background:var(--s1);border:1px solid var(--bd);border-radius:8px;overflow-x:auto}}
.md pre code{{padding:0;background:none;border:none;color:var(--td);font-size:12.5px;line-height:1.7}}
.md pre code .kw{{color:#c4a1ff}}.md pre code .str{{color:#a8e6a1}}.md pre code .num{{color:#ffb86c}}
.md pre code .cm{{color:#5c5b70;font-style:italic}}.md pre code .fn{{color:#7dcfff}}
.md pre code .op{{color:#e8e6f0}}.md pre code .dec{{color:#ff6b8a}}

/* raw file viewer */
.rawpre{{margin:0;padding:0;background:transparent;border:none}}
.rawpre code{{font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.75;color:var(--td);display:block}}
.rawpre code .kw{{color:#c4a1ff}}.rawpre code .str{{color:#a8e6a1}}.rawpre code .num{{color:#ffb86c}}
.rawpre code .cm{{color:#5c5b70;font-style:italic}}.rawpre code .fn{{color:#7dcfff}}
.rawpre code .op{{color:#e8e6f0}}.rawpre code .dec{{color:#ff6b8a}}
.md blockquote{{margin:14px 0;padding:10px 18px;border-left:3px solid var(--acd);background:var(--acg);border-radius:0 8px 8px 0}}
.md table{{width:100%;margin:14px 0;border-collapse:collapse;font-size:13px}}
.md th{{text-align:left;padding:8px 12px;border-bottom:2px solid var(--bd);color:var(--t);font-weight:600}}
.md td{{padding:8px 12px;border-bottom:1px solid var(--bd)}}
.md hr{{margin:20px 0;border:none;border-top:1px solid var(--bd)}}

.nores{{text-align:center;padding:60px 20px;color:var(--tm);font-size:15px;font-weight:300}}
footer{{text-align:center;padding:32px;font-size:12px;color:var(--tm);border-top:1px solid var(--bd)}}
footer a{{color:var(--acd);text-decoration:none}}

@media(max-width:768px){{
.hero{{padding:48px 20px 36px}}.bar{{padding:10px 16px;flex-wrap:wrap}}
.pills{{width:100%;overflow-x:auto}}.wrap{{padding:20px 16px 40px}}
.grid{{grid-template-columns:1fr}}.pn{{width:100vw}}.pbody{{padding:20px}}
.mdbox{{width:96vw;max-height:92vh}}.mdbox-body{{padding:20px}}
}}
</style>
</head>
<body>

<div class="hero">
  <div class="htag">지식 업무 플러그인</div>
  <h1>Claude <em>플러그인</em> 카탈로그</h1>
  <p class="hdesc">각 플러그인의 스킬을 탐색하세요. 스킬을 클릭하면 폴더 구조를 확인하고, .md 파일을 열어볼 수 있습니다.</p>
  <div class="hstats">
    <div><div class="hs-n">{len(data)}</div><div class="hs-l">플러그인</div></div>
    <div><div class="hs-n">{total}</div><div class="hs-l">스킬</div></div>
    <div><div class="hs-n">{anth}</div><div class="hs-l">Anthropic 제작</div></div>
    <div><div class="hs-n">{part}</div><div class="hs-l">파트너 제작</div></div>
  </div>
</div>

<div class="bar">
  <div class="swrap">
    <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
    <input type="text" id="q" placeholder="플러그인 또는 스킬 검색..." autocomplete="off">
  </div>
  <div class="pills">
    <button class="pill on" data-f="all">전체</button>
    <button class="pill" data-f="anthropic">Anthropic 제작</button>
    <button class="pill" data-f="partner">파트너 제작</button>
  </div>
</div>

<div class="wrap" id="out"></div>

<!-- Side panel -->
<div class="ov" id="ov"></div>
<div class="pn" id="pn">
  <div class="ptop">
    <div class="ptit"><span class="ppb" id="ppb"></span><span class="pnm" id="pnm"></span></div>
    <button class="px" id="px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18"/><path d="M6 6l12 12"/></svg></button>
  </div>
  <div class="pbody" id="pb"></div>
</div>

<!-- Md popup -->
<div class="mdpop" id="mdpop">
  <div class="mdbox">
    <div class="mdbox-top">
      <span class="mdbox-file" id="mdf"><svg class="fi fi-md" viewBox="0 0 24 24" width="16" height="16"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span id="mdfn"></span></span>
      <button class="mdbox-x" id="mdx"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18"/><path d="M6 6l12 12"/></svg></button>
    </div>
    <div class="mdbox-body" id="mdb"></div>
  </div>
</div>

<footer>Apache 2.0 &mdash; <a href="https://github.com/anthropics/knowledge-work-plugins">anthropics/knowledge-work-plugins</a></footer>

<script id="pdata" type="application/json">'''

    part2 = '''</script>
<script>
const P=JSON.parse(document.getElementById('pdata').textContent);
let fl='all';
const $=id=>document.getElementById(id);

document.querySelectorAll('.pill').forEach(b=>{{
  b.onclick=()=>{{document.querySelectorAll('.pill').forEach(p=>p.classList.remove('on'));
  b.classList.add('on');fl=b.dataset.f;draw();}};
}});
$('q').oninput=draw;

function draw(){{
  const q=$('q').value.toLowerCase().trim();
  const ls=P.filter(p=>{{
    if(fl==='anthropic'&&p.partner)return false;
    if(fl==='partner'&&!p.partner)return false;
    if(!q)return true;
    if(p.name.includes(q)||p.desc.toLowerCase().includes(q))return true;
    return p.skills.some(s=>s.name.includes(q)||s.desc.toLowerCase().includes(q));
  }});
  if(!ls.length){{$('out').innerHTML='<div class="nores">검색 결과가 없습니다.</div>';return;}}
  const a=ls.filter(p=>!p.partner),b=ls.filter(p=>p.partner);
  let o='';
  if(a.length){{o+=`<div class="slbl">Anthropic 제작 &mdash; ${{a.length}}개</div><div class="grid">`;a.forEach(p=>{{o+=card(p)}});o+='</div>';}}
  if(b.length){{o+=`<div class="slbl">파트너 제작 &mdash; ${{b.length}}개</div><div class="grid">`;b.forEach(p=>{{o+=card(p)}});o+='</div>';}}
  $('out').innerHTML=o;
  $('out').querySelectorAll('.st').forEach(el=>{{
    el.onclick=()=>openPanel(P[+el.dataset.p],P[+el.dataset.p].skills[+el.dataset.s]);
  }});
  $('out').querySelectorAll('.rbtn:not(.fbtn)').forEach(el=>{{
    el.onclick=e=>{{e.stopPropagation();showContent(P[+el.dataset.pi].readme,'README.md');}};
  }});
  $('out').querySelectorAll('.fbtn').forEach(el=>{{
    el.onclick=e=>{{e.stopPropagation();openPluginFiles(P[+el.dataset.pi]);}};
  }});
}}

function card(p){{
  const pi=P.indexOf(p),c=p.partner?' pt':'';
  let sk='';
  if(!p.skills.length) sk='<div class="ce">MCP 서버 전용 (스킬 없음)</div>';
  else sk='<div class="stags">'+p.skills.map((s,si)=>
    `<span class="st" data-p="${{pi}}" data-s="${{si}}">${{esc(s.label||s.name)}}</span>`).join('')+'</div>';
  const ghUrl='https://github.com/yoon-gu/knowledge-work-plugins/tree/main/'+p.rel;
  const nameLabel=p.nameKo?esc(p.name)+' <span class="cn-ko">('+esc(p.nameKo)+')</span>':esc(p.name);
  const readmeBtn=p.readme?`<span class="rbtn" data-pi="${{pi}}">README</span>`:'';
  const folderBtn=p.rootFiles.length?`<span class="rbtn fbtn" data-pi="${{pi}}">폴더</span>`:'';
  return `<div class="card${{c}}"><div class="ch"><a class="cn" href="${{ghUrl}}" target="_blank">${{nameLabel}}</a>
    <div class="cm">${{folderBtn}}${{readmeBtn}}<span class="tg tv">v${{p.ver}}</span>
    ${{p.partner?`<span class="tg tp">${{esc(p.author)}}</span>`:''}}</div></div>
    <div class="cd">${{esc(p.desc)}}</div>
    <div class="cs"><div class="cst">스킬 &middot; ${{p.skills.length}}개</div>${{sk}}</div></div>`;
}}

function renderFileTree(files){{
  let o='<ul class="ftree">';
  files.forEach((f,fi)=>{{
    const raw=f.name.trimStart();
    const isSub=f.name.startsWith('  ');
    const isDir=f.dir;
    const isMd=raw.endsWith('.md');
    const hasContent=!isDir&&f.content;
    const ic=isDir?'fi-dir':isMd?'fi-md':'';
    const cls=[isSub?'sub':'',hasContent?'mdlink':''].filter(Boolean).join(' ');
    const dattr=hasContent?` data-fi="${{fi}}" data-fname="${{esc(raw)}}"`:'';
    const svg=isDir
      ?`<svg class="fi fi-dir" viewBox="0 0 24 24"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>`
      :`<svg class="fi ${{ic}}" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`;
    o+=`<li class="${{cls}}"${{dattr}}>${{svg}}${{esc(raw)}}</li>`;
  }});
  o+='</ul>';
  return o;
}}

function bindFileClicks(files){{
  $('pb').querySelectorAll('.mdlink').forEach(el=>{{
    el.onclick=()=>{{
      const fi=+el.dataset.fi;
      showContent(files[fi].content,el.dataset.fname);
    }};
  }});
}}

function openPluginFiles(plugin){{
  $('ppb').textContent=plugin.name;
  $('pnm').textContent=plugin.nameKo||'파일';
  let o=`<div class="ppath">${{esc(plugin.rel)}}/</div>`;
  o+=`<div class="pdlbl">파일 구조</div>`;
  o+=renderFileTree(plugin.rootFiles);
  $('pb').innerHTML=o;
  bindFileClicks(plugin.rootFiles);
  $('ov').classList.add('open');$('pn').classList.add('open');
  document.body.style.overflow='hidden';
}}

function openPanel(plugin,skill){{
  $('ppb').textContent=plugin.name;
  $('pnm').textContent=skill.name;
  let o=`<div class="ppath">skills/${{esc(skill.dir)}}/</div>`;
  if(skill.desc) o+=`<div class="pdlbl">설명</div><div class="pdtxt">${{esc(skill.desc)}}</div>`;
  if(skill.files.length){{
    o+=`<div class="pdlbl">파일 구조</div>`;
    o+=renderFileTree(skill.files);
  }}
  $('pb').innerHTML=o;
  bindFileClicks(skill.files);
  $('ov').classList.add('open');$('pn').classList.add('open');
  document.body.style.overflow='hidden';
}}

function closePanel(){{
  $('ov').classList.remove('open');$('pn').classList.remove('open');
  document.body.style.overflow='';
}}
$('px').onclick=closePanel;
$('ov').onclick=closePanel;

// --- File popup (reads from embedded data) ---
function showContent(txt,fname){{
  $('mdfn').textContent=fname;
  $('mdpop').classList.add('open');
  if(fname.endsWith('.md')){{
    // strip frontmatter
    if(txt.startsWith('---')){{const p=txt.split('---',3);if(p.length>=3) txt=p[2].trim();}}
    $('mdb').innerHTML='<div class="md">'+mdToHtml(txt)+'</div>';
  }}else{{
    const lang=extToLang(fname);
    $('mdb').innerHTML='<pre class="rawpre"><code>'+highlight(esc(txt),lang)+'</code></pre>';
  }}
}}

function extToLang(f){{
  if(f.endsWith('.py'))return 'python';
  if(f.endsWith('.js'))return 'js';
  if(f.endsWith('.ts'))return 'js';
  if(f.endsWith('.json'))return 'json';
  if(f.endsWith('.sh'))return 'bash';
  if(f.endsWith('.yml')||f.endsWith('.yaml'))return 'yaml';
  return 'text';
}}

function closeMd(){{$('mdpop').classList.remove('open');}}
$('mdx').onclick=closeMd;
$('mdpop').onclick=e=>{{if(e.target===$('mdpop'))closeMd();}};
document.onkeydown=e=>{{
  if(e.key==='Escape'){{
    if($('mdpop').classList.contains('open')) closeMd();
    else closePanel();
  }}
}};

// --- Markdown parser ---
function mdToHtml(s){{
  // code blocks first
  let blocks=[];
  s=s.replace(/```(\\w*)\\n([\\s\\S]*?)```/g,(_,lang,code)=>{{
    const l=lang||'text';
    blocks.push('<pre><code>'+highlight(esc(code.replace(/\\n$/,'')),l)+'</code></pre>');
    return '\\x00BLK'+(blocks.length-1)+'\\x00';
  }});
  const lines=s.split('\\n');
  let out='',inUl=false,inOl=false,inTbl=false,inBq=false,tblHead=true;
  function endList(){{if(inUl){{out+='</ul>';inUl=false;}}if(inOl){{out+='</ol>';inOl=false;}}}}
  function endTbl(){{if(inTbl){{out+='</tbody></table>';inTbl=false;}}}}
  function endBq(){{if(inBq){{out+='</blockquote>';inBq=false;}}}}

  for(let i=0;i<lines.length;i++){{
    let L=lines[i];
    // block placeholder
    const bm=L.match(/^\\x00BLK(\\d+)\\x00$/);
    if(bm){{endList();endTbl();endBq();out+=blocks[+bm[1]];continue;}}
    // table row
    if(L.match(/^\\|.*\\|\\s*$/)){{
      endList();endBq();
      if(!inTbl){{out+='<table><thead>';inTbl=true;tblHead=true;}}
      if(L.match(/^\\|[\\s\\-:|]+\\|\\s*$/)){{
        if(tblHead){{out+='</thead><tbody>';tblHead=false;}}
        continue;
      }}
      const cells=L.split('|').slice(1,-1).map(c=>c.trim());
      const tag=tblHead?'th':'td';
      out+='<tr>'+cells.map(c=>'<'+tag+'>'+inline(c)+'</'+tag+'>').join('')+'</tr>';
      continue;
    }}
    endTbl();
    // blockquote
    if(L.match(/^>\\s?/)){{
      endList();
      if(!inBq){{out+='<blockquote>';inBq=true;}}
      out+=inline(L.replace(/^>\\s?/,''))+'<br>';
      continue;
    }}
    endBq();
    // hr
    if(L.match(/^(---+|\\*\\*\\*+|___+)\\s*$/)){{endList();out+='<hr>';continue;}}
    // heading
    const hm=L.match(/^(#{{1,4}})\\s+(.*)/);
    if(hm){{endList();const lv=hm[1].length;out+='<h'+lv+'>'+inline(hm[2])+'</h'+lv+'>';continue;}}
    // unordered list
    if(L.match(/^\\s*[-*+]\\s/)){{
      if(!inUl){{endList();out+='<ul>';inUl=true;}}
      out+='<li>'+inline(L.replace(/^\\s*[-*+]\\s/,''))+'</li>';continue;
    }}
    // ordered list
    if(L.match(/^\\s*\\d+\\.\\s/)){{
      if(!inOl){{endList();out+='<ol>';inOl=true;}}
      out+='<li>'+inline(L.replace(/^\\s*\\d+\\.\\s/,''))+'</li>';continue;
    }}
    endList();
    if(!L.trim())continue;
    out+='<p>'+inline(L)+'</p>';
  }}
  endList();endTbl();endBq();
  return out;
}}

function inline(s){{
  s=esc(s);
  s=s.replace(/!\\[([^\\]]*)\\]\\(([^)]+)\\)/g,'<img src="$2" alt="$1">');
  s=s.replace(/\\[([^\\]]*)\\]\\(([^)]+)\\)/g,'<a href="$2" target="_blank">$1</a>');
  s=s.replace(/\\*\\*\\*(.+?)\\*\\*\\*/g,'<strong><em>$1</em></strong>');
  s=s.replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>');
  s=s.replace(/\\*(.+?)\\*/g,'<em>$1</em>');
  s=s.replace(/`([^`]+)`/g,'<code>$1</code>');
  s=s.replace(/~~(.+?)~~/g,'<del>$1</del>');
  return s;
}}

// --- Syntax highlighting (operates on already-escaped text) ---
function highlight(s,lang){{
  if(lang==='json'){{
    s=s.replace(/(&quot;[^&]*?&quot;)\\s*:/g,'<span class="fn">$1</span>:');
    s=s.replace(/:[ ]*(&quot;[^&]*?&quot;)/g,': <span class="str">$1</span>');
    s=s.replace(/\\b(true|false|null)\\b/g,'<span class="kw">$1</span>');
    s=s.replace(/\\b(\\d+\\.?\\d*)\\b/g,'<span class="num">$1</span>');
    return s;
  }}
  if(lang==='python'||lang==='py'){{
    s=s.replace(/(#[^\\n]*)/g,'<span class="cm">$1</span>');
    s=s.replace(/((?:&quot;{{3}}|&#x27;{{3}})[\\s\\S]*?(?:&quot;{{3}}|&#x27;{{3}}))/g,'<span class="str">$1</span>');
    s=s.replace(/(&quot;(?:[^&\\\\]|&[^q]|\\\\.)*)(&quot;)/g,'<span class="str">$1$2</span>');
    s=s.replace(/(&#x27;(?:[^&\\\\]|&[^#]|\\\\.)*)&#x27;/g,'<span class="str">$1&#x27;</span>');
    s=s.replace(/\\b(def|class|import|from|return|if|elif|else|for|while|try|except|finally|with|as|yield|lambda|pass|break|continue|raise|in|not|and|or|is|None|True|False|self|async|await|print)\\b/g,'<span class="kw">$1</span>');
    s=s.replace(/\\b(def|class)\\s+([\\w]+)/g,'<span class="kw">$1</span> <span class="fn">$2</span>');
    s=s.replace(/@([\\w.]+)/g,'<span class="dec">@$1</span>');
    s=s.replace(/\\b(\\d+\\.?\\d*)\\b/g,'<span class="num">$1</span>');
    return s;
  }}
  if(lang==='js'||lang==='javascript'||lang==='ts'||lang==='typescript'){{
    s=s.replace(/(\/\/[^\\n]*)/g,'<span class="cm">$1</span>');
    s=s.replace(/(&quot;(?:[^&\\\\]|&[^q]|\\\\.)*)(&quot;)/g,'<span class="str">$1$2</span>');
    s=s.replace(/(&#x27;(?:[^&\\\\]|&[^#]|\\\\.)*)&#x27;/g,'<span class="str">$1&#x27;</span>');
    s=s.replace(/\\b(const|let|var|function|return|if|else|for|while|class|import|export|from|default|new|this|async|await|try|catch|throw|switch|case|break|continue|typeof|instanceof|true|false|null|undefined)\\b/g,'<span class="kw">$1</span>');
    s=s.replace(/\\b(function)\\s+([\\w]+)/g,'<span class="kw">$1</span> <span class="fn">$2</span>');
    s=s.replace(/\\b(\\d+\\.?\\d*)\\b/g,'<span class="num">$1</span>');
    return s;
  }}
  if(lang==='bash'||lang==='sh'||lang==='shell'||lang==='zsh'){{
    s=s.replace(/(#[^\\n]*)/g,'<span class="cm">$1</span>');
    s=s.replace(/(&quot;(?:[^&\\\\]|&[^q]|\\\\.)*)(&quot;)/g,'<span class="str">$1$2</span>');
    s=s.replace(/\\b(if|then|else|elif|fi|for|do|done|while|case|esac|function|return|export|source|local|echo|cd|ls|mkdir|rm|cp|mv|cat|grep|sed|awk|curl|wget|sudo|pip|npm|git|python3?|node)\\b/g,'<span class="kw">$1</span>');
    return s;
  }}
  if(lang==='yaml'||lang==='yml'){{
    s=s.replace(/(#[^\\n]*)/g,'<span class="cm">$1</span>');
    s=s.replace(/^([ ]*[\\w][\\w\\-. ]*?):/gm,'<span class="fn">$1</span>:');
    s=s.replace(/:\\s*(&quot;.*?&quot;)/g,': <span class="str">$1</span>');
    s=s.replace(/\\b(true|false|null|yes|no)\\b/g,'<span class="kw">$1</span>');
    s=s.replace(/\\b(\\d+\\.?\\d*)\\b/g,'<span class="num">$1</span>');
    return s;
  }}
  return s;
}}

function esc(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}}

draw();
</script>
</body>
</html>'''

    # part2는 일반 string이므로 f-string용 이중괄호를 단일괄호로 복원
    part2 = part2.replace('{{', '{').replace('}}', '}')
    return part1 + js + part2


if __name__ == '__main__':
    plugins = find_plugins()
    html = build(plugins)
    out = os.path.join(REPO, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    total = sum(len(p['skills']) for p in plugins)
    print(f'Built: {len(plugins)} plugins, {total} skills -> {out}')
