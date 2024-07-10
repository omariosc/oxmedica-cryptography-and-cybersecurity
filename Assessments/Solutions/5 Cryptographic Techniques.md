# 5 Cryptographic Techniques Assesswment

Name: _NSR SDS_

## Chosen Technique:
Vigenère Cipher

## Original Message:
"Meet me at noon"

## Encryption Key:
"KEY"

## Encrypted Message:
"Wicd qc kx lysl" 

### Steps Taken for Encryption:
Take the first letter of the message and the first letter of the key, add their value (letters have a value depending on their rank in the alphabet, starting with 0). The result of the addition gives the rank of the ciphered letter.

## Decrypted Message:
"Meet me at noon"

### Steps Taken for Decryption:
To decrypt, take the first letter of the ciphertext and the first letter of the key, and subtract their value (letters have a value equal to their position in the alphabet starting from 0). If the result is negative, add 26 (26=the number of letters in the alphabet), the result gives the rank of the plain letter.
   
> The Vigenère Cipher is stronger than the Caesar Cipher due to its use of a keyword for encryption. Encryption and decryption were moderately easy once the key was known, but without the key, decryption would be challenging. This technique could be applied in scenarios where moderate security is required, such as historical military communications. More advanced techniques like AES would significantly improve security by employing larger keys and complex mathematical operations.

