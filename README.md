# Quiz-Application-Prototype-
A console-based quiz application using Python and MySQL that manages user registration/login with profile updates, serves randomized MCQ quizzes on DSA/DBMS/Python topics, tracks scores with timestamps in a dedicated database table, displays score history ordered by date, and maintains data synchronization between in-memory dictionaries .

# Quiz Application - Python + MySQL

Console-based quiz system with user authentication and score tracking.

## Features
- User registration and login
- 3 Quiz categories: DSA, DBMS, Python (5 MCQs each)
- Score recording with timestamps
- Profile view and update
- Database persistence

## Tech Stack
- Python 3.x
- MySQL
- mysql-connector-python

## Setup & Run
1. Install MySQL, create 'quiz' database
2. `pip install mysql-connector-python`
3. Update MySQL credentials in code (line 8-9)
4. `python quiz.py`
