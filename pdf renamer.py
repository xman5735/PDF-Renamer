import tkinter as tk
from tkinter import filedialog
import os

def choose_pdf():
    # Open file dialog to choose PDF
    file_path = filedialog.askopenfilename(initialdir = "/home/user/Documents", title = "Select file", filetypes = (("PDF files", "*.pdf"), ("all files", "*.*")))

    # Split the file path to get the directory and file name
    global dir_name, file_name
    dir_name, file_name = os.path.split(file_path)

    # Set the text of the file name label to the chosen file name
    file_name_label["text"] = file_name

def rename_pdf():
    # Get the new name from the text box
    new_file_name = entry.get()
    
    # Rename the file
    os.rename(os.path.join(dir_name, file_name), os.path.join(dir_name, new_file_name))
    
    # Update the file name label with the new name
    file_name_label["text"] = new_file_name

def choose_save_location():
    # Open file dialog to choose save location
    global dir_name
    dir_name = filedialog.askdirectory(initialdir = "/home/user/Documents", title = "Select save location")

# Create the main window
root = tk.Tk()
root.title("Rename PDF")

# Add a button to choose the PDF
choose_pdf_button = tk.Button(root, text="Choose PDF", command=choose_pdf)
choose_pdf_button.pack()

# Add a label to display the file name
file_name_label = tk.Label(root, text="No file selected")
file_name_label.pack()

# Add a text box for the new name
entry = tk.Entry(root)
entry.pack()

# Add a button to submit the new name
rename_pdf_button = tk.Button(root, text="Rename PDF", command=rename_pdf)
rename_pdf_button.pack()

# Add a button to change the save location
change_location_button = tk.Button(root, text="Change Save Location", command=choose_save_location)
change_location_button.pack()

# Start the main loop
root.mainloop()
