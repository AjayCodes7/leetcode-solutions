class Solution:
    def _markGuard(self, i,j,marking):
        # top
        for temp in range(i - 1, -1, -1 ):
            if marking[temp][j] == 3 or marking[temp][j] == 2:
                break
            marking[temp][j] = 1

        # bottom
        for temp in range(i + 1, len(marking)):
            if marking[temp][j] == 3 or marking[temp][j] == 2:
                break
            marking[temp][j] = 1

        # left
        for temp in range(j - 1, -1, -1):
            if marking[i][temp] == 3 or marking[i][temp] == 2:
                break
            marking[i][temp] = 1

        # right
        for temp in range(j + 1, len(marking[0])):
            if marking[i][temp] == 3 or marking[i][temp] == 2:
                break
            marking[i][temp] = 1

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        marking = [[0]*n for i in range(m)]

        for i,j in walls:
            marking[i][j] = 3

        for i,j in guards:
            marking[i][j] = 2
        
        for i,j in guards:
            self._markGuard(i,j, marking)

        count = 0
        for row in marking:
            for col in row:
                if col == 0:
                    count += 1
        return count
