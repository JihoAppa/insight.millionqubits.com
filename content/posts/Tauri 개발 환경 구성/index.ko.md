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

이 글에서는 타우리 개발을 위한 환경을 구성을 합니다. 

## cargo 를 이용한 개발환경 구성하기

cargo 명령어를 통해서 `create-tauri-app`을 설치합니다. 여기서 `--locked` 옵션은`Cargo.lock`파일을 엄격하게 따르도록 하는 옵션으로 예기치 않은 의존성 업데이트로 인한 오류를 방지한다. 

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
## pnpm 사용 시 주의사항

tauri 와 pnpm 을 사용 시 node 버전이 LTS 버전이어야 한다. 그렇지 않을 경우 에러가 발생할 수 있다. 아래는 node.js 버전을 LTS 가 아닌 버전으로 pnpm tauri dev 명령어를 실행할 경우 발생하는 에러이다. 

```zsh
You are using Node.js 18.20.8. Vite requires Node.js version 20.19+ or 22.12+. Please upgrade your Node.js version.
error when starting dev server:
TypeError: crypto.hash is not a function
```

해당 에러가 발생되지 않으려면 fnm 또는 nvm 을 사용해서 node.js 20.x.x 버전과 같은 LTS 버전을 설치한다. 

```zsh
brew install pnpm
fnm use 20
cd <타우리 프로젝트 폴더>
pnpm install 
pnpm tauri dev
```

## 마치며

- cargo 를 통해서 타우리를 설치 및 실행 하는 방법을 알아봄
- 환경을 구성하는 과정에서 발생할 수 있는 에러를 확인함

---

**참고 자료**:
- [tauri 공식 홈페이지](https://tauri.app/)
- [tauri 깃헙 페이지](https://github.com/tauri-apps/tauri)

