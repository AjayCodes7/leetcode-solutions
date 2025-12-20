class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        record = [""]*len(strs[0])
        result = 0
        for st in strs:
            for i in range(len(st)):
                record[i] += st[i]
        for st in record:
            if not st == "".join(sorted(st)):
                result += 1
        return result