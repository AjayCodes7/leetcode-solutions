class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        answer = 1
        target = points[0]
        for point in points[1:]:
            if point[0] <= target[1]:
                target[0] = max(point[0],target[0])
                target[1] = min(point[1],target[1])
            else:
                answer += 1
                target = point
        return answer