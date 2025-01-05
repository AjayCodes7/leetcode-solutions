class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift = [0] * n
        for i,j,k in shifts:
            if k == 0:
                shift[i] -= 1
                if j + 1 < n:
                    shift[j + 1] += 1
            else:
                shift[i] += 1
                if j + 1 < n:
                    shift[j+1] -= 1
        result = list(s)
        no_shifts = 0
        for i in range(n):
            no_shifts = (
                no_shifts + shift[i]
            ) % 26
            if no_shifts < 0:
                no_shifts += 26

            shifted_char = chr(
                (ord(s[i]) - ord("a") + no_shifts) % 26 + ord("a")
            )

            result[i] = shifted_char
        return "".join(result)
            
