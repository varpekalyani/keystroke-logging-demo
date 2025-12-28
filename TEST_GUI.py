import tkinter as tk

root = tk.Tk()
root.title("GUI TEST")
root.geometry("200x100")

label = tk.Label(root, text="Tkinter is working 👍")
label.pack(pady=20)

root.mainloop()
