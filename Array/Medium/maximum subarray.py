class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            max_value = max(max_value+nums[i],nums[i])
            res = max(res,max_value)
        return res
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))