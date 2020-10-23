#use the print() method to display somthing in the terminal 
print("Hello World")

#Like java you can concatenate strings in this method
print("Hello" + " Tomi" + " welcome to python")

#If you want to concatenate numbers in a print() expression wrap the number in str()
#str is used to convert an object into a string
print("2+3 = " + str(2+3))

#Print can take in a anything regardless of the data type

#Print() is a method meaning it can take in it's own arguments each seprated with a comma what it does is that it calls str() on every argument treating it as a string and also adds a space between each atrgument
print("Tomi did you know that", "2 + 3 =", 5)

#You can pass in sep as an argument which stands for seperator this allows you determine how you want to join items in a print method or assign spaces

#sep comes between elements not around them so be able to account for this
print("hello" , "world" , sep="\n")
print("home","user","documents", sep="/")
print('node', 'child', 'child', sep=' -> ')

#We can use the end arguement in order to prevent linebreaks this argument dictates what we end the line with in this example you can see that after the first print happens ok comes on the same line showing that we ended the line with an empty space
print("Checking file progres....", end="")
print("ok")

#Sep and End can be used together 
print('Mercury', 'Venus', 'Earth', sep=', ', end=', ')
print('Mars', 'Jupiter', 'Saturn', sep=', ', end=', ')
print('Uranus', 'Neptune', 'Pluto', sep=', ')