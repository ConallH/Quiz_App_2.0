import sqlite3
import customtkinter as ctk
import os
import sys

import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Base path is the script's directory (src folder in development)
        base_path = os.path.dirname(__file__)  # Corrects the base path to current script folder
    
    return os.path.join(base_path, relative_path)

def get_db_path():
    """ Return a path for the SQLite database inside the src/data folder """
    # Handle both development and packaged modes
    if getattr(sys, 'frozen', False):
        # Packaged mode, use the src/data folder in the base directory
        base_path = os.path.abspath(os.path.dirname(sys.executable))  # Path to the executable
        db_path = os.path.join(base_path, 'data', 'quiz.db')  # No redundant src
    else:
        # Development mode, use the src/data folder relative to the script
        db_path = resource_path(os.path.join('data', 'quiz.db'))  # Inside src/data
    
    return db_path

def connect_db():
    try:
        # Get the correct path for the database file
        db_path = get_db_path()

        print(f"Database path: {db_path}")  # Debugging - confirm the DB path
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def insert_data(cursor, data):
    # Insert data into the quiz_questions table
    cursor.executemany('''
    INSERT INTO quiz_questions (question, option_a, option_b, option_c, option_d, correct_answer, explanation)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)

def parse_input(input_text):
    try:
        # Evaluate the input as a Python list of tuples
        questions = eval(input_text.strip())
        
        # Check if the input is a list of tuples
        if not isinstance(questions, list) or not all(isinstance(q, tuple) and len(q) == 7 for q in questions):
            raise ValueError("Input should be a list of tuples, each containing 7 elements.")
        
        return questions
    except Exception as e:
        raise ValueError(f"Failed to parse input: {str(e)}")

def on_submit():
    input_text = text_box.get("1.0", "end")
    try:
        data = parse_input(input_text)
        conn, cursor = connect_db()
        insert_data(cursor, data)
        conn.commit()
        conn.close()
        result_label.configure(text="Data inserted successfully!", text_color="green")
        
        # Close the application after a brief pause to show success message
        app.after(2000, app.destroy)  # 2000ms = 2 seconds
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}", text_color="red")

# Set up the CustomTkinter window
app = ctk.CTk()
app.title("Insert Quiz Questions")
app.geometry("600x400")

# Text box for input
text_box = ctk.CTkTextbox(app, height=250, width=550)
text_box.pack(padx=20, pady=20)

# Submit button
submit_button = ctk.CTkButton(app, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(app, text="")
result_label.pack()

# Run the Tkinter event loop
app.mainloop()
