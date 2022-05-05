# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
import os
from tkinter import filedialog

folder = filedialog.askdirectory()
print(folder)

file_name = input("Enter the name: ")
if file_name.endswith(".txt"):
    pass
else:
    file_name = file_name + ".txt"

file = os.path.join(folder, file_name)
file_mode = input("Enter the mode of the file: ")

if file_mode in ["a", "w", "w+", "r+", "r", "wb", "rb"]:
    pass
else:
    file_mode = "w"

with open(file, file_mode) as file_obj:
    file_obj.write("Hi chandan, Start learning Python Tkinter")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
