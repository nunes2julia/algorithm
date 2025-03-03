#algoritmo?

def count_even(numbers):
    return sum (x % 2 == 0 for x in numbers)

   
    print(count_even([1, 2, 3])) # 1
    print(count_even([2, 2, 2, 2, 2])) # 5
    print(count_even([5, 4, 1, 7, 9, 6])) # 2

    #Eficiência dos algoritmos

# Algoritimo 1

def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x - y))
    return result

# Algoritimo 2

def max_diff(numbers):
    numbers = sorted(numbers)
    return numbers[-1] - numbers[0]

# Algoritmo 3

def max_diff(numbers):
    return max(numbers) - min(numbers)

# Medicao de eficiencia
# programa que testa a eficiencia da max_diff funcao :

import random
import time

def max_diff(numbers):

    n = 1000
    print("n:", n)
    random.seed(1337)
    numbers = [random.randint(1, 10**6) for _ in range(n)]

    start_time = time.time()
    result = max_diff(numbers)
    end_time = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")

    # Analise de algoritmos

    def count_even(numbers):
        result = 0 
        for x in numbers:
            if x % 2 == 0:
                result += 1
                return result

# complexidade de tempo dos loops


#algoritmos O(1):

def middle(numbers):
    n = len(numbers):
    return numbers[n // 2]


#  single Loop 
# O(n):

def calc_sum(numbers):
    result = 0 
    for x in numbers:
        result += x
    return result

# Nested loops 
# O(n²)

 def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False


#Sequantial code segments
# O(n)

def count_min(numbers):
    #stage 1 
    min_value = numbers[0]
    for x in numbers:
        if x == min_value:
            result += 1
    return result

