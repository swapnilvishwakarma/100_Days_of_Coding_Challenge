# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation 
# of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted 
# in ascending order).
# The replacement must be in place and use only constant extra memory.

class Solution:
    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
    
    def nextPermutation(self, nums: list) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec+1]:
            dec -= 1
        self.reverse(nums, dec+1, len(nums)-1)
        
        if dec == -1:
            return
        
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap(nums, next_num, dec)

        return nums

sol = Solution()
print(sol.nextPermutation([1,7,9,9,8,3]))