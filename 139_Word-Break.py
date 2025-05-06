class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # wordDict = set(wordDict)
        # # dp = [False]*n
        # def check(index):
        #     if index < 0 : return True
        #     for word in wordDict:
        #         if s[index - len(word)+1:index+1] == word and check(index - len(word)):
        #             return True
        #     return False
        # return check(n-1)

        # n = len(s)
        # wordDict = set(wordDict)
        # dp = [-1]*n
        # def check(index):
        #     if index < 0 : return True
        #     if dp[index] != -1: return dp[index]
        #     for word in wordDict:
        #         if s[index - len(word)+1:index+1] == word and check(index - len(word)):
        #             dp[index] = True
        #             return dp[index]
        #     dp[index] = False
        #     return dp[index]
        # return check(n-1)

        n = len(s)
        dp = [False]*n
        for i in range(0,n):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if s[i-len(word)+1:i+1] == word and (i-len(word)==-1 or dp[i-len(word)]):
                    dp[i] = True
        return dp[-1]