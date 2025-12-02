class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        MOD = 10**9 + 7
        ans, total_count = 0, 0
        for point in points:
            hashmap[point[1]] += 1
        
        for count in hashmap.values():
            edges = count * (count - 1) // 2
            ans = (ans + edges * total_count) % MOD
            total_count = (total_count + edges) % MOD
        return ans