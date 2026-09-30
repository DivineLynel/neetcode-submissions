class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y  
            }
        
        for i in tokens:
            if i not in op:
                i = int(i)
                stack.append(i)
            else:
                result = int(op[i](stack[-2], stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(result)
        return stack[0]