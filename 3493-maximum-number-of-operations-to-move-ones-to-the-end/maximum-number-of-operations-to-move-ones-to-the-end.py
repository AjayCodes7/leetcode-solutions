class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ones = [0]*n
        count = 0
        for i in range(n):
            if s[i] == '1' and i == 0:
                ones[i] = 1
            elif s[i] == '1':
                ones[i] = ones[i-1] + 1
            else:
                ones[i] = ones[i-1]
            if s[i] == '0' and (i == n-1 or s[i+1] == '1'):
                count += ones[i]
        return count