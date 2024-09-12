import sqlite3
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def connect_db():
    try:
        # Ensure the data directory exists
        data_dir = resource_path('data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # Connect to the SQLite database
        db_path = resource_path(os.path.join('data', 'quiz.db'))
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def create_table(cursor):
    try:
        # Create the quiz_questions table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer CHAR(1) NOT NULL,
            explanation TEXT NOT NULL
        );
        ''')
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        sys.exit(1)

def main():
    # Connect to the database and create the table
    conn, cursor = connect_db()
    create_table(cursor)
    
    # Commit and close the connection
    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    main()
