# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.

class Solution:
    def calPoints(self, ops: list) -> int:
        stack = []
        
        for i in ops:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(2*stack[-1])
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        print(sum(stack))    
        return sum(stack)


sol = Solution()
sol.calPoints(["5","-2","4","C","D","9","+","+"])