# 8 Final Written Assessment Brief

## Overview

Welcome to your eighth and final assessment! This assessment will cover all the major topics we have discussed previously, excluding hacking and cyber-attacks, which were addressed in the seventh assessment. The decision to move this written assessment to week 2 was due to the potential lack of time for marking.

This is an semi-open-book assessment, meaning you can refer to your notes and resources but not to the internet or other students. You will have 1 hour to complete this assessment. It is worth 20% of your final grade.

## Instructions

Answer the following questions to the best of your ability. Each question is designed to assess your understanding of key concepts related to cybersecurity, computer systems, and networking. Write your responses clearly and concisely, providing examples or explanations where appropriate.

1. **Cybersecurity Case Study:**
   - Explain the impact of a recent high-profile data breach on the affected company and its customers. What steps can organizations take to respond effectively to a data breach?
    recently a high profile data breach costing 10 billion passwords being leaked online, makeing it  the highest data haul ever, the customers had their accounts stolen and lost many vaulubale things

2. **Practical Python:**
   - Write a Python script that reads a text file and counts the number of occurrences of each word. Describe how your script processes the file and counts the words.
f
rom collections import defaultdict
import string

def count_words(file_path):
    word_count = defaultdict(int)
    
    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            # Split the line into words
            words = line.split()
            # Count each word
            for word in words:
                word_count[word] += 1
    
    # Print the word counts
    for word, count in word_count.items():
        print(f'{word}: {count}')

file_path = 'cool202'  # Replace with your file path
count_words(file_path)



3. **Computer Components and Logic Gates:**
   - Explain the role of RAM in a computer system. What are its inputs and outputs, and how does it interact with the CPU and storage devices?

RAM is temporary high-speed storage that enables programs open on a computer to run fast. It stores data for the processor to access instantly, and once you close the programs, the data moves from RAM to slower storage.

4. **Database Systems:** -- cant find an
   - Design an SQL schema for an online store with the following requirements:
     - Products have a unique ID, name, description, and price.
     - Customers have a unique ID, name, email, and address.
     - Orders have a unique ID, customer ID, order date, and total amount.
     - Each order can contain multiple products. Include primary keys, foreign keys, and relevant data types.

      # Connect to SQLite database
     import sqlite3

     conn = sqlite3.connect('example.db')
     cursor = conn.cursor()

     # Create a table
     cursor.execute('''
     CREATE TABLE IF NOT EXISTS Products (
         id INTEGER PRIMARY KEY,
         name TEXT,
         price REAL
     )
     ''')

     # Insert data into the table
     cursor.execute('''
     INSERT INTO Products (name, price) VALUES (?, ?)
     ''', ('Product1', 10.99))

     cursor.execute('''
     INSERT INTO Products (name, price) VALUES (?, ?)
     ''', ('Product2', 20.99))

     # Select data from the table
     cursor.execute('SELECT * FROM Products')
     rows = cursor.fetchall()
     for row in rows:
         print(row)

     # Update data in the table
     cursor.execute('''
     UPDATE Products SET price = ? WHERE name = ?
     ''', (15.99, 'Product1'))

     # Delete data from the table
     cursor.execute('''
     DELETE FROM Products WHERE name = ?
     ''', ('Product2',))

     conn.commit()
     conn.close()

     SELECT * FROM Users;
    INSERT INTO Users (username, password) VALUES ('XSPLYTS', 'COOL101');
    UPDATE Users SET password = '123' WHERE username = 'XSPLYTS';
    DELETE FROM Users WHERE username = 'XSPLYTS';

5. **Network Security Concepts:**
   - Describe the concept of a VPN (Virtual Private Network). How does it work, and what are its advantages and disadvantages in terms of network security?

   A VPN (Virtual Private Network) is a service that encrypts your internet connection and routes it through a server in another location. This process masks your IP address, making it appear as if you’re accessing the internet from the location of the server rather than your actual location.

Advantages:

Privacy: Hides your browsing activity from local networks and ISPs.
Security: Encrypts data to protect against eavesdropping and cyber threats.
Access: Allows you to bypass geo-restrictions and censorsh:D

Disadvantages:

Speed: Can slow down your internet connection due to encryption overhead.
Trust: Requires trust in the VPN provider not to log or misuse your data.
Complexity: May be complex to set up for inexperienced users.
VPNs are widely used for enhancing privacy and security online, especially on unsecured Wi-Fi networks D:

6. **Cryptographic Techniques:**
   - Explain the concept of public key cryptography. Describe how it differs from symmetric key cryptography and provide an example of how it can be used to secure communication.

the user seeks a concise explanation of public key cryptography, its distinction from symmetric key cryptography, and examples of its application in secure communication
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

```bat
```sql
-- SQL code goes here
```

Good luck, and take this opportunity to demonstrate your understanding of the key concepts we have covered in this course!

