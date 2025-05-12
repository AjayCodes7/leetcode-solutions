class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = []
        for i in range(100,999,2):
            num = str(i)
            if(num.count(num[0]) <= count[int(num[0])] and num.count(num[1]) <= count[int(num[1])] and num.count(num[2]) <= count[int(num[2])]):
                result.append(i)
        return result