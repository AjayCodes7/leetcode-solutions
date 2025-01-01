class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Simulation Approach
        zeros = 0
        # Count no of ones
        ones = s.count('1')
        result = 0
        '''Iterate through each string while counting 
        zeros from the left and calculate the result
        '''
        for i in s[:-1]:
            if i == '0':
                zeros += 1
            else:
                ones -= 1
            result = max(result, zeros+ones)
            '''
            Maximum result can be achieved is the length of the string
            (Occurs when all zeros alligned to left and ones to right)
            [Eg: "00..0011..11"]
            '''
            if result == len(s):
                return result
        return result
