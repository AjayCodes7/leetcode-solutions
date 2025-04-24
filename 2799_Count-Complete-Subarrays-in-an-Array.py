class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l = 0
        r = 0
        length = len(nums)
        track = defaultdict(int)
        distinct = len(set(nums))
        result = 0
        while r < length:
            track[nums[r]] += 1
            while len(track.keys()) == distinct:
                result += (length - r)
                track[nums[l]] -= 1
                if track[nums[l]] == 0:
                    del track[nums[l]]
                l += 1
            r += 1
        return result
