# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

class Solution:
    def evalRPN(self, tokens: list) -> int:
        ops = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)
        }
        
        stack = []
        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                ans = ops[i](a, b)
                stack.append(ans)
            else:
                stack.append(int(i))

        print(stack[0])        
        return stack[0]

sol = Solution()
sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])