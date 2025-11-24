# 배포 가이드

이 문서는 Hugo 블로그를 GitHub Pages에 배포하는 전체 프로세스를 안내합니다.

## 목차

1. [사전 준비](#사전-준비)
2. [GitHub 저장소 설정](#github-저장소-설정)
3. [초기 배포](#초기-배포)
4. [자동 배포 확인](#자동-배포-확인)
5. [배포 후 작업](#배포-후-작업)

---

## 사전 준비

### 필수 도구 설치 확인

```bash
# Hugo 버전 확인 (0.138.0 이상 필요)
hugo version

# Git 버전 확인
git --version

# Git 사용자 정보 설정 (처음이라면)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### GitHub 계정 준비

1. GitHub 계정이 없다면 [github.com](https://github.com) 에서 생성
2. 이메일 인증 완료
3. GitHub CLI 설치 (선택사항):
   ```bash
   # macOS
   brew install gh
   
   # 로그인
   gh auth login
   ```

---

## GitHub 저장소 설정

### 방법 1: GitHub 웹사이트에서 생성

1. [GitHub](https://github.com/) 로그인
2. 오른쪽 상단 **+** > **New repository** 클릭
3. 저장소 설정:
   - **Repository name**: `paper.millionqubits.com`
   - **Description**: "지호아빠의 딥(Deep) 블로깅 - 기술과 생각을 기록하는 블로그"
   - **Public** 선택
   - **Add a README file**: 체크 해제 (이미 README 있음)
   - **Add .gitignore**: None
   - **Choose a license**: MIT (선택사항)
4. **Create repository** 클릭

### 방법 2: GitHub CLI 사용

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 저장소 생성 및 연결
gh repo create paper.millionqubits.com --public --source=. --remote=origin
```

---

## 초기 배포

### 1단계: 원격 저장소 연결

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 원격 저장소 추가 (yourusername을 실제 사용자명으로 변경)
git remote add origin https://github.com/yourusername/paper.millionqubits.com.git

# 원격 저장소 확인
git remote -v
```

### 2단계: 브랜치 이름 확인/변경

```bash
# 현재 브랜치 확인
git branch

# main이 아니면 변경
git branch -M main
```

### 3단계: 첫 커밋 및 푸시

```bash
# 모든 파일 스테이징
git add .

# 커밋
git commit -m "Initial commit: Hugo blog with PaperMod theme

- 한영 이중언어 지원
- GitHub Actions 자동 배포 설정
- Obsidian 템플릿 추가
- 커스텀 도메인 설정 (paper.millionqubits.com)"

# GitHub에 푸시
git push -u origin main
```

### 4단계: GitHub Actions 권한 설정

1. GitHub 저장소 페이지로 이동
2. **Settings** > **Actions** > **General** 클릭
3. **Workflow permissions** 섹션:
   - **Read and write permissions** 선택
   - **Allow GitHub Actions to create and approve pull requests** 체크
4. **Save** 클릭

### 5단계: GitHub Pages 활성화

1. **Settings** > **Pages** 클릭
2. **Source**: **GitHub Actions** 선택
3. **Custom domain**: `paper.millionqubits.com` 입력 (DNS 설정 후)
4. **Enforce HTTPS** 체크 (DNS 전파 후 활성화됨)

---

## 자동 배포 확인

### GitHub Actions 실행 확인

1. GitHub 저장소 > **Actions** 탭 클릭
2. "Deploy Hugo site to GitHub Pages" 워크플로우 확인
3. 진행 상황 모니터링:
   - 🟡 노란색: 실행 중
   - 🟢 녹색: 성공
   - 🔴 빨간색: 실패

### 배포 로그 확인

1. 워크플로우 실행 클릭
2. **build** 작업 클릭하여 빌드 로그 확인
3. **deploy** 작업 클릭하여 배포 로그 확인

### 배포 시간

- 일반적으로 2-5분 소요
- 처음 배포는 조금 더 걸릴 수 있음

---

## 배포 후 작업

### 사이트 접속 확인

```bash
# GitHub Pages URL (DNS 설정 전)
# https://yourusername.github.io/paper.millionqubits.com

# 커스텀 도메인 (DNS 설정 후)
# https://paper.millionqubits.com
```

### 초기 테스트 포스트 작성

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 한국어 테스트 포스트 생성
hugo new content/ko/posts/hello-world.md

# 영어 테스트 포스트 생성
hugo new content/en/posts/hello-world.md
```

`content/ko/posts/hello-world.md` 편집:

```markdown
---
title: "안녕하세요!"
date: 2024-01-15T10:00:00+09:00
draft: false
tags: ["인사", "시작"]
categories: ["일반"]
author: "지호아빠"
description: "첫 번째 블로그 포스트입니다"
ShowToc: true
TocOpen: false
---

# 환영합니다!

지호아빠의 딥(Deep) 블로깅에 오신 것을 환영합니다.

이 블로그에서는 AI와 딥러닝에 관한 다양한 주제를 다룰 예정입니다.

## 다룰 주제들

- 딥러닝 기초
- TensorFlow와 PyTorch
- 컴퓨터 비전
- 자연어 처리
- 그리고 더 많은 내용들!

앞으로의 여정이 기대됩니다. 함께해주세요!
```

### 테스트 포스트 배포

```bash
# 변경사항 확인
git status

# 스테이징
git add content/ko/posts/hello-world.md

# 커밋
git commit -m "Add first post: Hello World"

# 푸시 (자동 배포 시작)
git push origin main
```

---

## 일상적인 배포 워크플로우

### 포스트 작성 및 배포

```bash
# 1. 새 포스트 작성
hugo new content/ko/posts/my-new-post.md

# 2. 포스트 편집
# (에디터에서 내용 작성)

# 3. 로컬에서 미리보기
hugo server -D

# 4. 완료되면 draft를 false로 변경

# 5. Git에 커밋
git add .
git commit -m "Add new post: My New Post"
git push origin main

# 6. GitHub Actions가 자동으로 배포
```

### Obsidian에서 작성한 경우

#### Obsidian Git 플러그인 사용 시
- 플러그인이 자동으로 커밋 및 푸시
- 별도 작업 불필요

#### 수동 복사 후
```bash
# Obsidian에서 Hugo로 파일 복사
cp "/Users/user/Vaults/appa-core-vault/공개저널/my-post.md" \
   "/Users/user/Websites/paper.millionqubits.com/content/ko/posts/"

# Git 배포
cd /Users/user/Websites/paper.millionqubits.com
git add .
git commit -m "Add post from Obsidian"
git push origin main
```

---

## 배포 문제 해결

### GitHub Actions 실패 시

#### 빌드 오류

```bash
# 로컬에서 빌드 테스트
cd /Users/user/Websites/paper.millionqubits.com
hugo --gc --minify

# 오류가 있다면 수정 후 다시 푸시
```

#### 권한 오류

1. Settings > Actions > General
2. Workflow permissions 확인
3. "Read and write permissions" 선택

#### 서브모듈 오류

```bash
# 서브모듈 업데이트
git submodule update --init --recursive

# 커밋 및 푸시
git add .
git commit -m "Update submodules"
git push origin main
```

### 404 에러

#### baseURL 확인

`hugo.yaml` 파일:
```yaml
baseURL: 'https://paper.millionqubits.com/'
```

#### CNAME 파일 확인

```bash
# CNAME 파일 내용 확인
cat static/CNAME

# 출력되어야 할 내용:
# paper.millionqubits.com
```

### 스타일 깨짐

#### 캐시 삭제

```bash
# Hugo 캐시 삭제
rm -rf public/ resources/

# 다시 빌드
hugo --gc --minify

# Git에 푸시
git add .
git commit -m "Rebuild site"
git push origin main
```

#### 브라우저 캐시

- 강력 새로고침: `Cmd + Shift + R` (macOS) 또는 `Ctrl + Shift + R` (Windows)

---

## 배포 최적화

### 빌드 속도 개선

#### 캐싱 활성화

GitHub Actions 워크플로우에 이미 캐싱이 설정되어 있습니다:
```yaml
env:
  HUGO_CACHEDIR: ${{ runner.temp }}/hugo_cache
```

### 이미지 최적화

배포 전에 이미지 최적화:

```bash
# ImageMagick 설치 (macOS)
brew install imagemagick

# 이미지 크기 조정
convert input.jpg -resize 1200x -quality 85 output.jpg

# WebP 형식으로 변환 (더 작은 파일 크기)
cwebp -q 80 input.jpg -o output.webp
```

### 리소스 압축

Hugo가 자동으로 압축합니다:
```yaml
# hugo.yaml에 이미 설정됨
# hugo --gc --minify 명령어 사용
```

---

## 배포 모니터링

### GitHub Actions 이메일 알림

1. GitHub 프로필 > **Settings**
2. **Notifications**
3. **Actions** 섹션에서 실패 알림 설정

### 업타임 모니터링

무료 서비스 사용:
- [UptimeRobot](https://uptimerobot.com/)
- [StatusCake](https://www.statuscake.com/)
- [Pingdom](https://www.pingdom.com/)

### 분석 도구

#### Google Analytics

1. [Google Analytics](https://analytics.google.com/) 계정 생성
2. 측정 ID 받기 (G-XXXXXXXXXX)
3. `hugo.yaml`에 추가:
   ```yaml
   services:
     googleAnalytics:
       ID: G-XXXXXXXXXX
   ```

#### Cloudflare Analytics

Cloudflare를 DNS로 사용하면 자동으로 제공됩니다.

---

## 백업 및 복구

### 저장소 백업

```bash
# 전체 저장소 클론 (백업)
git clone --recursive https://github.com/yourusername/paper.millionqubits.com.git backup/

# 또는 로컬 저장소 압축
tar -czf paper-blog-backup-$(date +%Y%m%d).tar.gz /Users/user/Websites/paper.millionqubits.com
```

### 복구

```bash
# 백업에서 복원
cd /path/to/backup
git push origin main --force

# 주의: --force는 원격 저장소를 덮어씁니다
```

---

## 추가 리소스

- [Hugo 공식 문서](https://gohugo.io/documentation/)
- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [PaperMod 테마 위키](https://github.com/adityatelange/hugo-PaperMod/wiki)
- [GitHub Pages 문서](https://docs.github.com/en/pages)

---

## 체크리스트

배포 완료 후 확인:

- [ ] GitHub 저장소 생성 및 푸시 완료
- [ ] GitHub Actions 워크플로우 성공적으로 실행
- [ ] 사이트가 GitHub Pages URL에서 접속 가능
- [ ] DNS 설정 완료 (커스텀 도메인 사용 시)
- [ ] SSL 인증서 발급 및 HTTPS 활성화
- [ ] 테스트 포스트 작성 및 확인
- [ ] 한영 언어 전환 기능 테스트
- [ ] 검색 기능 테스트
- [ ] 아카이브 페이지 확인
- [ ] 모바일 반응형 확인

---

## 문의

배포 과정에서 문제가 발생하면 이메일로 연락주세요:
📧 jiho_appa@naver.com

