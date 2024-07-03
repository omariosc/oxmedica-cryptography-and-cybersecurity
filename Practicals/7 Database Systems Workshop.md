# Practical 7: Database Systems Workshop

## Overview

This practical exercise is designed to introduce you to database systems, including database architecture, relational algebra, ER modelling, normalisation, and database design. To supplement this workshop, we will use online modelling software. This session will take about 90 minutes to complete.

## Task

### Part 1: Database Architecture (15 minutes)

1. **Overview:**
   - Discuss the basic architecture of a database system.
   - Components to cover:
     - Database Engine
     a database engine is the main componnent a dbms system uses to crate and delete SCUM data as well as update and process it 
     - Query Processor
     its the processng unit of a dbms system as its used to take inSQL results and process them by forming them relatively to the schema table format and then it takes in that data and hands it over to be rewriten and takenn in by logical components then if it suceedes it hades it over to the  optimizer then moves it over to the query executor
     - Storage Manager
     its an internal software layer witchrelies on I/O relations to store B-trees and Heaps witch is the transformed to internal data BLOBS

     - Transaction Manager
     it ennsures the saftey of then data after a crash

### Part 2: Relational Algebra (15 minutes)

1. **Introduction:**
   - Explain the fundamental operations of relational algebra:
     - Selection (σ)
     its whats used to find rows given a certian condition on a table
     - Projection (π)
     its what used to find tthe information excluuding the full row soit can be thought ifb as a collumn 
     for example if i were to store my clients info on a grid format leading with the names and ending with the age the value of - Projection (π)2 - would be the ages of all clients -theirnames and its useful in gathering statistic data
     - Union (∪)
     Where r and s are either database relations or relation result set (temporary relation).

For a union operation to be valid, the following conditions must hold 
r, and s must have the same number of attributes.
Attribute domains must be compatible.
Duplicate tuples are automatically eliminated.
the ressult being all of r s and r&s
     - Set Difference (−)
The result of set difference operation is tuples, which are present in one relation but are not in the second relation.

Notation − r − s

Finds all the tuples that are present in r but not in s.
the result being r-s
e.g R=[1,2,3] s = [2,9,5,]
R-S=[1,3]
     - Cartesian Product (×)
     the intersections btween the two lists 
     - Rename (ρ)
     Rename Operation (ρ)
The results of relational algebra are also relations but without any name. The rename operation allows us to rename the output relation. 'rename' operation is denoted with small Greek letter rho ρ.

Notation − ρ x (E)

Where the result of expression E is saved with name of x.

Additional operations are −

Set intersection
Assignment
Natural join


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
- Save the file with the name `"7 Database Systems Workshop.md"` in the `"Practical Solutions"` directory.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
