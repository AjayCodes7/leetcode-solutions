class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        maxevents = 0
        for event in events:
            maxevents = max(maxevents, event[1])
        events.sort()
        min_heap = []
        i, res, n = 0, 0, len(events)
        for day in range(1, maxevents+1):
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
                
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
                
            if min_heap:
                heapq.heappop(min_heap)
                res += 1

            if i >= n and not min_heap:
                break
                
        return res