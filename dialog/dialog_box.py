import tkinter as tk
from symlink.symbolic_link_generator import GenerateSymbolicLink

class MyApp():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("300x200")
        self.window.title("Symbolic Link Generator")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)

        self.browse_for_folder_button = tk.Button(self.window, text="Browse for Folder", command=self.browse_for_folder)
        self.browse_for_folder_button.pack()

        self.browse_for_files_button = tk.Button(self.window, text="Browse for File(s)...", command=self.browse_for_files)
        self.browse_for_files_button.pack()

    def browse_for_folder(self):
        return GenerateSymbolicLink.symlink_directories()


    def browse_for_files(self):
        return GenerateSymbolicLink.symlink_files()
