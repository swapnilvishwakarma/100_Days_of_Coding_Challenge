# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the 
# bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Using DP
        # dp = [[0 for _ in range(n)] for _ in range(m)]       
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]

        # Using the Pascal's Triangle Formula
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))

sol = Solution()
print(sol.uniquePaths(10, 7))
