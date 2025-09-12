class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        for ch in range(len(s)):
            if s[ch] in ['a','e','i','o','u']:
                count += 1
        if count == 0:
            return False
        return True
