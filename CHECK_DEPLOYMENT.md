# 배포 확인 체크리스트

로컬과 배포된 사이트가 다를 때 확인해야 할 사항들입니다.

## 🔍 즉시 확인 사항

### 1. 브라우저 캐시 강제 새로고침

**가장 흔한 원인**: 브라우저가 이전 버전의 CSS/JS를 캐시하고 있음

**해결 방법**:
- **Chrome/Edge**: `Cmd + Shift + R` (Mac) / `Ctrl + Shift + R` (Windows)
- **Safari**: `Cmd + Option + R`
- **Firefox**: `Ctrl + Shift + R` / `Cmd + Shift + R`

또는:
```
개발자 도구 (F12) → Network 탭 → "Disable cache" 체크 → 새로고침
```

### 2. GitHub Actions 빌드 상태 확인

1. https://github.com/yourusername/paper.millionqubits.com/actions 접속
2. 최신 워크플로우가 ✅ 성공했는지 확인
3. 실패했다면 로그 확인

### 3. 최신 커밋이 배포되었는지 확인

```bash
# 로컬의 최신 커밋
cd /Users/user/Websites/paper.millionqubits.com
git log -1 --oneline

# GitHub에 푸시되었는지 확인
git status
# "Your branch is up to date with 'origin/main'" 메시지 확인
```

---

## 🔧 CSS 스타일 문제

### 증상: 타이포그래피가 적용되지 않음

#### 확인 1: custom.css 파일이 배포되었는지

브라우저에서 직접 접속:
```
https://paper.millionqubits.com/css/extended/custom.css
```

- **404 오류**: CSS 파일이 빌드에 포함되지 않음
- **파일 내용 표시**: 올바르게 배포됨

#### 확인 2: 브라우저 개발자 도구

1. `F12` 또는 `Cmd + Option + I` (Mac)
2. **Elements** 탭 → `<body>` 또는 `.post-content` 선택
3. **Computed** 탭에서 실제 적용된 스타일 확인:
   ```css
   font-size: 16.96px  /* 올바름 */
   font-size: 18px     /* 또는 이것 */
   line-height: 28.832px  /* 올바름 */
   ```

#### 확인 3: Console 에러

개발자 도구 → **Console** 탭:
- CSS 로드 실패 에러가 있는지 확인
- 404 에러가 있는지 확인

---

## 🎨 레이아웃 문제

### 증상: 카드 크기/간격이 다름

#### 확인: 반응형 breakpoint

로컬에서 테스트한 화면 크기와 배포 사이트의 화면 크기가 다를 수 있습니다.

**테스트**:
1. 개발자 도구 → **Toggle device toolbar** (`Cmd + Shift + M`)
2. 다양한 화면 크기로 테스트:
   - Desktop: 1920px, 1440px, 1280px
   - Tablet: 768px, 1024px
   - Mobile: 375px, 414px

---

## 📁 파일/경로 문제

### baseURL 설정 확인

**현재 상태**: `hugo.yaml`에서 baseURL이 주석 처리됨

**GitHub Actions 빌드 시**:
```yaml
--baseURL "${{ steps.pages.outputs.base_url }}/"
```
이 명령으로 동적 설정됨

**테스트**:
로컬에서 프로덕션 빌드 테스트:

```bash
cd /Users/user/Websites/paper.millionqubits.com

# baseURL을 실제 도메인으로 빌드
hugo --baseURL "https://paper.millionqubits.com/"

# 빌드된 HTML 확인
grep -r "css/extended/custom.css" public/ | head -5
```

---

## 🌐 도메인/DNS 문제

### 증상: 사이트가 전혀 열리지 않음

#### 확인 1: DNS 전파

```bash
# DNS 조회
dig paper.millionqubits.com

# 또는
nslookup paper.millionqubits.com
```

예상 결과:
```
paper.millionqubits.com. 300 IN CNAME yourusername.github.io.
```

#### 확인 2: GitHub Pages 설정

1. GitHub 저장소 → **Settings** → **Pages**
2. **Custom domain**: `paper.millionqubits.com` 입력되어 있는지
3. **Enforce HTTPS**: 체크되어 있는지

---

## 🔄 캐시 문제

### Cloudflare 사용 시

Cloudflare를 사용 중이라면:

1. Cloudflare Dashboard 접속
2. **Caching** → **Configuration**
3. **Purge Everything** 클릭

### GitHub Pages 캐시

GitHub Pages는 CDN 캐시를 사용합니다. 완전히 전파되는 데 최대 10분 소요.

---

## 🐛 디버깅 단계

### 1단계: 로컬 프로덕션 빌드 테스트

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 캐시 삭제
rm -rf public/ resources/

# 프로덕션 빌드 (GitHub Actions와 동일)
hugo --gc --minify --baseURL "https://paper.millionqubits.com/"

# 로컬 서버로 빌드 결과 확인
cd public
python3 -m http.server 8000
# http://localhost:8000 접속
```

### 2단계: 빌드 결과물 확인

```bash
# custom.css가 포함되었는지
ls -la public/css/extended/custom.css

# HTML에서 CSS 링크 확인
grep -r "custom.css" public/*.html

# assets 디렉토리 확인
find public -type f -name "*.css" | grep custom
```

### 3단계: GitHub Actions 로그 상세 확인

1. Actions 탭 → 최신 워크플로우 클릭
2. **build** 작업 → **Build with Hugo** 단계 확인
3. 에러나 경고 메시지 확인

---

## 📝 비교 체크리스트

| 항목 | 로컬 | 배포 | 일치? |
|------|------|------|-------|
| 폰트 크기 | 16.96px | ? | [ ] |
| 줄 간격 | 28.832px | ? | [ ] |
| 카드 패딩 | 16px 20px | ? | [ ] |
| 본문 너비 | 680px | ? | [ ] |
| 메뉴 항목 | 이모티콘 없음 | ? | [ ] |

---

## 🔨 일반적인 해결 방법

### 해결책 1: 강제 재배포

```bash
# 빈 커밋으로 재배포 트리거
git commit --allow-empty -m "Force rebuild"
git push origin main
```

### 해결책 2: 서브모듈 업데이트

```bash
git submodule update --init --recursive --remote
git add themes/PaperMod
git commit -m "Update PaperMod theme"
git push origin main
```

### 해결책 3: baseURL 명시적 설정

`hugo.yaml`:
```yaml
baseURL: 'https://paper.millionqubits.com/'  # 주석 해제
```

**주의**: GitHub Actions의 동적 baseURL과 충돌할 수 있으므로 신중하게

---

## 📸 스크린샷으로 비교

### 로컬 vs 배포 비교

1. **같은 브라우저, 같은 화면 크기로** 스크린샷 촬영
2. 브라우저 확대/축소 100% 확인
3. 개발자 도구로 실제 CSS 값 비교

### 스크린샷 찍는 법

**로컬**:
```bash
hugo server
# http://localhost:1313 접속 → 스크린샷
```

**배포**:
```
https://paper.millionqubits.com 접속 → 스크린샷
```

---

## 🆘 여전히 다르다면

다음 정보를 확인해주세요:

1. **배포 사이트 URL**: 정확한 URL
2. **어떤 부분이 다른지**: 구체적인 차이점
3. **브라우저 정보**: Chrome 버전, Safari 등
4. **스크린샷**: 로컬과 배포 비교
5. **개발자 도구 Console**: 에러 메시지
6. **개발자 도구 Network**: CSS 파일 로드 상태

---

**대부분의 경우 브라우저 강제 새로고침 (`Cmd/Ctrl + Shift + R`)으로 해결됩니다!**

