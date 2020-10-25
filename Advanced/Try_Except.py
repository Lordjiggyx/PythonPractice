#Exception Handling

"We can use try catchs to handle exceptions"
"They try a block of code and then hadnle anything if an error occurs"
"Try execpt is like try catches in java "

try:
    print(X)
except:
    print("x does not exist")

"You can try multiple exceptions"
try:
    print(Y)
except NameError:
    print("Y does not exist")
except:
    print("somwthing unknown happended")

"you can use else in a try except as well"

"Finally is ran regardless of an error or not"
try:
    print(A)
except NameError:
    print("Y does not exist")
finally:
    print("Done")

"You can raise execeptiosn in your code for any condition using the raise and exceprion keywords"

x = -1

if x <0:
    raise Exception("Number must be > 0")