class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        len3 = len(nums3)
        if (len3 % 2) == 1:
            middle = int(len3/2)
            return nums3[middle]
        else:
            return (nums3[int(len3/2)-1]+nums3[int(len3/2)])/2

sol = Solution()
print(sol.findMedianSortedArrays([1,2], [3,4]))
