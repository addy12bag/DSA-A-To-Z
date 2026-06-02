def longestSubarray(nums,k):
    sum_so_far = 0
    max_length = 0
    sum_index_map = {}

    for i in range(len(nums)):
        sum_so_far += nums[i]

        if sum_so_far ==k:
            max_length =  i+1

        if sum_so_far - k in sum_index_map:
            max_length = max(max_length, i-sum_index_map[sum_so_far-k])
        if  sum_so_far not in sum_index_map:
            sum_index_map[sum_so_far] = i
    return max_length

if __name__ == "__main__":
    nums = [-3,2,1]
    k = 6
    print(longestSubarray(nums,k))