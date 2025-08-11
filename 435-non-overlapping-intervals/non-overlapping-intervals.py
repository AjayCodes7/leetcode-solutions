class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        answer = 0
        last = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < last[1]:
                answer += 1
                continue
            last = interval.copy()
        return answer