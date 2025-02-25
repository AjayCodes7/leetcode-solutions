class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cursum = 0
        even = 0
        odd = 0
        result = 0
        for i in arr:
            cursum += i
            if cursum % 2 != 0:
                odd += 1
                result += 1
                result += even
            else:
                even += 1
                result += odd
        return (result) % (10**9 + 7)