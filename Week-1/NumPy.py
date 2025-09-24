### I. Week 1

## 1. Introduction of Python Numpy
'''
- We use Python library - NumPy for working with arrays
- NumPy stands for Numerical Python
- Numpy is an open source project so it is free for everyone
- We use NumPy because it is faster than traditional Python lists in processing arrays
- Array object in NumPy is call ndarray, it provides many functions to help us working with ndarray easily
- NumPy is faster than Lists because NumPy stores data in continuously in memory, meaning the elements of a NumPy array are placed nexto each other in the memory so when you access this array, CPU can quickly access the elements in SEQUENCE. 
In contrast, Python lists stores data randomly, meaning each element can be located at different places in memory so when we access an element in a list, Python must find where is it location and this process takes a large amount of times and datas
'''

## 2. Introduction of NumPy Random
'''
- Random number means a random number that cant be predicted logically
- Random number in NumPy refers to Pseudo Random - create a random number with algoriths, and it can be predicted if we know the seed
- In order to generate Random Number in NumPy, we uses module random 
'''
## 3. Introduction of NumPy ufunc
'''
- ufuncs stands for "Universal Function, they are NumPy functions that operate on ndarray object
'''

## 5. Numpy Creating Arrays
# Note: If nested arrays are not at the same level. NumPy creates a 1-D object array instead
# We use function array() to create ndarrat
print("5. Numpy Creating Arrays")
print()
import numpy as np

def create_and_display_array(value):
    arr = np.array(value)
    print(arr)
    print("Dimensions:", arr.ndim)
    print()
    return arr

# We can also use a tuple/list/array-like object to create a NumPy array
create_and_display_array([(7, 8, 9, 10)])

# 0-D Arrays
print("0-D Array:")
create_and_display_array(42)

# 1-D Arrays
print("1-D Array:")
create_and_display_array([45, 89, 0, 88, 91])

# 2-D Arrays
print("2-D Array:")
create_and_display_array([ [1, 2, 3], [4, 5, 6] ])

# 3-D Arrays
print("3-D Array:")
create_and_display_array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# Higher Dimensional Arrays
arr6 = np.array([1, 2, 3, 4], ndmin=5)
print(arr6)
print('Number of dimensions:', arr6.ndim)
print("-------------")


## 6. Numpy Array Indexing
print("6. Numpy Array Indexing")
print()

# Index in NumPy Arrays is same as arrays in Python
a = create_and_display_array([1, 2, 3, 4])
print("First element:", a[0])
print("Last element:", a[-1])
print("Sum of second and third elements:", a[1] + a[2])
print()

# Access 2-D Arrays
# Think of 2-D arrays like a table with rows and colums, so we use comma separated intergers representing the  dimension and the index of the element

b = create_and_display_array([[18, 8, 2006], [4, 2, 2006]])
print("Second element on second row:", b[1, 1])   
print("Last element on first row:", b[0, -1])
print()

# Access 3-D Arrays
c = create_and_display_array([[[1, 2 , 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c[1, 0, 2])   # The output will be 9 cuz the first interger 1 will choose the second 2-D array (this 3-D array includes tw0 2-D arrays). In this chosen 2-D array has two 1-D arrays and the interger 0 will choose the first 1-D array. Finally interger 2 accesses to the third element of this 1-D array
print("-------------")

## 7. Numpy Array Slicing
print("7. Numpy Array Slicing")
print()

# Syntax: arr[start:end:step]       start: default = 0, end: default = length of array, step: default = 1
d = create_and_display_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(d[1:5])
print(d[4:])
print(d[:4])
print(d[-3:-1])
print(d[1:5:2])
print(d[::2])
print()

# Slicing 2-D Arrays
slicing_2d = create_and_display_array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(slicing_2d[1, 1:4])
print(slicing_2d[0:2, 3])
print(slicing_2d[0:2, 1:4])
print("-------------")


## 8. Numpy Data Types
print("8. Numpy Data Types")
print()
e = create_and_display_array([1, 2, 3, 4])
print(e.dtype)
d = create_and_display_array(["Dũng", "Việt", "Thành"])
print(d.dtype)

# Create Arrays with a defined data type
defined_array = np.array([1, 2, 3, 4], dtype ='S')
print(defined_array)
print(defined_array.dtype)

# Change data type to another type using function astype()
array = np.array([1.1, 2.1, 3.2, 0])
new_array = array.astype('i')
print(new_array)
print(new_array.dtype)
new_array2 = array.astype(bool)
print(new_array2)
print(new_array2.dtype)

