# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such 
# that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        if len(nums) < 4:
            return []
        nums.sort()
        L, N, S, M = len(nums), {j:i for i, j in enumerate(nums)}, set(), nums[-1]
        
        for i in range(L-3):
            a = nums[i]
            if a + 3*M < target:
                continue
            if 4*a > target:
                break
                
            for j in range(i+1, L-2):
                b = nums[j]
                if a + b + 2*M < target:
                    continue
                if a + 3*b > target:
                    break
                    
                for k in range(j+1, L-1):
                    c = nums[k]
                    d = target - (a+b+c)
                    if d > M:
                        continue
                    if d < c:
                        break
                    if d in N and N[d] > k:
                        S.add((a,b,c,d))
                        
        return S

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))