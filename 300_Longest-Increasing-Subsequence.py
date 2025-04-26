class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)

        # memory = {}
        # def recurse(currMax, next):
        #     if next == len(nums):
        #         return 0
        #     if (currMax, next) in memory:
        #         return memory[(currMax, next)]
        #     # Not Consider
        #     memory[(currMax, next+1)] = recurse(currMax,next+1)
        #     # Consider
        #     if currMax < nums[next]:
        #         memory[(nums[next], next+1)] = recurse(nums[next], next+1)
        #         return max(1 + memory[(nums[next], next+1)], memory[(currMax, next+1)])
        #     return memory[(currMax, next+1)]
        # return recurse(float("-inf"),0) 
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(i, -1, -1):
                exclude = dp[i+1][j]
                include = 0
                if j == 0 or nums[i] > nums[j-1]:
                    include = 1 + dp[i+1][i+1]
                dp[i][j] = max(include, exclude)
        return dp[0][0]
                