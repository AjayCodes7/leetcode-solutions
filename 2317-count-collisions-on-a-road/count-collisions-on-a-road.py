class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left = 0
        right = n - 1
        while left < n and directions[left] == 'L':
            left += 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        return (right - left + 1) - directions[left:right+1].count('S')
