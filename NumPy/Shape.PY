#Shape

"The shape of an array is the number of elements in each direaction"
"You can use the shape attribute tahta returns a tuple with each index having the number of corresponding elements"

import numpy as np

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2.shape)


#Reshaping
"You can reshape an array to change it's shape, by changing the hsape we can add or remove dimensions or change the numbe rof elements in each dimension"
"To do this by using the reshape method"
"This method allows you to specify the dimensions and how many elements you want in each"

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

"Creates a 2-d array with 4 1-d arrays each with 3 elements"
newArr2d = arr1.reshape(4,3)
print(newArr2d)


"Creates a 3-d array with 2 2-d arrays each with 3 1-d arrays each with 2 elements"
newArr3d = arr1.reshape(2,3,2)
print(newArr3d)

"You can have an unkown dimension when tryinhg to reshape an array meaning that python will calculate it for you"
newArr2dUnkown = arr1.reshape(-1,2,2)
print(newArr2dUnkown)

"Flattening an array means turning a multidimensional array into a 1d array"
"this can be done using the reshape method but passing in -1"
newarr = newArr3d.reshape(-1)
print(newarr)
