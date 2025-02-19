class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = ""
        self.k = k
        self.count = 0


        def backtrack(word, c, available):
            if c == n:
                self.count += 1
                if self.count == self.k:
                    self.res = word
                return
            for i in available:
                backtrack(word + i, c+1, 'abc'.replace(i,''))


        backtrack("",0,'abc')
        return self.res