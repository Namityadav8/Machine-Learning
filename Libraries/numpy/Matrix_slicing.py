import numpy as np 

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)
print(arr.T)  # Transpose of the matrix
print(np.sum(arr,axis=0))  # sum of the elements in the columns

# # now in order to acess the elements of the array we can use the slicing method

# print(arr[1:,2:])

#List comprehension is used here 
# var = [x for x in range(1,10) if x%2==0]
# print(var )