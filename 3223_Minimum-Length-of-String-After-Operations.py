class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        result = 0
        for i in count.values():
            if i < 3:
                result += i
                continue
            result += 2 if i%2 == 0 else 1
        return result