'''
Purpose: The os module provides a portable way of interacting with the operating system, including functions for file operations, directory operations, and process management.
'''

'''
1. Working with Files and Directories:
os.getcwd(): Returns the current working directory as a string.
os.chdir(path): Changes the current working directory to the given path.
os.listdir(path='.'): Returns a list containing the names of the entries in the directory given by path.
os.mkdir(path): Creates a directory named path.
os.makedirs(path): Creates a directory named path recursively.
os.remove(path): Removes the file path.
os.rmdir(path): Removes the directory path.
os.rename(src, dst): Renames the file or directory src to dst.
2. Path Manipulation:
os.path.join(path1[, path2[, ...]]): Join one or more path components intelligently.
os.path.abspath(path): Return a normalized absolutized version of the pathname path.
os.path.exists(path): Return True if path refers to an existing path.
os.path.isdir(path): Return True if path is an existing directory.
os.path.isfile(path): Return True if path is an existing regular file.
os.path.splitext(path): Split the pathname path into a pair (root, ext) such that root + ext == path.
3. Process Management:
os.system(command): Execute the command in a subshell.
os.spawn*: Functions for replacing the current process.
os.fork(): Fork a child process.
4. Miscellaneous:
os.environ: A mapping object representing the string environment.
os.getpid(): Returns the current process id.
os.getlogin(): Returns the name of the user logged in.
'''


import os

import os

# Getting Current Working Directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Creating a Directory
new_directory = "new_directory"
os.mkdir(new_directory)
print("Directory created:", new_directory)

# Listing Files in a Directory
files = os.listdir()
print("Files in current directory:", files)

# Joining Path Components
path1 = "/path/to"
path2 = "file.txt"
full_path = os.path.join(path1, path2)
print("Joined path:", full_path)

# Checking if a Path Exists
path = "file.txt"
if os.path.exists(path):
    print("Path", path, "exists.")
else:
    print("Path", path, "does not exist.")

# Removing a File
file_to_remove = "file_to_remove.txt"
os.remove(file_to_remove)
print("File removed:", file_to_remove)

# Getting the Process ID
pid = os.getpid()
print("Process ID:", pid)

