class Solution:
    def isValid(self, s: str):
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
