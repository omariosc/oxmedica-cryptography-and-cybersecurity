# Practical 12: System Design and Security Analysis

## Overview

This practical exercise is designed to help you understand how to design a theoretical system that interacts with the internet, identify potential vulnerabilities, and research ways to mitigate those vulnerabilities. You will also prepare and present a lightning talk on your findings. This session will take about 1 hour and 45 minutes to complete, over the course of 3 sessions.

**IMPORTANT: You need to prepare your lightning talk within the first 45 minutes and present it in the last 1 hour.**

## Task

### Part 1: System Design and Potential Vulnerabilities (15 minutes)

1. **Design a Theoretical System:**
   - Think about a system that interacts with the internet. It could be an e-commerce website, a social media platform, an online banking system, etc.
   - Describe the components of your system and how they interact with each other and the internet.

2. **Research Potential Vulnerabilities:**
   - Identify potential vulnerabilities in your system. Consider the following types of vulnerabilities:
     - **SQL Injection:** A vulnerability that allows attackers to execute arbitrary SQL code on a database.
     - **Cross-Site Scripting (XSS):** A vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users.
     - **Cross-Site Request Forgery (CSRF):** A vulnerability that tricks a user into performing actions on a web application without their consent.
     - **Man-in-the-Middle (MITM) Attacks:** A vulnerability where an attacker intercepts and potentially alters communication between two parties.
     - **Denial of Service (DoS) Attacks:** A vulnerability that makes a system unavailable by overwhelming it with traffic.
     - **Phishing:** A technique where attackers trick users into providing sensitive information by posing as a trustworthy entity.

3. **Document Your Findings:**
   - Write a brief description of your theoretical system and list the identified potential vulnerabilities.
   - Example:
        ```markdown
        **System Design: Online Banking System**

        **Components:**
        - Web Server: Hosts the online banking website.
        - Database Server: Stores user data, transaction history, and account information.
        - Authentication Server: Manages user login and authentication.
        - Payment Gateway: Processes online transactions.

        **Potential Vulnerabilities:**
        1. **SQL Injection:** The login form could be vulnerable to SQL injection attacks.
        2. **Cross-Site Scripting (XSS):** User input fields may allow malicious script injection.
        3. **Cross-Site Request Forgery (CSRF):** The system could be tricked into executing unauthorized actions.
        4. **Man-in-the-Middle (MITM) Attacks:** Data transmitted over the internet might be intercepted.
        5. **Denial of Service (DoS) Attacks:** The web server could be overwhelmed by excessive traffic.
        6. **Phishing:** Users might be tricked into providing their login credentials to a fake website.
        ```

### Part 2: Vulnerability Analysis and Mitigation Research (30 minutes)

1. **Analyse Your System:**
   - Review the system you designed in Part 1 and analyze the identified vulnerabilities in detail.

2. **Research Mitigation Strategies:**
   - Research online for ways to fix the identified vulnerabilities. Consider the following strategies:
     - **SQL Injection Mitigation:** Use prepared statements and parameterized queries to prevent SQL injection.
     - **XSS Mitigation:** Implement input validation and output encoding to prevent XSS attacks.
     - **CSRF Mitigation:** Use anti-CSRF tokens to protect against CSRF attacks.
     - **MITM Attack Mitigation:** Implement SSL/TLS encryption to secure data transmission.
     - **DoS Attack Mitigation:** Use rate limiting and web application firewalls (WAF) to prevent DoS attacks.
     - **Phishing Mitigation:** Educate users about phishing techniques and implement multi-factor authentication (MFA).

3. **Document Your Findings:**
   - Write a brief description of each identified vulnerability and the corresponding mitigation strategy.
   - Example:
        ```markdown
        **Vulnerability Analysis and Mitigation: Online Banking System**

        1. **SQL Injection:**
        - **Analysis:** The login form is vulnerable to SQL injection.
        - **Mitigation:** Use prepared statements and parameterized queries to prevent SQL injection.

        2. **Cross-Site Scripting (XSS):**
        - **Analysis:** User input fields may allow malicious script injection.
        - **Mitigation:** Implement input validation and output encoding to prevent XSS attacks.

        3. **Cross-Site Request Forgery (CSRF):**
        - **Analysis:** The system could be tricked into executing unauthorized actions.
        - **Mitigation:** Use anti-CSRF tokens to protect against CSRF attacks.

        4. **Man-in-the-Middle (MITM) Attacks:**
        - **Analysis:** Data transmitted over the internet might be intercepted.
        - **Mitigation:** Implement SSL/TLS encryption to secure data transmission.

        5. **Denial of Service (DoS) Attacks:**
        - **Analysis:** The web server could be overwhelmed by excessive traffic.
        - **Mitigation:** Use rate limiting and web application firewalls (WAF) to prevent DoS attacks.

        6. **Phishing:**
        - **Analysis:** Users might be tricked into providing their login credentials to a fake website.
        - **Mitigation:** Educate users about phishing techniques and implement multi-factor authentication (MFA).
        ```

### Part 3: Lightning Talks (1 hour)
   
## Submission

- Complete the exercises and ensure all solutions are documented.
- Save the file with the name `"12 System Design and Security Analysis.md"` in the `"Practical Solutions"` directory.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
