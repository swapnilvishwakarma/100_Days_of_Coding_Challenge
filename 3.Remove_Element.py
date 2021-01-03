# Given an array nums and a value val, remove all instances of that value in-place and return the new 
# length. Do not allocate extra space for another array, you must do this by modifying the input array 
# in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

sol = Solution()
print(sol.removeElement([0,2,5,1,2,4,2,6], 2))
