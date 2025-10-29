class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        unique = set()
        result = set()
        for i in range(len(s)-10 + 1):
            if s[i:i+10] in unique:
                result.add(s[i:i+10])
                continue
            else:
                unique.add(s[i:i+10])
        return list(result)
