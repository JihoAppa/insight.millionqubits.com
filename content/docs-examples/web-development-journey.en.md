---
title: "Web Development Journey: From Frontend to Full Stack"
date: 2024-01-25T09:15:00+09:00
draft: false
tags: ["web-development", "frontend", "backend", "career"]
categories: ["development", "retrospective"]
author: "Jiho Appa"
showToc: true
TocOpen: false
description: "Sharing my growth process and lessons learned as a web developer."
---

## The Beginning: HTML and CSS

My web development journey started, like many others, with learning HTML and CSS. At first, I felt a great sense of achievement just by creating simple static web pages.

### My First Website

My first website was really simple:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Website</title>
</head>
<body>
    <h1>Hello!</h1>
    <p>Welcome to the world of web development.</p>
</body>
</html>
```

Looking back now, it's very basic, but at the time, just seeing it displayed in a browser was fascinating.

## Meeting JavaScript

Not satisfied with static pages, I soon started learning JavaScript. The ability to create dynamic websites was really exciting.

### First Interaction

I still remember the joy of implementing a simple feature where a message appears when you click a button:

```javascript
document.getElementById('myButton').addEventListener('click', function() {
    alert('You clicked the button!');
});
```

## The World of Frameworks

As I developed with pure JavaScript, I felt its limitations and started learning React. I realized the power of component-based development.

### React Component Example

```jsx
function Welcome({ name }) {
    return (
        <div className="welcome-box">
            <h2>Hello, {name}!</h2>
            <p>Welcome to the world of React.</p>
        </div>
    );
}
```

## Expanding to Backend

Feeling that frontend alone wasn't enough, I studied Node.js and Express. By working with databases and APIs, I came to understand the overall structure of web applications.

### Simple API Server

```javascript
const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
    res.json({ users: ['Alice', 'Bob', 'Charlie'] });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

## Lessons Learned

Important lessons from my web development journey:

1. **Fundamentals Matter**: Frameworks change, but basic principles remain constant
2. **Continuous Learning**: Technology keeps evolving, so you can't stop learning
3. **Practical Projects**: Theory is important, but actually building things is most effective
4. **Community Engagement**: You can learn a lot by interacting with other developers

## Future Goals

Currently, I'm working on various projects as a full-stack developer, but there's still much more I want to learn:

- **Cloud Infrastructure**: Cloud services like AWS and Azure
- **DevOps**: Building CI/CD pipelines
- **Microservices**: Designing scalable architecture
- **Performance Optimization**: Developing faster and more efficient applications

## Closing Thoughts

Web development is a field that requires constant learning and growth. While it can be difficult and challenging at times, it's equally rewarding. I hope you enjoy your own journey!
