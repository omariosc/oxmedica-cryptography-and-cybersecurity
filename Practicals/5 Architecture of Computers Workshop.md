# Practical 5: Architecture of Computers Workshop

## Overview

This practical exercise is designed to introduce you to computer architecture, including Boolean logic, truth tables, number systems, memory, operating systems, CPUs, and GPUs. We will provide assembly code examples and demonstrate a buffer overflow in action. You will complete the provided interactive notebook during this 2-hour session.

## Task

### Part 1: Discussion and Demonstration (1 hour)

1. **Boolean Logic and Truth Tables:**
   - Discuss the basics of Boolean logic and how it is used in computer systems.
   Boolean logic is about using true/false values and operators like AND, OR, and NOT. Computers use it to make decisions, process data, and design circuits. It's essential for programming and understanding how computers work.
   - Provide examples of truth tables for AND, OR, and NOT gates.
   and gates require both A  & B to be on (ie A=1 B=1
   )to give a response however or gates require only one to be onm (A=1 B=0 and vice versa) not gates require both A and B to be of (A = 0 B = 0)to give a response
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
   Decimal (Base-10):
Uses 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
Each digit's position represents a power of 10. Example: 123 in decimal = 1 * 10^2 + 2 * 10^1 + 3 * 10^0 = 123. 
Binary (Base-2):
Uses 2 digits: 0 and 1. Each digit's position represents a power of 2. Example: 101 in binary = 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 5 in decimal.
Hexadecimal (Base-16):
Uses 16 digits: 0-9, and A-F (representing 10-15). Each digit's position represents a power of 16. Used often in computing due to its concise representation of binary data.Example: 1A3 in hexadecimal = 1 * 16^2 + A(10) * 16^1 + 3 * 16^0 = 419 in decimal.
   -demonstrate how to convert between these number systems 
   

3. **Memory and Operating Systems:**
   - Discuss the types of memory (RAM, ROM) and their roles in a computer.
   RAM is volatile and used for temporary storage of data and instructions that the CPU needs to access quickly.
ROM is non-volatile and holds essential firmware and startup instructions necessary for initializing the computer and performing low-level functions.
   - Provide an overview of how operating systems manage hardware and software resources.
   Operating systems efficiently manage computer resources like CPU scheduling, memory allocation, and device management. They also ensure file organization, system security, and user interface functionality. Overall, operating systems are essential for optimizing performance and enabling seamless interaction with computer hardware and software.

4. **CPUs and GPUs:**
   - Explain the functions of the CPU and GPU in a computer system.
   cpus handle the proscessing of information and excuting the tasks alocated to it and usualy takes from the ram however gpus takin more viual tasks like videos and pictures 
   - Discuss the differences between CPUs and GPUs in terms of processing tasks.
   same as whats written above 


5. **Assembly Code Examples:**
   - Provide simple examples of assembly code to illustrate low-level programming concepts.
   - Demonstrate how assembly code interacts with the computer's hardware.

6. **Buffer Overflow Demonstration:**
   - Show an example of a buffer overflow and explain how it can be exploited.
   - Discuss methods to prevent buffer overflow vulnerabilities.

### Part 2: Interactive Workbook (1 hour)

1. **Complete the Supplied Worksheet:**
   - You will be provided with a Python interactive workbook.
   - Work through the exercises and questions in the workbook, which will cover topics discussed in Part 1.

## Submission

- Complete the interactive workbook and save your progress.
- Submit your completed workbook to your GitHub repository.
