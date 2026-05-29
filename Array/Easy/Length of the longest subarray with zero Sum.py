def Length_of_the_longest_subarray_with_zero_Sum(arr):
    sum_so_far = 0
    max_length = 0
    sum_index_map ={}

    for i in range(len(arr)):
        sum_so_far +=arr[i]

        if sum_so_far == 0:
            max_length = i+1
        if max_length == 0 and sum_so_far in sum_index_map:
            max_length = max(max_length,i-sum_index_map[sum_so_far])
        if sum_so_far not in sum_index_map:
            sum_index_map[sum_so_far] = i
    return max_length

if __name__ == "__main__":
    arr = [1,2,-3,3,4,-7]
    print(Length_of_the_longest_subarray_with_zero_Sum(arr))