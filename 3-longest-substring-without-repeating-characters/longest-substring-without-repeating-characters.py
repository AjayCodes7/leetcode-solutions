class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)== 1: 
            return 1 
        left = 0 
        count = {} 
        result = 0 
        for right in range(len(s)): 
            if count.get(s[right],-1) != -1: 
                left = max(left, count.get(s[right]) + 1)
                while left < right and s[left] == s[right]:
                    left += 1 
            count[s[right]] = right 
            result = max(result, right - left + 1)
        return result 