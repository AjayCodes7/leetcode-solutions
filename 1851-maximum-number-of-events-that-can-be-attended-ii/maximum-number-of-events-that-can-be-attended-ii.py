class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key= lambda event: event[1])
        n = len(events)

        start_days = [e[0] for e in events]
        end_days = [e[1] for e in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            prev_index = bisect_right(end_days, start - 1, 0, i - 1)
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[prev_index][j - 1] + value)
        return dp[n][k]