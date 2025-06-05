import tkinter as tk  # Tkinter module is used to build graphical interface
from time import strftime



# Initialize the main window
root = tk.Tk()  
root.title("Digital Clock")



# Function to update time
def time():
    string = strftime('%H:%M:%S \n %d %b %Y %p')  # Fixed format string
    label.config(text=string)
    label.after(1000, time)



# Creating label to display the time

label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='yellow')  
label.pack(anchor='center')


# Call the time function to update the label
time()



# Run the Tkinter event loop
root.mainloop()


