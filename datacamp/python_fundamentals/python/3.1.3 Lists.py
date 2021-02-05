# Python knows a nubmer of compund data types. List might contain items of different types 
squares = [1, 4, 9, 16, 25]
print(squares)

# Like strings (and all other built-in sequence type), list can be indexed and sliced 
print(squares[0])
print(squares[-1])
print(squares[-3:])

# All slice operations return a new lsit containing the requested elements. This means that the following slice returns a new (shallow) copy of the list
print(squares[:])

# List also support operations like concatenation 
s = squares + [36, 49, 64, 81, 100]
print(s)

# Lists are mutable
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

cubes.append(7 ** 3)
print(cubes)

# Assignment to slices is also possible, and this can even chagne the size of the list or clear it entirely 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2: 5] = ['C', 'D', 'E']
print(letters)

letters[:] = []
print(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0])
print(x[0][1])