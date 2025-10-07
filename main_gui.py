import tkinter as tk
from tkinter import messagebox
from threading import Thread
import subprocess
import os

# Resolve paths dynamically
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TTS_SCRIPT = os.path.join(CURRENT_DIR, "Tts.py")
HAND_MOUSE_SCRIPT = os.path.join(CURRENT_DIR, "Hand_Virtual_Mouse.py")
EYE_MOUSE_SCRIPT = os.path.join(CURRENT_DIR, "Eye_Mouse.py")

# Utility to run scripts
def run_script(script_path):
    if not os.path.isfile(script_path):
        messagebox.showerror("Error", f"Script not found: {script_path}")
        return
    try:
        subprocess.Popen(["python", script_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run {script_path}:\n{e}")

def stop_script():
    try:
        # Kill all Python processes
        os.system("taskkill /f /im python.exe")
        messagebox.showinfo("Success", "Stopped all scripts")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop scripts:\n{e}")

# Launch functions

def launch_tts():
    Thread(target=run_script, args=(TTS_SCRIPT,)).start()


def launch_hand_mouse():
    Thread(target=run_script, args=(HAND_MOUSE_SCRIPT,)).start()

def launch_eye_mouse():
    Thread(target=run_script, args=(EYE_MOUSE_SCRIPT,)).start()

# Main GUI
def main_gui():
    root = tk.Tk()
    root.title("Virtual Assistant GUI")
    root.geometry("500x500")
    root.resizable(False, False)

    tk.Label(root, text="Virtual Assistant Control Panel", font=("Arial", 16)).pack(pady=20)

    
    # TTS
    tk.Label(root, text="Text-to-Speech", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Launch", command=launch_tts, width=15, bg="green", fg="white").pack()

    # Hand Virtual Mouse
    tk.Label(root, text="Hand Virtual Mouse", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Launch", command=launch_hand_mouse, width=15, bg="green", fg="white").pack()

    # Eye-Controlled Mouse
    tk.Label(root, text="Eye-Controlled Mouse", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Launch", command=launch_eye_mouse, width=15, bg="green", fg="white").pack()

    # Stop All Scripts
    tk.Label(root, text="Stop All Scripts", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Stop All", command=stop_script, width=15, bg="red", fg="white").pack()

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    main_gui()