class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        box = []
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y  
            }
        total = 0
        
        for i in tokens:
            if i not in op:
                i = int(i)
                box.append(i)
            else:
                result = int(op[i](box[-2], box[-1]))
                box.pop()
                box.pop()
                box.append(result)
        return box[0]