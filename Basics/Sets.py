#Sets

"To create a set you must use {} bracktes"
thisset = {1,2,3}
print(thisset)

"To access an item you must loop through the set the same way you would a list"
for x in thisset:
    print(x)

"To check if something is in a set it's the same as a list"

"To add a single object to a set use the .add() method"
thisset.add(4)
print(thisset)

"to add multiple values use the .update method and psas in values in [] brackets"
thisset.update([6,7,8])
print(thisset)

"Getting the length is the sane just use len()"

"to remove an item use the .remove() or discard"
thisset.remove(1)
print(thisset)

thisset.discard(3)
print(thisset)

".pop() will remove the last item"
".clear() will empty the set"
".del will delete the set"

" to join 2 sets use .union() method this method returns a new set with all items from both sets "
newset={10,12,13}
union =newset.union(thisset)
print(union)

".update can join two sets but instead this takes all items from set one and inserts it into set 2"
newset.update(thisset)
print(newset)