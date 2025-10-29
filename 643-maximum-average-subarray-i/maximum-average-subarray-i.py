class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in nums[:k]:
            currSum += i
        maxSum = currSum
        for i in range(1, len(nums) - k + 1):
            currSum = currSum - nums[i-1] + nums[i + k - 1]
            maxSum = max(currSum, maxSum)
        return maxSum/k