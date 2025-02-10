class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ""
        for i in range(len(s)):
            if not s[i].isdigit():
                stack += s[i]
            else:
                stack = stack[0:len(stack)-1]
        return stack