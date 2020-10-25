#Dictionary

"Creatiung a dictionary is like creating a json object they need keys and values "

thisdict = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":"1964"
}

print(thisdict)

"To access items in a dictionary you must refer to the key in square brackets"
print(thisdict["Model"])

"You can also use the .get() method making reference to the key"
print(thisdict.get("Brand"))

"To cahnge values you make reference to the key and reassign the items value"
thisdict["Model"] = "Fiat"
print(thisdict)

"Looping is realtively the same the only difference with dictionaries is that you can choose either the key or values to be acessed"

"Keys loop"
for x in thisdict:
    print(x)

"Values loop"
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

"Looping to get both key and values"
for x ,y in thisdict.items():
    print(x,y)

"Checking if somehting exists is the same"
"Getting the length is the same using the len() method"

"To add an item you create a key and assign a vlaue to it"
thisdict["colour"] = "red"
print(thisdict)

"To remove an item use the .pop method along with the key name"
thisdict.pop("colour")
print(thisdict)

"popitem() can be used to remove the last inserted item "

"del can be used to remove an item specified by key name"
del thisdict["Model"] 
print(thisdict)

"del can be used to delete a dictionary altogether when yoou do not specify the key name"

"clear() can be used to clear the dict"
"copying is the same you either use the .copy() method or use the dictionary function dict()"
"A new dictionary can be created b using the dict constrcutor too"
