#Count how many even and odd numbers are in the matrix.
list = [[1,2,3],[4,5,6],[7,8,9]]
even_count = 0  
odd_count = 0          
for row in list:
    for element in row:
        if element % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)