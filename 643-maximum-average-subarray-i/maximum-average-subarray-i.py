class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in nums[:k]:
            currSum += i
        maxAvg = currSum/k
        for i in range(1, len(nums) - k + 1):
            currSum -= nums[i-1]
            currSum += nums[i + k - 1]
            maxAvg = max(maxAvg, currSum/k)
        return maxAvg