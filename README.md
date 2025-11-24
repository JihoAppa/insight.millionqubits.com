# 지호아빠의 딥(Deep) 블로깅

기술과 생각을 기록하는 공간입니다.

## 🌐 사이트 정보

- **URL**: https://paper.millionqubits.com
- **테마**: [Hugo PaperMod](https://github.com/adityatelange/hugo-PaperMod)
- **언어**: 한국어 / English

## 📝 로컬에서 실행하기

### 사전 요구사항

- Hugo Extended v0.138.0 이상
- Git

### 설치 및 실행

```bash
# 저장소 클론
git clone https://github.com/yourusername/paper.millionqubits.com.git
cd paper.millionqubits.com

# 서브모듈 초기화 (테마)
git submodule update --init --recursive

# 로컬 서버 실행
hugo server -D
```

브라우저에서 http://localhost:1313 을 열어 확인하세요.

## 📂 프로젝트 구조

```
.
├── .github/
│   └── workflows/
│       └── hugo.yml          # GitHub Actions 자동 배포
├── archetypes/
│   └── default.md            # 새 포스트 템플릿
├── assets/
│   └── css/
│       └── extended/
│           └── custom.css    # 커스텀 스타일
├── content/
│   ├── posts/                # 블로그 포스트 (*.ko.md, *.en.md)
│   ├── docs-examples/        # 예제 포스트 (블로그에 표시 안 됨)
│   ├── archives.*.md         # 아카이브 페이지
│   └── search.*.md           # 검색 페이지
├── docs/                     # 문서 (블로그에 표시 안 됨)
│   ├── DEPLOYMENT.md         # 배포 가이드
│   ├── DNS_SETUP.md          # DNS 설정 가이드
│   ├── OBSIDIAN_SETUP.md     # Obsidian 플러그인 설정
│   └── OBSIDIAN_INTEGRATION.md  # Obsidian 연동 완벽 가이드
├── static/
│   ├── CNAME                 # 커스텀 도메인 설정
│   └── images/               # 이미지 파일
├── themes/
│   └── PaperMod/             # 테마 (서브모듈)
└── hugo.yaml                 # Hugo 설정 파일
```

## ✍️ 새 포스트 작성하기

### 파일명 규칙

이 블로그는 **파일명 기반 다국어 지원**을 사용합니다:

```bash
content/posts/
├── my-post.ko.md    # 한국어 버전
└── my-post.en.md    # 영어 버전
```

### Hugo CLI 사용

```bash
# 한국어 포스트
hugo new content/posts/my-post.ko.md

# 영어 포스트
hugo new content/posts/my-post.en.md
```

### Obsidian 연동 (권장)

**자세한 가이드**:
- [⚡ 간단 워크플로우 - 동기화 버튼 한 번으로 발행](docs/OBSIDIAN_SIMPLE_WORKFLOW.md) ⭐
- [🤖 제목 기반 자동 파일명 생성](docs/OBSIDIAN_AUTO_FILENAME.md) ⭐ **NEW!**
- [완벽한 Obsidian 연동 가이드](docs/OBSIDIAN_INTEGRATION.md)
- [템플릿 가이드](docs/TEMPLATES_README.md)

**빠른 시작 (동기화 버튼 방식)**:
1. Obsidian vault의 `블로그/` 폴더를 Hugo `content/posts/`와 연결
2. Obsidian Git 플러그인 설치 및 설정
3. `초안/` 폴더에서 글 작성
4. 완성되면 `블로그/` 폴더로 이동
5. **동기화 버튼 (⚡) 한 번 클릭** → 자동 발행!

## 🚀 배포

### 자동 배포 (GitHub Actions)

`main` 브랜치에 push하면 자동으로 GitHub Pages에 배포됩니다.

```bash
git add .
git commit -m "Add new post"
git push origin main
```

### GitHub Pages 설정

1. GitHub 저장소 설정 > Pages
2. Source: GitHub Actions
3. Custom domain: `paper.millionqubits.com` 설정
4. Enforce HTTPS 체크

## 🌍 DNS 설정

DNS 제공자(Cloudflare, 가비아 등)에서 다음 레코드 추가:

### CNAME 방식 (권장)

```
Type: CNAME
Name: paper
Content: yourusername.github.io
```

### A 레코드 방식

```
Type: A
Name: @
Content: 185.199.108.153
```

추가 A 레코드:
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

## 🔧 Hugo 설정

주요 설정은 `hugo.yaml`에서 관리합니다:

- 기본 URL
- 다국어 설정
- 메뉴 구성
- 테마 파라미터
- 검색 기능

## 📚 문서

### Obsidian 관련
- [⚡ **간단 워크플로우** - 동기화 버튼으로 발행](docs/OBSIDIAN_SIMPLE_WORKFLOW.md) ⭐ **추천!**
- [🤖 **제목 기반 자동 파일명 생성**](docs/OBSIDIAN_AUTO_FILENAME.md) ⭐ **NEW!**
- [Obsidian 연동 완벽 가이드](docs/OBSIDIAN_INTEGRATION.md)
- [Obsidian 플러그인 설정](docs/OBSIDIAN_SETUP.md)
- [템플릿 가이드 및 예시](docs/TEMPLATES_README.md)

### 배포 관련
- [배포 가이드](docs/DEPLOYMENT.md)
- [DNS 설정](docs/DNS_SETUP.md)
- [문제 해결 가이드](docs/TROUBLESHOOTING.md) 🔧

## 🎨 디자인 커스터마이징

커스텀 스타일은 `assets/css/extended/custom.css`에서 관리합니다.

현재 적용된 타이포그래피:
- Font: Lora (영어), Noto Serif KR (한국어)
- Font size: 16.96px
- Line height: 28.832px
- Text align: justify (양쪽 정렬)
- 본문 너비: 680px

## 📧 연락처

협업 및 연구 관련 문의: jiho_appa@naver.com

## 📄 라이선스

이 블로그의 콘텐츠는 저작권으로 보호됩니다.

