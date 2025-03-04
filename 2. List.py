# List in memory
""""
a = 7
b = -3
c = [1, 2, 3, 1, 2]
d = 99

"""

# List operations
# indexing

numbers = [4, 3, 7, 3, 2]
print(len(numbers)) # 5

# Searching

numbers = [4, 3, 7, 3, 2]

print(3 in numbers) # True
print(8 in numbers) # False

print(numbers.index(3)) # 1
print(numbers.index(3)) # 2

def count(items, target):
    result = 0
    for item in items:
        if item == target:
            result += 1
    return result

# Adding an element

numbers = [1, 2, 3, 4]

numbers.append(5)
print(numbers) # [1, 2, 3, 4, 5]

numbers.insert(1, 6)
print(numbers) # [1. 6. 2. 3. 4. 5]

