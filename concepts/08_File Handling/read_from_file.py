file = open("Name.txt" , 'r')

content = file.read()
print("File content\n")
print(content)

content1 = file.readline()
content2 = file.readline()
print("File content\n")
print(content1)
print(content2)

contents = file.readlines()
print("File content\n")
for content in contents:
         print(content, end='Thank you')


file.close()