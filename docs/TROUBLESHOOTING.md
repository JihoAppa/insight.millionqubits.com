# 문제 해결 가이드

블로그 운영 중 발생할 수 있는 문제들과 해결 방법을 정리한 문서입니다.

## 📋 목차

1. [Hugo 빌드 오류](#hugo-빌드-오류)
2. [GitHub Actions 배포 실패](#github-actions-배포-실패)
3. [Obsidian 동기화 문제](#obsidian-동기화-문제)
4. [포스트 표시 안 됨](#포스트-표시-안-됨)
5. [이미지 표시 안 됨](#이미지-표시-안-됨)
6. [스타일 적용 안 됨](#스타일-적용-안-됨)

---

## Hugo 빌드 오류

### 문제: Hugo 버전 호환성 오류

```
WARN Module "PaperMod" is not compatible with this Hugo version: Min 0.146.0
ERROR => hugo v0.146.0 or greater is required for hugo-PaperMod to build
```

**원인**: PaperMod 테마가 요구하는 Hugo 버전보다 낮은 버전 사용

**해결 방법**:

#### 로컬에서 Hugo 업그레이드

**macOS (Homebrew)**:
```bash
brew upgrade hugo
hugo version  # 확인
```

**Linux**:
```bash
# 최신 버전 다운로드 및 설치
HUGO_VERSION="0.139.3"  # 또는 최신 버전
wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
tar -xzf hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz
sudo mv hugo /usr/local/bin/
hugo version  # 확인
```

**Windows (Chocolatey)**:
```powershell
choco upgrade hugo-extended
hugo version  # 확인
```

#### GitHub Actions에서 Hugo 버전 업데이트

`.github/workflows/hugo.yml` 파일에서:

```yaml
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v3
  with:
    hugo-version: 'latest'  # 항상 최신 버전 사용
    extended: true
```

또는 특정 버전 지정:

```yaml
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v3
  with:
    hugo-version: '0.139.3'  # 특정 버전
    extended: true
```

### 문제: Google Analytics 템플릿 오류

```
ERROR partial "google_analytics.html" not found
```

**원인**: PaperMod 테마 버전과 Hugo 버전의 호환성 문제

**해결 방법**:

```bash
# 테마 서브모듈 업데이트
git submodule update --remote --merge
git add themes/PaperMod
git commit -m "Update PaperMod theme"
git push
```

---

## GitHub Actions 배포 실패

### 문제: 배포 권한 오류

```
Error: Resource not accessible by integration
```

**해결 방법**:

1. GitHub 저장소 → **Settings** → **Actions** → **General**
2. **Workflow permissions** → **Read and write permissions** 선택
3. **Save** 클릭

### 문제: Pages 설정 오류

```
Error: Pages deployment failed
```

**해결 방법**:

1. GitHub 저장소 → **Settings** → **Pages**
2. **Source**: GitHub Actions 선택
3. Custom domain이 있다면 다시 입력
4. **Save** 클릭

### 문제: 서브모듈 초기화 실패

```
Error: Submodule 'themes/PaperMod' not found
```

**해결 방법**:

`.github/workflows/hugo.yml`에서 확인:

```yaml
- name: Checkout
  uses: actions/checkout@v4
  with:
    submodules: recursive  # ✅ 이것이 있어야 함
    fetch-depth: 0
```

---

## Obsidian 동기화 문제

### 문제: Obsidian Git 플러그인이 작동하지 않음

**증상**: 동기화 버튼을 눌러도 아무 일도 일어나지 않음

**해결 방법**:

1. **Git 설정 확인**:
   ```bash
   cd /Users/user/Vaults/appa-core-vault/공개저널
   git config user.name "Your Name"
   git config user.email "your@email.com"
   ```

2. **원격 저장소 확인**:
   ```bash
   git remote -v
   # origin이 올바른 URL을 가리키는지 확인
   ```

3. **수동 테스트**:
   ```bash
   git status
   git add .
   git commit -m "test"
   git push origin main
   ```

4. **Obsidian Git 플러그인 재설정**:
   - 플러그인 비활성화 → 활성화
   - Obsidian 재시작

### 문제: Git 충돌 발생

**증상**: `CONFLICT` 메시지 또는 동기화 실패

**해결 방법**:

```bash
cd /Users/user/Vaults/appa-core-vault/공개저널

# 1. 현재 변경사항 임시 저장
git stash

# 2. 원격 변경사항 가져오기
git pull origin main

# 3. 임시 저장한 변경사항 적용
git stash pop

# 4. 충돌 파일 수동 편집 후
git add .
git commit -m "Resolve conflicts"
git push origin main
```

### 문제: 심볼릭 링크가 작동하지 않음

**증상**: 블로그 폴더의 파일이 Hugo에 나타나지 않음

**해결 방법**:

```bash
# 기존 링크 삭제
rm -rf /Users/user/Websites/paper.millionqubits.com/content/posts

# 새로 생성
ln -s "/Users/user/Vaults/appa-core-vault/공개저널/블로그" \
      "/Users/user/Websites/paper.millionqubits.com/content/posts"

# 확인
ls -la /Users/user/Websites/paper.millionqubits.com/content/posts
```

---

## 포스트 표시 안 됨

### 체크리스트

1. **Draft 상태 확인**:
   ```yaml
   draft: false  # ✅ false여야 함
   ```

2. **날짜 확인**:
   ```yaml
   # ❌ 미래 날짜는 표시 안 됨
   date: 2025-12-31T00:00:00+09:00
   
   # ✅ 현재 또는 과거 날짜
   date: 2024-11-24T15:00:00+09:00
   ```

3. **파일명 확인**:
   ```bash
   # ✅ 올바른 형식
   my-post.ko.md
   my-post.en.md
   
   # ❌ 잘못된 형식
   my-post.md        # 언어 지정 필요
   my post.ko.md     # 공백 사용 금지
   ```

4. **파일 위치 확인**:
   ```bash
   # ✅ 올바른 위치
   content/posts/my-post.ko.md
   
   # ❌ 잘못된 위치
   content/my-post.ko.md
   content/docs-examples/my-post.ko.md  # 예제 폴더
   ```

5. **Front Matter 형식 확인**:
   ```yaml
   ---
   title: "제목"  # ✅ 따옴표 사용
   date: 2024-11-24T15:00:00+09:00  # ✅ ISO 8601 형식
   draft: false
   ---
   ```

### 로컬 테스트

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 초안 포함하여 확인
hugo server -D

# 발행된 포스트만 확인
hugo server
```

---

## 이미지 표시 안 됨

### 문제: 상대 경로 이미지가 표시 안 됨

**잘못된 예**:
```markdown
![이미지](./images/photo.png)  # ❌
![이미지](../images/photo.png)  # ❌
```

**올바른 예**:
```markdown
# 포스트와 같은 폴더의 images/
![이미지](images/photo.png)  # ✅

# static/images/
![이미지](/images/photo.png)  # ✅
```

### 문제: Obsidian 위키링크 사용

**잘못된 예**:
```markdown
![[photo.png]]  # ❌ Hugo에서 작동 안 함
```

**올바른 예**:
```markdown
![사진](images/photo.png)  # ✅
```

### 이미지 파일 위치

```
content/posts/
├── my-post.ko.md
└── images/
    └── photo.png         # ✅ 상대 경로로 참조

static/images/
└── logo.png              # ✅ 절대 경로로 참조 (/images/logo.png)
```

---

## 스타일 적용 안 됨

### 문제: 커스텀 CSS가 적용되지 않음

**확인 사항**:

1. **파일 위치**:
   ```
   assets/css/extended/custom.css  # ✅ 올바른 위치
   ```

2. **Hugo 재시작**:
   ```bash
   # 서버 중지 (Ctrl+C)
   rm -rf public/ resources/  # 캐시 삭제
   hugo server -D             # 재시작
   ```

3. **브라우저 캐시 삭제**:
   - Chrome: `Cmd + Shift + R` (macOS) / `Ctrl + Shift + R` (Windows)
   - 또는 개발자 도구 → Network 탭 → "Disable cache" 체크

### 문제: 다크 모드 스타일 적용 안 됨

**해결 방법**:

`custom.css`에 다크 모드 변수 추가:

```css
:root {
  --primary: #1a1a1a;
  --theme: #ffffff;
  /* ... */
}

[data-theme="dark"] {
  --primary: #e4e4e4;
  --theme: #1a1a1a;
  /* ... */
}
```

---

## 일반적인 문제

### 문제: 한국어 포스트와 영어 포스트가 연결되지 않음

**원인**: 파일명 기본 부분이 다름

**잘못된 예**:
```
my-korean-post.ko.md
my-english-post.en.md
```

**올바른 예**:
```
my-post.ko.md   # ✅ 기본 부분 동일
my-post.en.md   # ✅
```

### 문제: 태그/카테고리 페이지가 비어있음

**원인**: 포스트에 태그나 카테고리가 없음

**해결 방법**:

```yaml
---
title: "제목"
tags: ["Python", "AI"]      # ✅ 태그 추가
categories: ["기술"]         # ✅ 카테고리 추가
---
```

### 문제: 검색 기능이 작동하지 않음

**확인 사항**:

1. **search.md 파일 존재**:
   ```
   content/search.ko.md  # ✅
   content/search.en.md  # ✅
   ```

2. **hugo.yaml 설정**:
   ```yaml
   outputs:
     home: ["HTML", "RSS", "JSON"]  # ✅ JSON 포함
   ```

3. **빌드 후 확인**:
   ```bash
   # public/index.json 파일이 생성되는지 확인
   ls -la public/index.json
   ```

---

## 🆘 추가 도움이 필요한 경우

### 로그 확인

**GitHub Actions 로그**:
1. GitHub 저장소 → **Actions** 탭
2. 실패한 워크플로우 클릭
3. 각 단계의 로그 확인

**로컬 Hugo 디버그**:
```bash
hugo server -D --verbose --debug
```

### 이슈 리포팅

문제가 지속되면 다음 정보와 함께 이슈 제기:

- Hugo 버전: `hugo version`
- OS 및 버전
- 에러 메시지 전문
- 재현 단계
- 관련 파일 내용 (front matter 등)

---

## 📚 관련 문서

- [Hugo 공식 문서](https://gohugo.io/documentation/)
- [PaperMod 위키](https://github.com/adityatelange/hugo-PaperMod/wiki)
- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [Obsidian Git 플러그인](https://github.com/denolehov/obsidian-git)

---

**문제가 해결되지 않으면 jiho_appa@naver.com으로 연락주세요!**

