class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(partial):
            result = ""
            count = 0
            prev = False
            for i in partial:
                if prev:
                    if prev == i:
                        count += 1
                        prev = i
                    else:
                        result += str(count) + prev
                        prev = i
                        count = 1
                else:
                    prev = i
                    count += 1
            result += str(count) + prev 
            return result           

        def recurse(n):
            if n == 1:
                return "1"
            return rle(recurse(n-1))
        return recurse(n)
