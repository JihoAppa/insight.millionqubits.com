---
title: "Python 기초: 변수와 자료형"
date: 2024-01-20T14:30:00+09:00
draft: false
tags: ["python", "프로그래밍", "튜토리얼"]
categories: ["개발"]
author: "지호아빠"
showToc: true
TocOpen: false
description: "Python의 기본적인 변수와 자료형에 대해 알아봅니다."
---

## Python이란?

Python은 1991년 귀도 반 로섬(Guido van Rossum)이 개발한 고급 프로그래밍 언어입니다. 읽기 쉽고 배우기 쉬운 문법으로 초보자부터 전문가까지 널리 사용되고 있습니다.

## 변수 선언하기

Python에서 변수를 선언하는 것은 매우 간단합니다. 다른 언어와 달리 타입을 명시할 필요가 없으며, 값을 할당하기만 하면 됩니다.

```python
# 변수 선언의 예
name = "지호아빠"
age = 35
is_developer = True
height = 175.5
```

### 변수 명명 규칙

변수 이름을 지을 때는 다음 규칙을 따라야 합니다:

1. 문자, 숫자, 언더스코어(_)만 사용할 수 있습니다
2. 숫자로 시작할 수 없습니다
3. 대소문자를 구분합니다
4. 예약어는 사용할 수 없습니다

## 기본 자료형

Python에는 여러 가지 기본 자료형이 있습니다. 각각의 특성을 이해하는 것이 중요합니다.

### 숫자형 (Numbers)

숫자형은 정수(int)와 실수(float)로 나뉩니다:

```python
# 정수형
count = 100
negative = -50

# 실수형
pi = 3.14159
temperature = -5.5
```

### 문자열 (String)

문자열은 텍스트 데이터를 표현합니다:

```python
# 문자열 선언
greeting = "안녕하세요"
message = '반갑습니다'
multiline = """여러 줄의
문자열을
작성할 수 있습니다"""
```

### 불리언 (Boolean)

참(True)과 거짓(False)을 나타내는 자료형입니다:

```python
is_active = True
is_admin = False
has_permission = True
```

### 리스트 (List)

여러 값을 순서대로 저장하는 자료형입니다:

```python
# 리스트 예제
numbers = [1, 2, 3, 4, 5]
fruits = ["사과", "바나나", "오렌지"]
mixed = [1, "Hello", True, 3.14]
```

## 타입 확인하기

변수의 타입을 확인하려면 `type()` 함수를 사용합니다:

```python
name = "Python"
print(type(name))  # <class 'str'>

age = 30
print(type(age))   # <class 'int'>
```

## 마치며

이번 포스트에서는 Python의 기본적인 변수와 자료형에 대해 알아보았습니다. 다음 포스트에서는 연산자와 조건문에 대해 다루겠습니다.
