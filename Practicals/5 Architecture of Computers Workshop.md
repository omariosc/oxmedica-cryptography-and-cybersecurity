# Practical 5: Architecture of Computers Workshop

## Overview

This practical exercise is designed to introduce you to computer architecture, including Boolean logic, truth tables, number systems, memory, operating systems, CPUs, and GPUs. We will provide assembly code examples and demonstrate a buffer overflow in action. You will complete the provided interactive notebook during this 2-hour session.

## Task

### Part 1: Discussion and Demonstration (1 hour)

1. **Boolean Logic and Truth Tables:**
   - Discuss the basics of Boolean logic and how it is used in computer systems.
   - Provide examples of truth tables for AND, OR, and NOT gates.
   <!-- - Example:
   | A | B | AND | OR | NOT A |
   |---|---|-----|----|-------|
   | 0 | 0 |  0  | 0  |   1   |
   | 0 | 1 |  0  | 1  |   1   |
   | 1 | 0 |  0  | 1  |   0   |
   | 1 | 1 |  1  | 1  |   0   |
   -->

2. **Number Systems:**
   - Explain different number systems such as binary, decimal, and hexadecimal.
   - Demonstrate how to convert between these number systems.

3. **Memory and Operating Systems:**
   - Discuss the types of memory (RAM, ROM) and their roles in a computer.
   - Provide an overview of how operating systems manage hardware and software resources.

4. **CPUs and GPUs:**
   - Explain the functions of the CPU and GPU in a computer system.
   - Discuss the differences between CPUs and GPUs in terms of processing tasks.

5. **Assembly Code Examples:**
   - Provide simple examples of assembly code to illustrate low-level programming concepts.
   - Demonstrate how assembly code interacts with the computer's hardware.

6. **Buffer Overflow Demonstration:**
   - Show an example of a buffer overflow and explain how it can be exploited.
   - Discuss methods to prevent buffer overflow vulnerabilities.

## **Answer**

1.
   Boolean Logic is a form of algaba where results are calculated as either TRUE or FALSE.

   | A | B | AND | OR | NOT B |
   |---|---|-----|----|-------|
   | 1 | 0 |  0  | 1  |   1   |
   | 1 | 1 |  1  | 1  |   0   |
   | 1 | 0 |  0  | 1  |   0   |
   | 0 | 0 |  0  | 0  |   1   |

2.
   -Binary is a number system that only uses two digits: 1 and 0.
   -Decimal system consists of ten digits, from 0 to 9.
   -Hexadecimal is a number system, that has a base value equal to 16. These symbols or values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F. Each digit represents a decimal value.

   | Binary | Decimal | Hexadecimal |
   |--------|---------|-------------|
   |  0000  |    0    |      0      |
   |  0001  |    1    |      1      |
   |  0010  |    2    |      2      |
   |  0011  |    3    |      3      |
   |  0100  |    4    |      4      |
   |  0101  |    5    |      5      |
   |  0110  |    6    |      6      |
   |  0111  |    7    |      7      |
   |  1000  |    8    |      8      |
   |  1001  |    9    |      9      |
   |  1010  |    10   |      A      |
   |  1011  |    11   |      B      |
   |  1100  |    12   |      C      |
   |  1101  |    13   |      D      |
   |  1101  |    14   |      E      |
   |  1111  |    15   |      F      |   
   
**chatgpt was not used i made this by hand ಠ_ಠ**

3.
   RAM is memory that stores the data that you're currently working with, but as soon as it loses power, that data disappears.
   ROM refers to permanent memory. It's non-volatile, so when it loses power, the data remains.

4.
   CPU is designed to handle a wide-range of tasks quickly, but is limited to the concurrency of tasks that are running.
   A GPU is designed to quickly render high-resolution images and video concurrently.

5.





### Part 2: Interactive Workbook (1 hour)

1. **Complete the Supplied Worksheet:**
   - You will be provided with a Python interactive workbook.
   - Work through the exercises and questions in the workbook, which will cover topics discussed in Part 1.

## Submission

- Complete the interactive workbook and save your progress.
- Submit your completed workbook to your GitHub repository.
