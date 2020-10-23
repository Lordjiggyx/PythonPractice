#Data Types

"""
Python has multiple data types

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

"""

#To get the data type of a variable use the type() method

x=5
print(type(x))

#Eaxh data type has a constructor that you can use to set it
x=float(20.5)
print(type(x))

#Type conversion
#you can actuallky use the construcors of datatypes in order to concert them

x = 1    # int
y = 2.8  # float

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

print(type(a))
print(type(b))


#Casting
"""
Sometimes you may want to specify a variable type on a variable this canb be done with casting

This is done by using the datatype constructor
"""

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'