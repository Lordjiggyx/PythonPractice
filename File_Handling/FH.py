#File handling 

#Python has several functions for creating,reading,updating and deleting files

"The key function for working with files in pythin is the opne() function"
"This function takes 2 parameters, filrname and mode, there are four different modes for opening a file"

"r - Read- Default values. Opens a file for reading, an error will occur if the file does not exist"
"a - Append - Opens a file for appending, this will create the file if it does not exist"
"w - Write - Opens a file for writing, this will create the file if it does not exist"
"x - Create - Creates the specfied file , returns an error if the file exists"

"You can also specify if you want the file to be handled as binary or text mode"
"t - text mode"
"b - binary mode"

"You cannot call the read() funciton more than once so use the seek method to reset the read cursor"

#Reading files

"To open a file use the opne() function"
f = open("File_Handling/demo.txt","r")

"read() is used to read the content of the file"
print(f.read())

"You can specify how many characters you want to return when the file has been read"
f.seek(0)
print(f.read(10))


"You can use readline() to return lines of a file"
f.seek(0)
print(f.readline())

"You can loop throiugh a file to display each line"
f.seek(0)
for x in f:
    print("Line:",x)

"You can use the .close() function to close a file when you are finished"
f.close()

#Wwriting to files

"To write to an existing file you must add a parameter to the open() function"
"a - will append to the end of the file"
"w - will overwrite any existing content"

#Appending
f = open("File_Handling/demo.txt","a")
f.write(" Now this file has more content")
f.close()

f = open("File_Handling/demo.txt","r")
print(f.read())
f.close()


#Overwriting
f = open("File_Handling/demo2.txt","w")
f.write(" Erased Everything")
f.close()

f = open("File_Handling/demo2.txt","r")
print(f.read())

#Creating

"To create a new file just call the open() function with one of the parameters x,a,w"
#f = open("File_Handling/demo3.txt","x")

#Deleting
"To delete a file you must import the os module and reun the os.remove() function"

import os
#os.remove("File_Handling/demo3.txt")

"Best thing to do is to check if the file exists before you delete it"

if os.path.exists("File_Handling/demo3.txt"):
    os.remove("File_Handling/demo3.txt")
else:
    print("The file does not exist")