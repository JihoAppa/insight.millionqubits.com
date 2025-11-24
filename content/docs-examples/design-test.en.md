---
title: "[Design Test] Deep Learning with Python Typography"
date: 2023-11-24T16:30:00+09:00
draft: false
author: "Jiho's Dad"
tags: ["design", "test", "typography"]
description: "Typography and layout design test post based on Deep Learning with Python book"
---

This post is a fictional article created to test the Deep Learning with Python style design. We are using this text to evaluate the readability of the font, the letter spacing, the line height, and the overall harmony between paragraphs. Specifically, we want to see if the reader feels comfortable reading long sentences and dense paragraphs without experiencing visual fatigue. The main purpose of this test is to check the visual density and the balance of the overall layout when the text is tightly packed.

## What is Deep Learning?

Deep Learning is a specific subfield of machine learning that learns data representations in successive layers. Beyond simply inputting data and getting results, it involves understanding the intrinsic structure and patterns of the data and extracting higher-level abstracted information from it. This learning method is inspired by how the human brain processes information and is designed to mimic the structure of numerous neurons intricately connected to transmit signals. Therefore, deep learning models tend to acquire more sophisticated and accurate predictive capabilities as the amount of data increases and the training time lengthens.

### 1.1 Artificial Intelligence, Machine Learning, and Deep Learning

![PaperMod Cover Image](/images/papermod-cover.png)
*This is an example of the PaperMod theme cover image.*

Artificial Intelligence is typically defined as the effort to automate intellectual tasks normally performed by humans. Early AI researchers attempted to implement intelligence through explicit rules and logic, but this approach had limitations in solving complex and uncertain real-world problems. In contrast, Machine Learning takes an approach of learning rules from data rather than being explicitly programmed. In other words, instead of directly telling the computer how to solve a problem, we show it numerous examples and encourage it to find the patterns on its own.

#### 1.1.1 The "Deep" in Deep Learning

The deep in deep learning doesn't simply mean profound insight, but rather represents the idea of learning representations through successive layers. The depth of a model is determined by how many layers are used to build the model from data. Recent deep learning models have tens to hundreds of layers, and each layer extracts slightly more complex and abstract features from the input data. For example, in an image recognition model, the first layer might recognize simple shapes like lines or edges, and as the layers get deeper, it recognizes partial features like eyes, noses, and mouths, eventually recognizing the entire human face.

## Mathematical Building Blocks of Neural Networks

To understand deep learning, you need to know a few simple mathematical concepts. Although the word mathematics might feel burdensome, the math used in deep learning is mostly based on the basics of linear algebra. If you understand how to represent data as arrays of numbers and how to manipulate them, you will be able to grasp how neural networks work much more intuitively.

### 2.1 Tensors

Tensors are containers for data. For example, a matrix is a 2D tensor. Tensors are a generalization of matrices to an arbitrary number of dimensions. Tensors are the fundamental data structure of deep learning, and all input data, output data, and weights inside the network are stored and processed in the form of tensors.

*   Scalar (0D tensor): A tensor containing only a single number. This is the most basic form of a tensor and has a 0-dimensional axis.
*   Vector (1D tensor): An array of numbers. A vector has one axis and can be seen as a list representing the features of the data.
*   Matrix (2D tensor): An array of vectors. A matrix has two axes (rows and columns) and is suitable for representing tabular data like an Excel spreadsheet.

## The Engine of Neural Networks: Gradient-Based Optimization

Each layer in a neural network transforms input data to produce output data. This transformation is determined by the layer's weights. Weights are parameters that determine the network's performance on the training data and are continuously updated during the learning process.

1.  Initially, weights are set randomly. In this state, the network cannot perform any meaningful tasks.
2.  Input data is passed through the network to obtain predictions. Initially, due to the random weights, the predictions will be significantly different from the actual values.
3.  The difference (loss) between predictions and actual values is calculated. This loss value serves as an indicator of how incorrectly the network predicted.
4.  Weights are adjusted slightly in the direction that reduces the loss. Mathematical techniques like differentiation are used to find the direction that minimizes the loss function.

By repeating this process, the network gradually learns how to correctly process the data. Through tens of thousands or hundreds of thousands of iterations, the loss value gradually approaches zero, and the network's prediction accuracy improves dramatically. This is the principle of how deep learning learns, and through this, we are achieving amazing results in various fields such as image recognition, natural language processing, and speech recognition.
