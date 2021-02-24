# You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.


class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        dic = {}
        
        for i in nums2:
            while (stack and i > stack[-1]):
                key = stack.pop()
                dic[key] = i
            stack.append(i)
            
        return [dic.get(i, -1) for i in nums1]


sol = Solution()
n1 = [4, 1, 2]
n2 = [1, 3, 4, 2]
x = sol.nextGreaterElement(n1, n2)
print(x)