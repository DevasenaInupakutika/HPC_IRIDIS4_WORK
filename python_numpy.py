# Numpy provides a high-performance multidimensional array object, and tools for working with these arrays.

# Arrays

# Numpy arrays

# Numpy arrays can be initialized from nested Python lists, and access elements using square brackets.

import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print type(a)            # Prints "<type 'numpy.ndarray'>"
print a.shape            # Prints "(3,)"
print a[0], a[1], a[2]   # Prints "1 2 3"
a[0] = 5                 # Change an element of the array
print a                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print b.shape                     # Prints "(2, 3)"
print b[0, 0], b[0, 1], b[1, 0]   # Prints "1 2 4"


# Numpy also provides many functions to create arrays.

c = np.zeros((2,2))  # Creating an array of all zeros.
print c 


# Creating array of all ones

d = np.ones((2,2))
print d

# Create an identity matrix

e = np.eye(2)
print e

# Creating a constant array

f = np.empty((2,2))
f.fill(7)
print f

# Creating an array filled with random values

g = np.random.random((2,2))
print g


