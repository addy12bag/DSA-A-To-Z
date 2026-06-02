class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if (n == 0):
            return nums1


        if (m == 0):
            for i in range(n):
                nums1[i] = nums2[i]


            return nums1


        x = m - 1   # 0
        y = n - 1   # 0
        
        for i in reversed(range(m + n)):
            if (x < 0):
                nums1[i] = nums2[y]
                y -= 1 

                continue 


            # i = 1
            r = nums2[y]    # 1
            l = nums1[x]    # 2
            
            if (r >= l):
                nums1[i] = r
                y -= 1

            else:
                nums1[i] = l 
                x -= 1


            if (y < 0):
                return nums1 
                

        return nums1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(Solution().merge(nums1,m,nums2,n))