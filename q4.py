# Find the largest element in a matrix.
list = [[1,2,3],[4,5,6],[7,8,9]]
largest = list[0][0]
for row in list:
    for element in row:
        if element > largest:
            largest = element
print("Largest element:", largest)