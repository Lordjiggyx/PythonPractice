#User Input

"User input is simple compared to java and javascriipt"
"You assign a varibale and use the input()methid following the question or prompt  "
username = input("What is your name ")
print(username)

"When python takes in numbers they are converted to string thus you need to convert them to numbers in order to perfrom mathematical ooperations on them"

def add2(a,b):
    result = a+b
    print(result)

num1 = input("Enter number 1 ")
num2 = input("Enter number 2 ")

num1 = int(num1)
num2 =int(num2)

add2(num1,num2)