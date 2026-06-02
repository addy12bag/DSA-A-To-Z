class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        attendance = [False] * (n * n + 1)
        duplicate = -1

       
        for i in range(n):
            for j in range(n):
                if attendance[grid[i][j]]:
                    duplicate = grid[i][j]
                else:
                    attendance[grid[i][j]] = True

   
        for i in range(1, n * n + 1):
            if not attendance[i]:
                return [duplicate, i]
        return []
    
if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 8]]
    print(Solution().findMissingAndRepeatedValues(grid))