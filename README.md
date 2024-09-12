# Quiz_App

## Overview

**Quiz_App_2.0** is a Python-based quiz application that utilizes SQLite for storing quiz questions and answers. This project allows users to take a quiz tailored to the questions added to the database.

## Features

- **Multiple-choice quiz**: Users are presented with a series of multiple-choice questions.
- **SQLite Integration**: The quiz data is stored in a SQLite database.
- **Score Tracking**: Users receive feedback on correct and incorrect answers, with a final score displayed at the end of the quiz.
- **Progress Tracking**: The last 5 results will show with a timestamp and the result of the quiz after each quiz is completed.
- **Database Setup**: Users to choose between using an existing database or creating a new one, with a streamlined process for data insertion and quiz initiation.

## Installation

### Prerequisites

- Python 3.10 or higher
  - Download from [Python Website](https://www.python.org/downloads/)
  - Windows:
    - `winget install Python 3.12`
  - MacOS:
    - `brew install python@3.12`
- Custom TKinter
  - Windows:
    - `pip install customtkinter`
  - MacOS:
    - `pip3 install customtkinter`

## Usage

### Running the Quiz

You can run the quiz by executing the `main.py` file:

```bash
python src/main.py
```

## Database Setup and Data Insertion
When you run `main.py`, you will be prompted to choose between using an existing database or creating a new one. The application will handle the database creation and data insertion based on your choice.

### Instructions

1. **Prepare Questions**: Format your questions in the following Python list of tuples format:
    ```python
    [
        ('Question?', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer', 'Explanation'),
        ('Question?', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer', 'Explanation'),
        ('Question?', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer', 'Explanation')
        ...
    ]
    ```

2. **Input Data**: A CustomTkinter window will open with a text box where you can paste your formatted list of questions.

3. **Submit Data**: Click the "Submit" button to insert the questions into the database. The script will validate the input, insert the data into the `quiz_questions` table, and display a success message. If there are errors in the input format, an error message will be shown.

4. **Automatic Closure**: After successful data insertion, the application will automatically close after a brief pause.

### Example of Input Format
To ensure the script works correctly, your input should be a properly formatted Python list of tuples. For example:
```python
[
    ('What is the capital of France?', 'Berlin', 'Madrid', 'Paris', 'Rome', 'C', 'Paris is the capital of France.'),
    ('Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'B', 'Mars is known as the Red Planet due to its reddish appearance.'),
    ...
]
```

## Project Structure

```bash
QUIZ_APP_2.0/
│
│
├── src/
│   ├── data/
│       └── quiz.db       # SQLite database file
│   ├── create_db.py      # Script to create the database and tables
│   ├── icon.ico          # Icon for package
│   ├── insert_data.py    # Script to insert quiz data into the database
│   ├── main.py           # Main script to run the entire process
│   ├── run_quiz_cli.py   # Script to run the quiz in the CLI
│   └── run_quiz_gui.py   # Script to run the quiz in a Graphical User Interface
│
├── license.txt           # MIT License
├── requirements.txt      # List of required Python Modules
└── README.md             # Project documentation
```