# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

class Solution:
    def maximalRectangle(self, matrix):
        if(not matrix) :
            return 0
        
        for i in range(0, len(matrix)):
            for j in range(len(matrix[0])):
                if( matrix[i][j] == '1' ):
                    matrix[i][j] = int(matrix[i][j]) + int(matrix[i-1][j] if(i>0) else 0 )
                else:
                    matrix[i][j] = 0
        
        def findLargestArea(heights):
            if(not heights):
                return 0
            
            heights.append(0)
            stack = [-1]
            ans = 0
            
            for i in range(len(heights)):
                while( heights[i] < heights[stack[-1]] ):
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max( ans, h*w )
                stack.append(i)
                
            return ans
            
        maxArea = 0
        for row in matrix:
            maxArea = max(maxArea, findLargestArea(row))

        print(maxArea)    
        return maxArea

sol = Solution()
sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])