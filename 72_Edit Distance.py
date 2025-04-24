class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # Dynamic Programming with memorization
        # dp = [[-1]*len(word2) for _ in range(len(word1))]
        # def recurse(i,j):
        #     # Base Condition
        #     if i == len(word1) and j == len(word2):
        #         return 0
        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     # Recursive Case
        #     if word1[i] == word2[j]:
        #         # Equal
        #         return recurse(i+1, j+1)
        #     # Not Equal
        #     dp[i][j] = 1 + min(recurse(i,j+1),recurse(i+1,j),recurse(i+1,j+1))
        #     return dp[i][j]
        # return recurse(0,0)
        # # Time Complexity : O(n*m)
        # # Space Complexity : O(n*m)

        # # Dynamic Programming with tabulation
        # dp = [[-1]*(len(word2)+1) for _ in range((len(word1)+1))]
        # dp[0] = [i for i in range(len(word2)+1)]
        # for j in range(len(word1)+1):
        #     dp[j][0] = j
        # for i in range(1,len(word1)+1):
        #     for j in range(1,len(word2)+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(1+dp[i-1][j-1],1+dp[i-1][j], 1+dp[i][j-1])
        # return dp[-1][-1]
        # # Time Complexity : O(n*m)
        # # Space Complexity : O(n*m)

        # Dynamic Programming with tabulation with space optimization
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        dp = [[i for i in range(len(word2)+1)] for _ in range(2)]
        for i in range(1,len(word1)+1):
            dp[1][0] = i
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[1][j] = dp[0][j-1]
                else:
                    dp[1][j] = min(1+dp[0][j-1],1+dp[0][j], 1+dp[1][j-1])
            dp[0] = dp[1][:]
        return dp[-1][-1]
        # Time Complexity : O(n*m)
        # Space Complexity : O(mix(n,m))