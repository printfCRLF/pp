# when a class definition is entered, a new namespace is created. 
# when a class definition is left, a class object is created. 

# 9.3.2 Class Objects 
# classes objects support two kinds of opoerations: attribute refereces and instantiation

class MyClass:
	"""A simple example class"""
	i = 12345

	def f(self):
		return "hello world"

x = MyClass()
print(x.i, x.f)

# __init__ function, constructor
class Complex: 
	def __init__(self, realpart, imagpart): 
		self.r = realpart
		self.i = imagpart
c = Complex(3.0, -4.5)
print(c.r, c.i)

# 9.3.3 Instance Objects
# The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names, data attributes and methods

x.counter = 1
while x.counter < 10: 
	x.counter = x.counter * 2
print(x.counter)
del x.counter

# 9.3.4 Method objects
y = MyClass()
print(x.f)
print(y.f)

# 9.3.5 Class and Instance Variables
# Generally speaking, instance variables are for data unique to each instance and 
# class variables are for attributes and methods shared by all instnaces of class: 
class Dog: 
	kind = 'canine'					# class variable shared by all instances

	sharedTricks = []

	def __init__(self, name): 
		self.name = name			# instance variable unique to each instance
		self.tricks = []

	def add_trick(self, trick): 
		self.sharedTricks.append(trick)
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print('name: {0}, kind: {1} '.format(d.name, d.kind))
print('name: {0}, kind: {1} '.format(e.name, e.kind))


d.add_trick('roll over')
e.add_trick('play dead')

print(d.sharedTricks)
print(e.sharedTricks)

print(d.tricks)
print(e.tricks)