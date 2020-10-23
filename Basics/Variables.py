#Variables

#Variabels are used to stor data values in python
#They are actually created the moment you assign a value to them meaning that you do not need to declare them with any type or such

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#String variables can be declared either by using single or double quotes

x = "John"
# is the same as
x = 'John'

#Variable name rules in python 
"""
A variable name must start with a letter or the underscore character

A variable name cannot start with a number

A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

Variable names are case-sensitive (age, Age and AGE are three different variables)

"""

#Python allows you to assign multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Global Variables
"""
a variable created outside a function or block of code is a global variable 
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

"""
unlike java if you create a variable inside a function with the same name as a global variable you wont get and error instead it will focus on the varibale in the block of code 
"""

def myfunc2():
  x="fun"  
  print("python is",x)  

myfunc()
myfunc2()
print("Python is ",x)

#Global Keyword
#You can make a global variable inside a function by using the global keyword

def myfunc3():
    global g
    g = "amazing"

myfunc3()
print(g)

##IF YOU WANT TO CHANGE THE VALUE OF A GLOBAL VARIABLE PLACE THE GLOBAL KEYWORD BESIDE IT