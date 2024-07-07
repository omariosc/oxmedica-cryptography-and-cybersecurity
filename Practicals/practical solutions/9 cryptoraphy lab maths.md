part 1
1:Encryption is the process of encoding information in such a way that only authorized parties can access it. It transforms plaintext (readable data) into ciphertext (encoded data) using an algorithm and a key. 

2: -Plaintext: This is the original, readable message or data that you want to protect.
  -Ciphertext: This is the encrypted, unreadable form of the plaintext produced by applying an encryption algorithm and a key.
  -Encryption Algorithm: A mathematical procedure used to convert plaintext into ciphertext. 
  -Encryption Key: A parameter used by the encryption algorithm to transform plaintext into ciphertext,
  -Decryption: The process of converting ciphertext back into plaintext
  -Applications: Encryption is used in various applications such as securing communications (e.g., HTTPS, SSL/TLS)
  -Security: Encryption ensures data confidentiality, integrity, and authenticity

3: -Symmetric-key algorithms: Also known as secret-key algorithms, these use a single key for both encryption and decryption. Both sender and receiver must share this key securely beforehand.
-advantage:
-Efficiency:Symmetric-key algorithms are typically faster and require less computational resources compared to asymmetric-key algorithms.
-Scalability: Symmetric-key algorithms scale well with increasing data volume because their computational cost remains relatively constant regardless of the amount of data being encrypted or decrypted.
-Simplicity: They are conceptually simpler to understand and implement compared to asymmetric-key algorithms
-Security: When used with sufficiently long keys (e.g., 128 bits or more), symmetric-key algorithms can provide strong security against brute-force attacks.
-Suitability for Symmetric Operations: Symmetric encryption is well-suited for operations where the same party both encrypts and decrypts data

-disadvantages:
-Key Storage: Symmetric encryption requires storing and protecting the encryption keys. If an attacker gains access to the key, they can decrypt all messages encrypted with that key
-Key Exchange: Establishing a shared key securely between two parties can be difficult, especially in scenarios where the parties have not previously communicated or shared a key
-Lack of Authentication: Symmetric-key algorithms by themselves do not provide mechanisms for authentication or non-repudiation. That means there is no inherent way to verify the identity of the sender or ensure that the message has not been tampered with after encryption

-Asymmetric-key algorithms: Also known as public-key algorithms, these use a pair of keys: a public key for encryption and a private key for decryption.
-advantage:
-Key Distribution: One of the most significant advantages of asymmetric-key cryptography is that it eliminates the need for secure key distribution channels required by symmetric-key algorithms. Each user has a pair of keys: a public key for encryption and a private key for decryption
-Authentication and Non-Repudiation: Asymmetric-key cryptography provides mechanisms for authentication and non-repudiation. A message encrypted with a sender's private key and decrypted with their public key verifies the sender's identity, ensuring the message's authenticity. 
-Flexibility and Versatility: Asymmetric-key cryptography supports a wide range of cryptographic operations beyond encryption and decryption, including digital signatures, key exchange protocols (like Diffie-Hellman), and key establishment schemes.

-disadvantage:
-Key Size: Asymmetric-key algorithms typically require larger key sizes compared to symmetric-key algorithms to achieve equivalent security levels, and couldlead to over heat.
-Safeguarding private keys is crucial, as compromising a private key can compromise the security of all communications encrypted with its corresponding public key.
-Performance Trade-offs: While asymmetric encryption is essential for key exchange and digital signatures, the performance trade-offs compared to symmetric encryption must be carefully considered in practical applications. Balancing security requirements with performance constraints is often a challenge in designing cryptographic systems.

-Hash functions take an input (message) and produce a fixed-size output (hash value or digest). They are used to verify data integrity and securely store passwords. 

advantage:
-Data Integrity: Hash functions are commonly used to ensure data integrity. By generating a fixed-size hash value (digest) from arbitrary input data, any change to the input data—even a minor alteration—will result in a completely different hash value. This property allows systems to verify that data has not been tampered with or corrupted.
-Fixed Length Output: Hash functions produce output of a fixed size, regardless of the input size. This makes them suitable for use in data structures and databases where fixed-size keys are required.
-Non-repudiation: Hash functions are integral to ensuring non-repudiation in digital signatures. By generating a hash of the message and then encrypting the hash with the sender's private key, anyone with the corresponding public key can verify the signature. This prevents the sender from denying their involvement or the authenticity of the message.

disadvantage:
-Hash Collisions: Although cryptographic hash functions aim to minimize collisions (where different inputs produce the same hash output), collisions are theoretically possible due to the finite size of the hash output. For non-cryptographic hash functions, collision resistance might not be guaranteed.
-Dependence on Algorithm Strength: The security of hash functions relies heavily on the strength and design of the algorithm used. If a hash function is found to have vulnerabilities or weaknesses (e.g., due to advances in cryptanalysis), previously encrypted data might become compromised.
