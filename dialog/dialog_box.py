import tkinter as tk
from tkinter import ttk, filedialog
from symlink.symbolic_link_generator import GenerateSymbolicLink
import sys

class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.insert(tk.END, str)
        self.widget.see(tk.END)

    def flush(self):
        pass

class MyApp():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("600x400")
        self.window.title("Symbolic Link Generator")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)

        self.create_widgets()

    def create_widgets(self):
        # create frame to hold the widgets
        frame = ttk.Frame(self.window, padding="20")
        frame.pack(fill="both", expand=True)  # fill window

        # create Browse for Folder button
        self.browse_for_folder_button = ttk.Button(frame, text="Browse for Folder", command=self.browse_for_folder)
        self.browse_for_folder_button.pack(pady=10, ipadx=20, ipady=10)

        # create Browse for File(s) button
        self.browse_for_files_button = ttk.Button(frame, text="Browse for File(s)...", command=self.browse_for_files)
        self.browse_for_files_button.pack(pady=10, ipadx=20, ipady=10)

        # create a label for the text area
        log_label = ttk.Label(frame, text="Activities Log:")
        log_label.pack(pady=10)

        # create a text area to display the selected files or folders
        self.text_area = tk.Text(frame, width=70, height=10)
        self.text_area.pack(pady=10)

        # redirect stdout to text widget
        sys.stdout = TextRedirector(self.text_area)

    def browse_for_folder(self):
        GenerateSymbolicLink.symlink_directories()

    def browse_for_files(self):
        GenerateSymbolicLink.symlink_files()
