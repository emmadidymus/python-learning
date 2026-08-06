def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

numbers = [1, 3, 5, 6, 8, 9]
print(sum_list(numbers))