def largest_element(arr):
    if not arr:
        return None
    largest  = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest

if __name__ == "__main__":
    arr = [99,10,4,6,90,100]
    print("Largest element in the array is :",largest_element(arr))