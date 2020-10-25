#Conditionals

"Python conditionals are pretty much like java and javascript the operators are relatively the same and function in the same way"

"Python relies on indentation to to define scope so this must be used in python to start an if"
if 2>1:
    print("true")

"Elif is pretty much like else if in other languages meaning if the previous conditions werent true try this one"

a=33
b=33
if a>b:
    print("a is greater than b")
elif a==b:
    print("there the same")


"else statements are the same for anything that isnt caught"

"python allows for short hand if statements"
if a==b: print("The same again")

"Also yoyu can do a do a short hand if else      [expression condtion else expression]  you can do multipple of these in one line "
print("im right") if a==b else print("im wrong")

#These short hand expressions are known as ternary expressions

"In python instread of using && || you use and & or for logical operations"

"If's should not be empty but if you need it to be empty use the pass keyword"
if a<b:
    pass