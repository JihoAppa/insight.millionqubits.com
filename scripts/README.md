# 블로그 유틸리티 스크립트

이 폴더에는 블로그 관리를 위한 유틸리티 스크립트들이 포함되어 있습니다.

## 📝 rename-by-title.py

Obsidian 파일명을 Front Matter의 `title` 속성을 기반으로 일괄 변경하는 스크립트입니다.

### 사용법

```bash
# 기본 사용
python3 rename-by-title.py <directory> [lang]

# 한국어 파일 처리
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" ko

# 영어 파일 처리
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" en

# Dry-run (실제 변경 없이 미리보기)
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" ko --dry-run
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" ko -n
```

### 예시

```yaml
# 파일: 임시파일.md
---
title: "보안 전문가의 DAST 솔루션 개발기"
---
```

실행 후:
```bash
✅ Renamed: 임시파일.md → 보안-전문가의-dast-솔루션-개발기.ko.md
```

### 변환 규칙

| 원본 제목 | 변환된 파일명 |
|-----------|---------------|
| "Python 기초 가이드" | `python-기초-가이드.ko.md` |
| "AI & Machine Learning" | `ai-machine-learning.en.md` |
| "보안 (Security) 101" | `보안-security-101.ko.md` |

### 기능

- ✅ Front matter의 `title` 자동 추출
- ✅ URL 친화적인 slug 생성
- ✅ 한글/영문 자동 처리
- ✅ 특수문자 자동 제거
- ✅ 중복 파일명 체크
- ✅ Dry-run 모드 지원
- ✅ 일괄 처리

### 옵션

| 옵션 | 설명 |
|------|------|
| `directory` | 대상 디렉토리 경로 |
| `lang` | 언어 접미사 (`ko` 또는 `en`, 기본값: `ko`) |
| `--dry-run`, `-n` | 실제 변경 없이 미리보기만 |

---

## 통합 워크플로우

### 자동화 옵션 1: Git Pre-commit Hook

커밋 전에 자동으로 파일명 정리:

```bash
# .git/hooks/pre-commit
#!/bin/bash

SCRIPT="/Users/user/Websites/paper.millionqubits.com/scripts/rename-by-title.py"
BLOG_DIR="/Users/user/Vaults/appa-core-vault/공개저널/블로그"

python3 "$SCRIPT" "$BLOG_DIR" ko
python3 "$SCRIPT" "$BLOG_DIR" en

git add "$BLOG_DIR"
```

### 자동화 옵션 2: Cron Job

정기적으로 자동 실행:

```bash
# crontab -e
# 매일 자정에 실행
0 0 * * * /usr/bin/python3 /Users/user/Websites/paper.millionqubits.com/scripts/rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" ko
```

### 자동화 옵션 3: Obsidian 단축키

Obsidian의 Shell commands 플러그인 활용:

1. Shell commands 플러그인 설치
2. 명령어 추가:
   ```
   Name: Rename by title (Korean)
   Command: python3 /path/to/rename-by-title.py "{{folder_path:absolute}}" ko
   ```
3. 단축키 설정: `Cmd + Shift + R`

---

## 🐛 문제 해결

### Python 버전 확인

```bash
python3 --version
# Python 3.8 이상 필요
```

### 권한 오류

```bash
chmod +x rename-by-title.py
```

### 경로 오류

```bash
# 절대 경로 사용
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" ko

# 상대 경로는 현재 디렉토리 기준
python3 rename-by-title.py "./초안" ko
```

---

## 📚 관련 문서

- [제목 기반 자동 파일명 생성 가이드](../docs/OBSIDIAN_AUTO_FILENAME.md)
- [간단 워크플로우](../docs/OBSIDIAN_SIMPLE_WORKFLOW.md)
- [Obsidian 연동 가이드](../docs/OBSIDIAN_INTEGRATION.md)

---

**Happy Blogging! 🚀**

