class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(','[','{'):
                stack.append(i)
                continue
            if i in (')',']','}'):
                if len(stack):
                    j = stack.pop()
                    if (i == ')' and j == '(') or (i == ']' and j == '[') or (i == '}' and j == '{'):
                        continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0