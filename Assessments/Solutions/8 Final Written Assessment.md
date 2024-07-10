
# FINAL ASSESSMENT. FINALLY!

1. Cybersecurity Case Study:

    # Hackers Leak Personal Information of 30,000 FBI and DHS Employees! #

        Some hackers finally saw that the american government is supporting isreal with all of its power. To "end" the palestinien country. As they say that they are "terrorest", while isreal is the real terrorest. In February 2016, hackers Leak Personal Information of 30,000 FBI and DHS Employees. 

        The released information comprised largely of names, titles, phone numbers and e-mail addresses. Such stolen information were mined, according to the hackers, by accessing a Department of Justice Database. The amount of the employees were more than the half of the FBI department.

        The hackers, through @DotGovs, said, “FBI and DHS info is dropped and that’s all we came to do, so now its time to go, bye folks! #FreePalestine.” Prior to this recent dump, on Sunday, the group declared matter-of-factly in a tweet, “Well folks, it looks like @TheJusticeDept has finally realized their computer has been breached after 1 week.”
  
        The hackers really expose the FBi and DHS weak defend power. And really showed to the world that they are really nothing but just an organism threatning us by their power.

2). Practical Python:

        def count_words(file_name):
        word_count = {}
    
        # Open the file in read mode
        with open(file_name, 'k') as file:
            # Read each line from the file
            for line in file:
                # Split the line into words
                words = line.split()
                for word in words:
                    # Remove any punctuation marks (We will only count words)
                    word = word.strip('.,!?;:"()[]{}')
                    # Convert the word to lowercase to ignore case sensitivity
                    word = word.lower()
                    # Count the occurrence of the word
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    
        return word_count

        def main():
            filename = 'sample.txt'  # Replace with the name of your text file
            word_count = count_words(filename)
    
            # Print the word count
            for word, count in word_count.items():
                print(f'{word}: {count}')

        if __name__ == '__main__':
            main()

3. Computer Components and Logic Gates:

        RAM provides the shorter-term memory the CPU needs to open files and move data around as it responds to the tasks given to it by your apps. Both RAM and the CPU work synchronously and complementarily to ensure that your computer's performance fits your needs and you have a good experience when using your device.

4). Database Systems:
        import sqlite3                                  # sqlite3 provides a SQL-like interface to read, query, and write SQL databases from Python.

        conn = sqlite3.connect('example.db')  # It made a file under this file named "example.db".
        cursor = conn.cursor()

        # Create a table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (     
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL
        )    
        ''')        # If the table was not in there, or simply not existed, the user should make it.   The code will make a table that we will insert data soon.

        # Insert data into the table
        cursor.execute('''
        INSERT INTO Products (name, price) VALUES (?, ?)        
        ''', ('Product1', 10.99))                         # The user will insert here hte values, whcih is the name, and price.

        cursor.execute('''
        INSERT INTO Products (name, price) VALUES (?, ?)  
        ''', ('Product2', 20.99))                          # Same here, the user shoul imsert the values.

        # Select data from the table
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()                                # Here, the code is trying to select a data from the table that was made.
        for row in rows:                                         # It will print the row number.
            print(row)

        # Update data in the table
        cursor.execute('''
        UPDATE Products SET price = ? WHERE name = ?                
        ''', (15.99, 'Product1'))                                   # The code will update the table here, if thr user wamted tp.

        # Delete data from the table
        cursor.execute('''
        DELETE FROM Products WHERE name = ?
        ''', ('Product2',))                                          # If the user wanted to delete a data from the table.

        conn.commit()
        conn.close()                                                   # Closes the code.

5. Network Security Concepts:

        A VPN (virtual private network) connection establishes a secure connection between you and the internet. Via the VPN, all your data traffic is routed through an encrypted virtual tunnel. This disguises your IP address when you use the internet, making its location invisible to everyone. A VPN connection is also secure against external attacks.

6. Cryptographic Techniques:
        
        In public key cryptography, there would instead be two keys. The public key would encrypt the data, and the private key would decrypt it.

        Public key cryptography, also known as asymmetric cryptography, is a cryptographic system that uses pairs of keys: a public key and a private key. These keys are mathematically related but are distinct from each other. The key pair is generated such that the public key can be shared freely with anyone, while the private key remains secret and known only to its owner.

        Encryption Process:

        Encryption: When Alice wants to send an encrypted email to Bob, she obtains Bob's public key.
        Message Encryption: Alice uses Bob's public key to encrypt the email message. Only Bob can decrypt this message using his corresponding private key.
        Decryption Process:

        Decryption: When Bob receives the encrypted email, he uses his private key (which he keeps secret) to decrypt the message and read it.
        Authentication: Public key cryptography also allows for authentication. If Alice encrypts a message with her private key, anyone with her public key can decrypt it, confirming that the message came from her (since only she has the private key).

        In summary, public key cryptography provides a powerful tool for secure communication by enabling encryption without requiring the secure exchange of a shared key beforehand. It addresses some of the key challenges of symmetric key cryptography, particularly key distribution and scalability in multi-party communication scenarios.

