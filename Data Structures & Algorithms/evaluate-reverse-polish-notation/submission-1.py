import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b),  # truncate toward zero
        }
        stack = []
        for t in tokens:
            if t in ops:
                b, a = stack.pop(), stack.pop()  # b = right operand
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))
        return stack.pop()