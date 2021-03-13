# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        stack = []
        result = [-1 for _ in nums]
        
        for _ in range(2):  # This is still linear because we are repeating this twice not n times!
            for i, num in enumerate(nums):
                while stack and num > nums[stack[-1]]:
                    result[stack.pop()] = num
                stack.append(i)
        
        print(result)
        return result

sol = Solution()
sol.nextGreaterElements([1,2,1])