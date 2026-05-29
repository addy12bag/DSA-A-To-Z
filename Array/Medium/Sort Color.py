class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    swapped = True
            if swapped == False:
                break
        return nums

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    print(Solution().sortColors(nums))