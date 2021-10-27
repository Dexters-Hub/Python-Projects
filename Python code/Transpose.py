matrix = [[1,2],[3,4],[5,6]]
for row in matrix :
    print(row)
res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("\n")
for row in res:
    print(row)
 #output
#[1, 2]
#[3, 4]
#[5, 6]

#[1, 3, 5]
#[2, 4, 6]
    
    
    
