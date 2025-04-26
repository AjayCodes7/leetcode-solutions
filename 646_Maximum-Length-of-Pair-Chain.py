class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda a : a[0])
        # dp = [1]*len(pairs)
        # for i in range(len(pairs)):
        #     for j in range(i):
        #         if pairs[j][1] < pairs[i][0] and 1 + dp[j] > dp[i]:
        #             dp[i] = 1 + dp[j]
        # return dp[-1]
        # # Time Complexity : O(n^2)
        # # Space Complexity : O(n)

        dp = []
        def bisect(num):
            i = 0
            j = len(dp)
            while i < j:
                mid = (i + j)//2
                if dp[mid][1] == num:
                    return mid
                if dp[mid][1] < num:
                    i = mid + 1
                else:
                    j = mid
            return i

        for pair in pairs:
            idx = bisect(pair[0])
            if idx == len(dp):
                dp.append(pair[:])
            else:
                if dp[idx][1] > pair[1]:
                      dp[idx] = pair[:]
        return len(dp)

        # Time Complexity : O(nlogn)
        # Space Complexity : O(n)