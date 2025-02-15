class Solution:
    def punishmentNumber(self, n: int) -> int:
        def recursion(curr, target,num,rem):
            if num:
                curr += int(num)
            if target == (curr + (int(rem) if rem else 0) ):
                return True
            if curr > target:
                return False
            for i in range(1, len(rem)+1):
                if recursion(curr, target, rem[:i], rem[i:]):
                    return True
            return False


        result = 0
        for i in range(1,n+1): 
            if(recursion(0,i,"",str(i*i))):
                result += i*i
        return result