class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = target[0]
        for i in range(1, len(target)):
            curr = target[i]
            if curr > target[i-1]:
                prev += curr - target[i-1]
        return prev
