class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        dp = [list((0,0,0) for _ in range(cols+1)) for _ in range(rows+1)]
        answer = [[0] * cols for _ in range(rows)]
        ans = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if mat[i-1][j-1] == 1:
                    temp = ans
                    ans += dp[i-1][j][0] + dp[i][j-1][1] + 1
                    if dp[i-1][j][0] and dp[i][j-1][1]:
                        corner = dp[i-1][j-1]
                        topTillNow = min(dp[i-1][j][0],corner[0])
                        leftMin = min(dp[i][j-1][1], corner[1])
                        for left in range(leftMin):
                            topTillNow = min(topTillNow,dp[i-1][j-left-1][0])
                            ans += topTillNow
                    answer[i-1][j-1] = ans-temp
                    dp[i][j] = (dp[i-1][j][0]+1, dp[i][j-1][1]+1, dp[i-1][j-1][2]+1 if dp[i-1][j][0] and dp[i][j-1][1] else 1)
        return ans