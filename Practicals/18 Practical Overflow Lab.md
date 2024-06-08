# Practical 18: Buffer Overflow Lab

## Overview

This practical exercise is designed to help you understand buffer overflows in the C programming language and how they can be avoided. You will investigate how buffer overflows occur, their consequences, and methods to prevent them. This session will take about 30 minutes to complete.

## Task

### Part 1: Introduction to Buffer Overflows (5 minutes)

1. **What is a Buffer Overflow?**
   - A buffer overflow occurs when data written to a buffer exceeds its capacity, causing data to overwrite adjacent memory.
   - This can lead to unexpected behavior, crashes, or security vulnerabilities, such as executing arbitrary code.

2. **Common Causes of Buffer Overflows:**
   - Inadequate boundary checking
   - Using unsafe functions (e.g., `gets()`, `strcpy()`, `sprintf()`)
   - Mismanagement of memory allocation

### Part 2: Investigating Buffer Overflows (15 minutes)

1. **Example of a Buffer Overflow in C:**

    ```c
    #include <stdio.h>
    #include <string.h>

    void vulnerable_function(char *str) {
        char buffer[10];
        strcpy(buffer, str); // No boundary checking
        printf("Buffer: %s\n", buffer);
    }

    int main() {
        char *large_string = "This string is definitely longer than ten characters!";
        vulnerable_function(large_string);
        return 0;
    }
    ```

- Compile and run the code to see what happens when a buffer overflow occurs. Use the website [OnlineGDB](https://www.onlinegdb.com/online_c_compiler) to compile and run the code.

2. **Understanding the Consequences:**
   - Observe the output and any potential crashes or unusual behavior.
   - Discuss how an attacker might exploit this vulnerability to execute arbitrary code.

### Part 3: Preventing Buffer Overflows (10 minutes)

1. **Using Safe Functions:**
   - Replace unsafe functions with safer alternatives that perform boundary checking (e.g., `strncpy()` instead of `strcpy()`).

    ```c
    #include <stdio.h>
    #include <string.h>

    void safe_function(char *str) {
        char buffer[10];
        strncpy(buffer, str, sizeof(buffer) - 1);
        buffer[sizeof(buffer) - 1] = '\0'; // Null-terminate the buffer
        printf("Buffer: %s\n", buffer);
    }

    int main() {
        char *large_string = "This string is definitely longer than ten characters!";
        safe_function(large_string);
        return 0;
    }
    ```

- Compile and run the modified code to see how it prevents buffer overflows.

2. **Implementing Boundary Checks:**
   - Ensure that all buffer operations include boundary checks to prevent overflows.
   - Use functions like `snprintf()`, `strncat()`, and `fgets()` for safer string operations.

### Part 4: Exercises (10 minutes)

1. **Exercise 1: Identify Buffer Overflows**
   - TODO: Review the following code and identify any potential buffer overflow vulnerabilities.
   
    ```c
    #include <stdio.h>

    void process_input(char *input) {
        char buffer[20];
        // TODO: Identify potential buffer overflow
        strcpy(buffer, input);
        printf("Processed input: %s\n", buffer);
    }

    int main() {
        char user_input[100];
        printf("Enter input: ");
        gets(user_input);
        process_input(user_input);
        return 0;
    }
    ```

2. **Exercise 2: Fix Buffer Overflows**
   - TODO: Modify the above code to prevent buffer overflows using safe functions and boundary checks.

3. **Exercise 3: Write Secure Code**
   - TODO: Write a function that safely copies a string into a buffer of a given size, ensuring no overflow occurs.

## Summary

- You have learned what buffer overflows are and how they occur in C programming.
- You have investigated the consequences of buffer overflows and seen an example of how they can be exploited.
- You have learned techniques to prevent buffer overflows by using safe functions and implementing boundary checks.
- You have completed exercises to identify and fix buffer overflow vulnerabilities.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"18 Buffer Overflow Lab.md"` in the `"Practical Solutions"` directory.
