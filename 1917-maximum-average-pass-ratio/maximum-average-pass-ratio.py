class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(p, t):
            return (p+1)/(t+1) - p/t
        
        heap = [(-gain(x[0],x[1]), x) for x in classes]
        heapify(heap)

        for _ in range(extraStudents):
            old = heappop(heap)
            new = [old[1][0]+1, old[1][1]+1]
            heappush(heap, (-gain(new[0], new[1]),new))

        temp = 0
        for item in heap:
            temp += item[1][0]/item[1][1]
        return round(temp/len(classes), 5)