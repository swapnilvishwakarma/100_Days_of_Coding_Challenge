# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        stack = [-1]
        heights.append(0)
        ans = 0
        
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()] 
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
            
        heights.pop()
        
        print(ans)
        return ans

sol = Solution()
sol.largestRectangleArea([2,1,5,6,2,3])