# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(", "]":"[", "}":"{"}

        for p in s:
            if p in lookup.values():
                stack.append()
            elif stack and lookup[p] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
