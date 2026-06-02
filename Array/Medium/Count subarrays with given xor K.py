def subarrysumxor(nums,k):
    count=0
    xor_so_far = 0
    xor_map_index = {}

    for i in range(len(nums)):
        xor_so_far ^= nums[i]

        if xor_so_far == k:
            count +=1
        if xor_so_far ^ k in xor_map_index:
            count += xor_map_index[xor_so_far ^ k]
        if xor_so_far not in xor_map_index:
            xor_map_index[xor_so_far] = 1
        else:
            xor_map_index[xor_so_far] += 1
    return count

if __name__ == "__main__":
    nums = [5, 6, 7, 8, 9]
    k = 5
    print(subarrysumxor(nums,k))