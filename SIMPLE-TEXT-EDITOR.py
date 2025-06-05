import tkinter as tk  # Importing Tkinter for GUI
from tkinter import filedialog, messagebox  # Importing file dialog and message box

# Function to create a new file (clear the text area)
def new_file():
    text.delete(1.0, tk.END)  # Deletes all text from the text widget

# Function to open an existing text file
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=[("Text Files", ".txt")]
    )  # Open file dialog to select a text file
    if file_path:  # If a file is selected
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)  # Clear existing text
            text.insert(tk.END, file.read())  # Insert file content into the text widget

# Function to save the current file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
    )  # Open save file dialog
    if file_path:  # If a file path is provided
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))  # Save the content of the text widget to the file
        messagebox.showinfo("Info", "File saved successfully!")  # Show confirmation message

# Initialize the main application window
root = tk.Tk()
root.title("Simple Text Editor")  # Set window title
root.geometry("800x600")  # Set window size

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Create a "File" menu with options
file_menu = tk.Menu(menu, tearoff=False)  # Remove dashed line in dropdown
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)  # New file option
file_menu.add_command(label="Open", command=open_file)  # Open file option
file_menu.add_command(label="Save", command=save_file)  # Save file option
file_menu.add_separator()  # Add separator line
file_menu.add_command(label="Exit", command=root.quit)  # Exit option

# Create a text widget where users can type
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")  # Configure text widget
text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand to fit window

# Run the application
root.mainloop()
