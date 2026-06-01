def pascaltriangle(nums):
    triangle = []
    for row in range(nums):
        arr =[]
        for j in range(row+1):
            if row == j or j == 0:
                arr.append(1)
            else:
                arr.append(triangle[row-1][j-1]+triangle[row-1][j])
        triangle.append(arr)
    return triangle

if __name__ == "__main__":
    nums = 5
    print(pascaltriangle(nums))