#Transpose of a matrix.
list = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]
for row in transpose:
    print(row)