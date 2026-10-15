def sum_positive(numbers):
    num = 0
    for i in numbers:
        if i > 0:
            num += i
        
    return num
print(sum_positive([1, -2, 3, -4, 5]))