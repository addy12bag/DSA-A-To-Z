class Solution(object):
    def moveZeroes(self, nums):
        last_non_zer = 0

        n = len(nums)

        for i in range(n):
            if nums[i]!=0:
                nums[last_non_zer],nums[i] = nums[i],nums[last_non_zer]
                last_non_zer +=1
        return nums
    
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)