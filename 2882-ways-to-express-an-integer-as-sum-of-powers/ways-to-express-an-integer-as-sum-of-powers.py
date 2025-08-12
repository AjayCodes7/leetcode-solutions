class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Recursive Approach : TLE
        # Memorization
        mod = 10**9 + 7
        memo = {}
        def recurse(num, curr):
            # Base
            if num - curr**x < 0:
                return 0

            if num - curr**x == 0:
                return 1
            # Recursive
            if (num, curr) in memo:
                return memo[(num, curr)]
            include = recurse(num - curr**x, curr+1)
            exclude = recurse(num, curr+1)
            memo[(num, curr)] = include + exclude
            return memo[(num, curr)]
        
        return recurse(n,1)%mod
