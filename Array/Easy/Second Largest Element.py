def second_largest(arr):
    n = len(arr)

    if n<2:
        return None

    largest = second_largest = float('-inf') 
    for i in range(n):
        if arr[i]>largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i]>second_largest and arr[i]!= largest:
            second_largest = arr[i]
    if second_largest == float('-inf'):
        return None
    return second_largest

if __name__ == "__main__":
    arr = [99,10,4,6,90,100]
    print("Second largest element in the array is :",second_largest(arr))