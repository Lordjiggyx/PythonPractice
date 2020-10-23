#Tuple

"To create a tuple you use normal brackets"
thistuple=(1,2,3,4)
print(thistuple)

"To get tuple items use a square bracket plus the index you want"
print(thistuple[1])

"negative indexing, ranges, looping through,getting the length, noinng with +, and checking if something is in the tuple is the same as lists"

"You are not meant to change tuple values but a workaround includes changing it ot a lisr and then changing what you want to change before changing it back to a tuple"
y = list(thistuple)

y[1]=5
"using the tuple constructor to change it back"
thistuple=tuple(y)

print(thistuple)

"To create a tuple with one item youi must put a comma after it"
newTuple=("apple",)
print(newTuple)

"You cannot remove itens from a tuple instead use del to delete the tuple altogether"