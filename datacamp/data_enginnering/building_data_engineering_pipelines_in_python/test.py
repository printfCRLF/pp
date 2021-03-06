# def factorial(n):
#     """returns n!"""
#     return 1 if n < 2 else n * factorial(n-1)

# print(factorial.__doc__)

a = {1, 2, 3, 4}
print(type(a))


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a.intersection(b)
# a.difference(b)

# [s.upper() for s in ['hello', 'world']]


# import random
# random.seed(2427)

# def efficient_sample(n):
#   x = [ for n]
#   x = [random.random() for i in range(n)]
#   return x

# efficient_sample(20)

# def multiply(by = None):
#     	def multiply_real_decorator(function):
# 		def wrapper(*args,**kwargs):
# 			return by * function(*args,**kwargs)
# 		return wrapper
# 	return multiply_real_decorator

# """add by 2"""
# @multiply(by = 2)
# def adder(a,b):
#   return a + b


# @multiply(by = 3)
# def subtractor(a,b):
#   return a - b

# print(adder(2,3))
# print(subtractor(2,3))