class Solution:
    def minFlips(self, s: str) -> int:
        possible =["",""]
        n = len(s)
        s += s
        if len(s)%2 == 0:
            possible[0] = "10"*(len(s)//2)
            possible[1] = "01"*(len(s)//2)
        else:
            possible[0] = "10" * (len(s)//2 )+ "1"
            possible[1] = "01" * (len(s)//2 )+ "0"
        print(possible)
        difs = [0,0]
        result = len(s)
        l = 0
        for i in range(len(s)):
            if possible[0][i] != s[i]:
                difs[0] += 1
            if possible[1][i] != s[i]:
                difs[1] += 1
            if (i - l + 1) > n:
                if s[l] != possible[0][l]:
                    difs[0] -= 1
                if s[l] != possible[1][l]:
                    difs[1] -= 1
                l += 1
            if (i - l + 1) == n:
                result = min(result, min(difs))
        return result


# 111000111000
#  101010
#  010101