# Pomodoro Technique 

 This project implements a web application based on the Pomodoro Technique. Users can create tasks, initiate a timer, and upon completion, the task is marked as finished. The application also provides functionalities for stopping and resetting the timer.
 ###

# Getting started
 ## - Setup flask framework

  ### Step 1: Install Virtual Environment
  Use apt to install virtualenv on Debian, Ubuntu and other related distributions

  ```bash
   sudo apt install python-virtualenv
  ```

  ### Step 2: Create an Environment
  Make a separate directory for your project:
  ```bash
   mkdir <project name>
  ```
  Move into the directory:
  ```bash
   cd <project name>
  ```
  To create a virtual environment for Python 3, use the venv module and give it a name:
  ```bash
   python3 -m venv <name of environment>
  ```
  ### Step 3: Activate the Environment
  ```bash
   . <name of environment>/bin/activate
  ```
  ###

 ## - running the application
  ```
   python main.py
  ```
   ###
# Tests
 this project using [Unittest](https://docs.python.org/3/library/unittest.html) framework to testing endpoints
 ### Running tests
  ```
   python -m unittest main.py
  ```




