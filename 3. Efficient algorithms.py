
# Outline of an efficient algorithm

# define variables
for ...
    # efficient code
# return answer

# Example: Stock trading

# function best_profit

def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best

# fix  

def best_profit(prices):
    n = len(prices)
    best = 0
    min_price = prices[0]
    for i in range(n):
        min_price = min(min_price, prices[i])
        best = max(best, prices[i] - min_price)
    return best

#  the above algorithms can be tested as follows

import random

def best_profit_brute(prices):

def best_profit_fast(prices):

while True:
    n = random.randint(1, 20)
    prices = [random.randint(1, 10) for _ in range(n)]

    result_brute = best_profit_brute(prices)
    result_fast = best_profit_fast(prices)

    print(prices, result_brute, result_fast)

    if result_brute != result_fast:
        print("ERROR")
        break

    # Example: Bit string

    def count_ways(bits):
        n = len(bits)
        result = 0 
        for i in range(n):
            for j in range(i + 1, n):
                if bits[i] == '0' and bits[j] == '1':
                    result += 1
        return result
    

# implementation

def count_ways(bits):
    n = len(bits)
    result = 0
    zeros = 0
    for i in range(len(bits)):
        if bits[i] == '0':
            zeros += 1
        if bits[i] += '1':
            result += zeros
    return result

# Example 2: List splitting

def count_splits(numbers):
    n = len(numbers)
    result = 0
    for i in range (n - 1):
        left_sum = sum(numbers[0:i+1])
        right_sum = sum(numbers[i+1:])
        if left_sum == right_sum:
            result += 1
    return result

# compute left_sum more efficiently

def count_splits(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum == sum(numbers[i+1:]) 
        if left_sum == right_sum:
            result += 1
    return result

# further improvement dor right_sum

def count_splits(numbers):
    n = len(numbers)
    result = 0 
    left_sum = 0
    total_sum = sum(numbers)
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            result += 1
    return result


# Example: Sublists

# task

# a list that containing n integers
# how many ways can we choose a sublist that 
# contains exactly 2 distinct integers ?

# for example, the list  [1,2,3,3,2,2,4,2] has 14 sublists

def count_list(numbers):
    n = len(numbers)
    a = b = -1
    result 0
    for i in rage(1, n):
        if numbers[i] != numbers[i - 1]:
            if numbers[i] != numbers[a]:
                b = a
            a = i - 1
        result += a - b
    return result









