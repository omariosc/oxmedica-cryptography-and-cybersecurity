# 8 Final Written Assessment Brief

## Overview

Welcome to your eighth and final assessment! This assessment will cover all the major topics we have discussed previously, excluding hacking and cyber-attacks, which were addressed in the seventh assessment. The decision to move this written assessment to week 2 was due to the potential lack of time for marking.

This is an semi-open-book assessment, meaning you can refer to your notes and resources but not to the internet or other students. You will have 1 hour to complete this assessment. It is worth 20% of your final grade.

## Instructions

Answer the following questions to the best of your ability. Each question is designed to assess your understanding of key concepts related to cybersecurity, computer systems, and networking. Write your responses clearly and concisely, providing examples or explanations where appropriate.

1. **Cybersecurity Case Study:**
   - Explain the impact of a recent high-profile data breach on the affected company and its customers. What steps can organizations take to respond effectively to a data breach?
   # TicketMaster Data Breach - May 2024 : Over half a billion of its customers had their infos leaked on the dark-web the datas included(full names, addresses, phone numbers, emails, and order historys) TicketMasters parent company (Live Nation): confirmed the breach in a filing to the US Securities and Exchange Commission and stated: “We are working to mitigate risk to our users and the company, and have notified and are cooperating with law enforcement.”

2. **Practical Python:**
   - Write a Python script that reads a text file and counts the number of occurrences of each word. Describe how your script processes the file and counts the words.

3. **Computer Components and Logic Gates:**
   - Explain the role of RAM in a computer system. What are its inputs and outputs, and how does it interact with the CPU and storage devices?
   # RAM is the (random access memory) this hardware is the principle of the temp storage for the opreating system (apps, etc..) and its keeps the apps open to provide quick opening for the processor.

4. **Database Systems:**
   - Design an SQL schema for an online store with the following requirements:
     - Products have a unique ID, name, description, and price.
     - Customers have a unique ID, name, email, and address.
     - Orders have a unique ID, customer ID, order date, and total amount.
     - Each order can contain multiple products. Include primary keys, foreign keys, and relevant data types.

5. **Network Security Concepts:**
   - Describe the concept of a VPN (Virtual Private Network). How does it work, and what are its advantages and disadvantages in terms of network security?
   # its a software thats make a non-real network to make you look that you connected to it to safe your real network, vpn works in-between the device and the and the targeted server, instead of relying on the browers to encrypt your data, it encrypt it instead with its own encrypts and routes, but its also has disadvantages that (you dont know where your infos is going, also if the vpn company got data breaches your infos will fo public, also the untrusted vpn companys can and will use your datas)

6. **Cryptographic Techniques:**
   - Explain the concept of public key cryptography. Describe how it differs from symmetric key cryptography and provide an example of how it can be used to secure communication.
   # Public key cryptography enables secure communication without requiring a shared secret by using key pairs—public and private—for encryption and decryption. It enables secure and scalable communication over unreliable channels, unlike symmetric cryptography, by encrypting messages using the recipient's public key and decrypting them using their private key.
### Submission

- Write your answers in a digital document.
- Include your name at the top of the document.
- Save the file with the name `"8 Final Written Assessment.md"` in the `"Solutions"` folder.
- Write your answer for the Python script question using a code block in the document e.g., triple backticks for Python code (```).
- Write your answer for SQL schema design using a code block in the document e.g., triple backticks for SQL code (```).

```bat
```python
import string

def count_words(file_path):
    word_count = {}
    
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the entire file
        text = file.read()
        
        # Remove punctuation from the text (replace with whitespace)
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = text.translate(translator)
        
        # Split the text into words by whitespace and convert to lowercase
        words = text.lower().split()
        
        # Count occurrences of each word
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count

def main():
    file_path = 'sample.txt'  # Replace with your file path
    word_count = count_words(file_path)
    
    # Print the word counts
    for word, count in word_count.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()

```

```bat
```sql
-- SQL code goes here
```

Good luck, and take this opportunity to demonstrate your understanding of the key concepts we have covered in this course!

#### RESOURCES:
https://www.electric.ai/blog/recent-big-company-data-breaches
