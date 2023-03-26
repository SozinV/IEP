from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

current_file = None

def new_file():
    global current_file
    text.delete(1.0, END)
    current_file = None

def save_file():
    global current_file
    if not current_file:
        current_file = asksaveasfilename(defaultextension=".iep",
                                    filetypes=[("Package Files", "*.iep"), ("All Files", "*.*")])
        if not current_file:
            return
    with open(current_file, "w") as f:
        f.write(text.get(1.0, END))

def open_file():
    global current_file
    current_file = askopenfilename(defaultextension=".iep",
                                    filetypes=[("Package Files", "*.iep"), ("All Files", "*.*")])
    if not current_file:
        return
    text.delete(1.0, END)
    with open(current_file, "r") as f:
        text.insert(1.0, f.read())

root = Tk()
root.title("IEP Editor")
root.iconbitmap(r"C:\Users\jowel\Downloads\2312983.ico")
root.wm_iconbitmap(r"C:\Users\jowel\Downloads\2312983.ico")

text = Text(root)
text.pack(expand=True, fill=BOTH)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
