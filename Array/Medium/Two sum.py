class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in lookup:
                return [lookup[complement], i]

            lookup[num] = i

if __name__ == "__main__":
    nums = [3,2,3]
    target = 6
    print(Solution().twoSum(nums,target))