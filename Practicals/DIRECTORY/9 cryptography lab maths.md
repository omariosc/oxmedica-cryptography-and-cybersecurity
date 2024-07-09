## Task
   ## Part 1 
3. 1. Symmetric Encryption

Definition: Symmetric encryption uses a single key to both encrypt and decrypt data. The same key is shared between the sender and the receiver.

Advantages:

Speed: Symmetric encryption is typically faster than asymmetric encryption because of its simpler algorithms.
Efficiency: It is more efficient for bulk data encryption, such as encrypting large files or streams of data.
Widely Supported: Symmetric encryption algorithms like AES (Advanced Encryption Standard) are widely adopted and standardized.

Disadvantages:

Key Distribution: Secure key distribution between sender and receiver can be challenging, especially over insecure channels.
Key Management: Managing and storing keys securely can be complex, especially in large systems or distributed environments.
No Authentication: Symmetric encryption alone does not provide mechanisms for authentication or non-repudiation.

2. Asymmetric Encryption (Public-Key Encryption)

Definition: Asymmetric encryption uses a pair of keys: a public key and a private key. The public key is used for encryption, while the private key is used for decryption.

Advantages:

Key Distribution: Only the public key needs to be distributed, which can be done openly. The private key remains secret.
Authentication and Non-Repudiation: Asymmetric encryption supports digital signatures, enabling authentication and non-repudiation.
Security: Asymmetric encryption is more secure for key exchange and avoids the key distribution problem of symmetric encryption.

Disadvantages:

Computational Complexity: Asymmetric encryption algorithms are more computationally intensive compared to symmetric encryption.
Speed: Due to the complexity, asymmetric encryption is slower than symmetric encryption, making it less suitable for bulk encryption.
Key Length: Typically, keys used in asymmetric encryption are longer than those in symmetric encryption, which can impact performance.

3. Hashing Algorithms
Definition: Hashing algorithms take an input (or 'message') and produce a fixed-size string of characters, which is typically a cryptographic hash. They are used primarily for ensuring data integrity.

Advantages:

Integrity: Hashing algorithms ensure that data has not been tampered with. A small change in the input will result in a drastically different hash value.
Fast: Hashing is generally fast and efficient.
One-Way Function: It is computationally infeasible to reverse a hash value to obtain the original input (pre-image resistance).

Disadvantages:

No Encryption: Hashing is not encryption; it's a one-way transformation. You cannot get the original data back from a hash value.
Hash Collisions: In theory, different inputs can produce the same hash value (collision), although good hashing algorithms minimize this risk.
No Secrecy: Hashes are meant for integrity, not secrecy. They do not protect the content of the data itself.
Conclusion
Each type of encryption algorithm—symmetric, asymmetric, and hashing—has its strengths and weaknesses, making them suitable for different use cases in cryptography. Understanding these differences helps in choosing the appropriate algorithm based on the specific security requirements of a given application or system.




