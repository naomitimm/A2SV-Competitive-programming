class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for index in range(len(s)):
            if s[index] == "(":
                stack.append(index)

            elif s[index] == ")":
                current = s[stack[-1] : index + 1]
                s = s[:stack[-1]] + current[:: -1] + s[index + 1:]
                stack.pop()

        fix = ""

        for char in s:
            if char != ")" and char != "(":
                fix += char

        return fix