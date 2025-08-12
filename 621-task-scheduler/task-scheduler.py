class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        noOfMax = tuple(freq.values()).count(maxFreq)
        emptySlots = (maxFreq-1)*(n-(noOfMax-1))
        remaining = len(tasks) - maxFreq*noOfMax
        idleSlots = max(0, emptySlots - remaining)
        return len(tasks) + idleSlots