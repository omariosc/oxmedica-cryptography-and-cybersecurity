A database engine (or storage engine) is the underlying software component that a database management system (DBMS) uses to create, read, update and delete (CRUD) data from a database.

-------------------------------------------

The query processor is the subcomponent of the data server that processes SQL requests. The SQL requests can access a single database or file system or reference multiple types of databases or file systems.

-------------------------------------------

The storage manager is a software layer within a database management system. It relies on operating system primitives for I/O, synchronization, etc. and exposes records in storage structures such as B-trees and heaps.
	
-------------------------------------------

A transaction manager plays an essential role in guiding various transactions within a business, ensuring they are executed smoothly and efficiently. They oversee each stage of a transaction, from initiation to completion, whilst adhering to set policies, rules and regulations.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The fundamental operations of relational algebra:

    
                                        -Selection (σ)	
In database theory, the selection (σ) operator is used to retrieve specific rows or tuples from a table based on a certain condition or criteria. It acts like a filter that extracts only the rows that satisfy a given condition.

For instance, if you have a table containing employee information with attributes like name, age, and department, the selection operation σ(age > 30) would return only the rows where the age of employees is greater than 30.

--------------------------------------------------------------------------------

-Projection (π)
In mathematics and computer science, a projection (π) is a function that maps a set of values to a subset of those values, often by selecting specific components or attributes from a larger set. 
For example, in relational databases, the projection operation (π) is used to select specific columns from a table. If we have a table with columns (A, B, C), then the projection π(B, C) would extract only columns B and C.

--------------------------------------------------------------------------------

-Union (∪)
The union symbol (∪) in set theory represents combining elements from two or more sets while eliminating duplicates. For example, if Set A = {1, 2, 3} and Set B = {3, 4, 5}, the union of A and B is A ∪ B = {1, 2, 3, 4, 5}. It includes all unique elements from both sets.

In set theory, the union (∪) of two sets combines all the unique elements from both sets into a single set.

For example, let's consider two sets:
Set A = {1, 2, 3, 4}
Set B = {3, 4, 5, 6}

The union of sets A and B (A ∪ B) would result in:
A ∪ B = {1, 2, 3, 4, 5, 6}

So, after performing the union operation, the resulting set contains all the distinct elements from both sets A and B.

--------------------------------------------------------------------------------

-Set Difference (−)
The set difference symbol (−) in set theory represents the elements that are in one set but not in another. For example, if Set A = {1, 2, 3, 4} and Set B = {3, 4, 5}, then A - B would be {1, 2}, as these are the elements that are in A but not in B.

Example:  
Sure! Let's consider the following sets for the set difference operation:

Set X = {1, 2, 3, 4, 5}
Set Y = {3, 4, 5, 6, 7}

The set difference operation (X - Y) would result in a set containing elements that are in Set X but not in Set Y.

Performing the set difference operation:
X - Y = {1, 2}
Therefore, the result of (X - Y) in this case would be the set {1, 2}.

--------------------------------------------------------------------------------

Cartesian Product (×)
The Cartesian Product (×) of two sets A and B is a set of all possible ordered pairs where the first element of each pair is from set A and the second element is from set B.

Let's consider two sets:
Set A = {a, b}
Set B = {1, 2}
The Cartesian Product of sets A and B (A × B) would be:
A × B = {(a, 1), (a, 2), (b, 1), (b, 2)}
Each ordered pair represents all possible combinations of elements from sets A and B. In this case, the Cartesian Product results in four ordered pairs.

--------------------------------------------------------------------------------

Rename (ρ)
In relational algebra, the Rename operation (ρ) is used to rename a relation or attributes within a relation. It allows you to change the name of a relation or attribute temporarily without changing its content.

For example, let's say we have a relation R with attributes A and B: R(A, B) If we want to rename attribute A to X in relation R, we would use the Rename operation as follows: ρ(X/Y)(R)
After the Rename operation, the relation R would look like this:
R(X, B)
