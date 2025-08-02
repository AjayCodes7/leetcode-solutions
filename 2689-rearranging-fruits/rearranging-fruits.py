class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter()
        min_cst = float("inf")
        for i in basket1:
            count[i] += 1
            min_cst = min(min_cst, i)
        for i in basket2:
            count[i] -= 1
            min_cst = min(min_cst, i)
        
        exchange = []
        for key, val in count.items():
            if val%2 != 0:
                return -1
            exchange.extend([key]* (abs(val)//2))
        
        if not exchange:
            return 0
        
        exchange.sort()
        return sum( min(2 * min_cst, x) for x in exchange[: len(exchange) // 2] )
        