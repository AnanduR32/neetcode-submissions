from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack:deque[int] = deque()        
        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.appendleft(int(char))
            else:
                result = 0
                b = stack.popleft()
                a = stack.popleft()
                match (char):
                    case '+':
                        result = a + b
                    case '-':
                        result = a - b
                    case '*':
                        result = a * b
                    case '/':
                        result = int(a / b)
                stack.appendleft(result)
        return stack[0]
                
                