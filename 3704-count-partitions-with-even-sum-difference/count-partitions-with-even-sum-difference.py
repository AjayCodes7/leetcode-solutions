class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        for num in nums:
            right += num
        for i in range(1,len(nums)):
            left += nums[i-1]
            right -= nums[i-1]

            if (right - left) % 2 == 0:
                result += 1
        return result