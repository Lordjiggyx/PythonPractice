# Copy & View

"The main difference between copy and view is that copy is a new array and view is just the view of the orginal array"

import numpy as np


arr = np.array([1,2,3])
"A new array is copied"
x = arr.copy()
y= arr.view()
arr[0]=12


print(arr)
"returns a new array copied form the orginal"
print(x)
"returns the exact same array as the original"
print(y)

"if you make a change to the view you will also change the original"
y[2] = 21
print(y)
print(arr)

"You can check if an array owns it's data by using the base attribute it will return none if the array owns it's own data"
print(x.base)
print(y.base)