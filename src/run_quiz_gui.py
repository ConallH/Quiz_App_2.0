import sqlite3
import random
import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame
from datetime import datetime
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
    conn = sqlite3.connect(resource_path('data\\quiz.db'))
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer CHAR(1) NOT NULL,
        explanation TEXT
    );
    ''')

def fetch_questions(cursor):
    cursor.execute("SELECT * FROM quiz_questions")
    return cursor.fetchall()

class QuizApp(CTk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz App")
        self.geometry("600x400")

        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.total_questions = len(questions)
        
        # Create a frame to hold the question and buttons
        self.main_frame = CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.question_label = CTkLabel(self.main_frame, text="", font=("Arial", 16), wraplength=500)
        self.question_label.pack(pady=20)

        self.option_a_button = CTkButton(self.main_frame, text="", command=lambda: self.check_answer('A'))
        self.option_a_button.pack(pady=5, fill='x')

        self.option_b_button = CTkButton(self.main_frame, text="", command=lambda: self.check_answer('B'))
        self.option_b_button.pack(pady=5, fill='x')

        self.option_c_button = CTkButton(self.main_frame, text="", command=lambda: self.check_answer('C'))
        self.option_c_button.pack(pady=5, fill='x')

        self.option_d_button = CTkButton(self.main_frame, text="", command=lambda: self.check_answer('D'))
        self.option_d_button.pack(pady=5, fill='x')

        self.explanation_label = CTkLabel(self.main_frame, text="", font=("Arial", 12), wraplength=500)
        self.explanation_label.pack(pady=10, fill='x')

        self.next_button = CTkButton(self.main_frame, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Results frame
        self.results_frame = CTkFrame(self)
        self.results_frame.pack(expand=True, fill="both", padx=20, pady=20)
        self.results_frame.pack_forget()  # Hide results frame initially

        self.results_label = CTkLabel(self.results_frame, text="", font=("Arial", 16), wraplength=500)
        self.results_label.pack(pady=20)

        # Update wraplength according to window size
        self.update_wraplength()

        # Bind window resize event to update wraplength
        self.bind("<Configure>", lambda event: self.update_wraplength())

        self.show_question()

    def update_wraplength(self):
        width = self.winfo_width() - 40  # Subtract padding
        self.question_label.configure(wraplength=width)
        self.explanation_label.configure(wraplength=width)
        self.results_label.configure(wraplength=width)

    def show_question(self):
        if self.current_question < self.total_questions:
            self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
            self.results_frame.pack_forget()  # Hide results frame
            
            question = self.questions[self.current_question]
            self.question_label.configure(text=question[1])
            self.option_a_button.configure(text=f"A. {question[2]}")
            self.option_b_button.configure(text=f"B. {question[3]}")
            self.option_c_button.configure(text=f"C. {question[4]}")
            self.option_d_button.configure(text=f"D. {question[5]}")
            self.explanation_label.configure(text="")  # Clear explanation label
        else:
            self.show_result()

    def check_answer(self, option):
        correct_answer = self.questions[self.current_question][6]
        explanation = self.questions[self.current_question][7]

        if option == correct_answer:
            self.score += 1
            result_text = "Correct!"
        else:
            result_text = f"Wrong! The correct answer is {correct_answer}."

        self.explanation_label.configure(text=f"{result_text}\nExplanation: {explanation}")

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_result(self):
        self.main_frame.pack_forget()  # Hide the main frame
        self.results_frame.pack(expand=True, fill="both", padx=20, pady=20)  # Show the results frame
        
        percentage = (self.score / self.total_questions) * 100
        result_text = f"Your final score is: {self.score}/{self.total_questions}\nYour percentage is: {percentage:.2f}%"
        self.results_label.configure(text=result_text)
        
        # Append results to the .md file
        self.generate_results_file(result_text)

    def generate_results_file(self, result_text):
        filename = "quiz_results.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, 'a') as file:
            file.write(f"\n## Quiz Results - {timestamp}\n")
            file.write(f"**Final Score:** {self.score}/{self.total_questions}\n")
            file.write(f"**Percentage:** {result_text.split('Your percentage is: ')[1]}\n")
            file.write("\n---\n")  # Separator between results

def main():
    conn, cursor = connect_db()
    create_table(cursor)
    questions = fetch_questions(cursor)
    selected_questions = random.sample(questions, 10)
    app = QuizApp(selected_questions)
    app.mainloop()
    conn.close()

if __name__ == "__main__":
    main()
