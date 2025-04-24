class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursive with memorization Solution
        # memory = [[-1]*len(text2) for _ in range(len(text1))]
        # def recurse(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if memory[i][j] != -1:
        #         return memory[i][j]
        #     else:
        #         if text1[i]==text2[j]:
        #             memory[i][j] = 1 + recurse(i+1,j+1)
        #             return memory[i][j]
        #         else:
        #             memory[i][j] = max(recurse(i+1,j),recurse(i, j+1))
        #             return memory[i][j]
        # return recurse(0,0)

        # Time Complexity: O(n*m)
        # Space Complexity: O(n*m)

        # Dynamic Programming (Tabulation with space optimization)
        dp = [[0]*len(text1) for _ in range(2)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[1][j] = dp[0][j-1] + 1 if i > 0 and j > 0 else 1
                else:
                    dp[1][j] = max(dp[0][j],dp[1][j-1]) if j > 0 else dp[0][j]
            dp[0] = dp[1][:]
        return dp[-1][-1]
        # Time Complexity: O(n*m)
        # Space Complexity: O(min(m,n))