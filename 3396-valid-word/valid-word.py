class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        if not any(i.lower() in ('a','e','i','o','u') for i in word):
            return False
        if not any(i.isalpha() and i.lower() not in ('a','e','i','o','u') for i in word):
            return False
        return True