# DNS 설정 가이드

이 문서는 `paper.millionqubits.com` 도메인을 GitHub Pages에 연결하는 방법을 안내합니다.

## 목차

1. [GitHub Pages 설정](#github-pages-설정)
2. [DNS 레코드 설정](#dns-레코드-설정)
3. [DNS 제공자별 가이드](#dns-제공자별-가이드)
4. [SSL 인증서 설정](#ssl-인증서-설정)
5. [문제 해결](#문제-해결)

---

## GitHub Pages 설정

### 1단계: GitHub 저장소 생성

1. GitHub에서 새 저장소 생성
2. 저장소 이름: `paper.millionqubits.com` (또는 원하는 이름)
3. Public으로 설정 (Private도 가능하나 Pro 계정 필요)

### 2단계: 저장소 업로드

```bash
cd /Users/user/Websites/paper.millionqubits.com

# 원격 저장소 추가 (yourusername을 실제 GitHub 사용자명으로 변경)
git remote add origin https://github.com/yourusername/paper.millionqubits.com.git

# 첫 커밋 및 푸시
git add .
git commit -m "Initial commit: Hugo blog setup"
git push -u origin main
```

### 3단계: GitHub Pages 활성화

1. GitHub 저장소로 이동
2. **Settings** > **Pages** 클릭
3. **Source** 섹션:
   - Source: **GitHub Actions** 선택
4. **Custom domain** 섹션:
   - `paper.millionqubits.com` 입력
   - **Save** 클릭
5. **Enforce HTTPS** 체크 (DNS 설정 후 활성화됨)

---

## DNS 레코드 설정

두 가지 방법 중 하나를 선택할 수 있습니다:

### 방법 1: CNAME 레코드 (권장)

**장점**: GitHub IP가 변경되어도 자동으로 업데이트됨

| Type  | Name  | Content (Target)          | TTL  |
|-------|-------|---------------------------|------|
| CNAME | paper | yourusername.github.io    | Auto |

### 방법 2: A 레코드

**장점**: 루트 도메인(@)도 사용 가능

GitHub Pages의 IP 주소 (2024년 기준):
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

| Type | Name   | Content          | TTL  |
|------|--------|------------------|------|
| A    | @      | 185.199.108.153  | Auto |
| A    | @      | 185.199.109.153  | Auto |
| A    | @      | 185.199.110.153  | Auto |
| A    | @      | 185.199.111.153  | Auto |
| CNAME| paper  | yourusername.github.io | Auto |

**주의**: GitHub Pages IP는 변경될 수 있으므로 [공식 문서](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain)에서 최신 IP를 확인하세요.

---

## DNS 제공자별 가이드

### Cloudflare

1. Cloudflare 대시보드 로그인
2. 도메인 (`millionqubits.com`) 선택
3. **DNS** 탭 클릭
4. **Add record** 클릭

#### CNAME 레코드 추가
```
Type: CNAME
Name: paper
Target: yourusername.github.io
Proxy status: DNS only (회색 구름)
TTL: Auto
```

**중요**: Proxy status를 **DNS only**로 설정해야 합니다. Proxied (주황색 구름)로 하면 SSL 인증서 발급이 실패할 수 있습니다.

#### 추가 설정 (선택사항)
- **SSL/TLS** > **Overview**: Full로 설정
- **SSL/TLS** > **Edge Certificates**: Always Use HTTPS 활성화

---

### 가비아 (Gabia)

1. [가비아 My가비아](https://my.gabia.com/) 로그인
2. **서비스 관리** > **도메인** 클릭
3. `millionqubits.com` 선택 > **관리** 클릭
4. **DNS 정보** > **DNS 설정** 클릭

#### CNAME 레코드 추가
```
레코드 타입: CNAME
호스트: paper
값/위치: yourusername.github.io
TTL: 3600
```

#### 적용 시간
- 가비아는 DNS 변경이 최대 24-48시간 소요될 수 있습니다.

---

### AWS Route 53

1. AWS 콘솔 > **Route 53** 이동
2. **Hosted zones** > `millionqubits.com` 선택
3. **Create record** 클릭

#### CNAME 레코드
```
Record name: paper
Record type: CNAME
Value: yourusername.github.io
Routing policy: Simple routing
TTL: 300
```

#### 별칭 레코드 (Alias)로도 가능
```
Record name: paper
Record type: A
Alias: No
Value: GitHub Pages IP 주소들
```

---

### Google Domains (현재 Squarespace로 이전)

1. [Google Domains](https://domains.google.com/) 로그인
2. 도메인 선택
3. **DNS** 클릭

#### Custom Records
```
Host name: paper
Type: CNAME
TTL: 1H
Data: yourusername.github.io
```

---

### Namecheap

1. Namecheap 대시보드 로그인
2. **Domain List** > 도메인 선택 > **Manage**
3. **Advanced DNS** 탭

#### CNAME 레코드
```
Type: CNAME Record
Host: paper
Value: yourusername.github.io
TTL: Automatic
```

---

## SSL 인증서 설정

### 자동 SSL (Let's Encrypt)

GitHub Pages는 자동으로 Let's Encrypt SSL 인증서를 발급합니다.

#### 활성화 절차

1. DNS 레코드 설정 완료 (위 단계)
2. DNS 전파 대기 (10분 ~ 24시간)
3. DNS 전파 확인:
   ```bash
   # 터미널에서 확인
   dig paper.millionqubits.com
   
   # 또는
   nslookup paper.millionqubits.com
   ```

4. GitHub 저장소 **Settings** > **Pages**
5. **Enforce HTTPS** 체크박스 활성화

#### 인증서 발급 시간
- 일반적으로 10분 이내
- 최대 24시간 소요 가능

### 인증서 갱신

- GitHub Pages가 자동으로 갱신합니다
- 추가 작업 불필요

---

## 문제 해결

### DNS 전파 확인

```bash
# macOS/Linux
dig paper.millionqubits.com

# Windows
nslookup paper.millionqubits.com

# 온라인 도구 사용
# https://www.whatsmydns.net/
```

### DNS가 전파되지 않을 때

1. **TTL 확인**: TTL이 높으면 전파가 느립니다
2. **캐시 삭제**:
   ```bash
   # macOS
   sudo dscacheutil -flushcache
   sudo killall -HUP mDNSResponder
   
   # Windows
   ipconfig /flushdns
   
   # Linux
   sudo systemd-resolve --flush-caches
   ```

3. **DNS 서버 변경**: Google DNS(8.8.8.8) 또는 Cloudflare DNS(1.1.1.1) 사용

### SSL 인증서가 발급되지 않을 때

1. **DNS 전파 확인**: 위의 명령어로 확인
2. **Cloudflare Proxy 해제**: Cloudflare 사용 시 DNS only로 설정
3. **HTTPS 체크 해제 후 재활성화**:
   - GitHub Pages 설정에서 Enforce HTTPS 체크 해제
   - 10분 대기
   - 다시 체크
4. **CNAME 파일 확인**: `static/CNAME` 파일에 도메인이 올바르게 입력되어 있는지 확인

### 404 에러가 발생할 때

1. **GitHub Actions 확인**:
   - GitHub 저장소 > **Actions** 탭
   - 최근 워크플로우 실행 상태 확인
   - 에러가 있다면 로그 확인

2. **CNAME 파일 확인**:
   ```bash
   # CNAME 파일 내용 확인
   cat /Users/user/Websites/paper.millionqubits.com/static/CNAME
   
   # 출력: paper.millionqubits.com
   ```

3. **baseURL 확인**:
   ```yaml
   # hugo.yaml
   baseURL: 'https://paper.millionqubits.com/'
   ```

### 스타일이 깨질 때

1. **baseURL 슬래시 확인**: 끝에 `/` 포함 여부
2. **브라우저 캐시 삭제**: Cmd+Shift+R (macOS) 또는 Ctrl+Shift+R (Windows)
3. **Hugo 빌드 확인**:
   ```bash
   cd /Users/user/Websites/paper.millionqubits.com
   hugo --gc --minify
   ```

---

## 도메인 검증

모든 설정이 완료되면 다음을 확인하세요:

### 체크리스트

- [ ] DNS 레코드 정상 설정 (`dig` 또는 `nslookup`으로 확인)
- [ ] GitHub Pages에서 커스텀 도메인 설정됨
- [ ] CNAME 파일이 `static/` 폴더에 존재
- [ ] SSL 인증서 발급됨 (자물쇠 아이콘 표시)
- [ ] `https://paper.millionqubits.com` 접속 가능
- [ ] `http://paper.millionqubits.com` 자동으로 HTTPS로 리다이렉트됨

### 접속 테스트

```bash
# HTTP 상태 확인
curl -I https://paper.millionqubits.com

# 예상 출력:
# HTTP/2 200
# content-type: text/html; charset=utf-8
# ...
```

---

## 유지보수

### DNS 레코드 업데이트

GitHub Pages IP가 변경되면 (매우 드뭄):

1. [GitHub 공식 문서](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) 확인
2. DNS 제공자에서 A 레코드 업데이트

### SSL 인증서 문제 시

```bash
# GitHub에서 인증서 강제 재발급
# 1. Settings > Pages에서 Custom domain 제거
# 2. Save
# 3. 다시 입력 후 Save
# 4. Enforce HTTPS 체크
```

---

## 참고 자료

- [GitHub Pages 공식 문서](https://docs.github.com/en/pages)
- [커스텀 도메인 설정](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [DNS 레코드 타입 설명](https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/)
- [Let's Encrypt SSL](https://letsencrypt.org/)

---

## 도움이 필요하신가요?

문제가 계속되면:

1. GitHub Pages 상태 페이지 확인: https://www.githubstatus.com/
2. DNS 전파 도구로 확인: https://www.whatsmydns.net/
3. GitHub 저장소 Issues에서 유사한 문제 검색
4. 이메일로 문의: jiho_appa@naver.com

