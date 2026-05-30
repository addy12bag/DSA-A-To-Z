def setmatrixZeroes(matrix):
    m  = len(matrix)
    n = len(matrix[0])
    row = set()
    col = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j] =0

if __name__ =="__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setmatrixZeroes(matrix)
    print(matrix) 

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setmatrixZeroes(matrix)
    print(matrix)   
