#Data Tyoes

"Numpy has extra data types and the are referred to by using characters"

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""
"To check the type of an ndarray use the dtype attribute"

import numpy as np


arr = np.array([1,2,3])

print(arr.dtype)

"when creating an array using the array() method we can pass in the dtype argument to define the expected data type"

arr1 = np.array([1,2,3,4,5,6], dtype='S')

print(arr1.dtype)


"You can convert the data types of an exisiting array by using the astype() method this method creates a copy if an array and allows you to specify the data type as a parameter"
"you can either use characters for example f,i or you can use the full name float int"

arrf = np.array([1.1,2.2,3.3])

newarrINt = arrf.astype('i')
print(arrf)
print(newarrINt)