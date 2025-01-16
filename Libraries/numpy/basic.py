import numpy as np

# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))


# arr1=arr.reshape(5,1)  # reshaping the array to 2d with having 5 rows
# print(arr1)



#arange function

# arr2=np.arange(0,10,2)  # start,stop,step
# print(arr2)

# print(np.ones(2))
# print(np.zeros(2))


arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.size)
print(arr.shape)    # shape of the array
print(arr.dtype)   # data type of the array
print(arr.ndim)  # number of dimensions
print(arr.itemsize)    # size of each element in the array
print(arr.data)