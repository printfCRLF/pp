import numpy as np

a = np.array([2, 3, 4])
print(a)

# a frequent error consists in calling array with multiple numeric arguments, rather than providing a single list of numbers as an argument
#a = np.array(1, 2, 3, 4) # Wrong

# array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on. 
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)

# create array with initial placeholder
print(np.zeros((3, 4)))

print(np.ones((2, 3, 4), dtype=np.int16))

print(np.empty((2, 3)))

# to create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists
print(np.arange(10, 30, 5))

print(np.arange(0, 2, 0.3))

