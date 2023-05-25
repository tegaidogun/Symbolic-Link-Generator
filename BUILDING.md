<h1>Building Symbolic Link Generator</h1>

<p>This document provides instructions on how to build Symbolic Link Generator for different operating systems. The build process may vary depending on the operating system and environment settings.</p>

<h2>General Requirements</h2>
<ul>
    <li>Python 3.6 or above</li>
    <li>Tkinter library</li>
    <li><code>setuptools</code> Python package</li>
    <li><code>PyInstaller</code> Python package</li>
</ul>

<h2>Building for Windows</h2>
<ol>
    <li>Ensure Python and pip are installed and available in your PATH.</li>
    <li>Install the required dependencies by running <code>pip install -r requirements.txt</code> in the command prompt.</li>
    <li>Run the build script with <code>python build.py</code>. The script will use PyInstaller to build the executable.</li>
    <li>The executable will be created in the <code>dist</code> directory.</li>
</ol>

<h2>Building for macOS</h2>
<ol>
    <li>Ensure Python and pip are installed and available in your PATH.</li>
    <li>Install the required dependencies by running <code>pip install -r requirements.txt</code> in the terminal.</li>
    <li>Run the build script with <code>python build.py</code>. The script will use PyInstaller to build the executable.</li>
    <li>The executable will be created in the <code>dist</code> directory.</li>
</ol>

<h2>Building for Linux</h2>
<ol>
    <li>Ensure Python and pip are installed and available in your PATH.</li>
    <li>Install the required dependencies by running <code>pip install -r requirements.txt</code> in the terminal.</li>
    <li>Run the build script with <code>python build.py</code>. The script will use PyInstaller to build the executable.</li>
    <li>The executable will be created in the <code>dist</code> directory.</li>
    <li>To add the application to your system menu, create a <code>.desktop</code> file:
        <ul>
            <li>Create a new file with the <code>.desktop</code> extension.</li>
            <li>Include the necessary information in the file, e.g.:
                <pre><code>[Desktop Entry]
                Type=Application
                Name=Symbolic Link Generator
                Exec=&lt;path_to_your_executable&gt;
                Icon=&lt;path_to_your_icon&gt;
                </code></pre>
            </li>
            <li>Make the .desktop file executable with <code>chmod +x &lt;your_desktop_file&gt;</code>.</li>
            <li>Place the .desktop file in the appropriate directory. If you want it to be accessible to all users, place it in <code>/usr/share/applications</code>. For user-specific access, place it in <code>~/.local/share/applications</code>.</li>
        </ul>
    </li>
</ol>

<h2>Troubleshooting</h2>

<p>If you encounter any issues during the build process, please refer to the <a href="https://github.com/your_repo/issues">issues page on GitHub</a>.</p>
