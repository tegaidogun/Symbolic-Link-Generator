import PyInstaller.__main__
import os

package_name = "Symbolic-Link-Generator" # Name of your application
file_to_compile = "main.py" # Entry point of your application

PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--onefile',
    '--windowed',
    '--add-binary=%s' % os.path.join('dialog', '*.py;dialog'),
    '--add-binary=%s' % os.path.join('symlink', '*.py;symlink'),
    file_to_compile,
])
