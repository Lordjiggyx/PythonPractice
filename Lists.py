#Collections
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

"""
#List

"To create a list you use [] brackets each element seperated by a commma"

mylist= ["tomi" , 2 , "IS", 3, "Too cool"]
print(mylist)

"To access an indiviual element you can use number to refer to the index"
print(mylist[2])

"Negative indexing works also to do this use - followed by the number to go in the reverse direction"
print(mylist[-1])

"Range of indexes can be obtained by specifying the index at the start until the index you want to get to seprated by a colon not including the last number"
print(mylist[1:3])

"If you leave the start number out it will start from the 1st number until the element specified"
print(mylist[:3])

"If you leave the end number out it will start from the the element specified until the end"
print(mylist[1:])

"Changing the value of an element in python is like java you specidy the index ands then change it"
mylist[1] = 3
print(mylist)

"To loop througha list you can use a for loop just like java the only difference is you use the in keyword "
for x in mylist:
    print(x)

"To check if an item exixst you can use an if along with the in keyword"
if "tomi" in mylist:
    print("tomi is in this list")
else:
    print("cant find tomi")

"To get the length of a list you can use len"
print(len(mylist))

"To add and item you can use the append() method"
mylist.append("lauren")
print(mylist)

"To add an item at a certain index use the insert method along with the index of where you want to insert the item"
mylist.insert(1,"bob")
print(mylist)


"""
DELETING

remove() removes a specified item
pop() removed the last item in the list if the index is not provided
del()removes the specified index or it can delete the list altoghter if no index is specified
clear() will empty the list

"""
mylist.remove("tomi")
print(mylist)

mylist.pop()
print(mylist)

del mylist[0]
print(mylist)

mylist.clear()
print(mylist)

del mylist
#print(mylist)

"To copy a list you must use the .copy method or you can use the list cmetod"
mylist= ["tomi" , 2 , "IS", 3, "Too cool"]
thislist = mylist.copy()
anotherlist = list(mylist)
print(thislist)
print(anotherlist)

"To join 2 lists just use the + operator or you can use the extend method"
lastlist = mylist + thislist
print(lastlist)

lastlist.extend(anotherlist)
print(lastlist)

"The list constructor can be used to create a list useing double normal brackets"
newlist = list((2,3,4,5))
print(newlist)

"There are a lot of more methods you can find em in the reference folder"