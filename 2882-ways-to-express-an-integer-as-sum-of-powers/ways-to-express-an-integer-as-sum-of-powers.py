class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Recursive Approach : TLE
        # Memorization
        # mod = 10**9 + 7
        # memo = {}
        # def recurse(num, curr):
        #     # Base
        #     if num - curr**x < 0:
        #         return 0

        #     if num - curr**x == 0:
        #         return 1
        #     # Recursive
        #     if (num, curr) in memo:
        #         return memo[(num, curr)]
        #     include = recurse(num - curr**x, curr+1)
        #     exclude = recurse(num, curr+1)
        #     memo[(num, curr)] = (include + exclude)%mod
        #     return memo[(num, curr)]
        
        # return recurse(n,1)%mod
        MOD = 10**9 + 7
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            temp = i**x
            for j in range(n+1):
                dp[i][j] = dp[i-1][j]
                if j - temp >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j - temp])%MOD
        return dp[n][n]