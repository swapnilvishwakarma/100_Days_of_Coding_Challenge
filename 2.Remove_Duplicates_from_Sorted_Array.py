# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and 
# returns the new length. Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory.

class Solution:
    def remove_duplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        length = 0
        for i in range(1, len(nums)):  # range is starting from 1 since nums[length=0] will never be less than nums[i=0]
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return (length + 1)

sol = Solution()
print(sol.remove_duplicates([0,1,2,3,3,4,5]))
