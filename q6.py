nums = [12, 45, 8, 27, 99, 34]
for i in nums:
    # largest number without using max() function
    if i == nums[0]:
        largest = i
    elif i > largest:
        largest = i
print(largest)