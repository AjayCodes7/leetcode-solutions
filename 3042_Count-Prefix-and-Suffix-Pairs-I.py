class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                str1 = words[i]
                str2 = words[j]
                if len(str1) > len(str2):
                    continue
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1
        return count