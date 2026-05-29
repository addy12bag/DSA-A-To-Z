def Longest_subarray_with_given_sum_k(arr,k):
    sum_so_far = 0
    max_length = 0
    sum_index_map ={}

    for i in range(len(arr)):
        sum_so_far += arr[i]

        if sum_so_far == k:
            max_length = i+1
        if max_length ==0 and (sum_so_far-k) in sum_index_map:
            max_length = max(max_length,i-sum_index_map[sum_so_far-k])
        if sum_so_far not in sum_index_map:
            sum_index_map[sum_so_far] = i
    return max_length

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    k =15
    print(Longest_subarray_with_given_sum_k(arr,k))