# Looping over elements of a list

animals = ['cat', 'elephant', 'dog', 'monkey']

for animal in animals:
    print animal

# Accessing index of each element within body of a loop using enumerate function

animals = ['cat', 'dog', 'monkey']

for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

# List comprehensions: While programming we might want to transform one data into another.
# Below code computes square numbers

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares

# This code can be made simple using a list comprehension

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print squares

# Example of list comprehensions containing conditions

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0 ]
print even_squares

# Dictionaries
# Dictionary stores [key, value] pairs similar to a hashmap/ map in java or an object in javascript. Following are the examples:

d = {'cat':'cute', 'dog':'funny'}
print d['cat']

print 'cat' in d  # Its like 'ls' in unix confirms the presence of that key or file in unix
d['fish'] = 'wet'
print d['fish']

print d

#print d['Monkey']
#print d.get('Monkey','N/A')
print d.get('Fish','N/A')

#print d

#del d['Fish']
#print d.get('Fish','N/A')

print d

# LOOPS with some examples for practice

# With loops it is easy to iterate over the dictionary keys

dict = {'person':2,'cat':4, 'spider':8}

for mammal in dict:
    legs = dict[mammal]
    print 'A %s has  %d legs' % (mammal, legs)

# Example for Dictionary comprehensions

# These allow to easily construct dictionaries

nums = [0, 1, 2, 3, 4]

even_num_to_squares = {x: x ** 2 for x in nums if x % 2 == 0}
print even_num_to_squares


# SETS --> Unordered collections of distinct elements.

animals = {'cat','dog'}
print 'cat' in animals
print 'fish' in animals

animals.add('fish')
print 'fish' in animals

print len(animals)
animals.add('cat')

print len(animals)
animals.remove('cat')

print len(animals)

# Iterating over sets using loops, Also since the sets are unordered, you can't make assumptions about the order in which you visit the elements of the set

animals = {'cat', 'dog', 'fish'}

for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx+1, animal)


# Set comprehensions example, pretty much similar to lists and dictionaries

from math import sqrt

nums = {int(sqrt(x)) for x in range(30)}

print nums


