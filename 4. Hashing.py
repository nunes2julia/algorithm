
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

#    Efficiency                       List                  Set
# Operation Adding ( append /add )    O(1)                  O(1)
# Finding ( in )                      O(n)	                O(1)
# Removing ( remove )                 O(n)                  O(1)

# Indexing
# in a list, elements can be accessed using index.

numbers = [1. 2. 3]
print(numbers[1]) #2

# A Set dos not support indexing:

numbers = set([1, 2, 3])
print(numbers[1]) # TypeError: 'set' object is not subscriptable

# Repeated elements
#In a list, an element can occur multiple times:

numbers = []
number.append(5)
number.append(5)
number.append(5)

print(numbers) # {5}

# Task

#You are given a list of numbers. How many distinct numbers does it contain?
#For example, when the list is [3,1,2,1,5,2,2,3], the desired answer is 
# 4 because the distinct numbers are 1, 2, 3 and 5

# slow solution (list)
def count_distinct(numbers):
    seen = []
    for x in numbers:
        if x not in seen:
            seen.append(x)
    return len(seen)

# Efficient solution (set)

def count_distinct(numbers):
    seen = set()
    for x in numbers:
        seen.add(x)
    return len(seen)

# shorten code

def count_distinct(numbers):
    return len(set(numbers))


# Dictionary

# Example (dictionary weights)

weights = {}

weights["apina"] = 100
weights["banaani"] = 1
weights["cembalo"] = 500

weights = {"apina": 100, "banaani": 1, "cembalo": 500}

# elements of a list:

print(weights["apina"]) # 100
weights["apina"] = 150
print(weights["apina"]) # 150

# operator 'in' checks if a given key is in the dictionary:

print("apina" in weights) # True
print("ananas" in weights) # False

# The comand 'del' removes a key

print(weights) # {'apina': 100, 'banaani': 1, 'cembalo': 500}
del weights["banaani"]
print(weights) # {'apina': 100, 'cembalo': 500}

# Using a  dictionary
# Has an element occured
# keep track of elements that have been seen

seen = {}
for x in items:
    seen[x] = True

# same functionality

seen = set()
for x in items:
    seen.add(x)

# Counting occurrences

count = {}
for x in items:
    if x not in count:
        count[x] = 0 
    count[x] += 1

# Position of occurrence

pos = {}
for i, x in enumerate(items):
    pos[x] = i

# TASK 2

You are given a list of numbers, and your task is to compute the mode, which is the most 
frequent number on the list. If the mode is not unique, you can choose any of the possible 
choices for the most frequent number.
For example, when the list is [1,2,3,2,2,3,2,2], the desired answer is 2.

def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count [x] = 0
        count [x] += 1

        if count [x] > count [mode]:
            mode = x

    return mode

# Algorithm implement

def find_mode(numbers):
    count {}
    mode = (0,0)

    for x in numbers:
        if x not in count:
            count [x] = 0
        count [x] += 1

        mode = max(mode, (count[x], x))


# Examples: Rounds 

# Task 3

# given a list that countains the numbers 1,2,....,n in some order.
# your task is to collect all the numbers in order, 
# from smallest to largest so that in each round you go through the list
# from left to right. How many rounds do you need?

# For example, the list [3,6,1,7,5,2,4,8] requires 4 rounds. 
# The first round collects the numbers 1 and 2, the second round 
# the numbers 3 and 4, the third round the number 5, and the fourth round 
# the numbers 6,7 and 8.

# A useful observation is that a new round starts whenever the number 
# to be collected next is to the left of the most recently collected 
# number. In the example list above, the number 
# starts a new round because it is to the left of the number.

# slow list

def count_rounds(numbers):
    n = len(numbers)

    rounds = 1
    for x in range(l, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1
    return rounds

# Efficient solution(dictionary)
    
def count_rounds(numbers):
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = l
    for i in range(l,n):
        if pos[i + l] < pos[i]:
            rounds += 1
            
    return rounds