class Solution:
    def compressedString(self, word: str) -> str:
        result = ""
        right = 0

        while right < len(word):
            curr = word[right]
            count = 0

            while right < len(word) and word[right] == curr and count < 9:
                count += 1
                right += 1
            
            result += str(count) + curr
        return result
            