class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                temp = sqrt(a**2 + b**2)
                if temp == int(temp) and temp <= n:
                    count += 1
        return count * 2