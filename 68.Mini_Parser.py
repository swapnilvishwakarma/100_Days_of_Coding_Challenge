# Given a nested list of integers represented as a string, implement a parser to deserialize it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Note: You may assume that the string is well-formed:

# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: '') -> NestedInteger:
        if not s:
            return NestedInteger()
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        start = 0
        
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(NestedInteger())
                start = i+1
                
            elif s[i] in ',]':
                if s[start:i].lstrip('-').isdigit():
                    num = int(s[start:i])
                    stack[-1].add(NestedInteger(num))
                    
                if s[i] == ']':
                    ni = stack.pop()
                    
                    if stack:
                        stack[-1].add(ni)
                    else:
                        return ni
                    
                start = i+1