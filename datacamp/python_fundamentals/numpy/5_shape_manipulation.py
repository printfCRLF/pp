import numpy as np

## chaning the shape of an array
a = np.floor(10 * np.random.random((3, 4)))
print(a)
print('a.shape: {0}'.format(a.shape))

# returns the array, flattened
print('a.ravel(): {0}'.format(a.ravel()))

print('a.reshape(6, 2) \n {0}'.format(a.reshape(6, 2)))

print('a.T \n {0}'.format(a.T))

print('a.T.shape \n {0}'.format(a.T.shape))

## stacking together different arrays
a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print('a \n {0}'.format(a))
print('b \n {0}'.format(b))
print('np.vstack((a, b)) \n {0}'.format(np.vstack((a, b))))
print('np.hstack((a, b)) \n {0}'.format(np.hstack((a, b))))

a = np.arange(12)
b = a
print('b is a: {0}'.format(b is a))
b.shape = 3,4
print('a.shape: {0}'.format(a.shape))

## View or shallow copy
# different array objects can share the same data. The view method creates a new array object that looks at the same data
c = a.view()
print('c is a: {0}'.format(c is a))
print('c.base is a: {0}'.format(c.base is a))
print('c.flags.owndata is a: {0}'.format(c.flags.owndata is a))

c.shape = 2, 6
print('a.shape: {0}'.format(a.shape))
c[0, 4] = 1234
print(a)

# Slicing an array returns a view of it: 
s = a[:, 1:3]
print(s)
s[:] = 10
print(a)

# deep copy
d = a.copy()
print('d is a {0}'.format(d is a))
print('d.base is a {0}'.format(d.base is a))
d[0, 0] = 9999
print(a)
