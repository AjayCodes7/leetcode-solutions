class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        map = {}
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] != t[i]:
                return False
            else:
                hashmap[s[i]] = t[i]
            if t[i] in map and map[t[i]] != s[i]:
                return False
            else:
                map[t[i]] = s[i]
        return True