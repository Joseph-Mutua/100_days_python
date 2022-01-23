# Python has functions for creating, reading, updating and deleting files

# Open a file
myFile = open("myfile.text", "w")

# Get some info
print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed)
print("Openig mode: ", myFile.mode)

# Write to file
myFile.write("I love Python")
myFile.write(" and Javascript")

# Read form file
myFile = open("myfile.text", "r+")
text = myFile.read(100)
print(text)