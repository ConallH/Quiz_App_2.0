import create_db
import run_quiz_gui
import customtkinter as ctk

def run_script(script_name):
    if script_name == "create_db":
        create_db.main()  # Call create_db.main() to create a new database
    elif script_name == "insert_data":
        try:
            import insert_data  # Import only when needed
            insert_data.main()  # Call insert_data.main() to insert data
        except AttributeError as e:
            print(f"Error: {e}. Please check if insert_data module has a main function.")
    elif script_name == "run_quiz_gui":
        run_quiz_gui.main()  # Call run_quiz_gui.main() to start the quiz

def on_confirm(choice):
    global user_choice
    user_choice = choice
    root.destroy()  # Close the Tkinter window

def main():
    global user_choice
    global root
    user_choice = None

    # Initialize CustomTkinter
    ctk.set_appearance_mode("System")  # "Light", "Dark", or "System"
    ctk.set_default_color_theme("blue")  # Choose a color theme

    # Create the main window
    root = ctk.CTk()
    root.title("Database Setup")

    # Create and place widgets
    label = ctk.CTkLabel(root, text="Do you want to use an existing database or create a new one?")
    label.pack(pady=20)

    button_existing = ctk.CTkButton(root, text="Use Existing Database", command=lambda: on_confirm('existing'))
    button_existing.pack(pady=10)

    button_new = ctk.CTkButton(root, text="Create New Database", command=lambda: on_confirm('new'))
    button_new.pack(pady=10)

    # Start the Tkinter event loop (wait for user input)
    root.mainloop()

    # Execute script based on user choice after the window is closed
    if user_choice == 'new':
        print("Creating the database and table...")
        run_script("create_db")  # Create a new database
        run_script("insert_data")  # Insert data into the new database
    elif user_choice == 'existing':
        print("Using the existing database...")
        # Add any additional logic needed for using the existing database

    print("Starting the quiz...")
    run_script("run_quiz_gui")  # Start the quiz GUI

if __name__ == "__main__":
    main()
