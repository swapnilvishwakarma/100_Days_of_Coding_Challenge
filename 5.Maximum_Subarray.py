# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the 
# largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        current = nums[0]
        MaxSum = nums[0]
        for i in range(1, len(nums)):
            if (current + nums[i] > current) and (current + nums[i] > nums[i]):
                current += nums[i]
            else:
                MaxSum = max(MaxSum, current)
                current = max(current + nums[i], nums[i])
        return max(MaxSum, current)

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
