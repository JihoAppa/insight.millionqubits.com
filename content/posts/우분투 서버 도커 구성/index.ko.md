---
title: 우분투 서버에서 도커 구성하기
date: 2025-12-03T18:09:02+09:00
draft: false
tags: []
categories: []
author: 지호아빠
showToc: true
TocOpen: true
description: ""
---

## 개요

시스템 패키지 목록을 업데이트 함. 그리고 도커 설치에 필요한 패키지들을 설치 
```zsh
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

도커 저장소의 패키지가 유효한지 확인을 위해 공식 GPG 키를 추가 

```zsh
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
도커의 stable 저장소를 추가하여 설치 소스를 지정함. 

```zsh
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
도커 엔진 설치 

```zsh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

설치 확이 후 테스트용 컨테이너를 실행

```zsh
sudo docker version
sudo docker run hello-world
```

sudo 없이 도커 사용을 위해 현재 사용자를 docker 그룹에 추가

```zsh
sudo usermod -aG docker $USER
```

도커 데몬 자동 시작을 설정함. 

```zsh
sudo systemctl enable docker  # 부팅 시 자동 시작 활성화
sudo systemctl status docker  # 현재 도커 서비스 상태 확인
```
## 마치며

gemini 를 통해서 튜토리얼을 뽑아서 고대로 명령어를 실행했더니 오류 없이 잘 끝남. GPG 설정이 왜 필요한지 그리고 sudo 없이 실행하는 방법을 적용해봄. 

---

**참고 자료**:
- [링크 1](https://example.com)
- [링크 2](https://example.com)

