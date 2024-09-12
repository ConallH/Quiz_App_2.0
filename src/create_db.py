import sqlite3
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

def ensure_data_directory_exists():
    """ Ensure the src/data directory exists """
    data_dir = resource_path('data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

def connect_db():
    try:
        # Ensure the src/data directory exists
        ensure_data_directory_exists()

        # Get the correct path for the database file
        db_path = get_db_path()

        print(f"Database path: {db_path}")  # Debugging - confirm the DB path
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
