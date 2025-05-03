class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        # Greedy Algorithm
        n = len(tops)
        top = [0]*6
        bottom = [0]*6
    
        for i in range(n):
            top[tops[i]-1] += 1
            bottom[bottoms[i]-1] += 1
    
        top = [[i,v] for i, v in enumerate(top)]
        top.sort(key = lambda a:-a[1])

        for i, v in top:
            for j in range(n):
                if tops[j] != i+1 and bottoms[j] != i+1:
                    break
            if j == n-1:
                return n - max(v,bottom[i])
        return -1

        # Time Complexity : O(n)
        # Space Complexity : O(1)
