# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

class Solution:
    def removeKdigits(self, num: '', k: int) -> '':

        stack = []
        number_to_remove = k
        for current_elt in num:
            while number_to_remove and stack and stack[-1] > current_elt:
                stack.pop()
                number_to_remove -= 1
            stack.append(current_elt)
        ans = ''.join(stack[0: len(num)-k]).lstrip('0')
        
        if len(ans):
            print(ans)
            return ans
        else:
            print('0')
            return '0'

sol = Solution()
sol.removeKdigits('123456789', 3)