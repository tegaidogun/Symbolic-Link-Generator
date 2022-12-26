import os
import tkinter as tk
from tkinter import filedialog, messagebox


def fix_slash(path):
    if isinstance(path, str):
        if path[-1] != "/":
            path = path + "/"
    return path

def validate_path(path):
    path = fix_slash(path)
    if isinstance(path, str):
        while not os.path.exists(path):
            answer = messagebox.askretrycancel("Question",
                                               "The directory picked was invalid. Do you want to try again?")
            if answer:
                print("It passed")
            else:
                break
                path = None
    else:
        for dir in path:
            while not os.path.isfile(dir):
                answer = messagebox.askretrycancel("Question",
                                                   "One of the directories/ files picked was invalid. Do you want to "
                                                   "try again?")
                if answer:
                    print("It passed")
                    break
                else:
                    path = None
                    break
    return path

class BrowseFolder:
    @staticmethod
    def folderpick(window_title):
        root = tk.Tk()
        root.withdraw()
        root.title(window_title)
        folder_path = filedialog.askdirectory(title=window_title)

        return validate_path(folder_path)

    @staticmethod
    def filepick(window_title):
        root = tk.Tk()
        root.withdraw()
        root.title(window_title)
        file_paths = filedialog.askopenfilenames(title=window_title)

        print (file_paths)
        return validate_path(file_paths)

