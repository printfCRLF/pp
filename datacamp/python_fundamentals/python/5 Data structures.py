# common list operations
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangrine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)
fruits.append('grape')
fruits.sort()
print(fruits)

# 5.1.3 List comprehensions
squares = []
for x in range(10): 
    squares.append(x ** 2)
print(squares)

squares2 = list(map(lambda x: x ** 2, range(10)))
print(squares2)

squares3 = [x ** 2 for x in range(10)]
print(squares3)

combs = []
for x in [1, 2, 3]: 
    for y in [3, 1, 4]: 
        if x != y: 
            combs.append((x, y))
print(combs)            

combs2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs2)

# create a new list with the values doubled
vec = [-3, 1, 0, 4]
print([x * 2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all elements
print([abs(x) for x in vec])
# create a lsit of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])

# 5.1.4 Nested list comprehension
matrix = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],]

transposed = []
for i in range(4): 
    tRow = []
    for row in matrix: 
        tRow.append(row[i])
    transposed.append(tRow)
print(transposed)

transposed2 = [[row[i] for row in matrix] for i in range(4)]
print(transposed2) 

# 5.4 Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b) 

# 5.6 Looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items(): 
    print(k, v)

for(i, v) in enumerate(['tic', 'tac', 'toe']): 
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for (q, a) in zip(questions, answers): 
    print('What is your {0}? It is {1}. '.format(q, a))

