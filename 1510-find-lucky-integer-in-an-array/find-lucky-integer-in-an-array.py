class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        hashmap = Counter(arr)
        for num, freq in hashmap.items():
            if num == freq:
                lucky = max(lucky,num)
        return lucky