class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # N = len(triangle)
        # result = [float("inf")]
        # def DFS(currSum, row, idx):
        #     if row == N:
        #         result[0] = min(currSum, result[0])
        #         return
        #     DFS(currSum + triangle[row][idx], row+1, idx)
        #     DFS(currSum + triangle[row][idx], row+1, idx+1)
        # DFS(0,0,0)
        # MLE

        N = len(triangle)
        dp = [[0]*(i+1) for i in range(N)]
        dp[0][0] = triangle[0][0]
        for i in range(1, N):
            for j in range(i+1):
                curr = triangle[i][j]
                if j == 0:
                    dp[i][j] = dp[i-1][j] + curr
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + curr
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + curr
        return min(dp[-1])
