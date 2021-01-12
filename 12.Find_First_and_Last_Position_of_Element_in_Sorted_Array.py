# Given an array of integers nums sorted in ascending order, find the starting and ending position of a 
# given target value.
# If target is not found in the array, return [-1, -1].

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: list, target: int) -> list:

        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        
        return (l, r-1) if l<r else (-1, -1)

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))