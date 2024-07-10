# 8 Final Written Assessment Brief
Feras Alzahrani
## Overview

Welcome to your eighth and final assessment! This assessment will cover all the major topics we have discussed previously, excluding hacking and cyber-attacks, which were addressed in the seventh assessment. The decision to move this written assessment to week 2 was due to the potential lack of time for marking.

This is an semi-open-book assessment, meaning you can refer to your notes and resources but not to the internet or other students. You will have 1 hour to complete this assessment. It is worth 20% of your final grade.

## Instructions

Answer the following questions to the best of your ability. Each question is designed to assess your understanding of key concepts related to cybersecurity, computer systems, and networking. Write your responses clearly and concisely, providing examples or explanations where appropriate.

1. **Cybersecurity Case Study:**
   - Explain the impact of a recent high-profile data breach on the affected company and its customers. What steps can organizations take to respond effectively to a data breach?

There many consequences to a high-profile data breach one of them is the leaking of the company's and customer's private information, the loss of trust from customers, and the destruction of the company's reputation. They first have to find where the breach happened and check up for what was stolen and then use the neccessary measure to stop the breach


2. **Practical Python:**
   - Write a Python script that reads a text file and counts the number of occurrences of each word. Describe how your script processes the file and counts the words.





3. **Computer Components and Logic Gates:**
   - Explain the role of RAM in a computer system. What are its inputs and outputs, and how does it interact with the CPU and storage devices?

RAM or Random access memory is a memory that temporarily stores data and program instructions that the CPU needs for fast access.
Inputs: Data signals(carry data to be written), Control signals(manage read/write operations)
Outputs Data signals(provide data during read operations)

Interactions with CPU: Fetching data/instruction, temporary storage, and program execution.
Interactions with Storage devices: moving(data is moved to storage when RAM is full), loading programs
4. **Database Systems:**
   - Design an SQL schema for an online store with the following requirements:
     - Products have a unique ID, name, description, and price.
     - Customers have a unique ID, name, email, and address.
     - Orders have a unique ID, customer ID, order date, and total amount.
     - Each order can contain multiple products. Include primary keys, foreign keys, and relevant data types.

5. **Network Security Concepts:**
   - Describe the concept of a VPN (Virtual Private Network). How does it work, and what are its advantages and disadvantages in terms of network security?

A VPN securely connects users to a private network over the internet, encrypting data for privacy and enabling secure remote access.

Advantages: Enhances security, protects privacy, and allows remote access to private resources.
Disadvantages: Can impact performance, complexity in setup, and dependency on VPN providers.
6. **Cryptographic Techniques:**
   - Explain the concept of public key cryptography. Describe how it differs from symmetric key cryptography and provide an example of how it can be used to secure communication.


Public key cryptography uses pairs of keys: a public key for encryption and a private key for decryption. It differs from symmetric key cryptography by using separate keys for encryption and decryption, enhancing security and enabling secure communication over insecure channels.

Difference from Symmetric Key Cryptography: Symmetric key cryptography uses the same key for both encryption and decryption, while public key cryptography uses a pair of keys: a public key for encryption and a private key for decryption.

Example: Alice encrypts a message using Bob's public key. Only Bob, with his private key, can decrypt the message, ensuring confidentiality even if the encrypted message is intercepted.

Public key cryptography also supports digital signatures, where the sender uses their private key to sign a message, and recipients verify the signature using the sender's public key, ensuring message authenticity and integrity.


### Submission

- Write your answers in a digital document.
- Include your name at the top of the document.
- Save the file with the name `"8 Final Written Assessment.md"` in the `"Solutions"` folder.
- Write your answer for the Python script question using a code block in the document e.g., triple backticks for Python code (```).
- Write your answer for SQL schema design using a code block in the document e.g., triple backticks for SQL code (```).

```bat
```python
# Python code goes here
```
from collections import Counter
import re

def count_words(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Use regular expression to find words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    return word_counts

# Specify the path to your text file
file_path = 'your_text_file.txt'

# Get the word counts
word_counts = count_words(file_path)

# Print the word counts
for word, count in word_counts.items():
    print(f'{word}: {count}')
```

```bat
```sql
-- SQL code goes here

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    ProductDescription TEXT NOT NULL,
    ProductPrice DECIMAL(10,2) NOT NULL
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerEmail VARCHAR(100) UNIQUE NOT NULL,
    CustomerAddress TEXT NOT NULL
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderDetails (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
```

Good luck, and take this opportunity to demonstrate your understanding of the key concepts we have covered in this course!
