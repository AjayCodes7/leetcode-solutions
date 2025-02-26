class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        max_cur_sum = nums[0]
        min_cur_sum = nums[0]

        for i in range(1,len(nums)):
            # Maximum Case
            max_cur_sum = max(nums[i], max_cur_sum+nums[i])
            max_sum = max(max_sum, max_cur_sum)
            # Minimum Case
            min_cur_sum = min(nums[i], min_cur_sum+nums[i])
            min_sum = min(min_sum, min_cur_sum)
        return max(abs(max_sum),abs(min_sum))