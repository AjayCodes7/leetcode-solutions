# 2559. Count Vowel Strings in Ranges

class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Pre-Processing 
        """ 
        count no of words in words list which
        are starting and ending with vowels till 
        that index starting from index 0
        """
        count = []
        n = 0
        for word in words:
            if word[0] in ('a','e','i','o','u') and word[-1] in ('a','e','i','o','u'):
                n += 1
            count.append(n)
        result = []
        """
        Find out the number of strings present in 
        the range li to ri by substracting the count[ri]
        with count[li]
        """
        for i,j in queries:
            if i == 0:
                result.append(count[j])
            else:
                result.append(count[j]-count[i-1])
        return result
            