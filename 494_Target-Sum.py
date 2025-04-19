class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Backtracking TLE
        # result = 0
        # def backtrack(n, currSum):
        #     nonlocal result
        #     if n == len(nums):
        #         if  currSum == target:
        #             result += 1
        #         return
        #     backtrack(n+1, currSum + nums[n])
        #     backtrack(n+1, currSum - nums[n])
        # backtrack(0, 0)
        # return result
        summ = sum(nums)
        if summ < abs(target) or (summ + target) & 1:
            return 0
        def targetSum(target):
            dp = [1] + [0]*summ
            for num in nums:
                for j in range(summ, num - 1, -1):
                    dp[j] += dp[j-num]
            return dp[target]
        return targetSum((summ+target)//2)