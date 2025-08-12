class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i, j = 0, len(people)-1
        while i <= j:
            boats += 1
            j -= 1
            if limit - people[j+1] >= people[j]:
                j -= 1
                return ceil((j-i+1)/2) + boats
            elif limit - people[j+1] >= people[i]:
                i += 1
        return boats