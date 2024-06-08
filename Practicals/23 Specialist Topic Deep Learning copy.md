# Practical 23: Deep Learning Crash Course

## Overview

This practical exercise is designed to provide a crash course on deep learning (DL). We will focus on neural networks, backpropagation, and gradient descent. Practical examples using the MNIST dataset will be included to classify handwritten numbers. The session is divided into three parts and will take about 3 hours and 15 minutes to complete, including a buffer for extension activities.

## Part 1: Introduction to Deep Learning (1 hour)

### Section 1: Neural Networks Fundamentals (20 minutes)

1. **What is Deep Learning?**
   - Deep Learning is a subset of machine learning that uses neural networks with many layers (deep networks) to model complex patterns in data.

2. **Neural Networks:**
   - **Neurons:** Basic unit of a neural network that receives input, processes it, and passes it to the next layer.
   - **Layers:** Neural networks consist of an input layer, hidden layers, and an output layer.
   - **Activation Functions:** Functions like ReLU, sigmoid, and tanh that introduce non-linearity to the model.

3. **Backpropagation:**
   - A method used to calculate the gradient of the loss function with respect to each weight by the chain rule, used for training the neural network.

4. **Gradient Descent:**
   - An optimization algorithm used to minimize the loss function by iteratively updating the weights in the direction of the negative gradient.

### Section 2: Practical Example - MNIST Dataset (40 minutes)

0. **Prerequisites:**
   ```python
   import numpy as np
   import os
   import struct


   def load_mnist(path, kind="train"):
      """Load MNIST data from `path`"""
      labels_path = os.path.join(path, f"{kind}-labels.idx1-ubyte")
      images_path = os.path.join(path, f"{kind}-images.idx3-ubyte")


      with open(labels_path, "rb") as lbpath:
         magic, n = struct.unpack(">II", lbpath.read(8))
         labels = np.fromfile(lbpath, dtype=np.uint8)

      with open(images_path, "rb") as imgpath:
         magic, num, rows, cols = struct.unpack(">IIII", imgpath.read(16))
         images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)

      return images, labels


   # Example usage
   X_train, y_train = load_mnist("mnist", kind="train")
   X_test, y_test = load_mnist("mnist", kind="t10k")
   ```
1. **Loading the MNIST Dataset:**
   ```python
   %pip install tensorflow
   import tensorflow as tf

   # Normalize the data
   X_train, X_test = X_train / 255.0, X_test / 255.0

   # Transform the data
   X_train = X_train.reshape(X_train.shape[0], 28, 28)
   X_test = X_test.reshape(X_test.shape[0], 28, 28)
   ```

2. **Building a Neural Network:**
   ```python
   from tensorflow.keras.models import Sequential
   from tensorflow.keras.layers import Dense, Flatten

   # Build the model
   model = Sequential([
       Flatten(input_shape=(28, 28)),
       Dense(128, activation='relu'),
       Dense(10, activation='softmax')
   ])

   # Compile the model
   model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])

   # Train the model
   model.fit(X_train, y_train, epochs=5)

   # Evaluate the model
   test_loss, test_acc = model.evaluate(X_test, y_test)
   print(f'Test accuracy: {test_acc}')
   ```

   **Exercise 1:**
   - TODO: Modify the neural network to add more layers and change activation functions. Observe how these changes affect performance.

## Part 2: Advanced Deep Learning Models (30 minutes)

### Section 1: Transformers and Convolutional Neural Networks (CNNs) (15 minutes)

1. **Transformers:**
   - Introduced in the paper "Attention is All You Need" by Vaswani et al.
   - Transformers use self-attention mechanisms to process input data in parallel, which is efficient for tasks like language modeling and translation.

2. **Convolutional Neural Networks (CNNs):**
   - Used primarily for image data.
   - Consist of convolutional layers that apply filters to the input data, pooling layers to reduce dimensionality, and fully connected layers for classification.

### Section 2: Practical Example - Image Segmentation with CNNs (15 minutes)

1. **Building a CNN for Image Segmentation:**
   ```python
   from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D

   # Build the model
   model = Sequential([
       Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)),
       MaxPooling2D((2, 2), padding='same'),
       UpSampling2D((2, 2)),
       Conv2D(1, (3, 3), activation='sigmoid', padding='same')
   ])

   # Compile the model
   model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

   # Prepare data (reshape and normalize)
   X_train = X_train.reshape(-1, 28, 28, 1)
   X_test = X_test.reshape(-1, 28, 28, 1)

   # Train the model
   model.fit(X_train, X_train, epochs=5, validation_data=(X_test, X_test))

   # Evaluate the model
   test_loss, test_acc = model.evaluate(X_test, X_test)
   print(f'Test accuracy: {test_acc}')
   ```

   **Exercise 2:**
   - TODO: Modify the CNN to add more convolutional and pooling layers. Experiment with different filter sizes and observe the impact on performance.

### Section 3: Applications in Cryptography and Cybersecurity (15 minutes)

1. **Deep Learning in Cryptography:**
   - **Encryption and Decryption:** Using neural networks to enhance encryption algorithms.
   - **Key Management:** Improving the security of key generation and distribution.

2. **Deep Learning in Cybersecurity:**
   - **Intrusion Detection Systems (IDS):** Identifying malicious activities in network traffic.
   - **Malware Detection:** Classifying and detecting malware using neural networks.

## Part 3: Extension Activities and Interactive Q&A (1 hour 45 minutes)

### Section 1: Interactive Q&A (45 minutes)

1. **Open Discussion:**
   - Encourage students to ask questions about the topics covered in the crash courses.
   - Discuss common challenges and solutions in implementing deep learning models.

### Section 2: Hands-On Extension Activities (1 hour)

1. **Activity 1: Experiment with Different Datasets:**
   - TODO: Load a new dataset and apply the neural network models you have learned to classify or segment the data.

2. **Activity 2: Hyperparameter Tuning:**
   - TODO: Experiment with different hyperparameters (learning rate, batch size, number of epochs) to improve model performance.

3. **Activity 3: Implement a Transformer Model:**
   - TODO: Use TensorFlow or PyTorch to implement a simple transformer model for a text classification task.

### Summary

- You have learned about neural networks, backpropagation, and gradient descent.
- You have implemented practical examples using the MNIST dataset.
- You have explored advanced deep learning models, such as transformers and CNNs.
- You have discussed the applications of deep learning in cryptography and cybersecurity.
- You have engaged in interactive Q&A and hands-on extension activities.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"23 Specialist Topic - Deep Learning.ipynb"` in the `"Practical Solutions"` directory.
