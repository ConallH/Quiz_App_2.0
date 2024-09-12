import sqlite3
import customtkinter as ctk
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def connect_db():
    # Connect to the SQLite database
    conn = sqlite3.connect(resource_path('data/quiz.db'))
    cursor = conn.cursor()
    return conn, cursor

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
