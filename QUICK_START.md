# 🚀 빠른 시작 가이드

이 문서는 Hugo 블로그를 빠르게 시작할 수 있도록 핵심 단계만 정리했습니다.

---

## ✅ 현재 상태

프로젝트 설정이 완료되었습니다! 다음 단계만 진행하면 블로그가 운영됩니다.

### 완료된 작업
- ✅ Hugo 프로젝트 구조 생성
- ✅ 한영 이중언어 설정
- ✅ PaperMod 테마 적용
- ✅ GitHub Actions 자동 배포 설정
- ✅ Obsidian 템플릿 생성
- ✅ 콘텐츠 디렉토리 구조 완성
- ✅ 문서화 완료

---

## 📋 다음 단계 (5단계)

### 1️⃣ GitHub 저장소 생성 및 업로드 (5분)

```bash
# GitHub에서 새 저장소 생성: paper.millionqubits.com

# 터미널에서 실행 (yourusername을 본인의 GitHub 사용자명으로 변경)
cd /Users/user/Websites/paper.millionqubits.com
git remote add origin https://github.com/yourusername/paper.millionqubits.com.git
git push -u origin main
```

**상세 가이드**: [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md)

---

### 2️⃣ GitHub Pages 활성화 (2분)

1. GitHub 저장소 > **Settings** > **Pages**
2. **Source**: **GitHub Actions** 선택
3. 2-5분 대기 (자동 배포)
4. `https://yourusername.github.io/` 접속하여 확인

---

### 3️⃣ DNS 설정 (10분 + 전파 시간)

DNS 제공자(Cloudflare, 가비아 등)에서:

```
Type: CNAME
Name: paper
Target: yourusername.github.io
```

**상세 가이드**: [`docs/DNS_SETUP.md`](docs/DNS_SETUP.md)

---

### 4️⃣ 커스텀 도메인 연결 (2분)

1. GitHub 저장소 > **Settings** > **Pages**
2. **Custom domain**: `paper.millionqubits.com` 입력
3. DNS 전파 대기 (10분~24시간)
4. **Enforce HTTPS** 체크

---

### 5️⃣ Obsidian 연동 (10분)

**옵션 A - Obsidian Git 플러그인 (권장)**

1. Obsidian에서 "Obsidian Git" 플러그인 설치
2. 자동 커밋/푸시 설정
3. 작성 후 자동 배포

**옵션 B - 수동 복사**

```bash
# Obsidian에서 작성 후
cp "/Users/user/Vaults/appa-core-vault/공개저널/포스트.md" \
   "/Users/user/Websites/paper.millionqubits.com/content/ko/posts/"

cd /Users/user/Websites/paper.millionqubits.com
git add .
git commit -m "Add new post"
git push
```

**상세 가이드**: [`docs/OBSIDIAN_SETUP.md`](docs/OBSIDIAN_SETUP.md)

---

## 📝 첫 포스트 작성하기

### 방법 1: Hugo CLI

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 한국어 포스트
hugo new content/ko/posts/my-first-post.md

# 영어 포스트
hugo new content/en/posts/my-first-post.md
```

### 방법 2: Obsidian 템플릿

1. Obsidian에서 새 노트 생성
2. 템플릿 삽입:
   - 한국어: `hugo-post-ko.md`
   - 영어: `hugo-post-en.md`
3. 내용 작성
4. `draft: false`로 변경
5. 배포 (Git 푸시 또는 Obsidian Git 플러그인)

---

## 🔍 로컬 미리보기

```bash
cd /Users/user/Websites/paper.millionqubits.com
hugo server -D
```

브라우저에서 http://localhost:1313 열기

---

## 🌐 사이트 URL

- **GitHub Pages**: `https://yourusername.github.io/paper.millionqubits.com`
- **커스텀 도메인**: `https://paper.millionqubits.com`

---

## 📂 주요 파일 위치

```
프로젝트/
├── hugo.yaml                 # 사이트 설정
├── content/
│   ├── ko/posts/             # 한국어 포스트
│   └── en/posts/             # 영어 포스트
├── static/
│   ├── CNAME                 # 커스텀 도메인
│   └── images/               # 이미지
└── .github/workflows/
    └── hugo.yml              # 자동 배포 설정

Obsidian Vault/
└── 공개저널/
    └── .templates/           # Hugo 템플릿
        ├── hugo-post-ko.md
        └── hugo-post-en.md
```

---

## 🎨 포스트 Front Matter 예시

```yaml
---
title: "포스트 제목"
date: 2024-01-15T10:00:00+09:00
draft: false
tags: ["AI", "딥러닝"]
categories: ["기술"]
author: "지호아빠"
description: "포스트 설명"
cover:
    image: "/images/cover.jpg"
    alt: "커버 이미지"
    caption: "이미지 캡션"
ShowToc: true
TocOpen: false
---

# 포스트 내용 시작

여기에 마크다운 형식으로 작성합니다.
```

---

## 🛠️ 일상적인 워크플로우

### 포스트 작성 → 배포

1. **작성**: Obsidian 또는 에디터에서 포스트 작성
2. **미리보기**: `hugo server -D`로 로컬 확인
3. **발행**: `draft: false`로 변경
4. **배포**: Git push (또는 Obsidian Git 자동)
5. **확인**: 2-5분 후 사이트에서 확인

---

## 📚 상세 문서

- **배포 가이드**: [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md)
- **DNS 설정**: [`docs/DNS_SETUP.md`](docs/DNS_SETUP.md)
- **Obsidian 연동**: [`docs/OBSIDIAN_SETUP.md`](docs/OBSIDIAN_SETUP.md)
- **프로젝트 README**: [`README.md`](README.md)

---

## ⚙️ 사이트 설정 변경

`hugo.yaml` 파일에서 수정:

```yaml
# 사이트 제목 변경
languages:
  ko:
    title: '새로운 제목'
  en:
    title: 'New Title'

# 홈페이지 메시지 변경
params:
  homeInfoParams:
    Title: "환영 메시지"
    Content: "사이트 설명"
```

---

## 🐛 문제 해결

### 배포가 안 될 때
```bash
# GitHub Actions 로그 확인
# GitHub 저장소 > Actions 탭

# 로컬에서 빌드 테스트
hugo --gc --minify
```

### 스타일이 깨질 때
```bash
# 캐시 삭제 후 재빌드
rm -rf public/ resources/
hugo --gc --minify
git add .
git commit -m "Rebuild"
git push
```

### DNS가 안 될 때
```bash
# DNS 전파 확인
dig paper.millionqubits.com

# 또는
nslookup paper.millionqubits.com
```

---

## 📧 문의

이메일: jiho_appa@naver.com

---

## 🎉 시작하기

이제 위의 5단계만 진행하면 블로그가 운영됩니다!

```bash
# 1. GitHub에 푸시
git push -u origin main

# 2. 첫 포스트 작성
hugo new content/ko/posts/hello-world.md

# 3. 로컬 미리보기
hugo server -D

# 4. 배포
git add .
git commit -m "First post"
git push

# 완료! 🚀
```

**행운을 빕니다!** 🎊

