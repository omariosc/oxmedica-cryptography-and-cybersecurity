# 4 Database Systems Assessment Brief

## Overview

Welcome to your fourth assessment! This exercise is designed to introduce you to database systems, including SQL schema design and Entity-Relationship (ER) modelling. You will be given a list of requirements to design an SQL schema and create an ER model. Additionally, you will answer a question involving an SQL query. This assessment should take about 30 minutes to complete.

This is an open-book assessment, so feel free to refer to any resources you find helpful. It is worth 10% of your final grade.

## Part 1: SQL Schema Design and ER Modelling

### SQL Schema Design Instructions

1. **Requirements:**
   - Design a database for a library system with the following requirements:
     - Each book has a unique ID, title, author, and publication year.
     - Each member has a unique ID, name, and date of membership.
     - Members can borrow multiple books, but a book can only be borrowed by one member at a time.
     - Track the borrowing history with dates of borrow and return.

2. **SQL Schema:**
   - Write an SQL schema to create the necessary tables based on the requirements.
   - Include primary keys, foreign keys, and relevant data types.

3. **ER Model:**
   - Draw an ER diagram representing the entities, attributes, and relationships.

<!-- ### Example

**SQL Schema:**

```sql
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    publication_year INT
);

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(255),
    date_of_membership DATE
);

CREATE TABLE BorrowingHistory (
    borrow_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);
```

**ER Model:**

- **Entities:** Books, Members, BorrowingHistory
- **Attributes:**
  - **Books:** book_id, title, author, publication_year
  - **Members:** member_id, name, date_of_membership
  - **BorrowingHistory:** borrow_id, book_id, member_id, borrow_date, return_date
- **Relationships:**
  - One-to-Many between Members and BorrowingHistory
  - One-to-Many between Books and BorrowingHistory -->

## Part 2: SQL Query

### SQL Query Instructions

Write an SQL query to find all books borrowed by a member with the name "John Doe."

<!-- ### Example SQL Query

```sql
SELECT Books.title, Books.author, BorrowingHistory.borrow_date, BorrowingHistory.return_date
FROM Books
JOIN BorrowingHistory ON Books.book_id = BorrowingHistory.book_id
JOIN Members ON BorrowingHistory.member_id = Members.member_id
WHERE Members.name = 'John Doe';
``` -->

## Submission

- Write your SQL schema, ER model description, and SQL query in a digital document.
- Use [draw.io](https://draw.io) or any other diagram tool to create the ER diagram.
- Include your name at the top of the document.
- Save the file with the name `"4 Databases Assessment.md"` in the `"Solutions"` folder.
- You are allowed to use `".docx"`, `".pdf"`, or any other text format.

Have fun, and enjoy exploring the world of database systems and SQL queries!
