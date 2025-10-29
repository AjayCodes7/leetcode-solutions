class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        maxSum = currSum
        for i in range(1, len(nums) - k + 1):
            currSum = currSum - nums[i-1] + nums[i + k - 1]
            if currSum > maxSum:
                maxSum = currSum
        return maxSum/k