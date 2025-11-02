class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        flag = False
        l = 0 
        r = 0
        cur_sum = 0
        while r < len(nums):
            cur_sum += nums[r]
            while l < len(nums) and cur_sum >= target:
                if cur_sum >= target:
                    flag = True
                    result = min(result, r-l+1)
                cur_sum -= nums[l]
                l += 1
            r += 1
        if flag:
            return result
        return 0
