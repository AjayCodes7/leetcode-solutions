class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')] += 1
        max_vowels = 0
        for i in 'aeiou':
            max_vowels = max(freq[ord(i)-ord('a')], max_vowels)
            freq[ord(i)-ord('a')] = 0
        return max_vowels + max(freq)