def max_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_rest = max_list(numbers[1:])
        return numbers[0] if numbers[0] > max_rest else max_rest

numbers = [1, 2, 4, 5, 7, 12, 65, 34, 9]
print(max_list(numbers))