# Program to multiply two matrices using nested loops

def multiply(a, b):
    # The number of columns in the first matrix should be the same 
    # as the number of rows in the second matrix
    
    if len(a[0]) != len(b):
        raise('It is impossible to multiply this matrices!')

    result = [[0 for i in range(len(b[0]))] for j in range(len(a))]

    # iterate through rows of X
    for i in range(len(a)):
    # iterate through columns of Y
        for j in range(len(b[0])):
            # iterate through rows of Y
            for k in range(len(a)):
                result[i][j] += a[i][k] * b[k][j]

    return result

# 3x3 matrix
X = [
    [12, 7, 3],
    [4 ,5, 6],
    [7 ,8, 9]
]
# 3x4 matrix
Y = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

result = multiply(X, Y)

for r in result:
   print(r)
