class Solution:
    def isValid(self, word: str) -> bool:
        # Check if length of word atleast 3
        if not (len(word) > 2):
            return False
        # Check if there is a special character
        if '@' in word or '#' in word  or '$' in word:
            return False
        # Check if there is a vowel
        if not any( i.lower() in ('a','e','i','o','u') for i in word):
            return False
        # Check if there is a consonant
        if not any(i.isalpha() and i.lower() not in ('a','e','i','o','u') for i in word):
            return False
        # All conditions saticified
        return True
        
