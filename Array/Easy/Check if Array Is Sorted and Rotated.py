class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                count +=1
        if nums[n-1]>nums[0]:
            count +=1

        return count<2

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(Solution().check(nums))
        