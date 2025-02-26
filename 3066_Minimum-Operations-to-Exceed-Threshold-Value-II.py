class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        result = 0
        while len(nums) >= 2 and nums[0]<k:
            a,b = heappop(nums), heappop(nums)
            heappush(nums, min(a,b)*2 + max(a,b))
            result += 1
        return result
