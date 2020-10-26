#NumPy intro
import os
"""
NumPy is a pythin library for woriking with arrays it stands for numerical python

It used as lists are slow to use pretty much so this is faster 

an array object is created called an ndarray 

To start you need to install numpy if you dont have in the cmd linw call pip install numpy
"""

"To start you need to import the numpy module "
import numpy as np

"Then to create an array object use the array() function and in the paraentheses use sqaure or normal brackets"
"We can pass any array like object into this method and it will be converted into an ndarray"
arr = np.array([1,2,3])

print(arr)

#Dimensions
"A dimension refers to the level of the array depth"

#0-D Arrays
"Known as scalars these are the eleents in an array"
arr0 = np.array(42)
print("A 0-D Array",arr0)

#1-D Arrays
"This is an array that has 0-D arrays as it's elements"
arr1 = np.array([1,2,3,4,5])
print("A 1-D Array",arr1)

#2-D Arrays
"This is an array that has 1-D arrays as it's elements used to represent matrices or tensors"
arr2 = np.array([[1,2,3],[4,5,6]])
print("A 2-D Array",arr2)

#3-D Arrays
"This is an array that has 2-D arrays as it's elements used to represent 3rd order tensors"
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("A 3-D Array",arr3)

"To check the number of dimensionsuse the ndim attribute"
os.system('clear')

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
