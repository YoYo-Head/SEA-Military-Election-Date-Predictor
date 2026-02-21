import subprocess
import os

# Run this file to start the program
base_dir = os.path.dirname(os.path.abspath(__file__))

venvPath = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
scriptPath = os.path.join(base_dir, "src", "main.py")

subprocess.run([venvPath, scriptPath])