class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        last = -10**18
        for n in nums:
            choose = max(last + 1, n - k)
            if choose <= n + k:
                count += 1
                last = choose
        return count