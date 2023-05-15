# Digit_Recognizer

## Overview
This repository contains a digit recognizer project that utilizes a neural network model trained on the MNIST dataset. It includes a graphical user interface (GUI) where you can select an image file and predict the digit represented in the image.

## Features
- Graphical user interface for easy interaction.
- Trained model capable of recognizing handwritten digits.
- Simple and intuitive interface for selecting image files.

## Model
The digit recognizer project uses a neural network model to classify handwritten digits.
The model architecture consists of three layers:
- Input Layer: A flatten layer that takes input images of size 28x28 pixels and flattens them into a 1D array.
- Hidden Layers: Two dense layers with 128 and 20 units, respectively. These layers use the ReLU activation function, which introduces non-linearity to the model.
- Output Layer: A dense layer with 10 units, corresponding to the 10 possible digit classes (0 to 9). The output layer uses the softmax activation function to produce probabilities for each class.

The model is trained using the Adam optimizer and the sparse categorical cross-entropy loss function. It is trained on the MNIST dataset.

## Requirements
- Python 3.x
- Tkinter
- PIL (Python Imaging Library)
- TensorFlow
- NumPy

## Screen Shots
![image](https://github.com/Kerolos-Noshy/Digit_Recognizer/assets/101178275/a099065f-cf70-4150-b754-ad1d5558b8f5)
![image](https://github.com/Kerolos-Noshy/Digit_Recognizer/assets/101178275/1bf0c386-8620-46ed-b026-d72aea947ca7)

