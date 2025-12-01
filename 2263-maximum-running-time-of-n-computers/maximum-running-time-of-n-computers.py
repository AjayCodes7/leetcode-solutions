class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = 0
        for i in range(len(batteries) - n):
            extra += batteries[i]
        
        live = batteries[len(batteries) - n : ]
        
        for i in range(n-1):
            if (extra < (i+1) * (live[i+1] - live[i])):
                return live[i] + extra//(i+1)
            
            extra -= (i+1) * (live[i+1] - live[i])
        return live[n - 1] + extra // n
        