class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 1
        time = 0
        n = len(colors)
        while i < n:
            temp = neededTime[i-1]
            cur_sum = temp
            flag = False
            while i < n and colors[i-1] == colors[i]:
                flag = True
                cur_sum += neededTime[i]
                temp = max(temp, neededTime[i])
                i += 1
            if flag:
                time += cur_sum - temp
            i += 1
        return time