# Print a matrix column-wise.
list = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(list[0])):
    for row in list:
        print(row[i], end=" ")
    print()