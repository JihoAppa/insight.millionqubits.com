---
title: "Python Fundamentals: Variables and Data Types"
date: 2024-01-20T14:30:00+09:00
draft: false
tags: ["python", "programming", "tutorial"]
categories: ["development"]
author: "Jiho Appa"
showToc: true
TocOpen: false
description: "Learn about basic variables and data types in Python programming."
---

## What is Python?

Python is a high-level programming language developed by Guido van Rossum in 1991. With its easy-to-read and easy-to-learn syntax, it's widely used by beginners and professionals alike.

## Declaring Variables

Declaring variables in Python is very straightforward. Unlike other languages, you don't need to specify the type; you simply assign a value.

```python
# Examples of variable declaration
name = "Jiho Appa"
age = 35
is_developer = True
height = 175.5
```

### Variable Naming Rules

When naming variables, you must follow these rules:

1. Only letters, numbers, and underscores (_) are allowed
2. Cannot start with a number
3. Case-sensitive
4. Reserved keywords cannot be used

## Basic Data Types

Python has several basic data types. Understanding the characteristics of each is important.

### Numbers

Numeric types are divided into integers (int) and floating-point numbers (float):

```python
# Integer type
count = 100
negative = -50

# Float type
pi = 3.14159
temperature = -5.5
```

### Strings

Strings represent text data:

```python
# String declaration
greeting = "Hello"
message = 'Welcome'
multiline = """You can write
multiple lines
of text"""
```

### Booleans

A data type that represents True or False:

```python
is_active = True
is_admin = False
has_permission = True
```

### Lists

A data type that stores multiple values in order:

```python
# List examples
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "Hello", True, 3.14]
```

## Checking Types

To check the type of a variable, use the `type()` function:

```python
name = "Python"
print(type(name))  # <class 'str'>

age = 30
print(type(age))   # <class 'int'>
```

## Conclusion

In this post, we learned about basic variables and data types in Python. In the next post, we'll cover operators and conditional statements.
