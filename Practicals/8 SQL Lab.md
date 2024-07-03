# Practical 8: SQL Lab

## Overview

This practical exercise is designed to introduce you to relational data in SQL, learn how to exploit vulnerabilities, perform SQL injections, and supplement this with exercises in SQL and Python. This session will take about 1 hour to complete.

## Task

### Part 1: Relational Data in SQL (20 minutes)

1. **Introduction to SQL:**
   - Discuss the basics of SQL and relational databases.
   - Explain tables, rows, columns, and relationships between tables.

2. **SQL Queries:**
   - Write basic SQL queries to select, insert, update, and delete data. Here is an example for a users table, change it and make it for a different table (e.g. below uses the `Users` table).

<!-- - Example Queries:
    SELECT * FROM Users;
    INSERT INTO Users (username, password) VALUES ('user1', 'password1');
    UPDATE Users SET password = 'newpassword' WHERE username = 'user1';
    DELETE FROM Users WHERE username = 'user1';
    -->

### Part 2: SQL Vulnerabilities and Exploitation (20 minutes)

1. **Understanding SQL Injection:**
   - Explain what SQL injection is and how it can be exploited.
   - Provide examples of vulnerable SQL code and how an attacker can exploit it.

2. **Demonstration:**
   - Show a demonstration of a simple SQL injection attack. Try to make it work for your example from Part 1.

<!-- - Example:
    SELECT * FROM Users WHERE username = 'admin' -- ' AND password = 'password';
    -->

3. **Preventing SQL Injection:**
   - Discuss methods to prevent SQL injection, such as using prepared statements and parameterized queries. Copy the code in markdown, you do not need to run this, just see how it runs te code.

<!-- - Example:
    import sqlite3

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    -->

### Part 3: SQL and Python Exercises (20 minutes)

1. **SQL Exercise:**
  - See how the following SQL is converted into Python code. Run the following code and explain the output, describing the steps taken and final table. Use comments or markdown cells.
     ```sql
     -- Create a table
     CREATE TABLE Products (
         id INTEGER PRIMARY KEY,
         name TEXT,
         price REAL
     );

     -- Insert data into the table
     INSERT INTO Products (name, price) VALUES ('Product1', 10.99);
     INSERT INTO Products (name, price) VALUES ('Product2', 20.99);

     -- Select data from the table
     SELECT * FROM Products;

     -- Update data in the table
     UPDATE Products SET price = 15.99 WHERE name = 'Product1';

     -- Delete data from the table
     DELETE FROM Products WHERE name = 'Product2';
     ```
   
     ```python
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
     ```

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"8 SQL Lab.ipynb"` in the `"Practical Solutions"` directory.

Have fun, and enjoy learning about SQL and its integration with Python!
