#Strings

#Strings are usually surrounded with single/double quotation marks
x = "Hello world"

#You can create multiline strings by using a triple quotation
a = """ lorem 
ipsum
dolor 
sit amet
"""

print(a)

#Acessing strings

"""To access elements of a string you can use square brackets"""

print(x[4])

#Slicing

"""
You can return a range of characters by using slice syntax
You just specify the start index and the end index seperated by a colon to return a part of a string this must be done in sqaure brackets"""
print(x[0:5])


#Negative indexing
"""
Use negative indexesd to start the slice from the end of the string aka going backwards
the range that it ends at does not include the start number
"""
print(x[-5:-3])

#Length
"""
Use the len() method to get the length of the string
"""

print("This string is ",len(x) , " cahratcers long")

#Check String
"""
To check if a phrase or character is present in a string we can use "in" or "not in" keywords
"""

txt = "Heloo my name is tomi"
a= "tomi" in txt
b = "Travis" in txt

print(a)
print(b)

#String Formatting
"""
We can combine strings and number by using the format method 

This method takes in the argyments and formats them and places them in the string where the placeholders are{}
"""

quantity=3
itemno=5
price=32.99
order = "I want {} pieces of item {} for {} euro"
print(order.format(quantity,itemno,price))

"""
You can actually specify what arguments are used in each set of curly brackets by using numbers
"""
order = "I want {1} pieces of item {0} for {2} euro"
print(order.format(quantity,itemno,price))

#There is a list of string methods like loads you made a small list in the Reference folder so go to that to have a look