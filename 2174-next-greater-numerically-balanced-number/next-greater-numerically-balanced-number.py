class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1224445):
            freq = Counter(str(i))
            flag = True
            for key, value in freq.items():
                if int(key) != value:
                    flag = False
                    break
            if flag:
                return i