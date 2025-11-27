---
title: 타우리(Tauri) 개발 환경 구축하기
date: 2025-11-27T11:15:41+09:00
draft: false
tags:
  - tauri
  - 타우리
  - rust
categories:
  - 개발환경구축
author: 지호아빠
showToc: true
TocOpen: true
description: tauri 를 활용한 개발환경 구축하기
filename: 영어-영어-en.md
---

## 개요

이 글에서는 타우리 개발을 위한 환경을 구성을 합니다. 향후 

## cargo 를 이용한 개발환경 구성하기

cargo 명령어를 통해서 `create-tauri-app`을 설치합니다. 여기서 `--locked` 옵션은 `Cargo.lock` 를 활용해 


```zsh
cargo install create-tauri-app --locked
```

tauri 는 프로젝트를 시작하기 위한 cli 도구를 지원합니다. 

```zsh
cargo create-tauri-app 
✔ Project name · 프로젝트 이름
✔ Identifier · com.사용자이름.프로젝트 이름
✔ Choose which language to use for your frontend · TypeScript / JavaScript - (pnpm, yarn, npm, deno, bun)
✔ Choose your package manager · pnpm
✔ Choose your UI template · React - (https://react.dev/)
✔ Choose your UI flavor · TypeScript

Template created! To get started run:
  cd 프로젝트 이름 
  pnpm install
  pnpm tauri android init
  pnpm tauri ios init

For Desktop development, run:
  pnpm tauri dev

For Android development, run:
  pnpm tauri android dev

For iOS development, run:
  pnpm tauri ios dev
```
### 섹션 1

첫 번째 주제에 대한 내용을 작성합니다.

### 섹션 2

두 번째 주제에 대한 내용을 작성합니다.

```python
# 코드 블록 예시
def hello_world():
    print("Hello, World!")
```

### 섹션 3

세 번째 주제에 대한 내용을 작성합니다.

## 실전 팁

실무에서 유용한 팁을 공유합니다:

1. **팁 1**: 첫 번째 팁 설명
2. **팁 2**: 두 번째 팁 설명
3. **팁 3**: 세 번째 팁 설명

## 마치며

이 글의 요약 및 마무리 내용을 작성합니다.

---

**참고 자료**:
- [링크 1](https://example.com)
- [링크 2](https://example.com)

