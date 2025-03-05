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

# Removing a element
# method pop

numbers = [1, 2, 3, 4, 5, 6]

numbers.pop()
print(numbers) # [1, 2, 3, 4, 5, 5]

numbers.pop(1)
print(numbers) # [1, 3, 4, 5]

# method remove

numbers = [1, 2, 3, 1, 2, 3]

numbers.remove(3)
print(numbers) # [1, 2, 1, 2, 3]

# References and copying

a = [1, 2, 3, 4]
b = a
a.append(5)

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]

# method copy

a = [1, 2, 3, 4]
b = a.copy()
a.append(5)

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4]

# side effects of functions

# function double

def double(numbers):
    result = numbers
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers)) # [2, 4, 6, 8]
print(numbers) #[2, 4, 6, 8]

# function can be corrected with the method copy

def double(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        result[i] *= 2
    return result

# original list are not changed

numbers = [1, 2, 3, 4]
print(double(numbers)) # [2, 4, 6, 8]
print(numbers) # [1, 2, 3, 4]

# slicing and concatenation

# python slice operator ( [ : ] )

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6]) # [3, 4, 5, 6]

result = numbers.copy()

result = numbers[:]

# the operator + can be used for concatenating lists:

first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first + second) # [1, 2, 3, 4, 5, 6, 7, 8]

# list in other languages
""""
# in C++, the data structure std::vector implements a list

std::vector<int> numbers;

numbers.push_back(1);
numbers.push_back(2);
numbers.push_back(3);

# in Java, the data structure ArrayList implements a list

ArrayList<Integer> numbers = new ArrayList<>();

numbers.add(1);
numbers.add(2);
numbers.add(3);

# in JavaScript, the basic data structure is called Array , but it is
# really a list since its size can be changed

numbers = [];

numbers.push(1);
numbers.push(2);
numbers.push(3);

""""