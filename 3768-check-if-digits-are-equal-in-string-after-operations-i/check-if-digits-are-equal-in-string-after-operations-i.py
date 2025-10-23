class Solution:
    def hasSameDigits(self, s: str) -> bool:
        num = [int(c) for c in s]
        while len(num) > 2:
            new = []
            for i in range(1, len(num)):
                new.append((num[i-1]+num[i])%10)
            num = new[:]
        return num[0] == num[1]