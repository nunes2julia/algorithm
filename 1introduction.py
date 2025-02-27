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



