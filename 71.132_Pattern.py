# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.
# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

class Solution:
    def find132pattern(self, nums: list) -> bool:
        min_list = []
        stack = []
        
        min_list.append(nums[0])
        
        for i in range(1, len(nums)):
            min_list.append(min(nums[:i]))
            
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                    
                if stack and stack[-1] < nums[j]:
                    print('True')
                    return True
                
                stack.append(nums[j])

        print('False')        
        return False


sol = Solution()
sol.find132pattern([-1,3,2,0])