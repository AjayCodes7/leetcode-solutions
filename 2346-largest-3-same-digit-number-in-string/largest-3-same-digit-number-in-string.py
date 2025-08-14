class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goodInt = ""
        # for i in range(0,len(num)-2):
        #     if num[i] == num[i+1] == num[i+2]:
        #         if not goodInt:
        #             goodInt = num[i:i+3]
        #         else:
        #             goodInt = max(goodInt, num[i:i+3])
        # return goodInt
        goodInts = ['999','888','777','666','555','444','333','222','111','000']
        for i in goodInts:
            if i in num:
                return i
        return ""