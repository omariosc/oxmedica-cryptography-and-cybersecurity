# Practical 9: Cryptography Lab Maths

## Overview

This practical exercise is designed to introduce you to the mathematical principles behind encryption. You will learn how to encrypt a message using simple mathematical techniques. This session will take about 30 minutes to complete.

## Task

### Part 1: Introduction to Encryption (10 minutes)

1. **What is Encryption?**
   - Encryption is the process of converting a plain text message into an unreadable format using a mathematical algorithm and a key.
   - The purpose of encryption is to protect the confidentiality of the message.

2. **Basic Concepts:**
   - **Plaintext:** The original message that needs to be encrypted.
   - **Ciphertext:** The encrypted message.
   - **Key:** A piece of information used in the encryption process to convert plaintext into ciphertext and vice versa.

3. **Research Task:**
   - Research different types of encryption algorithms used in modern cryptography, such as symmetric encryption, asymmetric encryption, and hashing algorithms.
   - Discuss the advantages and disadvantages of each type of encryption algorithm.

### Part 2: Caesar Cipher (10 minutes)

1. **Introduction to Caesar Cipher:**
   - The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
   - Example: With a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

2. **Encryption Process:**
   - Choose a shift value (key).
   - For each letter in the plaintext, find its corresponding letter in the ciphertext by shifting it by the chosen value.
3. **Example:**
   - Plaintext: HELLO
   - Key: 3
   - Encryption Steps:
     - H -> K
     - E -> H
     - L -> O
     - L -> O
     - O -> R
   - Ciphertext: KHOOR

4. **Decryption Process:**
   - To decrypt the message, shift each letter in the ciphertext back by the same value.
   - Example:
     - K -> H
     - H -> E
     - O -> L
     - O -> L
     - R -> O
   - Plaintext: HELLO

### Part 3: Vigenère Cipher (10 minutes)

1. **Introduction to Vigenère Cipher:**
   - The Vigenère Cipher is a more complex form of substitution cipher that uses a keyword to shift letters by different amounts.
   - Example: Using the keyword "KEY", the shifts would be based on the positions of 'K', 'E', and 'Y' in the alphabet.

2. **Encryption Process:**
   - Choose a keyword.
   - Repeat the keyword so it matches the length of the plaintext.
   - For each letter in the plaintext, shift it by the corresponding letter in the keyword.

3. **Example:**
   - Plaintext: ATTACKATDAWN
   - Keyword: KEYKEYKEYKEY
   - Encryption Steps:
     - A (shift by K) -> K
     - T (shift by E) -> X
     - T (shift by Y) -> R
     - A (shift by K) -> K
     - C (shift by E) -> G
     - K (shift by Y) -> I
     - A (shift by K) -> K
     - T (shift by E) -> X
     - D (shift by Y) -> B
     - A (shift by K) -> K
     - W (shift by E) -> A
     - N (shift by Y) -> L
   - Ciphertext: KXRGIKXBKAL

4. **Decryption Process:**
   - To decrypt the message, shift each letter in the ciphertext back by the corresponding letter in the keyword.
   - Example:
     - K (shift by K) -> A
     - X (shift by E) -> T
     - R (shift by Y) -> T
     - K (shift by K) -> A
     - G (shift by E) -> C
     - I (shift by Y) -> K
     - K (shift by K) -> A
     - X (shift by E) -> T
     - B (shift by Y) -> D
     - K (shift by K) -> A
     - A (shift by E) -> W
     - L (shift by Y) -> N
   - Plaintext: ATTACKATDAWN


## Answers:
Part 2: 

Plaintext: HIHOWAREYOU
Key: 2
Encryption Steps:
- H --> J
- I --> K
- H --> J
- O --> Q
- W --> Y
- A --> C
- R --> T
- E --> G
- Y --> A
- O --> Q
- U --> W
Ciphertext: JKJQYCTGAQW

Decryption Steps:
- J --> H
- K --> I
- J --> H
- Q --> O
- Y --> W
- C --> A
- T --> R
- G --> E
- A --> Y
- Q --> O
- W --> U
Plaintext: HIHOWAREYOU

Part 3:
Plaintext: HIHOWAREYOU
Keyword: AREAREAREAR
Encryption Steps:
- H (shift by A) -> H
- I (shift by R) -> Z
- H (shift by E) -> L
- O (shift by A) -> O
- W (shift by R) -> N
- A (shift by E) -> E
- R (shift by A) -> R
- E (shift by R) -> V
- Y (shift by E) -> C
- O (shift by A) -> O
- U (shift by R) -> L
Ciphertext: HZLONERVCOL

Decryption Steps:
- H (shift by A) -> H
- Z (shift by R) -> I
- L (shift by E) -> H
- O (shift by A) -> O
- N (shift by R) -> W
- E (shift by E) -> A
- R (shift by A) -> R
- V (shift by R) -> E
- C (shift by E) -> Y
- O (shift by A) -> O
- L (shift by R) -> U
Plaintext: HIHOWAREYOU
## Summary

- Encryption is a method of protecting the confidentiality of a message by converting it into an unreadable format.
- The Caesar Cipher is a simple substitution cipher that shifts each letter by a fixed value.
- The Vigenère Cipher is a more complex substitution cipher that uses a keyword to shift letters by different amounts.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"9 Encryption Lab Maths.md"` in the `"Practical Solutions"` directory.
