class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            if i%2 == 0:
                result += nums[i]
        return result