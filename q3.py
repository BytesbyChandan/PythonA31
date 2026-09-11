# Find the sum of all elements in a matrix.
list = [[1,2,3],[4,5,6],[7,8,9]]
total = 0
for row in list:
    for element in row:
        total += element
print("Sum of all elements:", total)