class Solution:
    def smallestNumber(self, pattern: str):
        pattern += pattern[-1]
        nums = [i for i in range(1,len(pattern)+1)]
        result = 0
        i = 0
        while i < len(pattern):
            I = 0
            D = 0
            if pattern[i] == 'I':
                while i < len(pattern) and pattern[i] == 'I':
                    result *= 10
                    result += nums.pop(0)
                    i += 1
            else:
                while i < len(pattern) and pattern[i] == 'D':
                    D += 1
                    i += 1
                if len(nums) == D:
                    for n in range(D):
                        result *= 10
                        result += nums.pop()
                else:
                    for n in range(D,0,-1):
                        result *= 10
                        result += nums.pop(n)
            if len(nums) == 1:
                result *= 10
                result += nums.pop()
                i+=1
        return str(result)