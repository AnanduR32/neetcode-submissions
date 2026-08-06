from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set(['*','+','-','/'])
        stack = deque()
        for token in tokens:
            if token in op:
                result = 0
                match token:
                    case '*':
                        operand_2 = stack.popleft()
                        operand_1 = stack.popleft()
                        result = operand_1 * operand_2
                    case '/':
                        operand_2 = stack.popleft()
                        operand_1 = stack.popleft()
                        result = int(operand_1 / operand_2)
                    case '+':
                        operand_2 = stack.popleft()
                        operand_1 = stack.popleft()
                        result = operand_1 + operand_2
                    case '-':
                        operand_2 = stack.popleft()
                        operand_1 = stack.popleft()
                        result = operand_1 - operand_2
                stack.appendleft(result)
            else:
                stack.appendleft(int(token))
        return stack[0]
            
