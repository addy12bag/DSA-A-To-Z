def leaderinArray(arr):
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    return leaders[::-1]

if __name__ == "__main__":
    arr =  [1, 2, 5, 3, 1, 2]
    print(leaderinArray(arr))  

    arr = [-3, 4, 5, 1, -4, -5]
    print(leaderinArray(arr))  

    arr =  [-3, 4, 5, 1, -30, -10]
    print(leaderinArray(arr))  