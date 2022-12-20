class Solution:
    def isValid(self, s: str) -> bool:
        opener = "({["
        closer = ")}]"

        stack = []

        for bracket in s:
            if bracket in opener:
                stack.append(bracket)
            elif bracket in closer:
                index = closer.index(bracket)
                if not stack:
                    return False
                elif stack.pop() != opener[index]:
                    return  False
          
        return stack == []