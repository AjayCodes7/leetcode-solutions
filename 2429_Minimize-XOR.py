class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2 = bin(num2).count('1')
        num1 = bin(num1)[2:]
        result = ['0'] * len(num1)
        i = 0
        while num2 and i < len(num1):
            if num1[i] == '1':
                result[i] = '1'
                num2 -= 1
            i += 1
        result = ['0'] * num2 + result
        i = len(result) - 1
        while num2 and i >= 0:
            if(result[i]=='0'):
                result[i] = '1'
                num2 -= 1
            i -= 1
        return int("".join(result),2)