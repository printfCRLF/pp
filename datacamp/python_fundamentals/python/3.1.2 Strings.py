# string literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''
print("""\
Usage: thingy [OPTIONS]
    -h 
    -H hostname    
""")

# string can be indexed, with the first character having index 0
word = 'Python'
print(word[0])
print(word[5])

# indices may also be negative numbers, to start  counting form the right
print(word[-1])
print(word[-2])
print(word[-6])

# slicing, characters from position 2 (included) to position 5 (excluded)
print(word[0: 2]) 
print(word[2: 5])     

print(word[:2] + word[2:])
print(word[:4] + word[4:])

# slicing indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced 
print(word[:2])
print(word[4:])
print(word[-2:])

# python strings are immutable 
#word[0] = 'J'

# The built-in function len() returns the length of a string 
s = 'supercalifragilisticexpialidocious'
print(len(s))