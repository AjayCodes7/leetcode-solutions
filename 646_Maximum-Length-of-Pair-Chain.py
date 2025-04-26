class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda a : a[0])
        dp = [1]*len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
        return dp[-1]