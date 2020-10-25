#module

"Modules are code libraries with functions in them to create a module save a function in another file with the .py extension "

"myModule.py"

"When the module has been created you can then call it using the import keyword"
import myModule

"You can then call the method"
myModule.greeting("Tomi")

"Varibales can be accessed from modules as well"
brand = myModule.car["Brand"]
print(brand)

"you can rename modules using the as keyword"
import myModule as mx

mx.greeting("Bob")

"You can use the dir() fucntion to print all the functions or varibales in a module"
import platform

x = dir(platform)
print(x)

"you can also specify waht you want to import from a module by using the keyword from"
from myModule import car

print(car)