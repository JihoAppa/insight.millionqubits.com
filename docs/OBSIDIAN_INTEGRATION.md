# Obsidian 연동 완벽 가이드

Hugo 블로그와 Obsidian을 연동하여 효율적으로 블로그 포스트를 작성하고 발행하는 방법을 안내합니다.

## 📋 목차

1. [개요](#개요)
2. [권장 워크플로우](#권장-워크플로우)
3. [Obsidian 설정](#obsidian-설정)
4. [포스트 작성 템플릿](#포스트-작성-템플릿)
5. [발행 프로세스](#발행-프로세스)
6. [이미지 및 첨부파일 관리](#이미지-및-첨부파일-관리)
7. [문제 해결](#문제-해결)

---

## 개요

이 블로그는 다음과 같은 구조로 설계되었습니다:

```
paper.millionqubits.com/
├── content/
│   ├── posts/          # 실제 블로그 포스트 (한/영)
│   ├── docs-examples/  # 예제 및 테스트 포스트
│   ├── archives.*.md   # 아카이브 페이지
│   └── search.*.md     # 검색 페이지
├── static/
│   └── images/         # 이미지 파일
└── docs/               # 문서 (블로그에 표시 안 됨)
```

### 파일 명명 규칙

Hugo는 파일명 기반 다국어 지원을 사용합니다:

- `post-name.ko.md` - 한국어 버전
- `post-name.en.md` - 영어 버전

---

## 권장 워크플로우

### 방법 1: 심볼릭 링크 (가장 간단, 권장)

Obsidian vault와 Hugo content 폴더를 심볼릭 링크로 연결합니다.

#### 1단계: 심볼릭 링크 생성

```bash
# Obsidian vault의 특정 폴더를 Hugo posts 폴더로 링크
ln -s "/Users/user/Vaults/appa-core-vault/공개저널/블로그" \
      "/Users/user/Websites/paper.millionqubits.com/content/posts"
```

#### 2단계: Obsidian에서 작성

- Obsidian에서 `공개저널/블로그` 폴더에 포스트 작성
- 파일명은 `my-post.ko.md` 또는 `my-post.en.md` 형식 사용
- 자동으로 Hugo `content/posts/` 폴더에 반영됨

#### 3단계: 로컬 미리보기

```bash
cd /Users/user/Websites/paper.millionqubits.com
hugo server -D
```

브라우저에서 http://localhost:1313 접속하여 확인

#### 4단계: 발행

```bash
# content/posts 폴더로 이동 (실제로는 Obsidian vault)
cd /Users/user/Websites/paper.millionqubits.com
git add content/posts/
git commit -m "Add: 새 포스트 제목"
git push origin main
```

### 방법 2: Obsidian Git 플러그인 (자동화)

Obsidian에서 자동으로 Git 커밋/푸시를 처리합니다.

#### 1단계: Obsidian Git 플러그인 설치

1. Obsidian 설정 (`Cmd/Ctrl + ,`)
2. Community plugins → Browse
3. "Obsidian Git" 검색 및 설치
4. 플러그인 활성화

#### 2단계: Git 저장소 연결

```bash
# Obsidian vault를 Git 저장소로 초기화 (한 번만)
cd /Users/user/Vaults/appa-core-vault
git init
git remote add blog https://github.com/yourusername/paper.millionqubits.com.git
```

#### 3단계: Obsidian Git 설정

Obsidian 설정 → Obsidian Git:

- **Vault backup interval (minutes)**: 10 (10분마다 자동 커밋)
- **Auto pull interval (minutes)**: 10 (10분마다 원격 변경사항 가져오기)
- **Commit message**: `vault backup: {{date}}`
- **Auto push**: 활성화

#### 4단계: 워크플로우

1. Obsidian에서 포스트 작성
2. 10분마다 자동으로 커밋/푸시
3. GitHub Actions가 자동으로 배포
4. 5-10분 후 https://paper.millionqubits.com 에 반영

---

## Obsidian 설정

### 필수 설정

#### 파일 및 링크 설정

Obsidian 설정 → Files & Links:

```yaml
Default location for new attachments: In subfolder under current folder
Subfolder name: images
Use [[Wikilinks]]: OFF (비활성화 - Hugo는 표준 마크다운 사용)
```

#### 폴더 구조

Obsidian vault 내 권장 구조:

```
appa-core-vault/
├── 공개저널/
│   ├── 블로그/              # Hugo content/posts/와 연결
│   │   ├── my-post.ko.md
│   │   ├── my-post.en.md
│   │   └── images/
│   │       └── my-image.png
│   └── .templates/          # 템플릿 폴더
│       ├── hugo-post-ko.md
│       └── hugo-post-en.md
└── 비공개/                   # 블로그에 표시 안 됨
```

### 추천 플러그인

1. **Templater** (필수)
   - 포스트 템플릿 자동화
   - 날짜, 파일명 등 자동 입력

2. **Obsidian Git** (선택)
   - 자동 Git 커밋/푸시

3. **Linter** (선택)
   - 마크다운 포맷 자동 정리

4. **Paste Image Rename** (선택)
   - 이미지 붙여넣기 시 자동 이름 변경

---

## 포스트 작성 템플릿

### 한국어 포스트 템플릿 (`hugo-post-ko.md`)

```markdown
---
title: "{{title}}"
date: {{date:YYYY-MM-DDTHH:mm:ssZ}}
draft: true
tags: []
categories: []
author: "Jiho's Dad"
description: ""
---

## 개요

이곳에 포스트 내용을 작성하세요.

## 본문

### 섹션 1

내용...

### 섹션 2

내용...

## 결론

요약...
```

### 영어 포스트 템플릿 (`hugo-post-en.md`)

```markdown
---
title: "{{title}}"
date: {{date:YYYY-MM-DDTHH:mm:ssZ}}
draft: true
tags: []
categories: []
author: "Jiho's Dad"
description: ""
---

## Overview

Write your post content here.

## Main Content

### Section 1

Content...

### Section 2

Content...

## Conclusion

Summary...
```

### Front Matter 필드 설명

| 필드 | 필수 | 설명 | 예시 |
|------|------|------|------|
| `title` | ✅ | 포스트 제목 | "My First Post" |
| `date` | ✅ | 발행 날짜 | 2024-11-24T10:00:00+09:00 |
| `draft` | ✅ | 초안 여부 (true: 숨김) | false |
| `tags` | ⭕ | 태그 목록 | ["Python", "AI"] |
| `categories` | ⭕ | 카테고리 | ["Programming"] |
| `author` | ⭕ | 작성자 | "Jiho's Dad" |
| `description` | ⭕ | 포스트 요약 (SEO) | "Learn Python basics" |
| `cover.image` | ⭕ | 커버 이미지 경로 | "/images/cover.png" |

---

## 발행 프로세스

### 로컬 테스트

#### 1. 초안 포스트 확인

```bash
cd /Users/user/Websites/paper.millionqubits.com
hugo server -D  # -D: 초안(draft) 포함
```

→ http://localhost:1313 접속

#### 2. 발행 버전 확인

```bash
hugo server  # 초안 제외
```

### 발행하기

#### 방법 1: Manual Git

```bash
cd /Users/user/Websites/paper.millionqubits.com
git add content/posts/my-post.ko.md content/posts/my-post.en.md
git commit -m "Add: My Post Title"
git push origin main
```

#### 방법 2: Obsidian Git 사용

1. Obsidian 명령 팔레트 (`Cmd/Ctrl + P`)
2. "Obsidian Git: Commit all changes" 실행
3. "Obsidian Git: Push" 실행

#### 자동 배포 확인

- GitHub Actions: https://github.com/yourusername/paper.millionqubits.com/actions
- 배포 완료 시간: 약 2-5분
- 사이트 확인: https://paper.millionqubits.com

---

## 이미지 및 첨부파일 관리

### 이미지 추가하기

#### 1. Obsidian에서 이미지 붙여넣기

포스트 폴더 내 `images/` 서브폴더에 자동 저장됨:

```
content/posts/
├── my-post.ko.md
├── my-post.en.md
└── images/
    └── screenshot.png
```

#### 2. 마크다운에서 참조

```markdown
# 상대 경로 (권장)
![스크린샷](images/screenshot.png)

# 절대 경로 (static 폴더 사용 시)
![스크린샷](/images/screenshot.png)
```

#### 3. Hugo static 폴더로 이동 (선택)

전역적으로 사용할 이미지는 `static/images/`로 이동:

```bash
mv content/posts/images/logo.png static/images/
```

### 커버 이미지 설정

Front matter에 추가:

```yaml
---
title: "My Post"
cover:
  image: "/images/my-cover.png"
  alt: "Cover image description"
  caption: "Photo by Someone"
---
```

---

## 문제 해결

### 포스트가 표시되지 않음

#### 체크리스트

1. **Draft 상태 확인**
   ```yaml
   draft: false  # true이면 표시 안 됨
   ```

2. **날짜 확인**
   ```yaml
   # 미래 날짜는 표시 안 됨
   date: 2024-11-24T10:00:00+09:00
   ```

3. **파일명 확인**
   ```bash
   # 올바른 형식
   my-post.ko.md  # 한국어
   my-post.en.md  # 영어
   ```

4. **Front Matter 형식**
   ```yaml
   ---
   title: "Title"  # 따옴표 필수
   ---
   ```

### 이미지가 표시되지 않음

```bash
# 경로 확인
content/posts/my-post.ko.md
content/posts/images/screenshot.png  # ✅ 상대 경로
static/images/screenshot.png         # ✅ 절대 경로

# 마크다운
![이미지](images/screenshot.png)     # ✅ 상대 경로
![이미지](/images/screenshot.png)    # ✅ 절대 경로
```

### Git 충돌 해결

```bash
# 1. 현재 변경사항 임시 저장
git stash

# 2. 원격 변경사항 가져오기
git pull origin main

# 3. 임시 저장한 변경사항 적용
git stash pop

# 4. 충돌 해결 후
git add .
git commit -m "Resolve merge conflict"
git push origin main
```

### Hugo 서버 오류

```bash
# 캐시 삭제
rm -rf public/ resources/

# 서버 재시작
hugo server -D
```

---

## 고급 팁

### 다국어 포스트 링크

한국어 포스트에서 영어 버전 링크:

```yaml
---
# my-post.ko.md
title: "내 포스트"
---

[Read in English](/en/posts/my-post/)
```

### 포스트 시리즈

```yaml
---
title: "Python 기초 - Part 1"
series: ["Python Tutorial"]
tags: ["Python", "Tutorial"]
---
```

### 목차 비활성화

```yaml
---
title: "Short Post"
ShowToc: false
---
```

### 댓글 시스템 (추후 추가 가능)

```yaml
---
title: "My Post"
comments: true
---
```

---

## 유용한 명령어

```bash
# 새 포스트 생성 (Hugo CLI)
hugo new content/posts/my-post.ko.md

# 로컬 서버 (초안 포함)
hugo server -D

# 로컬 서버 (발행된 포스트만)
hugo server

# 빌드 (public 폴더 생성)
hugo

# 빌드 (초안 포함)
hugo -D

# Git 상태 확인
git status

# 전체 커밋 및 푸시
git add . && git commit -m "Update posts" && git push origin main
```

---

## 참고 자료

- [Hugo 공식 문서](https://gohugo.io/documentation/)
- [PaperMod 테마 위키](https://github.com/adityatelange/hugo-PaperMod/wiki)
- [Obsidian 공식 문서](https://help.obsidian.md/)
- [Markdown 가이드](https://www.markdownguide.org/)

---

## 연락처

질문이나 문제가 있으면 이메일로 연락주세요: jiho_appa@naver.com

