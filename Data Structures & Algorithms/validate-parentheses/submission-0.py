class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            c = s[i]

            if c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

            
