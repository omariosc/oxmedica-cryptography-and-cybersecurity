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

   ANSWER:
   Symmetric Encryption Algorithms:

   IDEA (International Data Encryption Algorithm):

IDEA is a symmetric encryption algorithm used in some older systems.
It uses a 128-bit key and operates on 64-bit blocks

   Blowfish:

Blowfish is a symmetric encryption algorithm designed for fast performance.
It supports key sizes from 32 bits to 448 bits

Asymmetric Encryption Algorithms:

DSA (Digital Signature Algorithm):

DSA is a digital signature algorithm used for generating and verifying digital signatures.
It is based on the difficulty of computing discrete logarithms.

ECC (Elliptic Curve Cryptography):

ECC is an asymmetric encryption technique based on elliptic curves.
It offers strong security with shorter key lengths compared to RSA.

Hashing Algorithms:

SHA-256 (Secure Hash Algorithm 256-bit):

SHA-256 is part of the SHA-2 family and is widely used for secure hashing.
It produces a 256-bit hash value.

SHA-3 (Secure Hash Algorithm 3):

SHA-3 is the latest member of the Secure Hash Algorithm family.
It was designed as an alternative to SHA-2 and offers improved security features.

   - Discuss the advantages and disadvantages of each type of encryption algorithm.

   Symmetric Encryption: Fast, efficient, but requires secure key distribution.

Asymmetric Encryption: Solves key distribution issues, provides authentication, but is computationally expensive.

Hashing Algorithms: Ensure data integrity, efficient, but not reversible and susceptible to collisions.

### Part 2: Caesar Cipher (10 minutes)

Plain text; CYBER
Key; -1
Encrybtion steps;
C-->B
Y-->X
B-->A
E-->D
R-->Q
Cipher text; BXADQ

Decrybtion steps;
Decrybtion key; 1
B-->C
X-->Y
A-->B
D-->E
Q-->R
Plain text; CYBER

### Part 3: Vigenère Cipher (10 minutes)



Part 3 Q2:

Plain text; CODING
Keyword; CARCAR
Encrybtion steps;
C--(C)>F
O--(A)>P
D--(R)>V
I--(C)>L
N--(A)>O
G--(R)>Y
Cipher text; FPVLOY

Decrybtion steps;
F--(C)>C
P--(A)>O
V--(R)>D
L--(C)>I
O--(A)>N
Y--(R)>G
Plain text; CODING

## Summary

- Encryption is a method of protecting the confidentiality of a message by converting it into an unreadable format.
- The Caesar Cipher is a simple substitution cipher that shifts each letter by a fixed value.
- The Vigenère Cipher is a more complex substitution cipher that uses a keyword to shift letters by different amounts.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"9 Encryption Lab Maths.md"` in the `"Practical Solutions"` directory.
