#Slicing

"""
Slicning in pythin means taking elements from one given index to another given index

we pass slice instead if the index like the: [start:end]
we can also indicate the step like this: [start:end:step]

if start isnt passed it's 0
if end isnt passed it's the lenght of the array
if step isnt oassed its considered 1
"""

import numpy as np

#1-D Arrays

arr = np.array([1,2,3])

print(arr[0:])
print(arr[:2])
print(arr[0:1])

"You can negatively slice too"
print(arr[0:-1])


#2-D Arrays
"to slice 2-d arrays you specify the array and then the slice you want"
arr2 = np.array([[1,2,3,5,6],[4,5,6,7,8,9]])
print(arr2[1,1:]) 

