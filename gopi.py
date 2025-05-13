def first_large_number(numbers, threshold):
    for num in numbers:
        if num > threshold:
            return num
    return None

nums = [3, 8, 15, 2, 22, 5]
threshold = 10
result = first_large_number(nums, threshold)
print("First large number:", result)
