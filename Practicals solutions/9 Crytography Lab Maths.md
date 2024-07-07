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

## **Answer**
   
   1.Symmetric Encryption:
      Advantages:
         1.Speed:Symmetric encryption algorithms are generally faster because they use simpler mathematical operations.
         2.Efficiency: They require less computational power and resources.
      Disadvantages:
         1.Lack of Authentication:Symmetric encryption alone does not provide mechanisms for verifying the identity of the sender.
         2.Key Exchange: sending a shared key securely over an insecure channel without it being intercepted is a challenge.
   2.Asymmetric Encryption:
      1.Key Distribution: Public-key cryptography gets rid of the need for a secure channel to share the key because each user has a public and private key pair.
      2.Authentication: It allows for authentication and digital signatures, allowing the user to verify the sender's identity.
### Part 2: Caesar Cipher (10 minutes)

1. **Introduction to Caesar Cipher:**
   - The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
   - Example: With a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

2. **Encryption Process:**
   - Choose a shift value (key).
   - For each letter in the plaintext, find its corresponding letter in the ciphertext by shifting it by the chosen value.

## **Answer**

3. **Encryption Process:**
   - Plaintext: ATTACK
   - Key: 5
   - Encryption Steps:
     - A -> F
     - T -> Y
     - T -> Y
     - A -> F
     - C -> H
     - K -> P
   - Ciphertext: FYYFHP

4. **Decryption Process:**
   - To decrypt the message, shift each letter in the ciphertext back by the same value.
   - Example:
     - F -> A
     - Y -> T
     - Y -> T
     - F -> A
     - H -> C
     - P -> K
   - Plaintext: ATTACK

### Part 3: Vigenère Cipher (10 minutes)

1. **Introduction to Vigenère Cipher:**
   - The Vigenère Cipher is a more complex form of substitution cipher that uses a keyword to shift letters by different amounts.
   - Example: Using the keyword "KEY", the shifts would be based on the positions of 'K', 'E', and 'Y' in the alphabet.

2. **Encryption Process:**
   - Choose a keyword.
   - Repeat the keyword so it matches the length of the plaintext.
   - For each letter in the plaintext, shift it by the corresponding letter in the keyword.

3. **Example:**
   - Plaintext: ARTILLERYINBOUND
   - Keyword: HSUEKFGHQMALTRPE
   - Encryption Steps:
     - A (shift by H) -> H
     - R (shift by S) -> J
     - T (shift by U) -> N
     - I (shift by E) -> M
     - L (shift by K) -> V
     - L (shift by F) -> Q
     - E (shift by G) -> K
     - R (shift by H) -> Y
     - Y (shift by Q) -> O
     - I (shift by M) -> U
     - N (shift by A) -> N
     - B (shift by L) -> M
     - O (shift by T) -> H
     - U (shift by R) -> L
     - N (shift by P) -> D
     - D (shift by E) -> H
   - Ciphertext: HJNMVQKYOUNMHLDH

4. **Decryption Process:**
   - To decrypt the message, shift each letter in the ciphertext back by the corresponding letter in the keyword.
   - Example:
     - H (shift by K) -> A
     - J (shift by E) -> R
     - N (shift by Y) -> T
     - M (shift by K) -> I
     - V (shift by E) -> L
     - Q (shift by Y) -> L
     - K (shift by K) -> E
     - Y (shift by E) -> R
     - O (shift by Y) -> Y
     - U (shift by K) -> I
     - N (shift by E) -> N
     - M (shift by Y) -> B
     - H (shift by Y) -> O
     - L (shift by K) -> U
     - D (shift by E) -> N
     - H (shift by Y) -> D
   - Plaintext: ARTILLERYINBOUND

## Summary

- Encryption is a method of protecting the confidentiality of a message by converting it into an unreadable format.
- The Caesar Cipher is a simple substitution cipher that shifts each letter by a fixed value.
- The Vigenère Cipher is a more complex substitution cipher that uses a keyword to shift letters by different amounts.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"9 Encryption Lab Maths.md"` in the `"Practical Solutions"` directory.
