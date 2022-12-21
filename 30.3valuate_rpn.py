# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = "+ - * /"

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if len(stack) > 0:
                    if token == "+":
                        result = stack.pop() + stack.pop()
                        stack.append(result)
                    elif token == "-":
                        result = stack.pop() - stack.pop()
                        stack.append(result)
                    elif token == "*":
                        result = stack.pop() * stack.pop()
                        stack.append(result)
                    elif token == "/":
                        result = stack.pop() // stack.pop()
                        stack.append(result)
                    
        return stack.pop()
