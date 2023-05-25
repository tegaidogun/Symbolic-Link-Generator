import os
import sys
import subprocess

def build():
    # Detect the operating system
    platform = sys.platform

    # The PyInstaller command for Windows
    if platform == "win32":
        command = ['pyinstaller', '--onefile', '--windowed', '--icon=icon.png', '--name=Symbolic Link Generator', 'main.py']
    # The PyInstaller command for macOS, including the icon file
    elif platform == "darwin":
        command = ['pyinstaller', '--onefile', '--windowed', '--icon=icon.png', '--name=Symbolic Link Generator', 'main.py']
    # The PyInstaller command for Linux
    elif platform == "linux" or platform == "linux2":
        command = ['pyinstaller', '--onefile', '--windowed', '--icon=icon.png', '--name=Symbolic Link Generator', 'main.py']
    else:
        print("Unsupported platform:", platform)
        return

    # Run the PyInstaller command
    subprocess.run(command)

if __name__ == "__main__":
    build()
