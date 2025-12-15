class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        result = n
        temp = 0
        for i in range(1, n):
            if prices[i - 1] - 1 == prices[i]:
                result += temp + 1
                temp += 1
            else:
                temp = 0
        return result
