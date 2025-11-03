class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        
        intervals.sort(key = lambda x : x[0])
        result = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] < intervals[i][0]:
                result.append(prev[:])
                prev = intervals[i]
            else:
                prev[1] = max(prev[1], intervals[i][1])
        result.append(prev)
        return result
            