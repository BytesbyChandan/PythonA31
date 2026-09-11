#Count total number of elements in a matrix.
list = [[1,2,3],[4,5,6],[7,8,9]]
count = 0
for row in list:
    count += len(row)
print("Total number of elements:", count)