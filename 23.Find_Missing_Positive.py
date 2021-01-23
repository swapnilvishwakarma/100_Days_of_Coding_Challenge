# Given an unsorted integer array nums, find the smallest missing positive integer.
# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        ans = 1
        if 1 not in nums:
            return ans
        for _ in range(len(nums)):
            if ans in nums:
                ans += 1
        
        return ans

sol = Solution()
print(sol.firstMissingPositive([7,8,9,11,12]))