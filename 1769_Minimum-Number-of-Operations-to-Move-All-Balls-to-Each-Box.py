class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        # Focus on constraints
        # The length is only 2000
        # So we can use Brute-force approach here
        # Simply calculate no of moves at each possible step
        answer = [0] * len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == '1':
                for j in range(len(boxes)):
                    answer[j] += abs(j - i)
        return answer