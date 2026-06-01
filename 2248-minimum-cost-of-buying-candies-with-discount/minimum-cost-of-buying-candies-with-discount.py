class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        result = 0
        for i, c in enumerate(cost[::-1]):
            if (i + 1) % 3:
                result += c
        return result
