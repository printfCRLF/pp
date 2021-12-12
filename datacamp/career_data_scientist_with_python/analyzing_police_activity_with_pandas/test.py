import numpy as np 

n = np.array([[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]])

print(n.sum())

print( n.max(axis = 1))

print(n.sum(axis = 0))

print(n.shape)

a = np.array([4, 10, 7, 7, 6, 9, 3, 8, 9])
print(a.std())