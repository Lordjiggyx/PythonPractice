#Getters and Setters in classes


"""
The way to create getters and setter is differnet in python you can't just write the get and set method it dont work like that 

In python you use what is know as properties

To use a property you must use the @property annotation in front of the method you want to use to return the attribute and the <variableName>.setter for the method you want to use to set the attribute
"""

class P:
    def __init__(self,x):
        self.x = x
    
    #This is the getter method
    @property
    def x(self):
        return self.__x

    #This is the setter method
    @x.setter
    def x(self,x):
        if x<0:
            self.__x = 0
        elif x>1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(1000)
print(p1.x)

p2 =P(-12)
print(p2.x)

p3 = P(20)
print(p3.x)