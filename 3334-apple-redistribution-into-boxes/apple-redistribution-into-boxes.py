class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total = sum(apple)
        print(capacity)
        print(total)
        filled = 0
        for i in range(len(capacity)):
            filled += capacity[i]
            if filled >= total:
                return i + 1
                
