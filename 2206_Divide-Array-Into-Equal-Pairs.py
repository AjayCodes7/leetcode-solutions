class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # count = Counter(nums)
        # for n in count.values():
        #     if n%2 != 0:
        #         return False
        # return True
        track = set()
        for i in nums:
            if i in track:
                track.remove(i)
            else:
                track.add(i)
        return len(track) == 0