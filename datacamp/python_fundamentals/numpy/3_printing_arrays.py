import numpy as np

print(np.arange(6))

print(np.arange(12).reshape(4, 3))

print(np.arange(24).reshape(2, 3, 4))

# Basic operations
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
print(c)

print(b ** 2)

print(10 * np.sin(a))

print(a < 35)

# elementwise product
A = np.array([[1, 1], 
              [0, 1]])
B = np.array([[2, 0], 
              [3, 4]])
print(A * B)

print(A.dot(B))
# [[ 1 * 2 + 1 * 3, 1 * 0 + 1 * 4],
#  [ 0 * 2 + 1 * 3, 0 * 3 + 1 * 4]]
# [[ 5, 4],
#  [ 3, 4]]

# Many unary operations, such as computing the sum of all the elemtns in the array, are implemented as methods of the ndarray class
a = np.random.random((2, 3))
print(a)

print(a.sum())

print(a.min())

# By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However by specifying the axis parameter you can apply an operation along the specified axis of an array 
b = np.arange(12).reshape(3, 4)
print(b)

print(b.sum(axis = 0))

print(b.min(axis = 1))

print(b.cumsum(axis = 1))

