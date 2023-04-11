import tkinter as tk
from tkinter import filedialog
import os
import git


class PackageInstaller:



    def __init__(self, root):
        self.root = root
        self.root.title("Package Installer")
        self.root.geometry("500x300")

        # Read Only
        entry = tk.Entry(root, width=50, state='readonly')


        # create labels and entries
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Author:").grid(row=1, column=0, sticky="w")
        self.author_entry = tk.Entry(self.root)
        self.author_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Version:").grid(row=2, column=0, sticky="w")
        self.version_entry = tk.Entry(self.root)
        self.version_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Directory:").grid(row=3, column=0, sticky="w")
        self.directory_entry = tk.Entry(self.root)
        self.directory_entry.grid(row=3, column=1)

        tk.Label(self.root, text="URL:").grid(row=4, column=0, sticky="w")
        self.url_entry = tk.Entry(self.root)
        self.url_entry.grid(row=4, column=1)

        # create install button
        tk.Button(self.root, text="Install", command=self.install).grid(row=5, column=0, columnspan=2, pady=10)

        # read package info from file
        self.read_package_info()

    def read_package_info(self):
        # open package info file
        filename = filedialog.askopenfilename(initialdir="./", title="Select a package file",
                                              filetypes=(("Package Files", "*.iep"), ("Extension Packs", "*.pak*"),("All files", "*.*")))
        if filename:
            with open(filename, "r") as f:
                # read and set package info
                for line in f:
                    key_value = line.strip().split(":")
                    if len(key_value) == 2:
                        key, value = key_value
                        if key == "name":
                            self.name_entry.insert(0, value)
                        elif key == "author":
                            self.author_entry.insert(0, value)
                        elif key == "version":
                            self.version_entry.insert(0, value)
                        elif key == "directory":
                            self.directory_entry.insert(0, value)
                        elif key == "url":
                            self.url_entry.insert(0, value)

    def install(self):
        # create package directory
        package_dir = self.directory_entry.get()


        # create package file
        package_info = os.path.join(package_dir, f"{self.name_entry.get()}_{self.version_entry.get()}.info")
        with open(package_info, "w") as f:
            f.write(f"name:{self.name_entry.get()}\n")
            f.write(f"author:{self.author_entry.get()}\n")
            f.write(f"version:{self.version_entry.get()}\n")
            f.write(f"directory:{self.directory_entry.get()}\n")
            f.write(f"url:{self.url_entry.get()}")
            git.Repo.clone_from(f'{self.url_entry.get()}', package_dir)
            repo = git.Repo(package_dir)
            repo.index.add([f'package_dir/logs/gitlogs.txt'])


        # Import Files from Git



        # show success message
        tk.messagebox.showinfo("Success", "Package installed successfully!")


# create root window
root = tk.Tk()

# create package installer window
my_installer = PackageInstaller(root)

# run main loop
root.mainloop()
