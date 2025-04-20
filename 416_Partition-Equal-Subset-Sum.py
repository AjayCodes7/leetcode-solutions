class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if sum(nums) % 2:
            return False
        half = summ//2
        dp = set()
        for num in nums:
            if num == half or half - num in dp:
                return True
            for i in list(dp)[:]:
                if (num+i) < half:
                    dp.add(num+i)
            dp.add(num)
        return False