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
hashing: its by far the strongest and most unbreakable however its a one way tranaction ie there is no way to go back to the original text 
**Benefits of Symmetric Encryption:**
1. **Security:** Provides strong encryption when implemented correctly, ensuring data confidentiality.
2. **Speed:** Fast encryption and decryption processes due to the simplicity of using a single key.
3. **Efficiency:** Requires less computational resources compared to asymmetric encryption.
4. **Simplicity:** Easy to implement and manage because it involves only one key for both encryption and decryption.
5. **Compatibility:** Widely supported across various software and hardware platforms, making it versatile for different applications.

**Drawback of Symmetric Encryption:**
- **Key Management:** The main challenge is securely managing the encryption key, as any compromise can lead to unauthorized access to encrypted data.(source:device authority)
meanwhile aysmetric encryption reaps all the benifits whiel eleminationg drawbacks however it is more complex to manage 
### Part 2: Caesar Cipher (10 minutes)

1. **Introduction to Caesar Cipher:**
   - The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
   - Example: With a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

2. **Encryption Process:**
   - Choose a shift value (key).
   - For each letter in the plaintext, find its corresponding letter in the ciphertext by shifting it by the chosen value.
   -
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
plain text hi
encryption:
h->i
i->j
ciphertext : ij
4. **Decryption Process:**
   - To decrypt the message, shift each letter in the ciphertext back by the same value.
   - Example:
     - K -> H
     - H -> E
     - O -> L
     - O -> L
     - R -> O
   - Plaintext: HELLO
   ciphertext:ij
decryption 
i->h
j->i

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
PLAINTEXT:NIGERIA
KEY WORD :RIVER
ENCRYPTION STEPS
N SHIFT BY R = e
i shift by i = r
g shift by v = b
e shift by e = j
r ahift by r = i
i shift by r = z
a shift by i = j 
cipher text = erbjizj
4. **DecryptionA Process:**
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
cipher text =erbjizj
decryption
e SHIFT BY R = n
r shift by i = i
b shift by v = g
j shift by e = e
i ahift by r = r
z shift by r = i
j shift by i = a 
## Summary

- Encryption is a method of protecting the confidentiality of a message by converting it into an unreadable format.
- The Caesar Cipher is a simple substitution cipher that shifts each letter by a fixed value.
- The Vigenère Cipher is a more complex substitution cipher that uses a keyword to shift letters by different amounts.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"9 Encryption Lab Maths.md"` in the `"Practical Solutions"` directory.
