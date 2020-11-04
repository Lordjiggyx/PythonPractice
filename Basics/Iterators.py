#Iterators 

"""
An iterator is an object that contains a countable number of values or an object that can be traverses through

An iteratror in python is an object with 2 methods __iter__ & __next__()

Any python collection can be iterated upon and have an iter method used to get an iterator from them
"""

mytuple = ("apple" , "bannana" , "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


"Strings can also be iterated upon using the iter method"

mystr = "banana"
stringIter = iter(mystr)

print(next(stringIter))
print(next(stringIter))
print(next(stringIter))


"You can create your own iterator but they must implement both the next and iter methods"

class myNumbers:
    #A variable called a has been created and set to = 1 the iter method returns this
    def __iter__(self):
        self.a = 1
        return self
    #The next method itmplemnets how it traverses to the next element in this case a gets incremented by 1 then returned
    def __next__(self):

        #To stop the iterator from going on infintely we can use the StopIteration statement in an if statement
        if self.a<=5:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

        

#Iteraror created
mclass = myNumbers()
myiter = iter(mclass)

#The iterator next method is called 5 times meaning that it will increment up until 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#Iteraror stops after the 5th call
print(next(myiter))
print(next(myiter))
print(next(myiter))
l