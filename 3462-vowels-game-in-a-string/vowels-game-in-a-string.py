class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s
