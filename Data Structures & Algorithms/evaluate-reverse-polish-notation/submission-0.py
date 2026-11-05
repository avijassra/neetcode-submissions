from collections import deque

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for s in tokens:
            match s:
                case '+':
                    a = stack.pop()
                    b = stack.pop()
                    c = a + b
                    stack.append(c)
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    c = b - a
                    stack.append(c)
                case '*':
                    a = stack.pop()
                    b = stack.pop()
                    c = a * b
                    stack.append(c)
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    c = b / a
                    stack.append(int(c))
                case _:  # The underscore acts as the default case (catch-all)
                    stack.append(int(s))

        return int(stack[0])