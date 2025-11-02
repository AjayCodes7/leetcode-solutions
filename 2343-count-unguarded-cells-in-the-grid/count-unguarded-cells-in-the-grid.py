class Solution:
    UNGUARD = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3
    def _markGuard(self, i,j,marking):
        # top
        for temp in range(i - 1, -1, -1 ):
            if marking[temp][j] == self.WALL or marking[temp][j] == self.GUARD:
                break
            marking[temp][j] = 1

        # bottom
        for temp in range(i + 1, len(marking)):
            if marking[temp][j] == self.WALL or marking[temp][j] == self.GUARD:
                break
            marking[temp][j] = 1

        # left
        for temp in range(j - 1, -1, -1):
            if marking[i][temp] == self.WALL or marking[i][temp] == self.GUARD:
                break
            marking[i][temp] = 1

        # right
        for temp in range(j + 1, len(marking[0])):
            if marking[i][temp] == self.WALL or marking[i][temp] == self.GUARD:
                break
            marking[i][temp] = 1

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        marking = [[self.UNGUARD]*n for _ in range(m)]

        for i,j in walls:
            marking[i][j] = self.WALL

        for i,j in guards:
            marking[i][j] = self.GUARD
        
        for i,j in guards:
            self._markGuard(i,j, marking)

        count = 0
        for row in marking:
            for col in row:
                if col == 0:
                    count += 1
        return count
