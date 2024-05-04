
try:
    file = open("Name.txt", "r")
    content = file.read()
    print("File content:", content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()
