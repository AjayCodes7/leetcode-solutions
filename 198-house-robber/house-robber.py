class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        dp[0] = nums[0]
        for i in range(1, N):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]