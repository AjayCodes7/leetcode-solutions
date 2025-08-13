class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i]-cost[i] for i in range(n)]
        if sum(diff) < 0:
            return -1
        total = 0
        res = 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                total = 0
                res = i + 1
                continue
        return res
