class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        seen = {} # Dictonary to search faster in O(n) time instead of two for loops
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[value] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
