# Obsidian 제목 기반 자동 파일명 생성

이 가이드는 Obsidian에서 front matter의 `title` 속성을 참조하여 파일명이 자동으로 생성되도록 설정하는 방법을 설명합니다.

## 🎯 목표

```yaml
---
title: "보안 전문가의 DAST 솔루션 개발기"
---
```

위 제목이 자동으로 `보안-전문가의-dast-솔루션-개발기.ko.md`로 변환됨

---

## 방법 1: Templater + 파일명 변경 스크립트 (권장)

### 1단계: Templater 플러그인 설치 및 설정

1. **Templater 설치**
   - Community plugins → "Templater" 검색 및 설치

2. **Templater 설정**
   ```
   Settings → Templater
   Template folder location: 공개저널/.templates
   Trigger Templater on new file creation: ON
   Enable Folder Templates: ON
   ```

3. **폴더별 템플릿 설정**
   ```
   Add New (Folder Templates)
   Folder: 공개저널/초안
   Template: .templates/auto-filename-ko.md
   ```

### 2단계: 자동 파일명 생성 템플릿 작성

**파일**: `공개저널/.templates/auto-filename-ko.md`

```markdown
---
title: "<% tp.file.cursor(1) %>"
date: <% tp.date.now("YYYY-MM-DDTHH:mm:ssZ") %>
draft: true
tags: []
categories: []
author: "지호아빠"
showToc: true
TocOpen: false
description: ""
---

## 개요

<% tp.file.cursor(2) %>

## 본문

### 섹션 1

내용...

### 섹션 2

내용...

## 마치며

요약...

<%*
// 제목 입력 후 파일명 자동 변경 스크립트
setTimeout(async () => {
    const file = tp.config.target_file;
    const frontmatter = await tp.file.include("[[" + file.basename + "]]");
    const titleMatch = frontmatter.match(/^title:\s*"?([^"\n]+)"?/m);
    
    if (titleMatch && titleMatch[1]) {
        const title = titleMatch[1];
        // 한글, 영문, 숫자를 하이픈으로 연결
        const filename = title
            .toLowerCase()
            .replace(/[^\w\s가-힣ㄱ-ㅎㅏ-ㅣ-]/g, '') // 특수문자 제거
            .replace(/\s+/g, '-')                     // 공백을 하이픈으로
            .replace(/-+/g, '-')                      // 연속 하이픈 제거
            .replace(/^-|-$/g, '');                   // 앞뒤 하이픈 제거
        
        const newFilename = filename + '.ko.md';
        const newPath = file.parent.path + '/' + newFilename;
        
        // 파일명 변경
        if (file.basename !== filename) {
            await tp.file.rename(newFilename);
            new Notice(`파일명이 "${newFilename}"로 변경되었습니다.`);
        }
    }
}, 1000);
%>
```

### 3단계: 영어 버전 템플릿

**파일**: `공개저널/.templates/auto-filename-en.md`

```markdown
---
title: "<% tp.file.cursor(1) %>"
date: <% tp.date.now("YYYY-MM-DDTHH:mm:ssZ") %>
draft: true
tags: []
categories: []
author: "Jiho's Dad"
showToc: true
TocOpen: false
description: ""
---

## Overview

<% tp.file.cursor(2) %>

## Main Content

### Section 1

Content...

### Section 2

Content...

## Conclusion

Summary...

<%*
// Auto-rename file based on title
setTimeout(async () => {
    const file = tp.config.target_file;
    const frontmatter = await tp.file.include("[[" + file.basename + "]]");
    const titleMatch = frontmatter.match(/^title:\s*"?([^"\n]+)"?/m);
    
    if (titleMatch && titleMatch[1]) {
        const title = titleMatch[1];
        // Convert to URL-friendly slug
        const filename = title
            .toLowerCase()
            .replace(/[^\w\s-]/g, '')      // Remove special characters
            .replace(/\s+/g, '-')          // Replace spaces with hyphens
            .replace(/-+/g, '-')           // Remove consecutive hyphens
            .replace(/^-|-$/g, '');        // Remove leading/trailing hyphens
        
        const newFilename = filename + '.en.md';
        const newPath = file.parent.path + '/' + newFilename;
        
        // Rename file
        if (file.basename !== filename) {
            await tp.file.rename(newFilename);
            new Notice(`File renamed to "${newFilename}"`);
        }
    }
}, 1000);
%>
```

### 4단계: 사용 방법

1. **새 파일 생성**
   - `공개저널/초안/` 폴더에서 새 파일 생성
   - 임시 파일명으로 시작 (예: `Untitled.md`)

2. **템플릿 자동 적용**
   - 폴더 템플릿 설정으로 자동 적용

3. **제목 입력**
   ```yaml
   title: "보안 전문가의 DAST 솔루션 개발기"
   ```

4. **자동 파일명 변경**
   - 1초 후 자동으로 `보안-전문가의-dast-솔루션-개발기.ko.md`로 변경
   - 알림 표시

---

## 방법 2: Filename Heading Sync 플러그인

더 간단한 방법으로, 제목과 파일명을 항상 동기화하는 플러그인 사용:

### 1단계: 플러그인 설치

1. Community plugins → "Filename Heading Sync" 검색 및 설치
2. 플러그인 활성화

### 2단계: 설정

```
Settings → Filename Heading Sync

Sync Direction: File name → Heading
Ignore Regex: ^_.*  (언더스코어로 시작하는 파일 무시)
Use File Open Hook: ON
Use File Save Hook: ON
```

### 3단계: 사용

1. 파일의 첫 번째 H1 제목(`# 제목`)을 작성
2. 파일 저장 시 자동으로 파일명이 제목과 동기화됨

**한계**: Front matter의 title이 아닌 첫 번째 헤딩을 사용

---

## 방법 3: Python 스크립트로 일괄 변경

파일명을 나중에 일괄 변경하는 방법:

### 스크립트 생성

**파일**: `rename-by-title.py`

```python
#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^\w\s가-힣ㄱ-ㅎㅏ-ㅣ-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove consecutive hyphens
    text = re.sub(r'-+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text

def get_title_from_file(filepath):
    """Extract title from front matter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    try:
        front_matter = yaml.safe_load(match.group(1))
        return front_matter.get('title')
    except:
        return None

def rename_files(directory, lang='ko'):
    """Rename files based on title in front matter"""
    for filepath in Path(directory).glob('*.md'):
        title = get_title_from_file(filepath)
        if not title:
            print(f"⚠️  No title found: {filepath.name}")
            continue
        
        slug = slugify(title)
        new_filename = f"{slug}.{lang}.md"
        new_filepath = filepath.parent / new_filename
        
        if filepath.name == new_filename:
            print(f"✓ Already correct: {filepath.name}")
            continue
        
        if new_filepath.exists():
            print(f"❌ File exists: {new_filename}")
            continue
        
        filepath.rename(new_filepath)
        print(f"✓ Renamed: {filepath.name} → {new_filename}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 rename-by-title.py <directory> [lang]")
        print("Example: python3 rename-by-title.py ./초안 ko")
        sys.exit(1)
    
    directory = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else 'ko'
    
    print(f"Renaming files in: {directory}")
    print(f"Language suffix: {lang}")
    print("-" * 50)
    
    rename_files(directory, lang)
    print("-" * 50)
    print("Done!")
```

### 사용 방법

```bash
# 의존성 설치
pip3 install pyyaml

# 스크립트 실행
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" ko

# 영어 파일
python3 rename-by-title.py "/Users/user/Vaults/appa-core-vault/공개저널/초안" en
```

---

## 방법 4: Obsidian Git 커밋 전 자동 변환

Git commit 전에 자동으로 파일명 변경:

### Git Pre-commit Hook 설정

**파일**: `.git/hooks/pre-commit`

```bash
#!/bin/bash

# Python 스크립트 경로
SCRIPT="/Users/user/Websites/paper.millionqubits.com/scripts/rename-by-title.py"
DRAFT_DIR="/Users/user/Vaults/appa-core-vault/공개저널/블로그"

# 파일명 정리
python3 "$SCRIPT" "$DRAFT_DIR" ko
python3 "$SCRIPT" "$DRAFT_DIR" en

# 변경사항 추가
git add "$DRAFT_DIR"
```

실행 권한 부여:
```bash
chmod +x .git/hooks/pre-commit
```

---

## 권장 워크플로우

### 최종 권장: Templater 자동 파일명 변경

1. **새 파일 생성**
   - `초안/` 폴더에 임의의 이름으로 생성

2. **템플릿 적용**
   - 자동으로 적용되거나 `Cmd + T`

3. **제목 입력**
   ```yaml
   title: "AI 기반 DAST 솔루션 개발 여정"
   ```

4. **자동 변환**
   - 1초 후 → `ai-기반-dast-솔루션-개발-여정.ko.md`

5. **글 작성**
   - 자유롭게 작성

6. **발행**
   - `블로그/` 폴더로 이동
   - 동기화 버튼 클릭

---

## 파일명 규칙

### 자동 변환 규칙

| 원본 제목 | 변환된 파일명 |
|-----------|---------------|
| "Python 기초 가이드" | `python-기초-가이드.ko.md` |
| "DAST 솔루션 개발" | `dast-솔루션-개발.ko.md` |
| "AI & Machine Learning" | `ai-machine-learning.en.md` |
| "보안 (Security) 101" | `보안-security-101.ko.md` |

### 규칙 상세

1. **소문자 변환**: 모든 영문자 소문자
2. **특수문자 제거**: `!@#$%^&*()` 등 제거
3. **공백 → 하이픈**: 모든 공백을 `-`로 변환
4. **연속 하이픈 제거**: `--` → `-`
5. **언어 접미사**: `.ko.md` 또는 `.en.md` 자동 추가

---

## 🐛 문제 해결

### Templater 스크립트가 작동하지 않음

1. **Templater 설정 확인**
   ```
   Enable System Commands: ON
   ```

2. **콘솔 로그 확인**
   - `Cmd + Opt + I` (개발자 도구)
   - Console 탭에서 에러 확인

3. **수동 실행 테스트**
   - `Cmd + P` → "Templater: Replace templates in the active file"

### 파일명에 이상한 문자

```python
# slugify 함수 커스터마이징
def slugify(text):
    # 허용할 문자 추가
    text = re.sub(r'[^\w\s가-힣ㄱ-ㅎㅏ-ㅣ0-9-]', '', text)
    # ...
```

### 중복 파일명

템플릿에 타임스탬프 추가:

```markdown
<%*
const filename = slug + '-' + tp.date.now("YYYYMMDDHHmmss") + '.ko.md';
%>
```

---

## 📚 추가 리소스

- [Templater 문서](https://silentvoid13.github.io/Templater/)
- [Obsidian API](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin)
- [Python slugify](https://github.com/un33k/python-slugify)

---

**자동화된 워크플로우로 더 효율적인 블로깅을! 🚀**

