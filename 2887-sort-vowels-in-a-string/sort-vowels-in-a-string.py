class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        tosort = []
        result = [0]*len(s)
        for i in range(len(s)):
            if s[i] in vowels:
                tosort.append(s[i])
            else:
                result[i] = s[i]
        tosort.sort()
        for i in range(len(s)):
            if result[i] == 0:
                result[i] = tosort.pop(0)
        return ''.join(result)