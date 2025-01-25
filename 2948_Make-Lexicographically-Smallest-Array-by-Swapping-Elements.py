class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        mappings = {}

        for n in sorted(nums):
            if not groups or n - groups[-1][-1] > limit:
                groups.append(deque())
            groups[-1].append(n)
            mappings[n] = len(groups) - 1

        result = []
        for n in nums:
            result.append(groups[mappings[n]].popleft())
        return result