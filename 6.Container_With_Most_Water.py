class Solution:
    def maxArea(self, height: list) -> int:
        MaxWater = 0
        i, j = 0, len(height)-1
        while i < j:
            Area = min(height[i], height[j]) * (j-i)
            MaxWater = max(MaxWater, Area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return MaxWater

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))