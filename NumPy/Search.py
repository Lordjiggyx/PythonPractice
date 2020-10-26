#Search

"You can seacrh an array for a certain valie and return the indexes that get a match"
"this is done using the where method"

import numpy as np

arr = np.array([1,4,3,1,2,51,4,4,12,33,5])
"To do this use the where method and oass in the condition"
x =np.where(arr==4)

"This will return a tuple with each matching index"
print(x)


