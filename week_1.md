# Week 1: Development Environment & Project Setup

Welcome to the **MSU AI Club Guided AI Project!**

This project focuses on **classical Artificial Intelligence**, where an agent analyses the current game state and uses programmed strategies to make decisions.

You'll begin by building the game itself, then create your own AI agent and improve its decision-making through experimentation and testing. At the end of the project, your AI will compete in a tournament against other student submissions.

This week is all about getting your development environment ready.

By the end of Week 1, you'll have everything installed, your project repository set up, and your development environment ready for Week 2.

---

# Prerequisites

- Basic Python programming knowledge is recommended.
- No previous Artificial Intelligence experience is required.
- No previous Git or GitHub experience is required.

---

# Learning Objectives

By the end of this week, you should be able to:

- Install Visual Studio Code.
- Install Python.
- Install Git.
- Navigate your computer using the terminal.
- Create a GitHub account.
- Clone a GitHub repository.
- Create and activate a Python virtual environment.
- Install project dependencies.
- Verify that your development environment is working.
- Use the basic Git workflow.

---

# What You'll Build

The complete project will eventually contain:

- A Connect 4 game engine.
- A graphical interface using Pygame.
- Your own AI agent.
- A system for testing AI performance.
- A final tournament between student submissions.

You will **not** build all of these components this week.

Instead, you'll build the project step by step throughout the seven-week guide.

---

# Table of Contents

1. Required Software
2. Basic Terminal Commands
3. Installing Visual Studio Code
4. Installing Python
5. Installing Git
6. Creating a GitHub Account
7. Cloning the Repository
8. Understanding the Starter Project
9. Opening the Project
10. Python Virtual Environments
11. Installing Dependencies
12. Verifying Your Environment
13. Basic Git Workflow
14. Week 1 Checklist
15. Troubleshooting
16. Week 1 Summary
17. Looking Ahead

---

# Required Software

Before continuing, install the following software.

| Software | Purpose |
|----------|---------|
| Visual Studio Code | Code editor used throughout the project |
| Python 3.11 or newer | Programming language |
| Git | Version control |
| GitHub Account | Store and manage your project |

---

# Basic Terminal Commands

Modern software development relies heavily on the command line.

Don't worry—you only need a few commands to get started.

## Display Your Current Directory

### Windows

```cmd
cd
```

### macOS / Linux

```bash
pwd
```

---

## List Files

### Windows

```cmd
dir
```

### macOS / Linux

```bash
ls
```

---

## Change Directory

```bash
cd folder-name
```

---

## Move Back One Directory

```bash
cd ..
```

---

## Create a Folder

```bash
mkdir practice
```

---

## Open the Current Folder in Visual Studio Code

```bash
code .
```

---

# Installing Visual Studio Code

Download Visual Studio Code from the official Visual Studio Code website.

During installation, enable:

- Add to PATH
- Register Code as an editor
- Create Desktop Shortcut (optional)

After installation, open a terminal and verify that Visual Studio Code is available:

```bash
code --version
```

If a version number appears, the installation was successful.

---

# Recommended VS Code Extensions

Open the Extensions tab using:

```text
Ctrl + Shift + X
```

Install:

- Python
- Pylance
- GitHub Pull Requests & Issues (optional)

The Python and Pylance extensions provide useful features such as syntax highlighting, code completion, error detection, and debugging support.

---

# Installing Python

Install Python 3.11 or newer from the official Python website.

During installation on Windows, make sure to enable:

```text
Add Python to PATH
```

After installation, open a new terminal and verify Python:

```bash
python --version
```

You should see a version number such as:

```text
Python 3.11.x
```

or newer.

### Windows Alternative

If `python` does not work, try:

```bash
py --version
```

Some Windows installations use the `py` command instead.

---

# Installing Git

Install Git from the official Git website.

After installation, verify Git:

```bash
git --version
```

You should see a Git version number.

---

# Configure Git

Before using Git, configure the name and email associated with your commits.

Replace the values below with your own information:

```bash
git config --global user.name "Your Name"

git config --global user.email "your@email.com"
```

You can verify your configuration with:

```bash
git config --list
```

---

# Creating a GitHub Account

Create a GitHub account if you do not already have one.

After creating your account:

- Verify your email address.
- Choose a professional username.
- Make sure you can sign in successfully.

GitHub will be used throughout this project to store your code and track your progress.

---

# Cloning the Repository

Your instructor will provide the GitHub repository for the project.

Open a terminal and navigate to the location where you want to store the project.

For example:

```bash
cd Desktop
```

Clone the repository:

```bash
git clone <repository-url>
```

Then move into the repository:

```bash
cd <repository-name>
```

You can verify that the repository was downloaded by listing its files.

### Windows

```cmd
dir
```

### macOS / Linux

```bash
ls
```

---

# Understanding the Starter Project

At the beginning of the project, you will receive a small starter project.

It intentionally does **not** contain the finished game.

Your starting structure should look similar to:

```text
starter_code/
│
├── agents/
│   ├── __init__.py
│   └── random_agent.py
│
├── connect4/
│   └── __init__.py
│
├── requirements.txt
└── run.py
```

Don't worry if this looks incomplete.

That's intentional.

Throughout the project, you'll create the missing files yourself.

---

## The Random Agent

The starter project includes a simple `RandomAgent`.

This is a basic testing opponent that chooses from the legal moves available to it.

You'll use it later to test your game engine and graphical interface.

You will **not** build your own AI yet.

Your own AI will be created in Week 5.

---

# How the Project Will Grow

The project will gradually become larger as you progress through the weekly guides.

By the end, your project will look similar to:

```text
starter_code/
│
├── agents/
│   ├── __init__.py
│   ├── random_agent.py
│   ├── base_agent.py
│   └── student_agent.py
│
├── connect4/
│   ├── __init__.py
│   ├── constants.py
│   ├── board.py
│   ├── rules.py
│   ├── state.py
│   ├── match_result.py
│   ├── game.py
│   └── renderer.py
│
├── requirements.txt
└── run.py
```

You will build these components gradually.

Do not worry about understanding all of them yet.

We'll introduce each part when you need it.

---

# Opening the Project

Move into the project folder:

```bash
cd <repository-name>
```

Then open it in Visual Studio Code:

```bash
code .
```

You should now see the project files in the VS Code Explorer.

Make sure you can locate:

```text
agents/
connect4/
requirements.txt
run.py
```

Inside `agents/`, you should also see:

```text
__init__.py
random_agent.py
```

---

# Python Virtual Environments

A Python virtual environment creates an isolated workspace for your project.

This means the packages used by this project can be installed separately from other Python projects on your computer.

Virtual environments are commonly used in Python development.

---

## Create a Virtual Environment

Open a terminal inside the project folder and run:

```bash
python -m venv .venv
```

On Windows, you can also use:

```bash
py -m venv .venv
```

This creates a folder named:

```text
.venv/
```

inside your project.

---

# Activate the Virtual Environment

## Windows

```cmd
.venv\Scripts\activate
```

## macOS / Linux

```bash
source .venv/bin/activate
```

If activation is successful, your terminal should begin with:

```text
(.venv)
```

This tells you that the virtual environment is currently active.

---

# Installing Project Dependencies

The project includes a `requirements.txt` file containing the Python packages needed for the project.

With your virtual environment activated, run:

```bash
python -m pip install -r requirements.txt
```

Using:

```bash
python -m pip
```

helps ensure that you're using the `pip` associated with the Python environment you're currently working in.

After installation, you can verify the installed packages with:

```bash
python -m pip list
```

You should see **pygame** listed.

---

# Verifying Pygame

Pygame will be used later to create the graphical Connect 4 interface.

You don't need to build anything with Pygame yet.

For now, simply verify that it installed correctly.

Run:

```bash
python -c "import pygame; print(pygame.version.ver)"
```

If Pygame is installed correctly, a version number should be displayed.

For example:

```text
2.x.x
```

---

# Important: Don't Expect the Game to Run Yet

At the beginning of this project, the game engine has not been built yet.

That's intentional.

You should **not** expect a complete Connect 4 game window at the end of Week 1.

Over the next few weeks, you'll build:

```text
Board
  ↓
Rules
  ↓
Game State
  ↓
Game Engine
  ↓
Renderer
  ↓
AI Agent
```

Each week adds another piece of the project.

---

# Basic Git Workflow

Throughout this project, you'll regularly save your progress using Git.

The basic workflow is:

```text
Make Changes
     ↓
git status
     ↓
git add .
     ↓
git commit
     ↓
git push
```

You'll use this workflow throughout the project.

---

## Check the Status of Your Project

```bash
git status
```

This shows which files have been modified or added.

---

## Stage Your Changes

```bash
git add .
```

This prepares your changes to be committed.

---

## Create a Commit

```bash
git commit -m "Completed Week 1 setup"
```

A commit creates a snapshot of your project at that point in time.

---

## Push Your Changes to GitHub

```bash
git push
```

This uploads your commits to your GitHub repository.

After pushing, open your repository on GitHub and confirm that your changes are visible.

---

# Your First Git Checkpoint

Before finishing Week 1, make sure you've created at least one commit.

You can check your commit history with:

```bash
git log --oneline
```

You should see your Week 1 commit listed.

For example:

```text
a1b2c3d Completed Week 1 setup
```

The exact characters will be different for your repository.

---

# Week 1 Checklist

Before moving on to Week 2, make sure you've completed all of the following:

- [ ] Installed Visual Studio Code
- [ ] Installed Python
- [ ] Installed Git
- [ ] Created a GitHub account
- [ ] Cloned the project repository
- [ ] Opened the project in Visual Studio Code
- [ ] Confirmed the starter project structure
- [ ] Created a Python virtual environment
- [ ] Activated the virtual environment
- [ ] Installed the project dependencies
- [ ] Verified that Pygame is installed
- [ ] Configured Git
- [ ] Made your first Git commit
- [ ] Pushed your changes to GitHub

---

# Troubleshooting

## Python Isn't Recognised

If this command doesn't work:

```bash
python --version
```

try:

```bash
py --version
```

on Windows.

If neither command works, reinstall Python and make sure **Add Python to PATH** is enabled during installation.

Restart your terminal after installing Python.

---

## The `code` Command Isn't Recognised

If:

```bash
code --version
```

doesn't work, reinstall Visual Studio Code with the PATH option enabled.

You can also open the project manually through:

```text
VS Code → File → Open Folder
```

---

## Git Isn't Recognised

If:

```bash
git --version
```

doesn't work, make sure Git was installed correctly.

Restart your terminal after installation.

---

## Virtual Environment Won't Activate

On Windows, PowerShell may prevent scripts from running.

If you receive a permissions error, you may need to run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating the environment again:

```powershell
.venv\Scripts\activate
```

---


# Week 1 Summary

Congratulations! 🎉

You've completed the first step of the MSU AI Club Guided AI Project.

This week you:

- Set up your development environment.
- Installed Python, Git, and Visual Studio Code.
- Learned basic terminal commands.
- Created a GitHub account.
- Cloned the project repository.
- Learned about the starter project structure.
- Created and activated a Python virtual environment.
- Installed the required dependencies.
- Verified that Pygame is installed.
- Learned the basic Git workflow.
- Created and pushed your first commit.

Your project may look very small right now.

That's intentional.

You will build the rest of it throughout the following weeks.

---

# Key Takeaways

Before moving on, make sure you're comfortable with:

- Navigating folders using the terminal.
- Opening a project in Visual Studio Code.
- Creating and activating a Python virtual environment.
- Installing Python packages.
- Running Python commands.
- Using Git to save your work.
- Pushing your project to GitHub.

These skills will be used throughout the rest of the project.

---

# Looking Ahead

Next week, you'll begin building the actual Connect 4 game.

You'll learn:

- How Connect 4 is represented in code.
- How a two-dimensional list can represent a game board.
- How constants improve code readability.
- How legal moves are validated.
- How pieces are placed on the board.
- Why creating copies of the board will eventually become important for AI.

By the end of Week 2, you'll have created the foundation that the rest of the project will build upon.

See you in **Week 2!** 🚀
