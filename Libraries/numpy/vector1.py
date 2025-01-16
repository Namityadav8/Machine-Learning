import numpy as np 

#Vectorized mathematical operations on Vectors
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])
# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)

# a=np.zeros((2,3))
# print(a)






arr = np.array([1, 2, 3, 4, 5, 6,1,2,3])
print(np.unique(arr))
array = np.array_split(arr, 3)
print(array)
# array1=np.split(arr,2)
# print(array1)