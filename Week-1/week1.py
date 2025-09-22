# I. Week 1

# 1. Introduction of Python Numpy
'''
- We use Python library - NumPy for working with arrays
- NumPy stands for Numerical Python
- Numpy is an open source project so it is free for everyone
- We use NumPy because it is faster than traditional Python lists in processing arrays
- Array object in NumPy is call ndarray, it provides many functions to help us working with ndarray easily
- NumPy is faster than Lists because NumPy stores data in continuously in memory, meaning the elements of a NumPy array are placed nexto each other in the memory so when you access this array, CPU can quickly access the elements in SEQUENCE. 
In contrast, Python lists stores data randomly, meaning each element can be located at different places in memory so when we access an element in a list, Python must find where is it location and this process takes a large amount of times and datas
'''

# 2. Introduction of NumPy Random
'''
- Random number means a random number that cant be predicted logically
- Random number in NumPy refers to Pseudo Random - create a random number with algoriths, and it can be predicted if we know the seed
- In order to generate Random Number in NumPy, we uses module random 
'''

# 5. Numpy Creating Arrays
# We use function array() to create ndarrat

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print()

# We can also use a tuple/list/array-like object to create a NumPy array
arr1 = np.array((7, 8, 9, 10))
print(arr1)
print(type(arr1))
print()

# 0-D Arrays
arr2 = np.array(42)
print("0-D Array:", arr2)
print("Dimensions:", arr2.ndim)
print()

# 1-D Arrays
arr3 = np.array([45, 89, 0, 88, 91])
print("1-D Array:", arr3)
print("Dimensions:", arr3.ndim)
print()

# 2-D Arrays
arr4 = np.array([ [1, 2, 3], [4, 5, 6] ])
print("2-D Array:")
print(arr4)
print("Dimensions:", arr4.ndim)
print()

# 3-D Arrays
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Array:")
print(arr5)
print("Dimensions:", arr5.ndim)    # Check dimensions
print()

# Higher Dimensional Arrays
arr6 = np.array([1, 2, 3, 4], ndmin=5)
print(arr6)
print('Number of dimensions :', arr6.ndim)
