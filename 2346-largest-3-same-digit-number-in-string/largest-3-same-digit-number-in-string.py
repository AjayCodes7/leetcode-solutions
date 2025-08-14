class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goodInt = ""
        for i in range(0,len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if not goodInt:
                    goodInt = num[i:i+3]
                else:
                    goodInt = max(goodInt, num[i:i+3])
        return goodInt