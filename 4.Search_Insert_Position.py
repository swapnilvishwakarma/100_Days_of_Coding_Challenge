class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        
        # O(nlogn) approach:
        # while target in nums:
        #     return nums.index(target)
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)
        
        
        # O(n) approach:
        # return bisect.bisect_left(nums, target)
        
        
        # O(logn) approach:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
            
        # When the target is not in the list:
        if nums[l] >= target:
            return l
        else:
            return l+1

sol = Solution()
print(sol.searchInsert([1, 3, 5, 7], 4))
