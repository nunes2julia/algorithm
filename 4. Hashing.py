
# Hashing is a technique that is frequently 
# used in implementing efficient algotithms.

# set & dict(dictionary) are based hashing.

# data structures based on hashing and their 
# use in algorith design.

#######################################################################




# SET # maintains a set of elements.

# the method 'add' adds an element to the set
# the operator 'in' finds if a given element is in the set
# the method 'remove' removes an element from the set

# Example
# following code creates a set 'numbers' and adds elements to the set


numbers = set()

numbers.add(1)
numbers.add(2)
numbers.add(3)

print(numbers) # {1, 2, 3}

# create a set directly from a list

numbers = set([1, 2, 3])

print(numbers) # {1, 2, 3}

# The operator 'in' tests if an element is in the set

print(3 in numbers) # True
print(4 in numbers) # False

# method 'remove'

print(numbers) # {1, 2, 3}
numbers.remove(2)
print(nummbers) # {1, 3}

# List vs set