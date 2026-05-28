class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

if __name__ == "__main__":
    nums = [-1,-100,3,99]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)
    print(nums)