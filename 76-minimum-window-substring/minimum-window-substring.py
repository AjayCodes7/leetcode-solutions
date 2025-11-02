class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        sliding_window = {}
        for i in t:
            need[i] = 1 + need.get(i, 0)
        req = len(need)
        have = 0
        l = 0
        result = []
        cur_length = float('inf')
        for r in range(len(s)):
            # Update sliding Window
            if s[r] in need:
                sliding_window[s[r]] = 1 + sliding_window.get(s[r], 0)

            # check if the condition met
            if s[r] in need and need[s[r]] == sliding_window[s[r]]:
                have += 1

            # Update the left
            while have == req:
                if cur_length > (r - l + 1):
                    cur_length = r - l + 1
                    result = [l,r]
                
                if s[l] in need:
                    sliding_window[s[l]] -= 1
                    if sliding_window[s[l]] < need[s[l]]:
                        have -= 1
                l += 1
        if not result:
            return ""
        return s[result[0]:result[1]+1]