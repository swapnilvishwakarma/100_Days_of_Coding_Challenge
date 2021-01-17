# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums: list) -> bool:
        reach = 0
        for i, val in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i+val)
        return True

sol = Solution()
print(sol.canJump([2,3,1,1,4]))