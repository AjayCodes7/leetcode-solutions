class Solution:
    def maximum69Number (self, num: int) -> int:
        n = len(str(num)) - 1
        for i in str(num):
            if i == '6':
                num += 3 * 10**n
                break
            n -= 1
        return num
