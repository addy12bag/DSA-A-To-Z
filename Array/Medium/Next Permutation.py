class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

   
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

    
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

     
        nums[i + 1:] = reversed(nums[i + 1:])

if __name__ == "__main__":
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    print(nums)  # Output: [1, 3, 2]

    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)  # Output: [1, 2, 3]

    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    print(nums)  # Output: [1, 5, 1]