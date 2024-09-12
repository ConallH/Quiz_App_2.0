# Quiz_App

## Overview

**Quiz_App** is a Python-based quiz application that utilizes SQLite for storing quiz questions and answers. This project allows users to take a quiz tailored to the questions added to the insert_data.py script, with questions and options stored in a SQLite database.

## Features

- **Multiple-choice quiz**: Users are presented with a series of multiple-choice questions.
- **SQLite Integration**: The quiz data is stored in a SQLite database.
- **Score Tracking**: Users receive feedback on correct and incorrect answers, with a final score displayed at the end of the quiz.
- **Progress Tracking**: A Markdown file with a timestamp and the result of the quiz will be created/appended after each quiz is completed.

## Installation

### Prerequisites

- Python 3.10 or higher
  - Download from Python Website
  - Windows:
    - winget install Python 3.12
  - MacOS:
    - brew install python@3.12
- Custom TKinter
  - Windows:
    - pip install customtkinter
  - MacOS
    - pip3 install customtkinter


## Usage

### Running the Quiz

You can run the quiz by executing the `main.py` file:

```bash
python src/main.py
```

## Database Setup
The project automatically creates and populates the SQLite database `quiz.db` with the content of `insert_data.py` when you run `main.py`. If you need to manually create the database or insert data, you can run:
```bash
python src/create_db.py
python src/insert_data.py
```

## Adding Question to the Quiz
To add your own questions, you can modify the `insert_data.py` script following the sample question format. Once run this will insert (appends existing `quiz.db`) the questions into the `quiz.db` SQLite database. Script will fail if there are less than 10 questions.

## Project Structure
```bash
PYTHON-QUIZ/
│
├── src/
│   └── data/
│       └── quiz.db           # SQLite database file
│   ├── create_db.py          # Script to create the database and tables
│   ├── icon.ico              # Icon for package
│   ├── insert_data.py        # Script to insert quiz data into the database
│   ├── main.py               # Main script to run the entire process
│   ├── run_quiz_cli.py       # Script to run the quiz in the CLI
│   └── run_quiz_gui.py       # Script to run the quiz in a Graphical User Interface
│
├── license.txt               # MIT License
├── Quiz_App_1.0_setup.exe    # Installable version
├── requirements.txt          # List of required Python Modules
└── README.md                 # Project documentation
```