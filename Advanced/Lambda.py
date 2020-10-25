#Lambda

"Lambda is a small funciton"
"lambad can take multiple arguments but only  have one expressions"

"lambda arguments : expression"

x = lambda a,b : a*b
print(x(2,10))

"Lambda is bet used when the are used inside another function"
def myfunc(n):
    return lambda a: a*n

myDoubler = myfunc(2)

print(myDoubler(11))