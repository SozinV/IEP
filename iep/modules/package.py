import os
import tkinter as tk
from tkinter import messagebox
import requests

class PackageInstaller:
    def __init__(self, filepath):
        self.filepath = filepath
        self.root = tk.Tk()
        self.root.withdraw()

    def execute(self):
        try:
            with open(self.filepath) as f:
                code = f.read()
            globals_dict = {}
            exec(code, globals_dict)
            package_name = globals_dict.get('name')
            package_author = globals_dict.get('author')
            package_version = globals_dict.get('version')
            package_directory = globals_dict.get('directory')
            if not os.path.exists(package_directory):
                os.makedirs(package_directory)
            package_url = globals_dict.get('url', '')
            if not package_url:
                raise ValueError('Package URL is not specified')
            package_filename = os.path.basename(package_url)
            package_filepath = os.path.join(package_directory, package_filename)
            r = requests.get(package_url, allow_redirects=False)
            open(package_filepath, 'wb').write(r.content)
            messagebox.showinfo("Success", f"{package_name} {package_version} by {package_author} has been installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Installation failed: {str(e)}")

if __name__ == '__main__':
    installer = PackageInstaller('path/to/package.iep')
    installer.execute()
