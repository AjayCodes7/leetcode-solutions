class Solution:
    def findHash(self, prevHash, new, old):
        return prevHash * 4 - old * 4**(10) + new

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        self.map = {
            'A':0,
            'C':1,
            'G':2,
            'T':3
        }

        if len(s) < 11:
            return []

        unique = set()
        result = set()

        currHash = 0
        for i in range(9,-1,-1):
            currHash += self.map.get(s[9 - i]) * 4 ** i
        unique.add(currHash)

        for i in range(1, len(s)-10 + 1):
            currHash = self.findHash(currHash, self.map.get(s[i+9]), self.map.get(s[i-1]))
            if currHash in unique:
                result.add(s[i:i+10])
            else:
                unique.add(currHash)
        return list(result)