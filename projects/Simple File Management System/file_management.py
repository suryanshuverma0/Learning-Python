import threading

class FileSystem:
    def __init__(self):
        self.content = None
    
    def inputFromUser(self):
        data = input("Enter the data you want to write: \n")
        return data
    
    def writeToFile(self):
        data = self.inputFromUser()
        with open("file.txt", "w") as file:
            file.write(data)
    
    def readFromFile(self):
        with open("file.txt", "r") as file:
            self.content = file.read()
    
    def performReadWriteOperations(self):
        write_thread = threading.Thread(target=self.writeToFile)
        read_thread = threading.Thread(target=self.readFromFile)
        
        write_thread.start()
        read_thread.start()
        
        write_thread.join()
        read_thread.join()
        
        return self.content

# Usage
fs = FileSystem()
content = fs.performReadWriteOperations()
print("Content read from file:", content)
