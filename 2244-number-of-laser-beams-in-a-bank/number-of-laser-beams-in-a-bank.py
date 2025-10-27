class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count('1')
        result = 0
        for row in bank[1:]:
            curr = row.count('1')
            if curr:
                result += curr * prev
                prev = curr
        return result
        