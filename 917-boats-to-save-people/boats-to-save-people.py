class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i, j = 0, len(people)-1
        while i <= j:
            boats += 1
            weight = people[j]
            j -= 1
            if people and limit - weight >= people[j]:
                j -= 1
                return ceil((j-i+1)/2) + boats
            elif people and limit - weight >= people[i]:
                i += 1
        return boats