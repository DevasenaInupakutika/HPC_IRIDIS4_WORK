
# Numpy arrays command where we can explicitly specify the datatype of the array.

import numpy as np

x = np.array([1,2]) # Let numpy choose the datatype
print x.dtype

x = np.array([1.0, 2.0]) # Let numpy choose the datatype
print x.dtype

x = np.array([1,2], dtype = np.int64) # Forcing the datatype
print x.dtype


# Array mathematics

# Basic mathematical functions operate element-wise on arrays and are available as operator and function overloads in the numpy module.

x = np.array([[1,2],[3,4]], dtype = np.float64)
y = np.array([[5,6],[7,8]], dtype = np.float64)

# Element-wise sum; both produce the array

print x + y
print np.add(x,y)

# Element-wise difference, both produce the array

print x - y
print np.subtract(x,y)

# Element-wise product, both produce the array

print x * y
print np.multiply(x, y)

# Element-wise division, both produce the array

print x / y
print np.divide(x,y)

# Element-wise square root; produces the array

print np.sqrt(x)
print np.sqrt(y)

# Matrix multiplication using dot. * is an element-wise multiplication.

v = np.array([9,10])
w = np.array([11,12])

# Inner product of vectors

print v.dot(w)
print np.dot(v,w)

# Another vector product example

print x.dot(v)
print np.dot(x,v)

# x, y inner product

print x.dot(y)
print np.dot(x,y)

# Numpy also provides some useful functions for performing computations on arrays.

z = np.array([[1,2],[3,4]])

print np.sum(z) # This computes sum of all the elements
print np.sum(z, axis = 0) # Computes sum of each column.

print np.sum(z, axis = 1) # Computes sum of each row.

# NUMPY manipulating data in the arrays

# Example: Transposing of matrix

u = np.array([[1,2], [3,4]])

print u

print u.T

# Transposing a rank one array

w = np.array([1,2,3])

print w
print w.T
