# Practical 7: Database Systems Workshop

## Overview

This practical exercise is designed to introduce you to database systems, including database architecture, relational algebra, ER modelling, normalisation, and database design. To supplement this workshop, we will use online modelling software. This session will take about 90 minutes to complete.

## Task

### Part 1: Database Architecture (15 minutes)

1. **Overview:**
   - Discuss the basic architecture of a database system.
   - Components to cover:
     - Database Engine
     - Query Processor
     - Storage Manager
     - Transaction Manager

### Part 2: Relational Algebra (15 minutes)

1. **Introduction:**
   - Explain the fundamental operations of relational algebra:
     - Selection (σ)
     - Projection (π)
     - Union (∪)
     - Set Difference (−)
     - Cartesian Product (×)
     - Rename (ρ)

2. **Examples:**
   - Provide examples of how these operations can be used to query a database.

### Part 3: ER Modelling (20 minutes)

1. **Introduction to ER Models:**
   - Explain the components of an Entity-Relationship (ER) model:
     - Entities
     - Attributes
     - Relationships

2. **Create an ER Model:**
   - Use online modelling software (e.g., draw.io, Lucidchart) to create an ER model for a sample database.

### Part 4: Normalisation (20 minutes)

1. **Introduction to Normalisation:**
   - Explain the purpose of normalisation in database design.
   - Discuss the normal forms (1NF, 2NF, 3NF, BCNF).

2. **Normalisation Process:**
   - Provide examples of how to normalise a database schema to eliminate redundancy and improve data integrity.

### Part 5: Database Design (20 minutes)

1. **Design a Database:**
   - Using the ER model created earlier, design a database schema.
   - Define tables, primary keys, and foreign keys based on the ER model.

2. **Implementation:**
   - Use an online SQL editor (e.g., db-fiddle.com) to create tables and relationships.

<!-- ## Example Exercises

```markdown
# Relational Algebra Example

## Exercise 1: Selection and Projection

Given a relation Students(Name, Age, Major), write the relational algebra expressions to:
1. Select students majoring in 'Computer Science'.
2. Project the names and ages of all students.

### Solution:

1. σ(Major='Computer Science')(Students)
2. π(Name, Age)(Students)

# ER Modelling Example

## Exercise 2: Create an ER Model

Create an ER model for a library system where:
- Books have attributes: ISBN, Title, Author, and Publication Year.
- Members have attributes: MemberID, Name, and MembershipDate.
- Each member can borrow multiple books, and each book can be borrowed by multiple members.

# Normalisation Example

## Exercise 3: Normalise the Schema

Given a table Orders(OrderID, CustomerName, CustomerAddress, OrderDate, ProductID, ProductName, Quantity), normalise this table up to 3NF.

### Solution:

1NF: Ensure each column has atomic values.
Orders(OrderID, CustomerName, CustomerAddress, OrderDate, ProductID, ProductName, Quantity)

2NF: Remove partial dependencies.
Orders(OrderID, OrderDate, CustomerID)
Customers(CustomerID, CustomerName, CustomerAddress)
OrderDetails(OrderID, ProductID, ProductName, Quantity)

3NF: Remove transitive dependencies.
Products(ProductID, ProductName)

# Database Design Example

## Exercise 4: Create Tables

Using an online SQL editor, create tables for the library system ER model.

```sql
CREATE TABLE Books (
    ISBN VARCHAR(20) PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    PublicationYear INT
);

CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(255),
    MembershipDate DATE
);

CREATE TABLE Borrowings (
    BorrowingID INT PRIMARY KEY,
    MemberID INT,
    ISBN VARCHAR(20),
    BorrowDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (ISBN) REFERENCES Books(ISBN)
);
``` -->

## Submission

- Document your progress and any important concepts you learn.
- Save the file with the name "7 Database Systems Workshop.md" in the "Practical Solutions" directory.
