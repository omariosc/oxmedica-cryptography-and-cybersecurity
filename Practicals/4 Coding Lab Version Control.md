# Practical 4: Coding Lab Version Control

## Overview

This practical exercise is designed to introduce you to version control using Git and GitHub. You will create GitHub accounts, set up repositories using your IDE, create branches, make commits, and perform push and pull requests. This task should take about 30 minutes to complete. This version control setup will help you store all your previous and future work from this course.

**Important Note: You need to have Git installed. If it does not work in your terminal, change your terminal to use Git bash. If you need to install Git, click [here](https://git-scm.com/download/win) and select `Next` in all of the installation step.

## Task

### Part 1: GitHub Account Setup

1. **Create a GitHub Account:**
   - Go to [GitHub](https://github.com/) and sign up for a free account if you don’t already have one.

### Part 2: Repository Setup in IDE

1. **Initialize Git in Your IDE:**
   - Open your IDE (e.g., VSCode) and initialize a new Git repository in your project folder.
   - Open the terminal in your IDE and run the following commands: `git init` to initialize Git, `git add .` to stage all files, and `git commit -m "Initial commit"` to make the first commit.

2. **Create a New Repository on GitHub:**
   - Log in to your GitHub account and create a new repository.
   - Follow the instructions to connect your local repository to the GitHub repository.

3. **Add Remote Repository:**
   - In your IDE terminal, link your local repository to the GitHub repository using the following commands:

```bat
git remote add origin https://github.com/your-username/your-repository-name.git
git branch -M main
git push -u origin main
```

### Part 3: Branching and Committing

1. **Create a New Branch:**
   - In your IDE terminal, create a new branch for your changes: `git checkout -b new-feature`.

2. **Make Changes and Commit:**
   - Make some changes to your project files.
   - Stage and commit your changes: `git add . && git commit -m "Add new feature"`

3. **Push Changes to GitHub:**
   - Push your changes to the new branch on GitHub: `git push origin new-feature`.

### Part 4: Pull Requests

1. **Create a Pull Request:**
   - Go to your GitHub repository and create a pull request from the new branch to the main branch.

2. **Merge Pull Request:**
   - Merge the pull request if there are no conflicts.
