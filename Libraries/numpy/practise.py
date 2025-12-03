import numpy as np

arr = np.array([1,2,3,4])
print(arr)
print(arr.shape)
arr1  = arr.reshape(4,1)
print(arr1 )


d = np.exp(np.sum(np.log(np.arange(1,6))))
print(int(d)+1)
