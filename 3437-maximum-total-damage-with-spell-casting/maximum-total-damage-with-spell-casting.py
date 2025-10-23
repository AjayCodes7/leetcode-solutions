class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq.keys())

        N = len(keys)
        if N == 1:
            return keys[0] * freq[keys[0]]
        if N == 2:
            if keys[0] + 2 < keys[1]:
                return keys[0] * freq[keys[0]] + keys[1] * freq[keys[1]]
            else:
                return max(keys[0] * freq[keys[0]], keys[1] * freq[keys[1]])
        
        dp = [0]*N
        dp[0] = keys[0] * freq[keys[0]]
        dp[1] = keys[0] * freq[keys[0]] + keys[1] * freq[keys[1]] if keys[0] + 2 < keys[1] else max(keys[0] * freq[keys[0]], keys[1] * freq[keys[1]])

        for i in range(2, N):
            if keys[i-1]+2 < keys[i]:
                dp[i] = dp[i-1] + keys[i] * freq[keys[i]]
            elif keys[i-2] + 2 < keys[i]:
                dp[i] = max(dp[i-1], dp[i-2] + keys[i] * freq[keys[i]])
            else:
                if i < 3:
                    dp[i] = max(dp[i-1], keys[i] * freq[keys[i]])
                else:
                    dp[i] = max(dp[i-1], dp[i-3] + keys[i] * freq[keys[i]])
        return dp[-1]
