# for statements 
words = ['cat', 'window', 'defenestrate']
for w in words: 
    print(w, len(w))

# range() function represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops. 
for i in range(-10, -100, -30): 
    print(i)
    
# function call by reference
a = 3
b = 5

def square(lists): 
    for i in lists: 
        i = i * i
        print(i)
    return

square([a, b])
print(a, b)

def fib2(n): 
    """Return a list containing t he Fibonacci series up to n. """
    result = []
    a, b, = 0, 1
    while a < n: 
        result.append(a)
        a, b, = b, a + b
    return result

f100 = fib2(100)
print(f100)

# 4.7 More on Defining Functions
# 4.7.1 Default Argument Values
def ask_ok(prompt, retries = 4, reminder = 'Pease try again!'): 
    while True: 
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): 
            return True
        if ok in ('n', 'no', 'nop', 'nope'): 
            return False
        retries = retries - 1
        if retries < 0: 
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')

# 4.7.2 Keyword Arguments 
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword