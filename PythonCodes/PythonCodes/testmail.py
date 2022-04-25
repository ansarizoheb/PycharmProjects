import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
arr3 = arr1 + arr2
print(arr3) # Addition of corresponding elements of array
print(type(arr3))

# Creating multidimensional arrays (1d, 2d, 3d)

a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print("Dimension of array a1 is: ",a1.ndim) # prints the dimension of an array

a2 = np.array([[1, 2, 3, 4, 5]])
print(a2)
print("Dimension of array a2 is: ",a2.ndim) # prints the dimension of an array

a3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(a3)
print("Dimension of array a3 is: ",a3.ndim) # prints the dimension of an array

a4 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]])
print(a4)
print("Dimension of array a4 is: ",a4.ndim) # prints the dimension of an array

# Item counts in an array
print("\nLength of arrays: \n")

print("Length of array a1 is: ",len(a1))
print("Length of array a2 is: ",len(a2))
print("Length of array a3 is: ",len(a3))
print("Length of array a4 is: ",len(a4))

# Shape of an array
print("\nShape of arrays: \n")

print("Shape of array a1 is: ",a1.shape)
print("Shape of array a2 is: ",a2.shape)
print("Shape of array a3 is: ",a3.shape)
print("Shape of array a4 is: ",a4.shape)

# Printing datatypes of 1d, 2d, 3d, 4d array
print("\nPrinting datatypes of 1D, 2D, 3D: \n")

print("Datatype of array a1 is: ",a1.dtype)
print("Datatype of array a2 is: ",a2.dtype)
print("Datatype of array a3 is: ",a3.dtype)
print("Datatype of array a4 is: ",a4.dtype)

# Printing random numbers
print("\nPrinting random integers in array form: \n")
np.random.randint(1000)
print("a) Random 200 integers from 0-5 i.e. [0, 5)\n")
a = np.random.randint(0, 5, 200) # Random 200 integers from 0-5 i.e. [0, 5)
print(a)

print("b) Random array of shape (3,5,5) where integers vary from 100-1000 i.e. [100, 1000)\n")
arr_1=np.random.randint(100, 1000, (3, 5, 5)) # Random array of shape (3,5,5) where integers vary from 100-1000 i.e. [100, 1000)
print(arr_1)
