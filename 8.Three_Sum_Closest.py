# Given an array nums of n integers and an integer target, find three integers in nums such that the sum 
# is closest to target. Return the sum of the three integers. You may assume that each input would have 
# exactly one solution.

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while(lo < hi):
                s = nums[i] + nums[lo] + nums[hi]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    lo += 1
                else:
                    hi -= 1
                
            if diff == 0:
                break
        
        return (target - diff)

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))
