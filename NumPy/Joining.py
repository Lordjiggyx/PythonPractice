#Join

"To join numpy arrays we use the concatenate function along withh the axis"
"Axis is a bit of a weird one it actually can go down alonf the rows and join array based on the postion of the elements"

import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

newarr = np.concatenate((arr1,arr2))
print(newarr)

arr3 = np.array([[1,2],[4,5]])
arr4 = np.array([[5,6],[7,8]])

"To add axis just pass it as a parameter"
new2DarrAxis1 = np.concatenate((arr3,arr4), axis=1)
print(new2DarrAxis1)
