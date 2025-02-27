

def count_even(numbers):
    return sum (x % 2 == 0 for x in numbers)

   
    print(count_even([1, 2, 3])) # 1
    print(count_even([2, 2, 2, 2, 2])) # 5
    print(count_even([5, 4, 1, 7, 9, 6])) # 2


