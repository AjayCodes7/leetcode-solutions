class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        while people:
            boats += 1
            weight = people.pop()
            if people and limit - weight >= people[-1]:
                people.pop()
                return (ceil(len(people)/2)) + boats
            elif people and limit - weight >= people[0]:
                people.pop(0)
        return boats