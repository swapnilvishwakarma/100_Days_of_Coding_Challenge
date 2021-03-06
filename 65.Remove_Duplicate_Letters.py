# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

class Solution:
    def removeDuplicateLetters(self, s: '') -> '':
        d = {char: indx for indx, char in enumerate(s)}
        
        result = []
        
        for indx, char in enumerate(s):
            if char not in result:
                while result and indx < d[result[-1]] and char < result[-1]:
                    result.pop()
                result.append(char)
        
        print(''.join(result))
        return ''.join(result)

sol = Solution()
sol.removeDuplicateLetters("cbacdcbc")