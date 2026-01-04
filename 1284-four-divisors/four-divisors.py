class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(num):
            if num < 6:
                return 0
            sett = set()
            sett.add(1)
            sett.add(num)
            for i in range(2, int(sqrt(num))+1):
                if num % i == 0:
                    sett.add(i)
                    sett.add(num//i)
            if len(sett) == 4:
                return sum(sett)
            else:
                return 0

        
        result = 0
        for n in nums:
            result += divisors(n)
        return result
                    
            
