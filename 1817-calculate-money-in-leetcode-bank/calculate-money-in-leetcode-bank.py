class Solution:
    def sum_of_firstn(self, n):
        return int(n*(n+1)/2)

    def totalMoney(self, n: int) -> int:
        curr = 0
        result = 0
        while n >= 7:
            result += self.sum_of_firstn(7+curr) - self.sum_of_firstn(curr)
            curr += 1
            n -= 7
        if n:
            result += self.sum_of_firstn(n+curr) - self.sum_of_firstn(curr)
        return result