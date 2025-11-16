class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        count = 0
        for i in s:
            if i == '0':
                result += count*(count+1)//2
                count = 0
            else:
                count += 1
        if count:
            result += count*(count+1)//2
        return result%MOD