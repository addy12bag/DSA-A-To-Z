def spiralmatrixTraversal(matrix):
    if not matrix:
        return []

    res = []
    m = len(matrix)
    n = len(matrix[0])
    top, left, bottom, right = 0, 0, m - 1, n - 1

    while top <= bottom and left <= right:

        # left → right
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        # top → bottom
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        # right → left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        # bottom → top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res
    
if __name__ =="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = spiralmatrixTraversal(matrix)
    print(res)

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = spiralmatrixTraversal(matrix)
    print(res)