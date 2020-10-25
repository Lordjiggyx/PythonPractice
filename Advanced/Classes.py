#Classes & Objects

"Like java python uses OOP"

"To create a class use the class keyword"
class Myclass:
    x=5

"To create an object we can use the class name assgining it to a new variable"
p1 = Myclass()
print(p1.x)


"The __init__ function is like a constructor function in java, this is executed when the class is being initiated, essentially it can be used to assign values"
class Person:
    def __init__(self , name , age):
        self.name =name
        self.age = age

"Creating an object and passing in the name and age values"
p1 = Person("Tomi" , 21)

print(p1.name)

"You can also have methods in python classes they take in self to refer to the variables in the constructor"
class nicePerson:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("Hello my name is", self.name)


np = nicePerson("Tomi",21)
np.greeting()

"The self parameter itself is a refernece to the current instance of the calss almost the same as this in java however it can be called anything but it must be the first parameter of any method in the class"
"To delete an object just use the del keyword"
"if you wnat and empty calss use the pass keyword"

#Inheritance
"Python allows for inheritance like other oop languages"

"1st you create the parent class"

class Parent:
    def __init__(self , name , age):
        self.name =name
        self.age = age

    def printname(self):
        print(self.name)

"then you create the child class you send the paret calss as a parameter and use the pass keyword if you do not want to add any more properteos or methods"

class child(Parent):
    pass

x= child("Tomi" , 21)
x.printname()

"__init__ can be added to a child calss as well when this is added the child wil no longer inherit the parents init funciton as it overides the parent one"
"To keep the inheritance you must call the parents init method as a property"

class Student(Parent):
    def __init__(self,fname , lname ,age):
        Parent.__init__(self,fname,age)

a = Student("Bob","Whitney",21)
print(a.age)
a.printname()


"Its better to use the super() method asthis just inherits all the methods and properties when using super() you do not need to call self"
"you can then add properties and methods"

class newStudent(Parent):
    def __init__(self, fname , lname  , age, year):
        super().__init__(fname,age)
        self.graduationyear = year
        self.lname = lname

    def welcome(self):
        print("Welcome",self.name,self.age, "to the calss of", self.graduationyear)

    def last(self):
        print(self.lname)


b = newStudent("Tomi", "Ilori" , 21, 2020)
print(b.graduationyear)
b.printname()
b.welcome()
b.last()