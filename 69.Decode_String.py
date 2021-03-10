# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: '') -> '':
        stack = []
        a, d = '', ''
        
        for letter in s:
            if letter.isdigit():
                d += letter
                
            elif letter.isalpha():
                a += letter
                
            elif letter == '[':
                stack.append((a, int(d)))
                a, d = '', ''
                
            elif letter == ']':
                p, n = stack.pop()
                a = p + a*n
                
        print(a)
        return a

sol = Solution()
sol.decodeString("2[abc]3[cd]ef")