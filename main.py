import tkinter as tk
import subprocess
import os

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="Program Runner")
label_a.pack()

frame_a.pack()

python_cmd = "python"
pip_cmd = "pip"
use_venv = os.path.exists("myenv")
if use_venv:
    python_cmd = "./myenv/bin/python"
if use_venv:
    pip_cmd = "./myenv/bin/pip"

init_command = [pip_cmd, "install", "-r", "requirements.txt"]
commands = [
    [python_cmd, 'scr1.py'],
    [python_cmd, 'scr2.py'],
]

label_output = tk.Label(master=frame_a, text="")
label_output.pack()
label_error = tk.Label(master=frame_a, text="")
label_error.pack()


def run_command(cmd):
    output, error = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True).communicate()
    label_output.config(text=output)
    label_error.config(text=error)


# create a button to install requirements
button = tk.Button(window, text=f"Run {' '.join(init_command)}", command=lambda: run_command(init_command))
button.pack()

# create a button for each command
for command in commands:
    button = tk.Button(window, text=f"Run {' '.join(command)}", command=lambda x=command: run_command(x))
    button.pack()

window.mainloop()
