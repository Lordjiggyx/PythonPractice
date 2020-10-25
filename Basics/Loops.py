#Loops

"Pyton uses 2 loops while and if loops"

#While
"while loops are used to execute a statment as long as a condition is true"

i=1
while i<6:
    print(i)
    i+=1

"We can use the break keyword to stop a while loop even if teh condiotn is treu"
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

"we can use the continue keyword to stop the current iteration and continue with the next"
a = 0 

while a<6:
    a+=1
    if a==3:
        continue
    print(a)

#For

"for loops are used to iterate over a sequence for works more like an iterator for collections"
"Apart from the change in syntax loops work the same as they would in java and javascript"
fruits = ["banana" , "apple" , "orange"]
for x in fruits:
    print(x)

"For loops can also use the continue break and pass keywords like while loops"

"The range method can be use to specify how many times you want to iterate through a block of code"
for x in range(6):
    print("hello")
"This actually goes from 0->5 6 is not included"

"By adding anothe parameter you can alter the start and end of iterations"
for x in range(0,2):
    print("bye")
"0->1"

"by adding a third parameter you can change the increment sequence"
for x in range(0,10,2):
    print(x+1)
