import numpy as np

# one-dimensional array can be indexed, sliced and interated over, much like lists an dother Python sequences. 
a = np.arange(10) ** 3
print(a)
print('a[2]: {0}'.format(a[2]))

print('a[2: 5]: {0}'.format(a[2: 5]))

a[:6:2] = -1000 # equivalent to a[0:6:2] = -1000
# from start to position 6, exclusive, set every 2nd element to -1000
print('a[:6:2]: {0}'.format(a))

# multidimensional arrays can have one index per axis, These indices are given in a tuple separated by commas
def f(x, y): 
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

print('b[2, 3]\n {0}'.format(b[2, 3]))

print('b[0:5, 1]\n {0}'.format(b[0:5, 1]))

print('b[:, 1]\n {0}'.format(b[:, 1]))

print('b[1:3, :]\n {0}'.format(b[1:3, :]))

# expression b[i] is treated as an i followed by as many instances of : as needed to represent the remaining axes. NumPy also allows you to write thins using dots as b[i,...]


c = np.array([[[0,  1,  2],               # a 3D array (two stacked 2D arrays)
               [10, 12, 13]],

              [[100,101,102],
               [110,112,113]]])
print(c)
print('c.shape {0}'.format(c.shape))

print('c[1,1,1] \n {0}'.format(c[1,1,1]))
print('c[1,...] \n {0}'.format(c[1,...]))
print('c[...2] \n {0}'.format(c[...,2]))

# iterating over multidimensional arrays is done with respect to the first axis
for row in b:
    print(row)
