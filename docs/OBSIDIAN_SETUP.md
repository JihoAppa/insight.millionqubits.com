# Obsidian 플러그인 설정 가이드

이 문서는 Obsidian에서 Hugo 블로그로 콘텐츠를 동기화하는 방법을 안내합니다.

## 목차

1. [방법 1: Obsidian Git 플러그인 (권장)](#방법-1-obsidian-git-플러그인-권장)
2. [방법 2: Enveloppe 플러그인](#방법-2-enveloppe-플러그인)
3. [방법 3: 수동 복사](#방법-3-수동-복사)

---

## 방법 1: Obsidian Git 플러그인 (권장)

Obsidian Git 플러그인을 사용하면 자동으로 변경사항을 커밋하고 GitHub에 푸시할 수 있습니다.

### 1단계: Obsidian Git 플러그인 설치

1. Obsidian 설정 열기 (`Cmd/Ctrl + ,`)
2. **Community plugins** > **Browse** 클릭
3. "**Obsidian Git**" 검색 후 설치
4. 플러그인 활성화

### 2단계: Hugo 프로젝트 내 콘텐츠 폴더를 Vault로 사용

#### 옵션 A: 심볼릭 링크 생성 (권장)

```bash
# Hugo 프로젝트의 content 폴더를 Obsidian vault와 연결
ln -s "/Users/user/Vaults/appa-core-vault/공개저널" "/Users/user/Websites/paper.millionqubits.com/content/ko/posts/obsidian"
```

#### 옵션 B: Git 서브모듈 사용

```bash
cd /Users/user/Websites/paper.millionqubits.com
git submodule add /Users/user/Vaults/appa-core-vault content/vault
```

### 3단계: Obsidian Git 플러그인 설정

1. Obsidian 설정 > **Obsidian Git**
2. 주요 설정:
   - **Automatic pull on startup**: 활성화
   - **Automatic push**: 활성화
   - **Auto pull interval (minutes)**: 10
   - **Auto commit interval (minutes)**: 5
   - **Commit message**: `vault backup: {{date}}`

### 4단계: Git 저장소 초기화 (Vault에서)

```bash
cd /Users/user/Vaults/appa-core-vault/공개저널
git init
git remote add origin https://github.com/yourusername/paper.millionqubits.com.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 5단계: 워크플로우

1. Obsidian에서 템플릿을 사용하여 새 포스트 작성
2. 플러그인이 자동으로 커밋 및 푸시
3. GitHub Actions가 자동으로 빌드 및 배포

---

## 방법 2: Enveloppe 플러그인

Enveloppe는 GitHub에 직접 파일을 업로드하는 플러그인입니다.

### 1단계: Enveloppe 플러그인 설치

1. Obsidian 설정 열기
2. **Community plugins** > **Browse**
3. "**Enveloppe**" 검색 후 설치
4. 플러그인 활성화

### 2단계: GitHub Token 생성

1. GitHub 설정 > **Developer settings** > **Personal access tokens** > **Tokens (classic)**
2. **Generate new token (classic)** 클릭
3. 권한 선택:
   - `repo` (전체 체크)
   - `workflow`
4. 토큰 복사 (한 번만 표시됨!)

### 3단계: Enveloppe 설정

1. Obsidian 설정 > **Enveloppe**
2. GitHub 설정:
   - **GitHub username**: `yourusername`
   - **GitHub repository**: `paper.millionqubits.com`
   - **GitHub token**: 위에서 생성한 토큰 입력
   - **Branch**: `main`

3. 업로드 경로 설정:
   - **Root folder in repository**: 
     - 한국어: `content/ko/posts`
     - 영어: `content/en/posts`

4. Front Matter 설정:
   - **Required front matter keys**: `title, date, draft`

### 4단계: 포스트 발행하기

1. 포스트 작성 완료
2. 명령 팔레트 열기 (`Cmd/Ctrl + P`)
3. "**Enveloppe: Share**" 선택
4. 언어 선택 (ko 또는 en)
5. 자동으로 GitHub에 업로드 및 배포 시작

---

## 방법 3: 수동 복사

가장 간단하지만 자동화가 없는 방법입니다.

### 워크플로우

1. Obsidian에서 포스트 작성
2. 파일을 Hugo 프로젝트로 복사:
   ```bash
   # 한국어 포스트
   cp "/Users/user/Vaults/appa-core-vault/공개저널/my-post.md" \
      "/Users/user/Websites/paper.millionqubits.com/content/ko/posts/"
   
   # 영어 포스트
   cp "/Users/user/Vaults/appa-core-vault/공개저널/my-post-en.md" \
      "/Users/user/Websites/paper.millionqubits.com/content/en/posts/"
   ```

3. Git 커밋 및 푸시:
   ```bash
   cd /Users/user/Websites/paper.millionqubits.com
   git add .
   git commit -m "Add new post: My Post Title"
   git push origin main
   ```

4. GitHub Actions가 자동 배포

---

## 이미지 처리

### Obsidian에서 이미지 첨부

1. Obsidian 설정 > **Files & Links**
2. **Default location for new attachments**: `In subfolder under current folder`
3. **Subfolder name**: `images`

### 이미지를 Hugo로 복사

#### 자동 (Git 사용 시)
이미지가 포함된 폴더 전체를 Git에 커밋하면 자동으로 동기화됩니다.

#### 수동
```bash
# 이미지를 Hugo static 폴더로 복사
cp -r "/Users/user/Vaults/appa-core-vault/공개저널/images" \
       "/Users/user/Websites/paper.millionqubits.com/static/"
```

### 마크다운에서 이미지 참조

```markdown
# Obsidian 형식 (로컬)
![[image.png]]

# Hugo 형식 (배포 시 필요)
![이미지 설명](/images/image.png)
```

**권장**: Hugo 형식으로 작성하면 Obsidian과 Hugo 모두에서 이미지가 표시됩니다.

---

## 템플릿 사용하기

### Templater 플러그인 (권장)

1. **Templater** 플러그인 설치
2. 설정:
   - **Template folder location**: `.templates`
   - **Automatic jump to cursor**: 활성화
3. 단축키 설정: `Cmd/Ctrl + T`

### 기본 Templates 플러그인

1. Core plugins에서 **Templates** 활성화
2. **Template folder location**: `.templates`
3. 명령 팔레트에서 "Insert template" 사용

---

## 문제 해결

### Git 충돌 발생 시

```bash
# 로컬 변경사항 백업
git stash

# 원격 저장소에서 최신 버전 가져오기
git pull origin main

# 백업한 변경사항 적용
git stash pop

# 충돌 해결 후
git add .
git commit -m "Resolve conflicts"
git push origin main
```

### 플러그인 오류 시

1. Obsidian 재시작
2. 플러그인 비활성화 후 재활성화
3. 플러그인 삭제 후 재설치

### 자동 커밋이 작동하지 않을 때

1. Git 설정 확인:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. Obsidian Git 플러그인 로그 확인
3. 수동으로 커밋 테스트

---

## 추천 워크플로우

### 일일 블로깅

1. **아침**: Obsidian Git 자동 pull로 최신 버전 동기화
2. **작성**: Templater로 새 포스트 생성
3. **편집**: 자유롭게 작성 및 수정
4. **발행**: 
   - `draft: false`로 변경
   - Obsidian Git이 자동으로 푸시
   - 또는 수동으로 "Obsidian Git: Commit and push" 실행
5. **확인**: 5-10분 후 https://paper.millionqubits.com 에서 확인

### 배치 작성

1. 여러 포스트를 `draft: true` 상태로 작성
2. 발행 준비가 된 포스트만 `draft: false`로 변경
3. 한 번에 커밋 및 푸시
4. GitHub Actions가 한 번에 배포

---

## 유용한 단축키

| 기능 | 단축키 (macOS) | 단축키 (Windows) |
|------|----------------|------------------|
| 명령 팔레트 | `Cmd + P` | `Ctrl + P` |
| 설정 | `Cmd + ,` | `Ctrl + ,` |
| Git 커밋 | 사용자 지정 | 사용자 지정 |
| 템플릿 삽입 | `Cmd + T` | `Ctrl + T` |
| 빠른 전환 | `Cmd + O` | `Ctrl + O` |

---

## 참고 자료

- [Obsidian Git 플러그인 문서](https://github.com/denolehov/obsidian-git)
- [Enveloppe 플러그인 문서](https://github.com/Enveloppe/obsidian-enveloppe)
- [Hugo 문서](https://gohugo.io/documentation/)
- [PaperMod 테마 문서](https://github.com/adityatelange/hugo-PaperMod/wiki)

