def RotateImage(matrix):
    n =len(matrix)
    
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[j][n-i-1] = matrix[i][j]
    return res

if __name__ =="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(RotateImage(matrix)) 

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(RotateImage(matrix))