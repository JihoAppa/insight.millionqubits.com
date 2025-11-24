# 블로그 포스트 템플릿 가이드

이 폴더에는 Obsidian에서 사용할 수 있는 다양한 블로그 포스트 템플릿이 포함되어 있습니다.

## 📁 템플릿 목록

### 기본 템플릿 (Templates 플러그인용)

1. **`blog-post-ko.md`** - 한국어 일반 포스트
2. **`blog-post-en.md`** - 영어 일반 포스트
3. **`blog-post-technical-ko.md`** - 한국어 기술 포스트 (단계별 튜토리얼)

### Templater 템플릿 (동적 생성)

4. **`templater-blog-post-ko.md`** - 한국어 (파일명과 날짜 자동 입력)
5. **`templater-blog-post-en.md`** - 영어 (파일명과 날짜 자동 입력)

---

## 🚀 사용 방법

### 방법 1: Templates 플러그인 (기본)

1. **플러그인 활성화**
   - Obsidian 설정 → Core plugins → Templates 활성화

2. **템플릿 폴더 설정**
   ```
   Settings → Templates
   Template folder location: 공개저널/.templates
   ```

3. **사용**
   - `Cmd + P` → "Templates: Insert template"
   - 원하는 템플릿 선택

### 방법 2: Templater 플러그인 (권장)

1. **플러그인 설치**
   - Community plugins → "Templater" 검색 및 설치

2. **설정**
   ```
   Settings → Templater
   Template folder location: 공개저널/.templates
   Trigger Templater on new file creation: ON
   ```

3. **사용**
   - `Cmd + T` → 템플릿 선택
   - 또는 새 파일 생성 시 자동 적용

---

## 📝 템플릿 상세 설명

### blog-post-ko.md (일반 포스트)

**용도**: 일반적인 블로그 글 작성

**구조**:
- 개요
- 본문 (섹션 1-3)
- 실전 팁
- 마치며

**예시**:
- 일상 경험 공유
- 책 리뷰
- 여행기
- 개인적인 생각

### blog-post-technical-ko.md (기술 포스트)

**용도**: 단계별 기술 튜토리얼

**구조**:
- 문제 상황/배경
- 환경 설정
- 구현 방법 (단계 1-3)
- 결과 및 성능
- 주의사항 및 한계
- 다음 단계

**예시**:
- 프로그래밍 튜토리얼
- 문제 해결 과정
- 도구 사용법
- 프로젝트 구현기

### Templater 템플릿

**차이점**: 동적 필드 사용

```markdown
title: "<% tp.file.title %>"        # 파일명 자동 입력
date: <% tp.date.now("...") %>      # 현재 날짜/시간 자동 입력
```

**장점**:
- 파일명이 자동으로 제목에 입력됨
- 현재 날짜/시간 자동 생성
- 템플릿 변수 활용 가능

---

## 🎨 Front Matter 필드 설명

| 필드 | 필수 | 설명 | 예시 |
|------|------|------|------|
| `title` | ✅ | 포스트 제목 | "Python 기초 가이드" |
| `date` | ✅ | 발행 날짜/시간 | 2024-11-24T15:00:00+09:00 |
| `draft` | ✅ | 초안 여부 | true (숨김), false (공개) |
| `tags` | ⭕ | 태그 목록 | ["Python", "프로그래밍"] |
| `categories` | ⭕ | 카테고리 | ["기술", "튜토리얼"] |
| `author` | ⭕ | 작성자 | "지호아빠" |
| `showToc` | ⭕ | 목차 표시 | true, false |
| `TocOpen` | ⭕ | 목차 펼침 | true, false |
| `description` | ⭕ | 포스트 요약 (SEO) | "Python 기초부터..." |

---

## 🔧 커스터마이징

### 템플릿 수정

1. 이 폴더의 템플릿 파일 직접 수정
2. Obsidian vault의 `.templates/` 폴더에 복사
3. 자신만의 스타일로 커스터마이징

### 새 템플릿 추가

```markdown
---
title: "나만의 템플릿"
date: 2024-11-24T15:00:00+09:00
draft: true
# 원하는 기본값 추가
---

원하는 구조로 작성...
```

---

## 📋 체크리스트

### 작성 전
- [ ] 적절한 템플릿 선택
- [ ] 파일명 규칙 확인 (`.ko.md` 또는 `.en.md`)
- [ ] 초안 폴더에 저장

### 작성 중
- [ ] 제목 입력
- [ ] 태그 추가
- [ ] 본문 작성
- [ ] 코드 블록 추가 (필요 시)
- [ ] 이미지 첨부 (필요 시)

### 발행 전
- [ ] `draft: true` → `false` 변경
- [ ] 날짜 확인 (현재 또는 과거)
- [ ] 설명(description) 입력 (SEO)
- [ ] 초안 → 블로그 폴더로 이동

---

## 💡 팁

### 효율적인 작성

1. **템플릿을 기반으로 시작**: 빈 문서보다 템플릿이 효율적
2. **Front matter는 나중에 수정**: 먼저 본문 작성에 집중
3. **태그는 작성 후 추가**: 내용을 다 쓴 후 관련 태그 추가
4. **코드 블록 언어 지정**: 구문 강조를 위해 언어 명시

### 일관성 유지

- 같은 유형의 글은 같은 템플릿 사용
- Front matter 필드 순서 통일
- 섹션 구조 일관성 유지

---

## 📚 참고

### 템플릿 복사 위치

Hugo 프로젝트의 템플릿들을 Obsidian vault로 복사:

```bash
# docs/templates/ → Obsidian vault의 .templates/
cp docs/templates/blog-post-ko.md \
   /Users/user/Vaults/appa-core-vault/공개저널/.templates/

cp docs/templates/templater-blog-post-ko.md \
   /Users/user/Vaults/appa-core-vault/공개저널/.templates/
```

### 추가 리소스

- [Obsidian Templates 문서](https://help.obsidian.md/Plugins/Templates)
- [Templater 문서](https://silentvoid13.github.io/Templater/)
- [Hugo Front Matter](https://gohugo.io/content-management/front-matter/)

---

**Happy Blogging! 📝**

