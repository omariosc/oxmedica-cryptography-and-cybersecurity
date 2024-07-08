# 5 Cryptographic Techniques Assessment Brief
Feras Alzahrani
Abdulaziz Almatrafi
## Overview

Welcome to your fifth assessment! This exercise is designed to introduce you to the fundamental concepts of cryptographic techniques through a practical activity. You will work in pairs to research, encrypt, and decrypt a message. This assessment should take about one hour to complete.

This is an open-book assessment, so feel free to refer to any resources you find helpful. It is worth 15% of your final grade.

## Instructions

### Part 1: Research (15 minutes)

1. **Form Pairs:**
   - Choose a partner to work with for this activity.

2. **Research:**
   - Spend time researching various cryptographic techniques such as Caesar Cipher, Substitution Cipher, Transposition Cipher, and Vigenère Cipher. The one you choose should be more complex than the Caesar Cipher.
   - Discuss with your partner and choose one cryptographic technique to use for this activity.
   - Take notes on how your chosen technique works, including examples.

### Part 2: Encrypt a Message (15 minutes)

1. **Select a Message:**
   - Decide on a short message (one or two sentences) to encrypt.

2. **Encrypt:**
   - Use the chosen cryptographic technique to encrypt the message.
   - Write down the encrypted message clearly.
   - Document the steps you took to encrypt the message, including any keys or shifts used.

### Part 3: Decrypt a Message (15 minutes)

1. **Exchange Messages:**
   - Exchange your encrypted message with another pair.

2. **Decrypt:**
   - Using the same cryptographic technique, decrypt the message you received from the other pair.
   - Write down the decrypted message clearly.
   - Document the steps you took to decrypt the message.

### Part 4: Analysis and Discussion (15 minutes)

1. **Analyze:**
   - Compare the decrypted message with the original message.
   - Discuss with your partner if there were any discrepancies and why they might have occurred.
   - Reflect on the effectiveness of the cryptographic technique you used.

2. **Discussion Questions:**
   - What are the strengths and weaknesses of the cryptographic technique you used?
   - How easy or difficult was it to encrypt and decrypt the messages?
   - In what real-world scenarios could this cryptographic technique be applied?
   - How might more advanced cryptographic techniques improve security?

## Example

**Chosen Technique:** Caesar Cipher

**Original Message:** "Hello World"
**Encryption Key:** 3

**Encrypted Message:** "Khoor Zruog"

**Decrypted Message:** "Hello World"

**Steps Taken:**

- Encryption: Shift each letter by 3 positions forward in the alphabet.
- Decryption: Shift each letter by 3 positions backward in the alphabet.

## Answers:
Part 2:
Plaintext: MEET ME AT THE PARK AT NOON
Chosen Technique: Vigenère Cipher
Key: SECRET
Encryption = Plaintext letter + Key letter mod 26
Encryption steps:
- M(13) + S(18) = 13 + 18 = 31(mod 26) = 5 (F)
- E(4) + E(4) = 4 + 4 = 8(I)
- E(4) + C(2) = 4 + 2 = 6(G)
- T(19) + R(17) = 19 + 17 = 36(mod 26) = 10(K)
- M(12) + E(4) = 12 + 4 = 16(mod 26) = 5(F)
- E(4) + S(18) = 4 + 18 = 22(W)
- A(0) + E(4) = 0 + 4 = 4(E)
- T(19) + C(2) = 19 + 2 = 21(V)
- T (19) + R (17) = 19 + 17 = 36 (mod 26) = 10 (K)
- H(7) + E(4) = 7 + 4 = 11(L)
- E(4) + T(19) = 4 + 19 = 23(W)
- P(15) + S(18) = 15 + 18 = 33 (mod 26) = 7(H)
- A (0) + E (4) = 0 + 4 = 4(E)
- R (17) + C (2) = 17 + 2 = 19(T)
- K (10) + R (17) = 10 + 17 = 27 (mod 26) = 1(B)
- A(0) + E(4) = 0 + 4 = 4(E)
- T(19) + T(19) = 19 + 19 = 38(mod 26) = 12(M)
- N(13) + S(18) = 13 + 18 = 31(mod 26) = 5(F)
- O(14) + E(4) = 14 + 4 = 18(S)
- O(14) + C(2) = 14 + 2 = 16(Q)
- N(13) + R(17) = 13 + 17 = 30(mod 26) = 4(R)
Ciphertext: FIGK FW EV KLW HETB EM FSQR

## Submission

- Write your encrypted and decrypted messages in a digital document.
- Include the names of both partners at the top of the document.
- Document the steps taken for encryption and decryption, as well as your analysis and discussion points.
- Save the file with the name `"5 Cryptographic Techniques Assessment.md"`.

Enjoy learning and exploring the exciting world of cryptography!
