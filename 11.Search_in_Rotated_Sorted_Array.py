# You are given an integer array nums sorted in ascending order (with distinct values), and an integer
# target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become 
# [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.

class Solution:
    def search(self, nums: list, target: int) -> int:
        
        res = []
        for i in range(0, len(nums)):
            if nums[i] == target:
                res.append(i)

        if len(res) == 1:
            return res[0]
        elif len(res) == 0:
            return '-1'

# Using Binary Search i.e. O(logn) approach
#         if not nums:
#             return -1
#         pivot = 0
#         if nums[0] > nums[-1]:
#             pivot = self.findPivot(nums, target, 0, len(nums) - 1)    
#         return self.rotatedBinarySearch(nums, target, pivot)
        
#     def findPivot(self, arr, target, lo, hi):
#         while lo < hi:
#             mid = lo + hi >> 1 # Right Shift bitwise operator
#             if arr[mid] > arr[hi]:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo
        
#     def rotatedBinarySearch(self, arr, target, pivot):
#         n = len(arr)
#         lo, hi = 0, n - 1
#         while lo <= hi:
#             mid = lo + hi >> 1 # Right Shift bitwise operator
#             if arr[(mid + pivot) % n] == target:
#                 return (mid + pivot) % n
#             elif arr[(mid + pivot) % n] > target:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))