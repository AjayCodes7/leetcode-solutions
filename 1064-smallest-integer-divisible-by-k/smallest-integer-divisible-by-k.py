class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        res = 1
        seen = set()
        while curr % k:
            if curr in seen:
                return -1
            seen.add(curr)
            curr = 10 * (curr % k) + 1
            res += 1
        return res