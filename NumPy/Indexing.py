#Indexing

import numpy as np

#1-D Arrays
"array indexing is the same as acessing an array element"
arr = np.array([1,2,3])

print(arr[0])

#2-D Arrays
"To access elements from a 2-d array we can use comma seperated integers representing the dimension and the index of the elements"
arr2 = np.array([[1,2,3],[4,5,6]])
print("2nd element on second dimension should be 5:",arr2[1,1]) 


#3-D Arrays
"To access elements from a 3-d array we can use comma seperated integers representing the dimension and the index of the elements"
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("3rd element of the second array of the second array should be 6:",arr3[1,1,2]) 

#Negative indexing
"Negative indexing works the same as it would with a normal array"
print("last element of 1st array in a 2-d array should be 3:", arr2[0,-1])