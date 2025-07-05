class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # lucky = -1
        # hashmap = Counter(arr)
        # for num, freq in hashmap.items():
        #     if num == freq:
        #         lucky = max(lucky,num)
        # return lucky

        freqmap = [0]*501
        for i in arr:
            freqmap[i] += 1
        for i in range(500,0,-1):
            if freqmap[i] == i:
                return i
        return -1
