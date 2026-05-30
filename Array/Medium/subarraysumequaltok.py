def subarraysumk(nums,k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarraysumk(nums,k)) 

    nums = [1, 2, 3]
    k = 3
    print(subarraysumk(nums,k)) 

    nums = [1, -1, 0]
    k = 0
    print(subarraysumk(nums,k))
