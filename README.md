# PYTHON-PROJECTS
Hello Guys, This is my profile. A collection of Python-based projects showcasing problem-solving, automation, data handling, and real-world applications. Ideal for learning, experimentation, and practical coding experience.




                                                                       1. Realtime-Digital-Clock
Digital Clock

Description : This is a simple digital clock application built using Python's Tkinter module. The clock displays the current time, date, and AM/PM status in a graphical window. The time updates dynamically every second using the after() method of Tkinter.

Features: Displays the current time in HH:MM:SS format. Shows the date in DD MMM YYYY format. Automatically updates every second. Simple and user-friendly graphical interface.

Installation: To run this script, ensure you have Python installed on your system. No additional libraries are required as Tkinter is included in standard Python distributions.

Usage: Run the Python script. A window will open displaying the current time and date. The clock updates automatically every second. Close the window to exit the application.

:Code Breakdown:

Importing Required Modules:
tkinter is used for creating the graphical user interface (GUI).

strftime from the time module is used to get the formatted current time and date.

Initializing the Main Window:
tk.Tk() creates the main application window.

root.title("Digital Clock") sets the window title.

Defining the time() Function:
Uses strftime('%H:%M:%S %d %b %Y %p') to format the current time and date.

Updates the label text dynamically.

Calls label.after(1000, time) to refresh the time every second.

Creating and Configuring the Label:

The tk.Label() widget is used to display the time.

Font is set to 'calibri', size 50, and bold.

Background color is black, and text color is white.

label.pack(anchor='center') places the label at the center of the window.

Starting the Clock and Running the Application:

The time() function is called to start updating the clock.

root.mainloop() runs the Tkinter event loop to keep the window open.

Example Output

14:30:45 10 Mar 2025 PM

Contributing

Feel free to improve the UI or add more features like different time zones or custom themes.




                                                                  2. SIMPLE-TEXT-EDITOR
Simple Text Editor

Overview

This is a simple text editor built using Python and Tkinter. It allows users to create, open, edit, and save text files with an easy-to-use graphical interface.

Features

Create a new file: Clears the text area for a new document.

Open an existing file: Loads a .txt file into the text editor.

Save the current file: Saves the content as a .txt file.

Exit the application: Closes the editor.

Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

Installation & Usage

Clone or download the script.

Run the script using:

python text_editor_app.py

Use the menu options to create, open, edit, and save files.

Customization

You can modify the font style and color by changing the font and fg attributes in the Text widget.

To add more features like dark mode or search functionality, modify the existing functions accordingly.

License

This project is open-source and free to use for educational purposes.







                                                                            3. Restaurant-Ordering-System
This is a simple Python-based restaurant ordering system that allows customers to order items from a predefined menu. The program presents the menu with item names and their corresponding prices, takes user input to select items, and calculates the total bill based on the selected items. It also allows the user to add another item to their order if they wish.

Features

Displays a predefined restaurant menu with item prices.

Takes user input for selecting an item.

Validates the availability of the selected item.

Allows the user to add a second item.

Calculates and displays the total amount to be paid.

Installation

No special installation is required. The script runs directly in Python. Ensure you have Python installed on your system.

Usage

Run the Python script.

The menu will be displayed.

Enter the name of the item you want to order.

The system will confirm whether the item is available.

You will be asked if you want to order another item.

If you choose 'Yes,' enter the second item's name.

The system will calculate and display the total bill.

Example Output

::::::::::::: WELCOME TO MY RESTAURANT ::::::::::::: Recipes of our restaurant :- pizza : 50; Pasta : 40; Burger : 50; Egg_Roll : 40; Biriyani : 150; Salad : 50; Butter_Chiken : 120; Mutton_Kosha : 170; Momo : 70; Chole_Bature : 110;

Enter the name of the item you want to order = Burger Your item "Burger" has been added to your order. Do you want to add another item? (Yes/No) Yes Enter the name of the second item = Momo Item "Momo" has been added to your order. The total amount of ordered items to pay is: 120

Contributing

Feel free to fork this repository and submit pull requests for improvements.

License

This project is open-source and available under the MIT License.  
   
      
