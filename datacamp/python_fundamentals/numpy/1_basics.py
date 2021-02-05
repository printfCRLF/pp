# NumPy's main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In NumPy dimensions are called axes. The number of axes is rank

import numpy as np 
a = np.arange(15).reshape(3, 5)
print(a)

# the dimensions of the array
print('shape: {0}'.format(a.shape))

# number of axes
print('ndim: {0}'.format(a.ndim))

print('dtype.name: {0}'.format(a.dtype.name))

# the size in bytes of each element of the array
print('itemsize: {0}'.format(a.itemsize))

# the total number of elements of the array. This is equal to the product of the elements of shape
print('size: {0}'.format(a.size))

print('type(a): {0}'.format(type(a)))