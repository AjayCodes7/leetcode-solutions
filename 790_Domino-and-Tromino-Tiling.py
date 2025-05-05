class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        elif n == 3:
            return 5
        MOD = 10**9 + 7
        dp = [1,2,5]
        for _ in range(n-3):
            dp.append((dp[-1]*2 + dp[-3])%MOD)
        return dp[n-1]