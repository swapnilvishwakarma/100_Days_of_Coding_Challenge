# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums: list) -> int:
        cur, tmp = 0, 0
        jump_count = 0
        length = len(nums)
        
        while cur < length - 1:
            cur_max = 0
            for i in range(1, nums[cur]+1):

                # Whenever reach end, return jump+1
                if cur+i >= length-1:
                    return (jump_count+1)
                    
                # Find out the furthest position
                elif cur + i + nums[cur+i] >= cur_max:
                    cur_max = cur + i + nums[cur+i]
                    tmp = cur + i
                    
            # If the furthest position is bigger than length, return jump+2
            if cur_max >= length-1:
                return (jump_count+2)                  
            jump_count += 1
            cur = tmp
        
        return jump_count

sol = Solution()
print(sol.jump([2,3,0,1,4]))