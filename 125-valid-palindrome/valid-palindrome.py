class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        s = "".join(list(filter(str.isalnum, s)))
        s = s.lower()
        return s == s[::-1]