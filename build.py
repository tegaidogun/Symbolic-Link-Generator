import os
import sys
import subprocess
import configparser

def create_desktop_file(executable_path, icon_path):
    # Define the path to the .desktop file
    desktop_file_path = os.path.join(os.path.dirname(executable_path), 'Symbolic Link Generator.desktop')
    # Define the content of the .desktop file
    content = {
        'Desktop Entry': {
            'Type': 'Application',
            'Name': 'Symbolic Link Generator',
            'Exec': executable_path,
            'Icon': icon_path,
            'Terminal': 'false'
        }
    }
    # Create a configparser object
    config = configparser.ConfigParser()
    # Add the content to the configparser object
    config.read_dict(content)
    # Write the content to the .desktop file
    with open(desktop_file_path, 'w') as configfile:
        config.write(configfile)

def build():
    # Detect the operating system
    platform = sys.platform

    # Define the output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'dist')

    # The PyInstaller command for Windows
    if platform == "win32":
        command = ['pyinstaller', '--onefile', '--windowed', '--icon=icon.png', '--name=Symbolic Link Generator', '--distpath', output_dir, 'main.py']
    # The PyInstaller command for macOS, including the icon file
    elif platform == "darwin":
        command = ['pyinstaller', '--onefile', '--windowed', '--icon=icon.png', '--name=Symbolic Link Generator', '--distpath', output_dir, 'main.py']
    # The PyInstaller command for Linux
    elif platform == "linux" or platform == "linux2":
        command = ['pyinstaller', '--onefile', '--windowed', '--name=Symbolic Link Generator', '--distpath', output_dir, 'main.py']
        # Run the PyInstaller command
        subprocess.run(command)
        # Define the path to the generated executable
        executable_path = os.path.join(output_dir, 'Symbolic Link Generator')
        # Define the path to the icon
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        # Create the .desktop file
        create_desktop_file(executable_path, icon_path)
    else:
        print("Unsupported platform:", platform)
        return

if __name__ == "__main__":
    build()
