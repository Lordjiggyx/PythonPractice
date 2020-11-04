#Python Variables

"""
Python does not actually have any privtae member or variable keyword in python it is done using two underscores
(__) can be placed at the beginning of any variable or method that needs to be private 
"""

"Example 1"

class maincalss:
    __privatevariable= 2020
    
    def __privateMethod(self):
        print("Here i'am inside a private method")

    def insideClass(self):
        print("Private Variable", maincalss.__privatevariable)
        self.__privateMethod()


foo = maincalss()
foo.insideClass()

"""
As we can see a class was made with a priavte variable along with a private method both have underscores
They can be accessed ONLY from inside the class they belong to so they cannot be called seperately
But they can not be accessed from outside the class

if we call the private method on it's own we get an error indicating that the method itself is hidden
"""

foo.__privateMethod()

"""
You can use a single underscore as well this is actually different and indicates that a variable is protected 
this prevents it from being accessed from being accessed unless it is from within the subclass doesnt really make mucch of a difference
"""