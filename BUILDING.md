<h1>Building the Symbolic Link Generator</h1>

<p>This document provides step-by-step instructions on how to build the Symbolic Link Generator application for different operating systems.</p>

<h2>Prerequisites</h2>

<ul>
  <li>Python 3.6 or above</li>
  <li>PyInstaller</li>
  <li>Setuptools</li>
  <li>Tkinter library</li>
</ul>

<h2>Installation of Dependencies</h2>

<p>Before you start, make sure all dependencies are installed. You can install them by running:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<h2>Building the Executable</h2>

<p>Once all the prerequisites are installed, you can build the executable with PyInstaller. PyInstaller will package the Python script and all its dependencies into a single executable file.</p>

<h3>For Windows:</h3>

<p>Open a terminal in the project directory and run the following command:</p>

<pre><code>pyinstaller --onefile --windowed main.py
</code></pre>

<h3>For macOS:</h3>

<p>Open a terminal in the project directory and run the following command:</p>

<pre><code>pyinstaller --onefile --windowed --icon=app.icns main.py
</code></pre>

<h3>For Linux:</h3>

<p>Open a terminal in the project directory and run the following command:</p>

<pre><code>pyinstaller --onefile --windowed main.py
</code></pre>

<h2>Output</h2>

<p>The built executable will be located in the "dist" folder which PyInstaller creates in the project directory. You can now distribute this file to users who want to use the Symbolic Link Generator application without having to install Python or any dependencies.</p>
