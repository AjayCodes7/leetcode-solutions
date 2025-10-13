class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if ''.join(sorted(words[i])) == ''.join(sorted(words[i-1])):
                words.pop(i)
                continue
            i+=1
        return words