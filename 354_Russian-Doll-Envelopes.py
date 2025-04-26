class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
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
        envelopes.sort(key = lambda a: (a[0],-a[1]))
        for envelope in envelopes:
            idx = bisect(envelope[1])
            if idx == len(dp):
                dp.append(envelope[:])
            else:
                dp[idx] = envelope[:]
        return len(dp)
        # Time Complexity : O(nlogn)
        # Space Complexity : O(n)