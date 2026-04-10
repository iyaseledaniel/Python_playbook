# working with file in python

file = open("python_notes.txt","w")
file.write("Hello World, we are working with Python files and this is our first write statement to a file")
file.close()

file = open("python_notes.txt","r")
data = file.read()
print(data)
file.close()