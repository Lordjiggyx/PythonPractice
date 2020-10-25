#Functions

"A function is a block of code that runs when its called"
"functions the same as it would in java and js"

"To create a function you must use the def keyword followed by the name and parentheses"
def my_function():
    print("hello world")

"functions are called in the same way"
my_function()

"in terms of arguments and parameters its generally the same however there are some special cases"

"Arbitary arguments are used if you do not know how many arguments will be passed into a function use *folloewed by the parameter this means a tuple will be received and accesed accordingly"
def my_kids(*kids):
    print("hello", kids[2])

my_kids("tomi" , "tobi","temi","tami")

"You can also send arguments with the key = value syntax"
def youngest(chilld1 , chilld3 , child2):
    print("The youngest child is", child2)

youngest(chilld1="tim" , child2="tom", chilld3="bob")

"Like arbitary arguments you can do the same with keyword arguments all you have to do is but ** followed by the parameter this means the function will get a dictionary"
def las_name(**kids):
    print("The last name is ", kids["fname"],kids["lname"])

las_name(fname="Tomi", lname="Ilori")

"You can pass in a default value as a paramter by just assigning it in the method"
def nationalty(country="Ireland"):
    print("Im from", country)

nationalty()
nationalty("UK")   

"A list can passed into a function"
"functions can return values like functions in other programming lnaguages"