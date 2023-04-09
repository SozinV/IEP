import tkinter as tk
from tkinter import filedialog, ttk
import os
from tkinter import filedialog, simpledialog, ttk


# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("IEP Editor")
root.iconbitmap(r"C:\Users\jowel\Downloads\2312983.ico")

# Define functions for the file menu commands
def open_file():
    file_path = filedialog.askopenfilename(
        initialdir="/", title="Open File", filetypes=(("Package Files", "*.iep"), ("Package Files", "*.iep*"))
    )
    if file_path:
        with open(file_path, "r") as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, file.read())

def save_file():
    if text_editor.get("1.0", "end-1c"):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".iep", filetypes=(("Package Files", "*.iep"), ("Package Files", "*.iep*"))
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_editor.get("1.0", tk.END))


def refresh():
    text_editor.delete(1.0, tk.END)

def cut():
    text_editor.event_generate("<<Cut>>")

def copy():
    text_editor.event_generate("<<Copy>>")

def paste():
    text_editor.event_generate("<<Paste>>")

def undo():
    text_editor.event_generate("<<Undo>>")

def find():
    search_term = tk.simpledialog.askstring("Find", "Enter search term:")
    if search_term:
        search_start = text_editor.search(search_term, "1.0", tk.END)
        if search_start:
            search_end = f"{search_start}+{len(search_term)}c"
            text_editor.tag_add("search", search_start, search_end)
            text_editor.tag_config("search", background="yellow")
            text_editor.mark_set("insert", search_start)
            text_editor.focus()

def replace():
    search_term = tk.simpledialog.askstring("Replace", "Enter search term:")
    if search_term:
        replace_term = tk.simpledialog.askstring("Replace", f"Replace {search_term} with:")
        if replace_term:
            content = text_editor.get(1.0, tk.END)
            new_content = content.replace(search_term, replace_term)
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, new_content)




def fill_treeview(tree, node):
    path = tree.set(node, "fullpath")
    if os.path.isdir(path):
        for subnode in2 os.listdir(path):
            subpath = os.path.join(path, subnode)
            if os.path.isdir(subpath):
                tree.insert(node, "end", text=subnode, open=False, values=[subpath], tags=("directory",))
                fill_treeview(tree, subnode)
            else:
                tree.insert(node, "end", text=subnode, values=[subpath], tags=("file",))
    else:
        tree.insert(node, "end", text=node, values=[path], tags=("file",))
    
    # Set the value of the "fullpath" data in the first column of the treeview item
    tree.set(node, "#0", path)



def show_documentation():
    root.clipboard_append("https://www.example.com/documentation")

def send_feedback():
    root.clipboard_append("https://www.example.com/feedback")

# Create a paned window
paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Create a file explorer on the left


file_explorer = ttk.Treeview(paned_window)
fill_treeview(file_explorer, "")
paned_window.add(file_explorer)

# Create a text editor on the right
text_editor = tk.Text(paned_window, wrap="word")
text_editor.configure(bg="#1e1e1e", fg="white") # Set background and text color
paned_window.add(text_editor)

# Create the menu bar
menu_bar = tk.Menu(root)

# Create the file menu
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Find", command=find)
edit_menu.add_command(label="Replace", command=replace)
edit_menu.add_command(label="Refresh", command=refresh)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=False)
help_menu.add_command(label="Documentation", command=show_documentation)
help_menu.add_command(label="Send Feedback", command=send_feedback)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()