import os, shutil
from dialog.subdir_dialog import BrowseFolder


def move_files(initial_directory, final_directory):
    print("Currently moving the documents...")
    if isinstance(initial_directory, str):
        for sub_dir in os.listdir(initial_directory):
            shutil.move(initial_directory + sub_dir, final_directory)
    else:
        for sub_dir in initial_directory:
            shutil.move(sub_dir, final_directory)
    print("Done moving the documents.")

def create_symlink_directory(initial_directory, final_directory):
    print("Currently making all the Symbolic Links...")
    for sub_dir in os.listdir(final_directory):
        os.symlink(final_directory + sub_dir, initial_directory + sub_dir)
    print("Done making the Symbolic Links.")

def create_symlink_files(files, final_directory):
    print("Currently making all the Symbolic Links...")
    for sub_dir in files:
        os.symlink(final_directory + sub_dir.partition("/")[-1], sub_dir)
    print("Done making the Symbolic Links.")

class GenerateSymbolicLink():
    @staticmethod
    def symlink_directories():
        initial_directory = BrowseFolder.folderpick("Select the directory containing the directories to symlink...")
        final_directory = BrowseFolder.folderpick("Select the directory where the symlinks should be placed...")
        move_files(initial_directory, final_directory)
        create_symlink_directory(initial_directory, final_directory)

    @staticmethod
    def symlink_files():
        initial_files = BrowseFolder.filepick("Select the directory containing the directories to symlink...")
        final_directory = BrowseFolder.folderpick("Select the directory where the symlinks should be placed...")
        move_files(initial_files, final_directory)
        create_symlink_files(initial_files, final_directory)



